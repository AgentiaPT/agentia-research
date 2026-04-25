## 12. Signals & Radar

### 🔴 Critical

- **The Great AI Coding Price Upheaval** — In 72 hours: Anthropic briefly pulled Claude Code from Pro ([reverted](https://simonwillison.net/2026/Apr/22/claude-code-confusion/)), GitHub [paused signups](https://github.blog/news-insights/company-news/changes-to-github-copilot-individual-plans/), OpenAI launched a [$100 tier](https://techcrunch.com/2026/04/09/chatgpt-pro-plan-100-month-codex/), and Microsoft reportedly moving to [token billing in June](https://www.wheresyoured.at/exclusive-microsoft-moving-all-github-copilot-subscribers-to-token-based-billing-in-june/). The $20 era is over — [analysis](https://pasqualepillitteri.it/en/news/1241/ai-coding-tools-2026-price-hike-claude-copilot-codex-gemini)
- **MCP "by design" RCE** — STDIO transport ships RCE across **200K+ servers**, **150M+ downloads**. Anthropic declined a protocol-level fix (§5) — [The Hacker News](https://thehackernews.com/2026/04/anthropic-mcp-design-vulnerability.html)
- **CanisterSprawl** — First cross-ecosystem worm (npm ↔ PyPI) via stolen publish tokens, decentralized C2 (§5) — [StepSecurity](https://www.stepsecurity.io/blog/pgserve-compromised-on-npm-malicious-versions-harvest-credentials)
- **GitHub Copilot training data policy** — Free/Pro/Pro+ interaction data used for AI training, opted in by default (Apr 24). Business/Enterprise exempt — [InfoQ](https://www.infoq.com/news/2026/04/github-copilot-training-data/)

### 🟠 Warning

- **Software stock repricing** — ServiceNow **−18%**, IBM **−9%** despite beating earnings (§7) — [Forbes](https://www.forbes.com/sites/aliciapark/2026/04/23/ai-fears-keep-hammering-software-stocks-even-those-reporting-good-earnings/)
- **92,000 tech layoffs YTD** — ~48% AI-attributed. Meta + Microsoft: 20K+ on the same day (§7) — [CNBC](https://www.cnbc.com/2026/04/24/20k-job-cuts-at-meta-microsoft-raise-concern-of-ai-labor-crisis-.html)
- **Tokenmaxxing** — Real gains 5–15% vs vendor-claimed 30–50%. Code churn **9.4×** higher. Goodhart's law in action (§8) — [TechCrunch](https://techcrunch.com/2026/04/17/tokenmaxxing-is-making-developers-less-productive-than-they-think/)
- **GPT-5.5 pricing 2×** — API doubles to $5/$30 per million tokens (§2) — [OpenAI](https://openai.com/index/introducing-gpt-5-5/)
- **EU AI Act Annex III: 14 weeks** — High-risk logging obligations Aug 2, 2026. Penalties up to €15M / 3% revenue (§5) — [Help Net Security](https://www.helpnetsecurity.com/2026/04/16/eu-ai-act-logging-requirements/)

### 🟢 Emerging

- **DeepSeek V4 on Huawei Ascend** — **$0.14/M** input (20–50× cheaper than Western APIs). Geopolitical divergence is real (§8) — [CNBC](https://www.cnbc.com/2026/04/24/deepseek-v4-llm-preview-open-source-ai-competition-china.html)
- **Claude Design vs Figma** — Stock **−7%** on launch. Krieger resigned from Figma board pre-launch (§4) — [TechCrunch](https://techcrunch.com/2026/04/17/anthropic-launches-claude-design-a-new-product-for-creating-quick-visuals/)
- **Anthropic postmortem precedent** — Detailed three-bug breakdown; rare AI industry candor (§3) — [Anthropic](https://www.anthropic.com/engineering/april-23-postmortem)
- **Karpathy's LLM Wiki** — Replace RAG with LLM-maintained markdown wikis. Gist: 5K+ stars, 5K+ forks — [GitHub Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- **Google Cloud Next '26** — $750M agentic fund, ADK, Workspace MCP Server, Apple/Gemini Siri — [Google Cloud Blog](https://cloud.google.com/blog/topics/google-cloud-next/welcome-to-google-cloud-next26)
- **Prompt injection industrialized** — Google found organized injection templates across the public web (§5) — [Google Security Blog](https://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html)

### 🔵 Watch

- **SpaceX/Cursor $60B** — Dev tooling enters geopolitical chess; Cursor trains on xAI Colossus (§6) — [Bloomberg](https://www.bloomberg.com/news/articles/2026-04-21/spacex-says-has-agreement-to-acquire-cursor-for-60-billion)
- **Kent Beck: "Nobody wants agents"** — Managing the swarm, not directing work. Counterpoint gaining traction — [Tidy First](https://tidyfirst.substack.com/p/genie-lessons-nobody-wants-agents)
- **Stanford AI Index** — Junior devs (22–25) down ~20%. SWE-bench near 100%. 88% org adoption (§8) — [Stanford HAI](https://hai.stanford.edu/news/inside-the-ai-index-12-takeaways-from-the-2026-report)
- **OpenAI Workspace Agents** — Codex-powered persistent agents replacing GPTs. Free until May 6 — [OpenAI](https://openai.com/index/introducing-workspace-agents-in-chatgpt/)
- **ICLR 2026 safety** — AlphaAlign & WaltzRL cut unsafe responses from ~40% → <5% — [ICLR 2026](https://iclr.cc/virtual/2026/papers.html)
- **Lovable BOLA incident** — Public projects exposed; fix in 2 hours. Cautionary tale for no-code AI builders (§5) — [Lovable Blog](https://lovable.dev/blog/our-response-to-the-april-2026-incident)
- **Pragmatic Engineer Survey** — 900+ engineers, three archetypes, roles converging (§8) — [Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/the-impact-of-ai-on-software-engineers-2026)

---

### Key Quotes of the Week

> "A new class of intelligence for real work."
> — **OpenAI**, GPT-5.5 launch announcement ([source](https://openai.com/index/introducing-gpt-5-5/))

> "This was the wrong tradeoff."
> — **Anthropic Engineering**, on the reasoning effort downgrade that degraded Claude Code ([source](https://www.anthropic.com/engineering/april-23-postmortem))

> "Nobody wants agents. Nobody wants agent swarms. I have a system and I want it to change. That's the whole thing."
> — **Kent Beck**, creator of XP and TDD ([source](https://tidyfirst.substack.com/p/genie-lessons-nobody-wants-agents))

> "If you're building agents, you basically need to throw away large parts of previous work that you set up to compensate for model limitations every few quarters."
> — **Aaron Levie**, Box CEO ([source](https://tech.yahoo.com/ai/articles/systems-built-arent-useful-anymore-163106806.html))

> "The challenge with AI in open source security has transitioned from an AI slop tsunami into more of a plain security report tsunami. Less slop but lots of reports. Many of them really good."
> — **Daniel Stenberg**, curl maintainer ([source](https://daniel.haxx.se/blog/2026/04/22/high-quality-chaos/))

> "I don't want AI turned on our own people."
> — **Dario Amodei**, Anthropic CEO, at the White House ([source](https://www.cnbc.com/2026/04/17/anthropic-dario-amodei-trump-mythos.html))

> One thing thing about AI, for better and worse, is that "everything around me is somebody's life work" is no longer a true assumption going forward.
> — **Ethan Mollick**, Wharton ([source](https://x.com/emollick/status/2045318277958709540))
