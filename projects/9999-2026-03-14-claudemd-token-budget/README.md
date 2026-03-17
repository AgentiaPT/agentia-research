---
title: "CLAUDE.md Token Budget Analyzer"
date: 2026-03-14
status: complete
tags: [ai, claude-code, tokens, context-window, tooling]
---

# CLAUDE.md Token Budget Analyzer

> **Note:** This project was authored by [Claude Code](https://claude.ai/claude-code) (AI) with human direction and review. While factual accuracy and quality were prioritized, AI-generated content may contain errors, hallucinations, or outdated information. Sources and claims should be independently verified before relying on them.

How much of Claude's 200K context window do `CLAUDE.md` and config files consume before the conversation even starts?

## What This Does

Scans a repo's Claude Code configuration files (`CLAUDE.md`, skills, hooks, settings) and:

1. **Estimates token usage** per file and per markdown section
2. **Identifies optimization opportunities** — verbose examples, repetition, oversized files
3. **Generates a markdown report** with tables and rankings
4. **Generates a standalone HTML dashboard** with visual bar charts and a context budget breakdown

## Run It

```bash
python3 analyze.py                    # analyzes ../../ (repo root)
python3 analyze.py /path/to/repo      # analyzes a specific repo
```

Outputs `report.md` and `dashboard.html` in this directory.

## Key Findings (This Repo)

- **Total config: ~3,193 tokens** (1.6% of 200K context window)
- **CLAUDE.md dominates** at 1,775 tokens (56% of config budget)
- Largest CLAUDE.md sections: File Organization, Research Conventions, Interactive HTML Standards
- **5 optimization opportunities** identified, ~780 tokens potentially saveable
- After system prompt overhead (~12K), **~184K tokens remain** for conversation

## Files

| File | Purpose |
|------|---------|
| `analyze.py` | Python analyzer — zero dependencies, runs anywhere |
| `report.md` | Generated markdown report with tables |
| `dashboard.html` | Standalone HTML dashboard — open in any browser |
| `README.md` | This file |
