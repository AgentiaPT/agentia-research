#!/usr/bin/env python3
"""CLAUDE.md Token Budget Analyzer

Analyzes how much of Claude's context window your CLAUDE.md and related
config files consume per session. Estimates token counts, ranks sections
by cost, and suggests optimizations.

Usage:
    python analyze.py [path-to-repo-root]

Defaults to ../../ (the playground repo root) if no path given.
Outputs: report.md and dashboard.html in the same directory as this script.
"""

import os
import re
import sys
import json
from pathlib import Path
from dataclasses import dataclass, field

# Claude uses a BPE tokenizer. The widely-cited approximation is ~4 chars
# per token for English prose, but code/markdown tends to be ~3.5 chars/token
# due to special characters and formatting. We use 3.5 for a conservative
# (higher) estimate.
CHARS_PER_TOKEN = 3.5

# Claude Opus/Sonnet context window
CONTEXT_WINDOW = 200_000

# Typical system prompt overhead (Claude Code's own instructions, tool
# definitions, etc.) — estimated from observed behavior.
SYSTEM_PROMPT_TOKENS = 12_000


@dataclass
class Section:
    """A heading-delimited section of a markdown file."""
    heading: str
    level: int
    content: str
    char_count: int = 0
    token_estimate: int = 0

    def __post_init__(self):
        self.char_count = len(self.content)
        self.token_estimate = max(1, int(self.char_count / CHARS_PER_TOKEN))


@dataclass
class FileAnalysis:
    """Analysis of a single context file."""
    path: str
    relative_path: str
    content: str
    sections: list = field(default_factory=list)
    char_count: int = 0
    token_estimate: int = 0
    line_count: int = 0

    def __post_init__(self):
        self.char_count = len(self.content)
        self.token_estimate = max(1, int(self.char_count / CHARS_PER_TOKEN))
        self.line_count = self.content.count('\n') + (1 if self.content else 0)


def parse_sections(content: str) -> list[Section]:
    """Split markdown content into heading-delimited sections."""
    lines = content.split('\n')
    sections = []
    current_heading = "(preamble)"
    current_level = 0
    current_lines = []

    for line in lines:
        match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if match:
            if current_lines:
                text = '\n'.join(current_lines)
                sections.append(Section(
                    heading=current_heading,
                    level=current_level,
                    content=text,
                ))
            current_heading = match.group(2)
            current_level = len(match.group(1))
            current_lines = [line]
        else:
            current_lines.append(line)

    if current_lines:
        text = '\n'.join(current_lines)
        sections.append(Section(
            heading=current_heading,
            level=current_level,
            content=text,
        ))

    return sections


def find_context_files(repo_root: Path) -> list[tuple[str, Path]]:
    """Find all files that Claude Code loads into context."""
    files = []

    # CLAUDE.md at repo root
    claude_md = repo_root / "CLAUDE.md"
    if claude_md.exists():
        files.append(("CLAUDE.md (project instructions)", claude_md))

    # .claude/settings.json
    settings = repo_root / ".claude" / "settings.json"
    if settings.exists():
        files.append((".claude/settings.json", settings))

    # Skill files
    skills_dir = repo_root / ".claude" / "skills"
    if skills_dir.exists():
        for skill_file in sorted(skills_dir.glob("*/SKILL.md")):
            rel = skill_file.relative_to(repo_root)
            files.append((f"Skill: {skill_file.parent.name}", skill_file))

    # Hook scripts
    hooks_dir = repo_root / ".claude" / "hooks"
    if hooks_dir.exists():
        for hook_file in sorted(hooks_dir.glob("*")):
            if hook_file.is_file():
                rel = hook_file.relative_to(repo_root)
                files.append((f"Hook: {hook_file.name}", hook_file))

    return files


def analyze_file(label: str, path: Path, repo_root: Path) -> FileAnalysis:
    """Analyze a single context file."""
    content = path.read_text(encoding='utf-8', errors='replace')
    rel_path = str(path.relative_to(repo_root))
    analysis = FileAnalysis(
        path=str(path),
        relative_path=rel_path,
        content=content,
    )
    if path.suffix == '.md':
        analysis.sections = parse_sections(content)
    return analysis


