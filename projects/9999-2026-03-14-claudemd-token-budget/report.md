# CLAUDE.md Token Budget Analysis

**Repo:** `/home/user/claude-code-playground`
**Date:** 2026-03-14
**Context window:** 200,000 tokens (Claude Opus/Sonnet)

## Summary

| Metric | Value |
|--------|-------|
| Total config characters | 11,185 |
| **Estimated tokens** | **3,193** |
| Context window used | 1.6% |
| System prompt overhead (est.) | ~12,000 tokens |
| **Available for conversation** | **184,807 tokens** (92.4%) |
| Potential savings identified | ~625 tokens |

## File Breakdown

| File | Lines | Chars | Est. Tokens | % of Budget |
|------|------:|------:|------------:|------------:|
| `CLAUDE.md` | 124 | 6,215 | 1,775 | 0.89% |
| `.claude/skills/fact-check/SKILL.md` | 47 | 1,795 | 512 | 0.26% |
| `.claude/skills/lisa-loop/SKILL.md` | 44 | 1,631 | 466 | 0.23% |
| `.claude/skills/new-experiment/SKILL.md` | 33 | 1,044 | 298 | 0.15% |
| `.claude/hooks/session-start.sh` | 12 | 275 | 78 | 0.04% |
| `.claude/settings.json` | 15 | 225 | 64 | 0.03% |

## Section-Level Breakdown (CLAUDE.md)

| Section | Level | Tokens | % of File |
|---------|------:|-------:|----------:|
| How the agent assigns numbers | H3 | 376 | 21.2% |
| Research Conventions | H2 | 209 | 11.8% |
| Interactive HTML Standards | H2 | 192 | 10.8% |
| External Sources & Citations | H2 | 186 | 10.5% |
| File Organization | H2 | 180 | 10.1% |
| Skills | H2 | 122 | 6.9% |
| Agent Interaction Rules | H2 | 116 | 6.5% |
| Task Types | H2 | 103 | 5.8% |
| Claude Code Playground | H1 | 74 | 4.2% |
| Tech Stack & Quality | H2 | 72 | 4.1% |
| Git Workflow | H2 | 60 | 3.4% |
| What NOT to Commit | H2 | 44 | 2.5% |
| SessionStart Hook | H2 | 33 | 1.9% |

## Optimization Opportunities

### 1. Large File — `CLAUDE.md`

CLAUDE.md is 1775 tokens. Consider if all sections are essential for every session.

**Potential savings:** ~355 tokens

### 2. Verbose Examples — `.claude/skills/fact-check/SKILL.md`

Section "Protocol" uses 301 tokens with 1 code blocks. Consider condensing examples.

**Potential savings:** ~90 tokens

### 3. Verbose Examples — `.claude/skills/lisa-loop/SKILL.md`

Section "Protocol" uses 215 tokens with 2 code blocks. Consider condensing examples.

**Potential savings:** ~64 tokens

### 4. Verbose Examples — `.claude/skills/new-experiment/SKILL.md`

Section "Steps" uses 203 tokens with 1 code blocks. Consider condensing examples.

**Potential savings:** ~60 tokens

### 5. Repetition — `CLAUDE.md`

Section "How the agent assigns numbers" has repeated terms: remote. Tightening language could save tokens.

**Potential savings:** ~56 tokens

## Methodology

- Token estimation: `chars / 3.5` (conservative for markdown/code)
- System prompt overhead: ~12,000 tokens (estimated from observed Claude Code behavior)
- Section parsing: H1–H6 heading boundaries in markdown files
- This is an approximation — actual BPE tokenization may vary ±15%
