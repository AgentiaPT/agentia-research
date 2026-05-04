# Voices & Thought Leaders — Apr 25–May 1, 2026

## Simon Willison

- Released **llm 0.32a1** (Apr 29) — alpha bugfix for tool-calling conversations not reinflating from SQLite; part of major refactor adding multi-message prompts and streaming structured responses
- Published detailed breakdown of **DeepSeek V4** (Apr 24) — noted it's "almost on the frontier, a fraction of the price" with MIT-licensed open weights, 1M context, V4 Pro at 1/7th the cost of Claude Opus 4.7
- Covered the **OpenAI/Microsoft AGI clause** nullification in his newsletter — the long-standing clause that would revoke Microsoft's IP rights upon AGI achievement was officially ended
- Documented **Claude system prompt diffing** between Opus 4.6 and 4.7, tracking behavioral changes around sycophancy and task approach
- Key quote: DeepSeek V4 is "almost on the frontier, a fraction of the price"
- Sources:
  - https://simonwillison.net/2026/Apr/29/llm-3/
  - https://simonwillison.net/2026/Apr/24/deepseek-v4/
  - https://simonwillison.net/tags/openai/
  - https://simonwillison.net/

## Aaron Levie

- Announced **Box Automate** at Reuters Momentum AI summit in New York (Apr 27) — new service enabling AI agents to handle enterprise workflows like invoice processing and data extraction
- Advocated **"Build for AI agents, not humans"** — argues agents will outnumber humans 100:1 in enterprises, software should prioritize APIs over GUIs, and be designed for autonomous agent consumption
- Claimed AI makes **each engineer 2X–5X more capable** — companies are hiring more engineers (not fewer) to exploit this productivity, calling it "Jevons paradox in real time"
- Framed Box's pivot as entering the **"era of context"** — using AI to bring order to unstructured enterprise data (contracts, legal docs, marketing assets)
- Sources:
  - https://money.usnews.com/investing/news/articles/2026-04-27/box-to-launch-box-automate-service-to-expedite-enterprise-business-processes-ceo-says
  - https://www.benzinga.com/markets/tech/26/05/52238209/box-ceo-aaron-levie-says-each-engineer-is-2x-or-5x-more-capable-as-ai-fuels-hiring-surge-instead-of-job-cuts
  - https://www.digit.in/features/general/build-software-for-ai-agents-not-necessarily-humans-box-ceo.html
  - https://www.fastcompany.com/91512532/aaron-levie-on-what-enterprise-ai-adoption-actually-looks-like

## Gergely Orosz

- Reported **"AI load breaks GitHub"** — availability dropped to ~90% ("one nine") due to overwhelming demand from AI coding agents; GitHub paused Copilot signups (late Apr)
- Published podcast interview **"Building Pi, and what makes self-modifying software so fascinating"** (Apr 29) with Mario Zechner and Armin Ronacher on agentic coding agents
- Covered **AI token spending crisis** — major companies blew through 2026 AI token budgets in Q1; some pausing signups and rationing compute
- Coined/popularized **"tokenmaxxing"** — developers deliberately burning AI tokens to inflate adoption metrics, comparing it to the old "lines of code" vanity metric
- Key critique: Token consumption as productivity metric is as misleading as lines-of-code counting
- Sources:
  - https://substack.com/@pragmaticengineer
  - https://www.forbes.com/sites/timkeary/2026/04/13/is-the-cult-of-tokenmaxxingjust-another-fad-or-the-new-normal/
  - https://techcrunch.com/2026/04/17/tokenmaxxing-is-making-developers-less-productive-than-they-think/
  - https://developer.upsun.com/posts/ai/aiweekly-2026-04-27

## Andrej Karpathy

- Spoke at **Sequoia AI Ascent 2026** on "Software 3.0" — engineers now shape outcomes via prompts and specs rather than writing explicit code; traditional interface layers "evaporate"
- Released/promoted **AutoResearch** open-source tool — automates ML experiments overnight on a single GPU using an AI agent that proposes, implements, evaluates, and keeps/reverts code changes ("ratchet loop")
- Popularized the **"Second Brain" concept** (Apr 3 viral post) — using LLMs to build self-evolving personal wikis from raw research data, compiled into interlinked Markdown; his own wiki reached 100+ articles and 400K words without manual editing
- Introduced the term **"agentic engineering"** — the shift from code authoring to orchestrating teams of AI agents
- Key quote: "The bottleneck isn't execution but human understanding, management, and judgment"
- Sources:
  - https://karpathy.bearblog.dev/sequoia-ascent-2026/
  - https://www.youtube.com/watch?v=96jN2OCOfLs
  - https://www.datacamp.com/tutorial/guide-to-autoresearch
  - https://medium.com/neuralnotions/andrej-karpathy-stopped-using-ai-to-write-code-hes-using-it-to-build-a-second-brain-instead-cddceadc5df5

## Sam Altman