def find_optimization_opportunities(analyses: list[FileAnalysis]) -> list[dict]:
    """Identify ways to reduce token usage."""
    opportunities = []

    for a in analyses:
        # Check for verbose sections
        for s in a.sections:
            if s.token_estimate > 200 and s.level >= 2:
                # Check for example blocks
                code_blocks = s.content.count('```')
                if code_blocks >= 2:
                    opportunities.append({
                        'file': a.relative_path,
                        'section': s.heading,
                        'type': 'verbose_examples',
                        'tokens': s.token_estimate,
                        'suggestion': f'Section "{s.heading}" uses {s.token_estimate} tokens with {code_blocks // 2} code blocks. Consider condensing examples.',
                        'potential_savings': int(s.token_estimate * 0.3),
                    })

            # Check for redundant/repeated phrasing
            if s.token_estimate > 150:
                words = s.content.lower().split()
                word_freq = {}
                for w in words:
                    if len(w) > 5:
                        word_freq[w] = word_freq.get(w, 0) + 1
                repeated = {w: c for w, c in word_freq.items() if c > 3}
                if repeated:
                    opportunities.append({
                        'file': a.relative_path,
                        'section': s.heading,
                        'type': 'repetition',
                        'tokens': s.token_estimate,
                        'suggestion': f'Section "{s.heading}" has repeated terms: {", ".join(list(repeated.keys())[:3])}. Tightening language could save tokens.',
                        'potential_savings': int(s.token_estimate * 0.15),
                    })

        # Check total file size
        if a.token_estimate > 1500:
            opportunities.append({
                'file': a.relative_path,
                'section': '(entire file)',
                'type': 'large_file',
                'tokens': a.token_estimate,
                'suggestion': f'{a.relative_path} is {a.token_estimate} tokens. Consider if all sections are essential for every session.',
                'potential_savings': int(a.token_estimate * 0.2),
            })

    opportunities.sort(key=lambda x: x['potential_savings'], reverse=True)
    return opportunities


def generate_report(analyses: list[FileAnalysis], opportunities: list[dict], repo_root: Path) -> str:
    """Generate the markdown report."""
    total_tokens = sum(a.token_estimate for a in analyses)
    total_chars = sum(a.char_count for a in analyses)
    budget_pct = (total_tokens / CONTEXT_WINDOW) * 100
    available_after = CONTEXT_WINDOW - SYSTEM_PROMPT_TOKENS - total_tokens
    total_savings = sum(o['potential_savings'] for o in opportunities)

    lines = [
        "# CLAUDE.md Token Budget Analysis",
        "",
        f"**Repo:** `{repo_root}`",
        f"**Date:** 2026-03-14",
        f"**Context window:** {CONTEXT_WINDOW:,} tokens (Claude Opus/Sonnet)",
        "",
        "## Summary",
        "",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Total config characters | {total_chars:,} |",
        f"| **Estimated tokens** | **{total_tokens:,}** |",
        f"| Context window used | {budget_pct:.1f}% |",
        f"| System prompt overhead (est.) | ~{SYSTEM_PROMPT_TOKENS:,} tokens |",
        f"| **Available for conversation** | **{available_after:,} tokens** ({available_after/CONTEXT_WINDOW*100:.1f}%) |",
        f"| Potential savings identified | ~{total_savings:,} tokens |",
        "",
        "## File Breakdown",
        "",
        "| File | Lines | Chars | Est. Tokens | % of Budget |",
        "|------|------:|------:|------------:|------------:|",
    ]

    for a in sorted(analyses, key=lambda x: x.token_estimate, reverse=True):
        pct = (a.token_estimate / CONTEXT_WINDOW) * 100
        lines.append(f"| `{a.relative_path}` | {a.line_count} | {a.char_count:,} | {a.token_estimate:,} | {pct:.2f}% |")

    lines.append("")
    lines.append("## Section-Level Breakdown (CLAUDE.md)")
    lines.append("")
    lines.append("| Section | Level | Tokens | % of File |")
    lines.append("|---------|------:|-------:|----------:|")

    claude_md = next((a for a in analyses if 'CLAUDE.md' in a.relative_path and a.sections), None)
    if claude_md:
        for s in sorted(claude_md.sections, key=lambda x: x.token_estimate, reverse=True):
            pct = (s.token_estimate / claude_md.token_estimate) * 100
            lines.append(f"| {s.heading} | H{s.level} | {s.token_estimate} | {pct:.1f}% |")

    lines.append("")
    lines.append("## Optimization Opportunities")
    lines.append("")

    if opportunities:
        for i, o in enumerate(opportunities, 1):
            lines.append(f"### {i}. {o['type'].replace('_', ' ').title()} — `{o['file']}`")
            lines.append("")
            lines.append(f"{o['suggestion']}")
            lines.append(f"")
            lines.append(f"**Potential savings:** ~{o['potential_savings']} tokens")
            lines.append("")
    else:
        lines.append("No significant optimization opportunities found. Your config is lean!")
        lines.append("")

    lines.append("## Methodology")
    lines.append("")
    lines.append(f"- Token estimation: `chars / {CHARS_PER_TOKEN}` (conservative for markdown/code)")
    lines.append(f"- System prompt overhead: ~{SYSTEM_PROMPT_TOKENS:,} tokens (estimated from observed Claude Code behavior)")
    lines.append("- Section parsing: H1–H6 heading boundaries in markdown files")
    lines.append("- This is an approximation — actual BPE tokenization may vary ±15%")
    lines.append("")

    return '\n'.join(lines)


