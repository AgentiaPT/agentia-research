## 10. Voice Tracker

**Who said what this week — the people shaping how software engineering meets AI.**

---

**Andrej Karpathy** — Sequoia Ascent, AutoResearch

- Declared "Software 3.0" and coined "agentic engineering" as successor to vibe coding
- Released [AutoResearch](https://github.com/karpathy/autoresearch) — autonomous ML experiments finding 11% efficiency gains
- See Section 7 for full analysis.

---

**Steve Yegge** — Google AI Drama, Gas City v1.0

- Viral X thread (1.9M views) claiming Google's AI adoption mirrors industry-average "20/60/20" split; provoked Hassabis pushback
- Released [Gas City v1.0](https://github.com/gastownhall/gascity) — MIT-licensed agent orchestration SDK
- See Section 7 for full analysis.

---

**Sam Altman** — GPT-5.5, Post-AGI Warning, Musk Trial

- Oversaw GPT-5.5 launch and AWS Bedrock distribution — largest OpenAI release since GPT-4
- Posted (Apr 27): *"Post-AGI, no one is going to work and the economy is going to collapse"*
- Codex reached 4M weekly active users; resets usage limits every 1M users added
- Facing Musk v. Altman trial (opened Apr 28) — $130B in damages sought
- Sources: [The News](https://www.thenews.com.pk/latest/1400502-after-gpt-55-release-sam-altman-warns-agi-could-trigger-economic-collapse) · [CNBC](https://www.cnbc.com/2026/04/28/openai-trial-elon-musk-sam-altman-live-updates.html)

---

**Aaron Levie** (Box CEO) — Box Automate, Agent-First Software

- Announced Box Automate at Reuters Momentum AI summit (Apr 27) — AI-driven enterprise process automation
- Key thesis: *"Build software for AI agents, not just humans"* — agents as primary internet users in B2B
- Claims AI makes each engineer **2X–5X more capable**; predicts hiring surge via Jevons paradox
- Sources: [US News](https://money.usnews.com/investing/news/articles/2026-04-27/box-to-launch-box-automate-service-to-expedite-enterprise-business-processes-ceo-says) · [Benzinga](https://www.benzinga.com/markets/tech/26/05/52238209/box-ceo-aaron-levie-says-each-engineer-is-2x-or-5x-more-capable-as-ai-fuels-hiring-surge-instead-of-job-cuts)

---

**Gergely Orosz** (The Pragmatic Engineer) — AI Load, Tokenmaxxing

- Reported "AI load breaks GitHub" — availability dropped to ~90% from overwhelming agent demand; GitHub paused Copilot signups
- Published interview on self-modifying software with Mario Zechner and Armin Ronacher (Apr 29)
- Covered AI token spending crisis — major companies blew through 2026 AI budgets in Q1
- Coined **"tokenmaxxing"** — developers deliberately burning tokens to inflate adoption metrics
- Sources: [Pragmatic Engineer](https://blog.pragmaticengineer.com/the-pulse-is-github-still-best-for-ai-native-development/) · [Forbes](https://www.forbes.com/sites/timkeary/2026/04/13/is-the-cult-of-tokenmaxxingjust-another-fad-or-the-new-normal/)

---

**Addy Osmani** (Google Chrome Engineering) — Long-Running Agents, AEO

- Published "Long-running Agents" (Apr 28) — architecture for agents persisting hours/days/weeks, surviving context resets
- Published "Agent Harness Engineering" (Apr 19): *"A decent model with a great harness beats a great model with a bad harness"*
- Published Agentic Engine Optimization (AEO) framework — extending SEO for AI agents
- **114 commits** in April across `agentic-seo` (64), `agent-skills` (40)
- Sources: [Long-running Agents](https://addyosmani.com/blog/long-running-agents/) · [Harness Engineering](https://addyosmani.com/blog/agent-harness-engineering/)

---

**Simon Willison** — llm 0.32a1, DeepSeek V4, Claude Prompt Diffing

- Released llm 0.32a1 (Apr 29) — alpha fixing tool-calling reinflation from SQLite; major refactor for multi-message prompts
- Detailed DeepSeek V4 breakdown (Apr 24): *"Almost on the frontier, a fraction of the price"* — MIT-licensed, 1M context, V4 Pro at 1/7th cost of Opus 4.7
- Covered OpenAI/Microsoft AGI clause nullification in weekly newsletter
- Documented Claude system prompt diffing between Opus 4.6 and 4.7
- Sources: [llm release](https://simonwillison.net/2026/Apr/29/llm-3/) · [DeepSeek V4](https://simonwillison.net/2026/Apr/24/deepseek-v4/)

---

**Daniel Stenberg** (curl creator) — Zero Bugs, AI Bug-Finding

- Spoke at foss-north (Apr 28): "Approaching Zero Bugs?" — proposed tracking bug age as progress metric
- One skilled researcher using AI tools led to **50 legitimate curl bug fixes** in a short period
- Bug bounty **permanently discontinued** (Jan 2026) — AI-generated "slop" reports overwhelmed the program (under 5% genuine by late 2025)
- Key insight: incentive structure *"shifted the cost from monetary payouts to massive amounts of unpaid triage time"*
- Sources: [daniel.haxx.se](https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bounty/) · [The New Stack](https://thenewstack.io/drowning-in-ai-slop-reports-curl-ends-bug-bounties/)

---

**Martin Fowler** (ThoughtWorks) — Harness Engineering, Productive Laziness

- Endorsed Harness Engineering as core discipline — everything except the model itself that makes agents reliable
- Critiqued lack of "productive laziness" in AI agents: LLMs generate excessive code because work is cheap, creating "layercake of garbage"
- Warned about **"intent debt"** — agents build things nobody needed, reasoning behind design choices goes unrecorded
- Key quote (citing Larry Wall): *"True productive laziness means building abstractions to avoid doing repetitive work again"*
- Sources: [Fragments](https://martinfowler.com/fragments/2026-04-02.html) · [Harness Engineering](https://martinfowler.com/articles/exploring-gen-ai/harness-engineering.html)

---
