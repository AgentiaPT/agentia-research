## 10. Voice Tracker

**Who said what this week — the people shaping how software engineering meets AI.**

---

**Andrej Karpathy** — Sequoia Ascent, AutoResearch

- Sequoia Ascent 2026 talk: declared "Software 3.0" — engineers shape outcomes via prompts/specs rather than explicit code; traditional interface layers "evaporate"
- Released [AutoResearch](https://github.com/karpathy/autoresearch) — 630-line Python framework running ~700 autonomous experiments in 2 days on a single GPU, finding 11% training efficiency gains
- Coined "agentic engineering" as successor to vibe coding
- Key quote: *"The bottleneck isn't execution but human understanding, management, and judgment"*
- Sources: [Sequoia Ascent writeup](https://karpathy.bearblog.dev/sequoia-ascent-2026/) · [MarkTechPost](https://www.marktechpost.com/2026/03/08/andrej-karpathy-open-sources-autoresearch-a-630-line-python-tool-letting-ai-agents-run-autonomous-ml-experiments-on-single-gpus/)

---

**Steve Yegge** — Google AI Drama, Gas City v1.0

- Viral X thread (1.9M views): claimed Google's AI adoption follows "20/60/20" pattern identical to industry average; alleged DeepMind engineers use Claude while rest locked into Gemini
- Provoked direct pushback from Demis Hassabis ("absolutely nonsense") and mobilized Google leadership response
- Released [Gas City v1.0](https://github.com/gastownhall/gascity) — ground-up rewrite, MIT-licensed agent orchestration SDK with composable "packs" and Dolt git-versioned database for audit trails
- Participated in "2026: The Year The IDE Died" panel — argues traditional IDEs being outmoded by agent-first environments
- Sources: [VentureBeat](https://venturebeat.com/orchestration/google-leaders-including-demis-hassabis-push-back-on-claim-of-uneven-ai-adoption-internally) · [Gas City announcement](https://steve-yegge.medium.com/welcome-to-gas-city-57f564bb3607)

---

**Sam Altman** — GPT-5.5, Post-AGI Warning, Musk Trial

- Oversaw GPT-5.5 launch and AWS Bedrock distribution — largest OpenAI release since GPT-4
- Posted provocative take (Apr 27): *"Post-AGI, no one is going to work and the economy is going to collapse"*
- Codex reached 4M weekly active users; resets usage limits every 1M users added
- Facing Musk v. Altman trial (opened Apr 28) — $130B in damages sought; dominated tech headlines
- Sources: [The News](https://www.thenews.com.pk/latest/1400502-after-gpt-55-release-sam-altman-warns-agi-could-trigger-economic-collapse) · [CNBC](https://www.cnbc.com/2026/04/28/openai-trial-elon-musk-sam-altman-live-updates.html)

---

**Aaron Levie** (Box CEO) — Box Automate, Agent-First Software

- Announced Box Automate at Reuters Momentum AI summit (Apr 27) — AI-driven service for enterprise process automation (invoice processing, document extraction)
- Key thesis: *"Build software for AI agents, not just humans"* — agents as primary internet users in B2B; software should prioritize APIs over GUIs
- Claims AI makes each engineer **2X–5X more capable**; predicts hiring surge, not job cuts (Jevons paradox)
- Sources: [US News](https://money.usnews.com/investing/news/articles/2026-04-27/box-to-launch-box-automate-service-to-expedite-enterprise-business-processes-ceo-says) · [Benzinga](https://www.benzinga.com/markets/tech/26/05/52238209/box-ceo-aaron-levie-says-each-engineer-is-2x-or-5x-more-capable-as-ai-fuels-hiring-surge-instead-of-job-cuts)

---

**Gergely Orosz** (The Pragmatic Engineer) — AI Load, Tokenmaxxing

- Reported "AI load breaks GitHub" — availability dropped to ~90% due to overwhelming demand from AI coding agents; GitHub paused Copilot signups
- Published interview on self-modifying software with Mario Zechner and Armin Ronacher (Apr 29)
- Covered AI token spending crisis — major companies blew through 2026 AI budgets in Q1
- Coined/popularized **"tokenmaxxing"** — developers deliberately burning tokens to inflate adoption metrics; as misleading as lines-of-code counting
- Sources: [Pragmatic Engineer](https://blog.pragmaticengineer.com/the-pulse-is-github-still-best-for-ai-native-development/) · [Forbes](https://www.forbes.com/sites/timkeary/2026/04/13/is-the-cult-of-tokenmaxxingjust-another-fad-or-the-new-normal/)

---

**Addy Osmani** (Google Chrome Engineering) — Long-Running Agents, AEO

- Published "Long-running Agents" (Apr 28) — architecture patterns for agents persisting hours/days/weeks, surviving context resets and session handoffs
- Published "Agent Harness Engineering" (Apr 19): *"A decent model with a great harness beats a great model with a bad harness"*
- Published Agentic Engine Optimization (AEO) framework — extending SEO for AI agents; content must be optimized for machine readability
- Made **114 commits** in April across `agentic-seo` (64), `agent-skills` (40) — intense focus on agent infrastructure
- Sources: [Long-running Agents](https://addyosmani.com/blog/long-running-agents/) · [Harness Engineering](https://addyosmani.com/blog/agent-harness-engineering/)

---

**Simon Willison** — llm 0.32a1, DeepSeek V4, Claude Prompt Diffing

- Released llm 0.32a1 (Apr 29) — alpha fixing tool-calling reinflation from SQLite; part of major refactor for multi-message prompts and streaming structured responses
- Detailed DeepSeek V4 breakdown (Apr 24): *"Almost on the frontier, a fraction of the price"* — MIT-licensed, 1M context, V4 Pro at 1/7th cost of Opus 4.7
- Covered OpenAI/Microsoft AGI clause nullification in weekly newsletter
- Documented Claude system prompt diffing between Opus 4.6 and 4.7, tracking behavioral changes
- Sources: [llm release](https://simonwillison.net/2026/Apr/29/llm-3/) · [DeepSeek V4](https://simonwillison.net/2026/Apr/24/deepseek-v4/)

---

**Daniel Stenberg** (curl creator) — Zero Bugs, AI Bug-Finding

- Spoke at foss-north (Apr 28): "Approaching Zero Bugs?" — proposed tracking bug age as progress metric; AI tools surfacing huge numbers of real and spurious bugs
- Data point: one skilled researcher using AI tools led to **50 legitimate curl bug fixes** in a short period
- Bug bounty **permanently discontinued** (Jan 2026) — will not be reactivated after AI-generated "slop" reports overwhelmed the program (under 5% genuine by late 2025)
- Key insight: incentive structure *"shifted the cost from monetary payouts to massive amounts of unpaid triage time"*
- Sources: [daniel.haxx.se](https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bounty/) · [The New Stack](https://thenewstack.io/drowning-in-ai-slop-reports-curl-ends-bug-bounties/)

---

**Martin Fowler** (ThoughtWorks) — Harness Engineering, Productive Laziness

- Endorsed Harness Engineering as core discipline — everything except the model itself (guides, constraints, context management) that makes agents reliable
- Critiqued lack of "productive laziness" in AI agents: LLMs generate excessive code because work is cheap for them, creating "layercake of garbage"
- Warned about **"intent debt"** — a new category where agents build things nobody actually needed, and the reasoning behind design choices goes unrecorded
- Key quote (citing Larry Wall): *"True productive laziness means building abstractions to avoid doing repetitive work again"*
- Sources: [Fragments](https://martinfowler.com/fragments/2026-04-02.html) · [Harness Engineering](https://martinfowler.com/articles/exploring-gen-ai/harness-engineering.html)

---