def generate_dashboard(analyses: list[FileAnalysis], opportunities: list[dict]) -> str:
    """Generate a standalone HTML dashboard."""
    total_tokens = sum(a.token_estimate for a in analyses)
    budget_pct = (total_tokens / CONTEXT_WINDOW) * 100
    available = CONTEXT_WINDOW - SYSTEM_PROMPT_TOKENS - total_tokens
    total_savings = sum(o['potential_savings'] for o in opportunities)

    # Prepare data for charts
    file_data = json.dumps([
        {"name": a.relative_path, "tokens": a.token_estimate, "chars": a.char_count, "lines": a.line_count}
        for a in sorted(analyses, key=lambda x: x.token_estimate, reverse=True)
    ])

    claude_md = next((a for a in analyses if 'CLAUDE.md' in a.relative_path and a.sections), None)
    section_data = "[]"
    if claude_md:
        section_data = json.dumps([
            {"name": s.heading, "tokens": s.token_estimate, "level": s.level}
            for s in sorted(claude_md.sections, key=lambda x: x.token_estimate, reverse=True)
        ])

    opp_data = json.dumps([
        {"file": o['file'], "section": o['section'], "type": o['type'], "savings": o['potential_savings'], "suggestion": o['suggestion']}
        for o in opportunities
    ])

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CLAUDE.md Token Budget Dashboard</title>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
:root {{
  --bg: #0f1117;
  --card: #1a1d27;
  --border: #2a2d3a;
  --text: #e0e0e0;
  --muted: #8890a0;
  --accent: #6c8cff;
  --green: #4caf50;
  --red: #ef5350;
  --orange: #ff9800;
  --yellow: #ffd54f;
  --purple: #b388ff;
}}
body {{
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.6;
  padding: 24px;
  max-width: 1200px;
  margin: 0 auto;
}}
h1 {{
  font-size: 1.8rem;
  font-weight: 700;
  background: linear-gradient(135deg, var(--accent), var(--purple));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 8px;
}}
.subtitle {{ color: var(--muted); margin-bottom: 32px; font-size: 0.9rem; }}
.grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-bottom: 32px; }}
.stat-card {{
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 20px;
}}
.stat-card .label {{ color: var(--muted); font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em; }}
.stat-card .value {{ font-size: 1.8rem; font-weight: 700; margin-top: 4px; }}
.stat-card .detail {{ color: var(--muted); font-size: 0.8rem; margin-top: 4px; }}
.accent {{ color: var(--accent); }}
.green {{ color: var(--green); }}
.orange {{ color: var(--orange); }}
.red {{ color: var(--red); }}
.section {{ margin-bottom: 32px; }}
.section h2 {{
  font-size: 1.2rem;
  font-weight: 600;
  margin-bottom: 16px;
  color: var(--text);
}}
.bar-chart {{ background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 20px; }}
.bar-row {{ display: flex; align-items: center; margin-bottom: 12px; gap: 12px; }}
.bar-label {{ min-width: 200px; font-size: 0.85rem; color: var(--muted); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
.bar-track {{ flex: 1; height: 28px; background: var(--bg); border-radius: 6px; position: relative; overflow: hidden; }}
.bar-fill {{ height: 100%; border-radius: 6px; display: flex; align-items: center; padding: 0 8px; font-size: 0.75rem; font-weight: 600; color: white; min-width: fit-content; transition: width 0.5s ease; }}
.bar-value {{ min-width: 80px; text-align: right; font-size: 0.85rem; font-weight: 600; font-variant-numeric: tabular-nums; }}
.budget-bar {{
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 20px;
  margin-bottom: 32px;
}}
.budget-track {{
  width: 100%;
  height: 40px;
  background: var(--bg);
  border-radius: 8px;
  overflow: hidden;
  display: flex;
  margin-top: 12px;
}}
.budget-segment {{
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.7rem;
  font-weight: 600;
  color: white;
  white-space: nowrap;
  overflow: hidden;
}}
.legend {{ display: flex; gap: 20px; margin-top: 12px; flex-wrap: wrap; }}
.legend-item {{ display: flex; align-items: center; gap: 6px; font-size: 0.8rem; color: var(--muted); }}
.legend-dot {{ width: 10px; height: 10px; border-radius: 3px; }}
.opp-card {{
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 16px 20px;
  margin-bottom: 12px;
}}
.opp-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; }}
.opp-type {{ font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--orange); font-weight: 600; }}
.opp-savings {{ font-size: 0.85rem; font-weight: 600; color: var(--green); }}
.opp-suggestion {{ font-size: 0.85rem; color: var(--muted); }}
.methodology {{
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 20px;
  font-size: 0.85rem;
  color: var(--muted);
}}
.methodology code {{ color: var(--accent); font-family: "SF Mono", "Fira Code", monospace; font-size: 0.8rem; }}
@media (max-width: 600px) {{
  body {{ padding: 16px; }}
  .grid {{ grid-template-columns: 1fr 1fr; }}
  .bar-label {{ min-width: 120px; font-size: 0.75rem; }}
}}
::-webkit-scrollbar {{ width: 6px; }}
::-webkit-scrollbar-track {{ background: var(--bg); }}
::-webkit-scrollbar-thumb {{ background: var(--border); border-radius: 3px; }}
</style>
</head>
<body>

