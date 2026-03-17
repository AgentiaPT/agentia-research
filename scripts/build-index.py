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
        # Skip blockquotes (e.g. AI authorship disclaimer)
        if para.startswith(">"):
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

    # Generate projects/README.md (full catalog)
    generate_projects_readme(projects)

    # Update root README.md (latest 10)
    update_root_readme(projects[:10])


PAGES_BASE = "https://agentiapt.github.io/agentia-research"


def make_table_row(p, relative_to_root=True):
    """Build a markdown table row for a project."""
    title = p["title"]
    folder = p["id"]
    path_prefix = "projects/" if relative_to_root else ""
    desc = p["description"][:120] + ("..." if len(p["description"]) > 120 else "")
    status = (p["status"] or "—").capitalize()
    date = p["date"] or "—"

    # Live demo links
    demos = []
    for f in p.get("htmlFiles", []):
        label = f.replace(".html", "").replace("-", " ").replace("_", " ").title()
        demos.append(f"[{label}]({PAGES_BASE}/projects/{folder}/{f})")
    demo_col = ", ".join(demos) if demos else "—"

    return f"| [{title}]({path_prefix}{folder}/) | {desc} | {demo_col} | {status} | {date} |"


def generate_projects_readme(projects):
    """Generate projects/README.md with full project catalog."""
    header = """# Projects

> **Note:** All projects are authored by [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (AI) with human direction and review. Content may contain errors — verify independently.

Complete catalog of all research projects, newest first.

| Project | Description | Live Demo | Status | Date |
|---------|-------------|-----------|--------|------|
"""
    rows = [make_table_row(p, relative_to_root=False) for p in projects]

    readme_path = os.path.join(PROJECTS_DIR, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(header)
        f.write("\n".join(rows))
        f.write("\n")

    print(f"Wrote projects/README.md with {len(projects)} projects")


def update_root_readme(projects):
    """Update the projects table in the root README.md (between markers)."""
    root = os.path.dirname(PROJECTS_DIR)
    readme_path = os.path.join(root, "README.md")

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    table_header = "| Project | Description | Live Demo | Status | Date |\n|---------|-------------|-----------|--------|------|\n"
    rows = [make_table_row(p, relative_to_root=True) for p in projects]
    table = table_header + "\n".join(rows)

    # Replace between markers
    begin = "<!-- BEGIN PROJECTS -->"
    end = "<!-- END PROJECTS -->"
    start_idx = content.find(begin)
    end_idx = content.find(end)

    if start_idx == -1 or end_idx == -1:
        print("WARNING: Could not find project markers in README.md")
        return

    new_content = content[:start_idx + len(begin)] + "\n" + table + "\n" + content[end_idx:]

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Updated root README.md with {len(projects)} latest projects")


if __name__ == "__main__":
    main()
