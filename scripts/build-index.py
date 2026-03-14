#!/usr/bin/env python3
"""Generate projects/index.json from project README.md frontmatter."""

import json
import os
import re
from datetime import datetime, timezone


PROJECTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "projects")


def parse_frontmatter(text):
    """Extract YAML frontmatter from markdown text, parsed manually."""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return {}, text
    raw = m.group(1)
    body = text[m.end():]
    meta = {}
    for line in raw.splitlines():
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        key = key.strip()
        val = val.strip()
        if key == "tags":
            # parse [tag1, tag2] format
            inner = re.search(r"\[(.*?)\]", val)
            if inner:
                meta[key] = [t.strip().strip("'\"") for t in inner.group(1).split(",") if t.strip()]
            else:
                meta[key] = []
        else:
            # strip surrounding quotes
            val = val.strip("'\"")
            meta[key] = val
    return meta, body


def extract_description(body):
    """Extract first real paragraph after frontmatter (skip headings, metadata, separators, etc.)."""
    for para in body.split("\n\n"):
        para = para.strip()
        if not para or para.startswith("#"):
            continue
        # Skip horizontal rules
        if re.match(r"^-{3,}$", para):
            continue
        # Skip metadata-looking lines: **Key:** value or **Key**: value
        if re.match(r"^\*\*\w+[\*:]", para):
            continue
        # Skip very short bold-only lines (subtitles like **A Research Survey**)
        if re.match(r"^\*\*.+\*\*$", para) and len(para) < 100:
            continue
        # Skip table of contents / numbered lists of links
        if re.match(r"^1\.\s+\[", para):
            continue
        # Collapse whitespace within the paragraph
        return re.sub(r"\s+", " ", para)
    return ""


def extract_slug(folder_name):
    """Extract slug from NNNN-YYYY-MM-DD-slug format."""
    m = re.match(r"^\d{4}-\d{4}-\d{2}-\d{2}-(.+)$", folder_name)
    return m.group(1) if m else folder_name


def main():
    projects = []

    if not os.path.isdir(PROJECTS_DIR):
        os.makedirs(PROJECTS_DIR, exist_ok=True)

    for entry in sorted(os.listdir(PROJECTS_DIR)):
        entry_path = os.path.join(PROJECTS_DIR, entry)
        if not os.path.isdir(entry_path):
            continue
        # Only process NNNN-dated folders
        if not re.match(r"^\d{4}-\d{4}-\d{2}-\d{2}-", entry):
            continue

        # Find the markdown source
        md_path = None
        for candidate in ("README.md",):
            p = os.path.join(entry_path, candidate)
            if os.path.isfile(p):
                md_path = p
                break

        meta = {}
        description = ""
        if md_path:
            with open(md_path, "r", encoding="utf-8") as f:
                text = f.read()
            meta, body = parse_frontmatter(text)
            description = extract_description(body)

        # Collect files
        files = sorted(f for f in os.listdir(entry_path) if os.path.isfile(os.path.join(entry_path, f)))
        html_files = [f for f in files if f.endswith(".html")]

        projects.append({
            "id": entry,
            "slug": extract_slug(entry),
            "title": meta.get("title", entry),
            "date": meta.get("date", ""),
            "status": meta.get("status", ""),
            "tags": meta.get("tags", []),
            "description": description,
            "files": files,
            "htmlFiles": html_files,
            "path": f"projects/{entry}",
        })

    output = {
        "generated": datetime.now(timezone.utc).isoformat(),
        "projects": projects,
    }

    out_path = os.path.join(PROJECTS_DIR, "index.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Wrote {len(projects)} projects to {out_path}")


if __name__ == "__main__":
    main()
