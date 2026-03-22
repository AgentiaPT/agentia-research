## 8. Open Source Under Pressure

Three tensions colliding simultaneously.

### Corporate Acquisition

OpenAI [acquires Astral](https://openai.com/index/openai-to-acquire-astral/) (Mar 19) — uv, ruff, ty. Community anxiety: 757 HN points, "overwhelmingly anxious." The fear articulated on Hacker News: "tools don't break, they just stop evolving for independent use cases and start evolving for Codex's use case."

Anthropic [acquired Bun](https://bun.com/blog/bun-joins-anthropic) (Dec 2025) — the JS runtime powering Claude Code. $0 revenue, $26M raised, now fully funded by Anthropic. Pattern: AI companies buying the language toolchains their products run on.

### AI Slop Attacks

Daniel Stenberg ended cURL's bug bounty program after AI-generated spam overwhelmed maintainers (Jan 2026). Roughly **20%** of all submissions were AI slop; only **5%** identified genuine vulnerabilities. Stenberg:

> "We need to make moves to ensure our survival and intact mental health"

Willison at the Pragmatic Summit (Mar 14): projects flooded with spam PRs, people trying to "convince GitHub to disable pull requests entirely." Not just cURL — the Python Software Foundation, React, and Apache Airflow all face the same problem.

Sources: [The New Stack](https://thenewstack.io/curls-daniel-stenberg-ai-is-ddosing-open-source-and-fixing-its-bugs/#:~:text=ensure%20our%20survival) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/curl-ending-bug-bounty-program-after-flood-of-ai-slop-reports/)

### The Ironic Counter-Move (March 20)

AI companies began [funding $12.5M in open source security grants](https://www.resultsense.com/news/2026-03-20-ai-companies-fund-open-source-security) through Alpha-Omega and OpenSSF. The companies whose tools generate the spam are now funding grants to help overworked maintainers deal with it.

**Why this matters:** Open source is simultaneously the foundation of agentic engineering ("agents love open source" — Willison) AND under threat from both AI spam and corporate acquisition. The irony isn't lost on anyone.

---