<h1>CLAUDE.md Token Budget</h1>
<p class="subtitle">How much context window does your config consume?</p>

<div class="grid">
  <div class="stat-card">
    <div class="label">Config Tokens</div>
    <div class="value accent">{total_tokens:,}</div>
    <div class="detail">{budget_pct:.1f}% of context window</div>
  </div>
  <div class="stat-card">
    <div class="label">System Overhead</div>
    <div class="value" style="color: var(--purple)">~{SYSTEM_PROMPT_TOKENS:,}</div>
    <div class="detail">Claude Code internals (est.)</div>
  </div>
  <div class="stat-card">
    <div class="label">Available</div>
    <div class="value green">{available:,}</div>
    <div class="detail">{available/CONTEXT_WINDOW*100:.1f}% for your conversation</div>
  </div>
  <div class="stat-card">
    <div class="label">Potential Savings</div>
    <div class="value orange">~{total_savings:,}</div>
    <div class="detail">{len(opportunities)} optimizations found</div>
  </div>
</div>

<div class="budget-bar">
  <h2>Context Window Budget</h2>
  <div class="budget-track">
    <div class="budget-segment" style="width: {SYSTEM_PROMPT_TOKENS/CONTEXT_WINDOW*100}%; background: var(--purple);">System</div>
    <div class="budget-segment" style="width: {total_tokens/CONTEXT_WINDOW*100}%; background: var(--accent);">Config</div>
    <div class="budget-segment" style="width: {available/CONTEXT_WINDOW*100}%; background: var(--green); opacity: 0.3;">Available</div>
  </div>
  <div class="legend">
    <div class="legend-item"><div class="legend-dot" style="background: var(--purple);"></div>System prompt (~{SYSTEM_PROMPT_TOKENS:,})</div>
    <div class="legend-item"><div class="legend-dot" style="background: var(--accent);"></div>Your config ({total_tokens:,})</div>
    <div class="legend-item"><div class="legend-dot" style="background: var(--green); opacity: 0.3;"></div>Available ({available:,})</div>
  </div>
