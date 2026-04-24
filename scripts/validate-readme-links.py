#!/usr/bin/env python3
"""
Validate every external URL in a README: fetch the page, confirm it's reachable
(not 4xx/5xx), and — when the URL carries a `#:~:text=` anchor — verify that the
anchored text actually appears in the response body.

Usage:
    python3 scripts/validate-readme-links.py <readme.md> [--out report.md] [--workers 8]

Emits a GFM report with one row per unique URL:
    status   = OK | REDIRECT | NOT_FOUND | BLOCKED | TIMEOUT | ERROR
    anchor   = MATCH | MISS | n/a
    http     = final HTTP status
    final    = final URL after redirects (if different from requested)
    note     = error message, blocking reason, or redirect target

Notes:
- Uses a desktop Chrome User-Agent. Some sites (Bloomberg, X/Twitter, some
  paywalled outlets) will still 403/block or require JS — those are flagged
  BLOCKED so a human can verify manually, rather than treated as dead.
- Text-fragment matching is naive substring-search over raw HTML with a lowered
  copy; it misses content that's lazy-loaded by JS. So MISS != "dead link",
  just "couldn't verify automatically". Combine with the status column.
- Regex for link extraction is shared logic with scripts/extract-readme-links.py.
"""
from __future__ import annotations

import argparse
import concurrent.futures as futures
import json
import re
import sys
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from urllib.parse import unquote, urlsplit

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

INLINE_LINK_RE = re.compile(
    r'\[(?P<label>[^\]]*)\]\(\s*(?P<url><[^>]+>|[^)\s]+)(?:\s+"[^"]*")?\s*\)'
)

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)
TIMEOUT = 20


@dataclass
class Result:
    url: str
    status: str         # OK | REDIRECT | NOT_FOUND | BLOCKED | TIMEOUT | ERROR
    http: int | None    # final HTTP status code
    anchor: str         # MATCH | MISS | n/a
    anchor_text: str    # empty if URL had no text-fragment
    final_url: str      # final URL after redirects
    note: str           # human-readable explanation
    elapsed_ms: int


def extract_unique_urls(text: str) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for m in INLINE_LINK_RE.finditer(text):
        url = m.group("url").strip().strip("<>")
        if not url.startswith(("http://", "https://")):
            continue
        if url in seen:
            continue
        seen.add(url)
        ordered.append(url)
    return ordered


def strip_text_fragment(url: str) -> tuple[str, str]:
    """Return (url_without_fragment, anchor_text)."""
    parts = urlsplit(url)
    fragment = parts.fragment
    anchor = ""
    if fragment.startswith(":~:"):
        # Parse the text= piece (text-fragment spec allows prefix-,start,end,-suffix)
        m = re.search(r"text=([^&]*)", fragment)
        if m:
            raw = unquote(m.group(1))
            # Take the first comma-separated segment; that's the primary start text
            anchor = raw.split(",", 1)[0]
    stripped = f"{parts.scheme}://{parts.netloc}{parts.path}"
    if parts.query:
        stripped += f"?{parts.query}"
    return stripped, anchor


def build_session() -> requests.Session:
    s = requests.Session()
    retry = Retry(
        total=2,
        connect=2,
        read=1,
        backoff_factor=1.0,
        status_forcelist=(502, 503, 504),
        allowed_methods=("GET", "HEAD"),
    )
    adapter = HTTPAdapter(max_retries=retry)
    s.mount("http://", adapter)
    s.mount("https://", adapter)
    s.headers.update(
        {
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Cache-Control": "no-cache",
        }
    )
    return s


def classify(r: requests.Response | None, exc: Exception | None) -> tuple[str, str]:
    """Return (status_label, note) for a (response, exception) pair."""
    if exc is not None:
        name = type(exc).__name__
        msg = str(exc).split("\n", 1)[0][:200]
        if "Timeout" in name:
            return "TIMEOUT", msg
        return "ERROR", f"{name}: {msg}"
    assert r is not None
    code = r.status_code
    if code == 200:
        return "OK", ""
    if code in (301, 302, 303, 307, 308):
        return "REDIRECT", f"HTTP {code} -> {r.headers.get('Location', '?')}"
    if code in (404, 410):
        return "NOT_FOUND", f"HTTP {code}"
    if code in (401, 403, 429, 451) or 500 <= code < 600:
        return "BLOCKED", f"HTTP {code} (may be paywall / bot block / server error)"
    return "ERROR", f"HTTP {code}"


def check_anchor(body: str, anchor: str) -> str:
    if not anchor:
        return "n/a"
    hay = body.lower()
    needle = anchor.lower().strip()
    if not needle:
        return "n/a"
    # Try direct substring first
    if needle in hay:
        return "MATCH"
    # Try collapsed whitespace
    collapsed_hay = re.sub(r"\s+", " ", hay)
    collapsed_needle = re.sub(r"\s+", " ", needle)
    if collapsed_needle in collapsed_hay:
        return "MATCH"
    return "MISS"