- Oversaw **GPT-5.5 release** (late Apr) — OpenAI's most agentic model, $5/$30 per million input/output tokens; private launch event scheduled for May 5
- Posted **"post-AGI" warning** (Apr 27): "Post-AGI, no one is going to work and the economy is going to collapse" — argued AGI will make traditional employment obsolete across sectors
- **Codex** continued rapid growth — GPT-5.5 integrated into Codex with improved efficiency (fewer tokens for same tasks); widespread enterprise adoption
- Facing **Musk v. Altman trial** (opened Apr 28) — Musk seeking $130B in damages and Altman's removal, alleging OpenAI abandoned its nonprofit mission; trial dominated tech headlines all week
- Joked about "switching to polyphasic sleep" to keep up with AI progress pace
- Sources:
  - https://www.thenews.com.pk/latest/1400502-after-gpt-55-release-sam-altman-warns-agi-could-trigger-economic-collapse
  - https://decrypt.co/365333/openai-gpt-5-5-release-agentic-coding-benchmarks
  - https://www.technologyreview.com/2026/04/27/1136466/elon-musk-and-sam-altman-are-going-to-court-over-openais-future/
  - https://dataconomy.com/2026/04/30/openai-expands-trusted-access-program-with-gpt-5-5-cyber/

## Addy Osmani

- Published **"Long-running Agents"** blog post (Apr 28) — framework for agents that persist across hours/days/weeks, surviving context resets and session handoffs; blending long-horizon reasoning with persistent agency
- Published **"Agent Harness Engineering"** (Apr 19) — defining the harness as everything around the model (prompts, tools, policies, hooks, observability); key insight: "A decent model with a great harness beats a great model with a bad harness"
- Published **Agentic Engine Optimization (AEO)** framework (Apr 11) — extending SEO principles for AI agents; urging documentation owners to optimize for machine readability and token efficiency
- Made **114 commits** across 4 repositories in April — primarily `agentic-seo` (64), `agent-skills` (40), `PatternsDev/skills` (9), reflecting intense focus on agent infrastructure
- Sources:
  - https://addyosmani.com/blog/long-running-agents/
  - https://addyosmani.com/blog/agent-harness-engineering/
  - https://addyosmani.com/blog/agentic-engine-optimization/
  - https://github.com/addyosmani

## Daniel Stenberg

- Spoke at **foss-north** (Apr 28) on "Approaching Zero Bugs?" — questioned whether AI bug-finders can achieve zero-bug state; proposed tracking age of discovered bugs as progress metric
- Reflected on the **"high quality chaos era"** — AI tools rapidly surfacing huge numbers of both real and spurious bugs, overwhelming maintainers
- Shared data on **AI-assisted bug discovery**: one skilled researcher using AI tools led to 50 legitimate curl bug fixes in a short period
- Confirmed **bug bounty permanently discontinued** (shut down Jan 2026) — will not be reactivated; AI-generated "slop" reports overwhelmed the program (only 1 in 20-30 reports were genuine by late 2025)
- Key quote: The incentive structure "shifted the cost from monetary payouts to massive amounts of unpaid triage time"
- Sources:
  - https://daniel.haxx.se/blog/2026/04/
  - https://thenewstack.io/curls-daniel-stenberg-ai-is-ddosing-open-source-and-fixing-its-bugs/
  - https://cybernews.com/security/curl-maintainer-stenberg-says-ai-help-fix-dozens-of-bugs/
  - https://socket.dev/blog/curl-shuts-down-bug-bounty-program-after-flood-of-ai-slop-reports

## Martin Fowler

- Published **"Fragments" posts** throughout April — short-form commentary on software engineering trends in the AI era
- Endorsed **Harness Engineering** as a core discipline — everything except the model itself (guides, feedback mechanisms, constraints, context management) that makes agents reliable; prompt engineering is "one turn," harness engineering is systemic control
- Critiqued lack of **"productive laziness"** in AI agents (Apr 14, Apr 22) — LLMs generate excessive code because work is cheap for them, creating "layercake of garbage"; real engineering virtue is restraint and knowing when NOT to build (YAGNI principle)
- Warned about **"intent debt"** — a new category beyond technical/cognitive debt where agents build things nobody actually needed
- Key quote: Referencing Larry Wall's programmer virtues: "True productive laziness means building abstractions to avoid doing repetitive work again"
- Sources:
  - https://martinfowler.com/fragments/2026-04-02.html
  - https://app.daily.dev/posts/fragments-april-14-g2hzi2bsh
  - https://www.agent-wars.com/news/2026-04-22-martin-fowler-technical-cognitive-and-intent-debt
  - https://medium.com/autocomplete-real-world-ai/harness-engineering-the-discipline-that-emerged-overnight-99fe349a8ee2

## Steve Yegge

- Viral **Google AI adoption thread** (Apr 13) — amassed 1.9M views, 4,500+ likes, 458 replies; claimed Google follows a "20/60/20" pattern (20% agentic adopters, 60% basic assistant users, 20% refusers); provoked pushback from Demis Hassabis and Google leadership
- Released **Gas City v1.0** (Apr) — ground-up rewrite of Gas Town; open-source MIT-licensed agent orchestration SDK with composable "packs," built on MEOW framework and Dolt git-versioned database for auditability
- Participated in **"2026: The Year The IDE Died"** panel with Gene Kim — argues traditional IDEs are being outmoded by agent-driven workflow-first environments; many devs remain 9-12 months behind the leading AI curve
- Doubled down on Google claims after employee corroboration — reported a "two-tier system" with DeepMind engineers using far more advanced agentic tools than the rest of Google
- Sources:
  - https://venturebeat.com/orchestration/google-leaders-including-demis-hassabis-push-back-on-claim-of-uneven-ai-adoption-internally
  - https://steve-yegge.medium.com/welcome-to-gas-city-57f564bb3607
  - https://www.youtube.com/watch?v=7Dtu2bilcFs
  - https://www.firstpost.com/tech/googlers-want-better-agentic-tools-steve-yegge-reiterates-concerns-over-uneven-ai-adoption-at-google-14002858.html
