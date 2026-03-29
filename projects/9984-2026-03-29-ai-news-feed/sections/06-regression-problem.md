## 6. The Regression Problem — Agents Break What They Fix

Two papers published in March converge on the same uncomfortable finding: AI coding agents that pass all tests on individual patches still break codebases over time. The question isn't whether agents can fix bugs — it's whether they can maintain software.

### SWE-CI: 75% Break Working Code
**March 4 | [arXiv:2603.03823](https://arxiv.org/abs/2603.03823) · [AwesomeAgents](https://awesomeagents.ai/news/alibaba-swe-ci-ai-coding-agents-long-term-maintenance/)**

Authors **Jialong Chen, Xander Xu** (equal contributors), **Hu Wei, Chuan Chen, Bing Zhao** (Sun Yat-sen University & Alibaba Group) built the first benchmark on the **Continuous Integration loop** — not isolated patches, but sequential commits to the same codebase over months.

The setup: **18 models from 8 providers** across **100 real Python repositories**, each spanning approximately **233 days and 71 consecutive commits**. The benchmark introduces **EvoScore**, a metric that penalizes short-term optimization and weights later iterations more heavily.

The results:

- **75% of AI coding agents** break previously working code during long-term maintenance — even when their patches initially pass all tests
- Only **two Claude Opus models** exceed a 50% zero-regression rate
- **Every other model** falls below 25%

The implication: passing tests on a single PR is necessary but radically insufficient. Codebases are evolving systems, and agents that optimize locally can degrade globally.

### TDAD: Test-Driven Agentic Development
**March 18 | [arXiv:2603.17973](https://arxiv.org/abs/2603.17973)**

Authors **Pepe Alonso and Victor A. Braberman** offer a mitigation: build a **dependency graph between source code and tests** so agents know which tests to verify before committing patches.

The results on SWE-bench Verified:

- **70% reduction** in test-level regressions (6.08% → 1.82%)
- Issue-resolution rate improved from **24% to 32%** when deployed as an agent skill

But the most provocative finding is the **TDD prompting paradox**: giving agents procedural TDD instructions *without* targeted test context actually **increased** regressions to 9.94% — worse than no intervention at all. Agents need to know **which tests** to check, not **how** to do TDD. Process without context is counterproductive.

### The Quality Data

Broader industry data reinforces the pattern:

- AI generates **42% of code** but correlates with **23.5% more incidents** and **30% higher failure rates**
- AI speeds code reviews by **91%** but slows experienced developers by **19%**

**Why this matters:** The AI coding debate has been stuck on "can agents write code?" The answer is clearly yes. The real question — "can agents maintain software?" — is getting its first rigorous answer, and it's a sobering one. The SWE-CI benchmark shifts the evaluation from "does this patch work?" to "does this patch work without breaking everything else?" That's the difference between a coding assistant and a software engineer.
