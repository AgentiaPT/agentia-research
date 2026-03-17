# agentIA Research

**Open AI-Powered Research & Experiments**

> **Disclaimer:** All research and code in this repository is authored by [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (AI) with human direction and review. While factual accuracy and quality are prioritized, AI-generated content may contain errors, hallucinations, or outdated information. Sources and claims should be independently verified before relying on them.

Deep research, interactive explorations, and tools at the intersection of AI and software engineering. Each project pairs rigorous markdown research with self-contained interactive HTML pages you can open in any browser.

## Projects

| Project | Description | Live Demo | Status | Date |
|---------|-------------|-----------|--------|------|
| [Git Secret Detection & Leak Prevention](projects/9992-2026-03-17-git-secret-detection/) | Comprehensive landscape analysis of secret scanning tools, PII detection patterns, GitHub push protection, and AI-authored content risks | — | Complete | 2026-03-17 |
| [Hardening the Claude Code Sandbox](projects/9993-2026-03-17-claude-code-sandbox-hardening/) | Security research & practical guide: three custom hardening layers for the Claude Code sandbox — env stripping, filesystem deny lists, AFK guard | — | Complete | 2026-03-17 |
| [Self-Correction Experiment](projects/9994-2026-03-15-self-correction-experiment/) | Can LLMs genuinely improve code through self-reflection, or is it just resampling? Multi-condition empirical test | — | Draft | 2026-03-15 |
| [AI News Feed](projects/9995-2026-03-13-ai-news-feed/) | Curated AI news tracking 17+ voices, signals, and narratives shaping software engineering — Mar 8–13, 2026 | [Explorer](https://agentiapt.github.io/agentia-research/projects/9995-2026-03-13-ai-news-feed/explorer.html) | Complete | 2026-03-13 |
| [Self-Improvement vs. Gradient Descent](projects/9996-2026-03-14-self-improvement-gradient-descent/) | Theoretical investigation: are LLM self-critique loops formally analogous to gradient descent? | — | Complete | 2026-03-14 |
| [Inference-Time Compute Scaling](projects/9997-2026-03-14-inference-time-compute/) | Research survey on test-time compute scaling, process reward models, and inference-time search | — | Complete | 2026-03-14 |
| [LLM Self-Improvement](projects/9998-2026-03-14-llm-self-improvement/) | Deep survey on self-refinement, self-correction, and iterative improvement in LLMs | [Research](https://agentiapt.github.io/agentia-research/projects/9998-2026-03-14-llm-self-improvement/research.html) | Complete | 2026-03-14 |
| [CLAUDE.md Token Budget](projects/9999-2026-03-14-claudemd-token-budget/) | Analyzer for Claude Code context window usage — how much budget do config files consume? | [Dashboard](https://agentiapt.github.io/agentia-research/projects/9999-2026-03-14-claudemd-token-budget/dashboard.html) | Complete | 2026-03-14 |

## How It Works

Each project lives in its own directory under `projects/`, using a `NNNN-YYYY-MM-DD-slug` naming convention. Browse any project folder on GitHub to see its README rendered automatically.

**With Claude Code:** Clone this repo and start exploring.

```bash
git clone https://github.com/AgentiaPT/agentia-research.git
cd agentia-research
```

## Structure

```
projects/
  NNNN-YYYY-MM-DD-slug/
    README.md           # Project overview (renders on GitHub)
    explorer.html       # Optional: interactive page
    ...                 # Whatever the research produces
```

## License

Code is licensed under [Apache 2.0](LICENSE). Written content is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

---

Built by [agentIA](https://github.com/AgentiaPT) — exploring what's possible when AI and human curiosity work together.