</div>

<div class="section">
  <h2>Token Usage by File</h2>
  <div class="bar-chart" id="file-chart"></div>
</div>

<div class="section">
  <h2>CLAUDE.md Section Breakdown</h2>
  <div class="bar-chart" id="section-chart"></div>
</div>

<div class="section">
  <h2>Optimization Opportunities</h2>
  <div id="opportunities"></div>
</div>

<div class="methodology">
  <h2 style="margin-bottom: 12px;">Methodology</h2>
  <p>Token estimation: <code>chars / {CHARS_PER_TOKEN}</code> (conservative for markdown/code). System prompt overhead estimated from observed Claude Code behavior. Actual BPE tokenization may vary ±15%.</p>
</div>

<script>
const fileData = {file_data};
const sectionData = {section_data};
const oppData = {opp_data};
const CONTEXT_WINDOW = {CONTEXT_WINDOW};
const colors = ['#6c8cff', '#b388ff', '#4caf50', '#ff9800', '#ef5350', '#ffd54f', '#26a69a', '#ec407a'];

function renderBars(containerId, data, maxVal) {{
  const container = document.getElementById(containerId);
  if (!data.length) {{ container.innerHTML = '<p style="color: var(--muted); padding: 8px;">No data</p>'; return; }}
  const max = maxVal || Math.max(...data.map(d => d.tokens));
  container.innerHTML = data.map((d, i) => `
    <div class="bar-row">
      <div class="bar-label" title="${{d.name}}">${{d.name}}</div>
      <div class="bar-track">
        <div class="bar-fill" style="width: ${{Math.max(2, d.tokens/max*100)}}%; background: ${{colors[i % colors.length]}};">
          ${{d.tokens > max * 0.15 ? d.tokens.toLocaleString() : ''}}
        </div>
      </div>
      <div class="bar-value">${{d.tokens.toLocaleString()}} tk</div>
    </div>
  `).join('');
}}

function renderOpportunities() {{
  const container = document.getElementById('opportunities');
  if (!oppData.length) {{
    container.innerHTML = '<div class="opp-card"><p style="color: var(--green);">No significant optimizations found — your config is lean!</p></div>';
    return;
  }}
  container.innerHTML = oppData.map(o => `
    <div class="opp-card">
      <div class="opp-header">
        <span class="opp-type">${{o.type.replace(/_/g, ' ')}}</span>
        <span class="opp-savings">~${{o.savings.toLocaleString()}} tokens saveable</span>
      </div>
      <div class="opp-suggestion">${{o.suggestion}}</div>
    </div>
  `).join('');
}}

renderBars('file-chart', fileData);
renderBars('section-chart', sectionData);
renderOpportunities();
</script>

</body>
</html>'''


def main():
    script_dir = Path(__file__).parent
    if len(sys.argv) > 1:
        repo_root = Path(sys.argv[1]).resolve()
    else:
        repo_root = (script_dir / ".." / "..").resolve()

    print(f"Analyzing: {repo_root}")

    context_files = find_context_files(repo_root)
    if not context_files:
        print("No CLAUDE.md or .claude/ config found.")
        sys.exit(1)

    analyses = []
    for label, path in context_files:
        a = analyze_file(label, path, repo_root)
        analyses.append(a)
        print(f"  {a.relative_path}: {a.char_count:,} chars → ~{a.token_estimate:,} tokens")

    total = sum(a.token_estimate for a in analyses)
    print(f"\nTotal config tokens: ~{total:,} / {CONTEXT_WINDOW:,} ({total/CONTEXT_WINDOW*100:.1f}%)")

    opportunities = find_optimization_opportunities(analyses)
    if opportunities:
        print(f"Found {len(opportunities)} optimization opportunities")

    report = generate_report(analyses, opportunities, repo_root)
    report_path = script_dir / "report.md"
    report_path.write_text(report)
    print(f"\nReport: {report_path}")

    dashboard = generate_dashboard(analyses, opportunities)
    dashboard_path = script_dir / "dashboard.html"
    dashboard_path.write_text(dashboard)
    print(f"Dashboard: {dashboard_path}")


if __name__ == "__main__":
    main()