def check_one(session: requests.Session, url: str) -> Result:
    start = time.time()
    base, anchor = strip_text_fragment(url)
    resp: requests.Response | None = None
    err: Exception | None = None
    try:
        resp = session.get(base, timeout=TIMEOUT, allow_redirects=True)
    except Exception as e:  # network, ssl, too many redirects, etc.
        err = e

    status, note = classify(resp, err)
    http_code = resp.status_code if resp is not None else None
    final_url = resp.url if resp is not None else ""

    anchor_match = "n/a"
    if resp is not None and status == "OK" and anchor:
        body = ""
        try:
            body = resp.text
        except Exception:
            body = ""
        anchor_match = check_anchor(body, anchor)

    # If the final URL redirected to a completely different path (e.g. homepage),
    # flag it — this catches articles that 200 but silently redirected to a
    # generic landing page.
    if resp is not None and 200 <= resp.status_code < 300:
        try:
            req_path = urlsplit(base).path.rstrip("/")
            fin_path = urlsplit(final_url).path.rstrip("/")
            req_host = urlsplit(base).netloc.lower()
            fin_host = urlsplit(final_url).netloc.lower()
            if req_host.replace("www.", "") != fin_host.replace("www.", ""):
                status = "REDIRECT"
                note = f"cross-domain redirect -> {final_url}"
            elif req_path and fin_path != req_path:
                # Same host, different path. If the new path is "" or "/", that's a
                # silent landing-page redirect (likely content removed).
                if fin_path in ("", "/") or fin_path.endswith("/404"):
                    status = "NOT_FOUND"
                    note = f"silent redirect to landing page: {final_url}"
        except Exception:
            pass

    elapsed = int((time.time() - start) * 1000)
    return Result(
        url=url,
        status=status,
        http=http_code,
        anchor=anchor_match,
        anchor_text=anchor,
        final_url=final_url,
        note=note,
        elapsed_ms=elapsed,
    )


def render_markdown(results: list[Result], source: Path) -> str:
    def esc(s: str, limit: int = 200) -> str:
        s = (s or "").replace("|", "\\|").replace("\n", " ")
        if len(s) > limit:
            s = s[: limit - 1] + "…"
        return s

    order = {"NOT_FOUND": 0, "REDIRECT": 1, "BLOCKED": 2, "TIMEOUT": 3, "ERROR": 4, "OK": 5}
    sorted_results = sorted(results, key=lambda r: (order.get(r.status, 9), r.anchor == "MATCH", r.url))

    by_status: dict[str, int] = {}
    for r in results:
        by_status[r.status] = by_status.get(r.status, 0) + 1
    anchor_stats = {
        "MATCH": sum(1 for r in results if r.anchor == "MATCH"),
        "MISS": sum(1 for r in results if r.anchor == "MISS"),
        "n/a": sum(1 for r in results if r.anchor == "n/a"),
    }

    lines: list[str] = []
    lines.append(f"# Link validation for `{source.name}`")
    lines.append("")
    lines.append(f"- Source: `{source}`")
    lines.append(f"- Total unique URLs checked: **{len(results)}**")
    lines.append("- Status breakdown: " + ", ".join(f"**{k}**: {v}" for k, v in sorted(by_status.items())))
    lines.append("- Anchor-text check (for URLs with `#:~:text=`): "
                 + ", ".join(f"**{k}**: {v}" for k, v in anchor_stats.items() if v))
    lines.append("")
    lines.append(
        "Generated by `scripts/validate-readme-links.py`. Status **BLOCKED** "
        "usually means the site is paywalled or blocks automated fetches "
        "(Bloomberg, X/Twitter, some news sites) — these need manual review, "
        "not automatic replacement. Status **NOT_FOUND** / **REDIRECT** to a "
        "landing page are the actionable items."
    )
    lines.append("")
    lines.append("| Status | Anchor | HTTP | URL | Note / Final URL | ms |")
    lines.append("|---|---|---|---|---|---|")
    for r in sorted_results:
        lines.append(
            f"| {r.status} | {r.anchor} | {r.http or '—'} | <{esc(r.url, 180)}> "
            f"| {esc(r.note or (r.final_url if r.final_url != r.url else ''), 160)} "
            f"| {r.elapsed_ms} |"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("readme", type=Path)
    p.add_argument("--out", type=Path, default=None)
    p.add_argument("--json", type=Path, default=None)
    p.add_argument("--workers", type=int, default=8)
    args = p.parse_args()

    if not args.readme.is_file():
        print(f"error: {args.readme} not found", file=sys.stderr)
        return 2

    urls = extract_unique_urls(args.readme.read_text())
    print(f"checking {len(urls)} unique URLs with {args.workers} workers...", file=sys.stderr)

    session = build_session()
    results: list[Result] = []
    with futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        future_to_url = {pool.submit(check_one, session, u): u for u in urls}
        for i, fut in enumerate(futures.as_completed(future_to_url), 1):
            r = fut.result()
            results.append(r)
            marker = {"OK": ".", "REDIRECT": "R", "NOT_FOUND": "X", "BLOCKED": "B",
                      "TIMEOUT": "T", "ERROR": "E"}.get(r.status, "?")
            anchor_marker = {"MATCH": "✓", "MISS": "✗", "n/a": " "}[r.anchor]
            print(f"  [{i:3d}/{len(urls)}] {marker}{anchor_marker} {r.url}", file=sys.stderr)

    md = render_markdown(results, args.readme)
    if args.out:
        args.out.write_text(md)
        print(f"wrote {args.out}", file=sys.stderr)
    else:
        print(md)

    if args.json:
        args.json.write_text(json.dumps([asdict(r) for r in results], indent=2))

    return 0


if __name__ == "__main__":
    sys.exit(main())
