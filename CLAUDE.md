# agentIA Research

AI-powered research repository and playground. Each topic produces deep markdown research and, when appropriate, a self-contained interactive HTML page. Sessions are typically started from mobile via Claude Code web, so prompts may be brief — the agent must be self-sufficient and proactive within these rules.

> **⚠️ PUBLIC REPOSITORY** — This repo is publicly visible on GitHub. Every commit, file, and piece of git history is permanently exposed to the internet. All rules below reflect this reality. When in doubt, leave it out.

## Agent Interaction Rules

- **Always use AskUserQuestion tool** to interact with the user — never output bare questions in text.
- **One question at a time** — never batch multiple questions in a single ask.
- **Status updates** at natural milestones during long tasks so progress is visible on mobile.
- **GitHub file links** — whenever mentioning a committed file in chat output, always include a clickable GitHub link to the file on the current branch. Format: `https://github.com/<owner>/<repo>/blob/<branch>/<path>`. Derive `<owner>/<repo>` from the git remote. This is critical for mobile users who can't easily navigate the file tree.
- **NEVER push to remote without explicit user permission** — this is the single most important safety rule. Commit freely, but treat `git push` as a privileged action that requires the user to say "push", "push it", "send it", or equivalent. Completing a task is NOT permission to push. Being told to "commit" is NOT permission to push. When in doubt, don't push.
- Adapt output format to the task: code, markdown reports, interactive HTML, essays — whatever fits.

## Skills

- `/new-experiment [topic-slug]` — scaffold a new `projects/NNNN-YYYY-MM-DD-<topic>/` directory and get started.
- `/new-research <topic-slug>` — scaffold a new `projects/NNNN-YYYY-MM-DD-<topic>/` directory and begin research immediately.
- `/lisa-loop [minutes] [task]` — force minimum working time with reflection, self-critique, and improvement cycles. Uses bash timestamps — no `sleep` or `while true`.
- `/fact-check [file-or-topic]` — multi-pass verification of all external claims, quotes, and URLs. Uses Playwright for dynamic pages.

## Repository Structure

- `projects/` — All project and research folders (NNNN-date-slug convention)
- `scripts/` — Build scripts (index generation, etc.)

## Task Types

Not everything needs a new folder:

- **Research topics** — new topic folders under `projects/`, the core use case.
- **Experiments & projects** — new folders under `projects/` for code-heavy work.
- **Playground improvements** — changes to CLAUDE.md, hooks, scripts, repo config. Work directly on existing files.
- **Maintenance** — cleanup, reorganization, fixing broken links or outdated content.

## Project Conventions

Projects live in `projects/NNNN-YYYY-MM-DD-<slug>/` using kebab-case names.

Every project has a `README.md` with YAML frontmatter:

```yaml
---
title: "Project Title"
date: YYYY-MM-DD
status: draft | complete | ongoing
tags: [tag1, tag2]
---
```

**AI authorship disclaimer** — every project README **must** include the following blockquote immediately after the first `#` heading:

```markdown
> **Note:** This project was authored by [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (AI) with human direction and review. While factual accuracy and quality were prioritized, AI-generated content may contain errors, hallucinations, or outdated information. Sources and claims should be independently verified before relying on them.
```

This is non-negotiable for a public repository where most content is AI-generated. Never omit it.

The `ongoing` status is for periodic/living research that receives new editions over time (e.g., news feeds, trend tracking). These projects are never "complete" — they accumulate dated entries in an `editions/` subdirectory.

Content can live in the README itself (simple projects) or in separate files alongside it (long-form essays, multi-file research). Interactive pages go in the same directory (e.g., `explorer.html`, `simulator.html`).

**HTML file links** — all links to `.html` files in project READMEs, the root README, and anywhere in the repo **must** use the GitHub Pages URL so they render as live pages, not raw source. Format: `https://agentiapt.github.io/agentia-research/projects/<folder>/<file>.html`. Never link to HTML files using relative paths or `github.com/...blob/...` URLs — GitHub shows raw HTML source for those.

When a project is added or completed, update the root README projects table.

## File Organization (Projects)

Experiment/project folders live inside `projects/` — never at the repo root.

Use **flat** `projects/NNNN-YYYY-MM-DD-<topic-slug>/` folders.

- **NNNN** — a 4-digit counter that counts **down** from 9999. The newest experiment gets the lowest number, so it sorts first on GitHub (which sorts A→Z).
- **YYYY-MM-DD** — the creation date, for human readability.
- **topic-slug** — descriptive kebab-case name.

Example sequence:
```
projects/
├── 9997-2026-03-14-llm-evaluation/      ← newest, sorts first
├── 9998-2026-03-13-web-scraping/
└── 9999-2026-03-12-prompt-injection/     ← oldest, sorts last
```

### How the agent assigns numbers

When creating a new experiment folder, the agent must check **all branches** — not just the current one — to avoid number collisions between parallel sessions:

1. **Fetch all remote refs**: run `git fetch origin --prune` to get the latest state of all remote branches (retry up to 4 times with exponential backoff on network failure). This is critical — stale refs can cause collisions.
2. **Scan the current working tree**: list `projects/NNNN-*` folders.
3. **Scan all remote branches**: run `git branch -r | grep 'origin/'` to list remote branches, then for each: `git ls-tree -d --name-only <branch> -- projects/ | grep -E '^projects/[0-9]{4}-'` to find experiment folders. This catches folders created on other `claude/*` session branches that haven't been merged yet.
4. **Collect all NNNN prefixes** from both sources (deduplicate). Extract the 4-digit prefix from each folder name.
5. Find the **lowest** existing NNNN prefix across all branches.
6. Subtract 1 to get the new folder's prefix.
7. If no experiment folders exist on any branch, start at `9999`.

> **Why this matters**: Multiple Claude Code sessions run in parallel on separate `claude/*` branches. Without checking origin, two sessions could independently pick the same number, causing merge conflicts later.

## Tech Stack & Quality

Mixed stack — Python, Node/TypeScript, shell, HTML, markdown. Varies per experiment.

Pragmatic quality: clean code, meaningful names, working results. No formal linting or testing ceremony — this is a playground, not production.

## External Sources & Citations

All external insights must be validated and tracked:

- **Track all sources** — add inline links near where the information is used.
- **Exact quotes only** — never paraphrase. Use blockquotes for direct citations.
- **Text fragment URLs** — every source link **must** use the `#:~:text=` fragment syntax to highlight the exact passage on the page. Format: `https://example.com/page#:~:text=exact%20quoted%20text`. This applies to all external content links, quotations, and cited insights. Never link to just a page root or section anchor when a text fragment can pinpoint the source.
- **Dynamic page verification** — if a page cannot be fetched via curl (e.g., JS-rendered content), use Playwright or Playwright CLI to retrieve actual contents.
- **Multi-pass verification** — iterate until every external insight has been verified against its source. No unverified claims in final output.

## Research Conventions

When a task involves research or analysis:

- **Multi-perspective analysis** — present multiple viewpoints, include contrarian positions. Never one-sided.
- **Scoring and tier frameworks** — use quantified ratings (e.g., 9/10, Tier 1-4) when comparing options or evaluating claims.
- **Concrete data points** — include statistics, dates, numbers, and citations. No vague assertions.
- **Structure**: framework first, then evidence, then synthesis.
- **Voice diversity** — when surveying a topic, include named experts/practitioners with their actual positions, not generic summaries.
- **Living research** — for ongoing topics, use dated entries within the project folder (e.g., `editions/2026-03-14.md`).
- For long-form essays: use modular sections, subdirectories for sections/sources when needed.

## Interactive HTML Standards

When a topic or experiment needs a UI, build self-contained single HTML files — all CSS and JS inline, no build step, and no external network dependencies (use system fonts or locally embedded fonts, e.g., Inter served from the same file).

Use the following design system:

```css
:root {
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
}
```

Key visual patterns:
- Dark theme with gradient text headings (`linear-gradient(135deg, var(--accent), var(--purple))`)
- Card components: `background: var(--card)`, `border: 1px solid var(--border)`, `border-radius: 12px`
- Font: `'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`
- Responsive layout: sidebar + main area grid, collapsing on mobile
- Thin scrollbars: `scrollbar-width: thin; scrollbar-color: var(--border) transparent`

Must work offline.

## Security & Sensitive Information

This is a **public repository** — treat every committed byte as permanently visible to the world.

- **No secrets in code or content** — never hardcode API keys, tokens, passwords, or credentials, even in examples or comments. Use placeholder values like `YOUR_API_KEY_HERE` or `<token>` if illustrating an API call.
- **No real personal data** — never include real names, email addresses, IP addresses, phone numbers, or any PII in research content, sample data, or code. Use synthetic or anonymized data instead.
- **No internal/private URLs** — never commit staging endpoints, org-internal links, private dashboards, or any URL that reveals infrastructure not intended to be public.
- **Sensitive topic caution** — when research covers security exploits, vulnerabilities, or attack techniques, keep content educational and analytical. Never produce ready-made exploit code, working attack scripts, or step-by-step intrusion instructions.
- **Git history is forever** — once something is committed and pushed, it lives in the public git history permanently. Deleting a file does not remove it from `git log`. Think before committing.
- **Review before commit** — before staging files, mentally audit for anything that shouldn't be public: credentials, PII, internal URLs, sensitive metadata, overly detailed exploit code.

## Git Workflow

> **⛔ CRITICAL: NEVER run `git push` unless the user has explicitly asked you to push in the current message or a recent message.** This is the #1 safety rule for this public repository. Violations expose unreviewed AI-generated content permanently to the internet. "Commit your work", "finish up", "wrap up", or completing a task are NOT push permission. Only explicit push language ("push", "push it", "send it to remote", "push to origin") counts.

- **Auto-commit** completed work without asking.
- **NEVER auto-push** — only push to the remote when the user explicitly requests it. This is a safety gate for a public repository. If you are unsure whether the user wants you to push, **do not push** — ask first using AskUserQuestion.
- Branch naming: `claude/<descriptive-slug>-<id>` (handled by the session).
- Commit messages: concise, descriptive, no ceremony.

## SessionStart Hook

Playwright and browsers are installed at session start. See `.claude/hooks/session-start.sh`.

## What NOT to Commit

- `.env` files, credentials, API keys, secrets
- `node_modules/`, `__pycache__/`, build artifacts
- Large binaries: model weights, datasets, checkpoint files
- IDE configuration (`.vscode/`, `.idea/`)
