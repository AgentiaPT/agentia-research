# AI × Software Engineering — March 30 – April 4, 2026 — Outline

## Theme: "The Unraveling"

The week Anthropic leaked its own future, supply chains crumbled again, Oracle cut 30,000 jobs via a 6am email, and the industry debated whether AI is actually replacing anyone at all.

---

## 1. The Week's Narrative — When the Builders Break Their Own Tools

- Anthropic triple crisis: Mythos leak → Claude Code source leak → DMCA takedown of 8,100 repos → Congressional scrutiny
- Supply chain attacks hit security tools themselves (TeamPCP: Trivy, LiteLLM) + Axios npm compromise
- Oracle's 30K layoff email as the starkest symbol of AI-driven restructuring
- Counternarrative: Andreessen says AI layoffs are a "farce" — companies 75% overstaffed
- Unifying thread: the infrastructure of trust is fracturing — from code registries to model labs to employment contracts

## 2. Anthropic's Week from Hell — Mythos, Claude Code, and Congressional Fire

- **Mythos CMS leak** (March 30): 3,000 unpublished assets exposed via config error, "Capybara" tier
- Mythos described as "step change" — Anthropic privately briefing US officials on cyber risks
- **Claude Code source leak** (March 31): 500K lines of code via npm source map in v2.1.88
- Unreleased features discovered: persistent assistant, cross-conversation learning, session review
- **DMCA takedown fiasco** (April 1): 8,100 repos nuked including legitimate forks
- Boris Cherny retraction, limited to 96 actual forks
- Fastest-growing repo in GitHub history
- **Gottheimer letter** (April 2): Congressional pressure on national security implications
- Safety policy narrowing: removed pledge to halt development if safety lags
- Sources: Axios, TechCrunch, Bloomberg, Fortune, The Hill, Euronews, The Register

## 3. Supply Chain Siege — TeamPCP and the Axios Bomb

- **TeamPCP campaign** (March 19–27): Trivy → KICS → LiteLLM → Telnyx
- Force-push to 76 of 77 version tags in trivy-action
- 1,000+ cloud environments infected (Mandiant's Carmakal)
- Weaponized security scanners — "the protectors became the attack vector"
- **Axios npm compromise** (March 31): 100M+ weekly downloads
- Poisoned versions 1.14.1 and 0.30.4 with hidden dependency
- Credential theft + RAT installation on install
- **AI coding tools make supply chain worse**: agents choose vulnerable versions 50% more often
- Sources: Palo Alto Unit42, InfoQ, The Register, SANS, Kaspersky, The New Stack

## 4. Google's Open Model Play — Gemma 4 Drops Under Apache 2.0

- **Gemma 4 release** (April 2): Four model variants (2B, 4B, 26B MoE, 31B Dense)
- 256K context, native vision/audio, 140+ languages
- 31B model ranked #3 on Arena AI leaderboard — beating models 20x its size
- Apache 2.0 license — first time (previous Gemma under restricted license)
- Gemma 4 Good Hackathon on Kaggle
- **Gemini 3.1 Pro** also rolling out — advanced reasoning mode
- Gemini in Chrome, Android Auto expansion (April 3)
- Sources: Google Blog, Engadget, CGTN, tbreak, AI Business

## 5. Oracle's 6am Email and the Great Layoff Reckoning

- **Oracle cuts 20,000–30,000** (~18% workforce) via mass email at 6am EST (March 31)
- No manager conversations, no HR heads-up
- Linked to Stargate initiative AI data center buildout with OpenAI/SoftBank
- Expected to free $8–10B in cash flow (TD Cowen)
- **Bloomberg data**: 52,000 tech layoffs in Q1 2026 — worst since 2023
- AI explicitly cited in 25% of March layoffs (15,341 jobs)
- **Andreessen counterpoint** (March 31): "Every large company is overstaffed" by 25-75%
- AI is the "silver bullet excuse" for post-COVID cleanup
- **Fortune counterargument**: 9 reasons AI isn't taking your job yet
- Productivity paradox: some workers report AI making them *less* productive (+346% time on some tasks)
- CFO survey: only 0.4% of roles (502K) projected to be cut
- Sources: CNBC, Rolling Out, HR Executive, Bloomberg, Fortune, Benzinga

## 6. GitHub Copilot Goes Cloud-Native — Research, Plan, and Code

- **Copilot cloud agent** rebranded from "coding agent"
- **April 1**: No longer limited to PR workflows — branch-only, implementation plans
- **April 3**: Commit signing (Verified badge), org runner controls
- Shift from "code suggestion" to "autonomous development workflow"
- Running on Claude Sonnet 4.6
- Sources: GitHub Blog, GitHub Changelog, GitHub Docs

## 7. Vibe Coding's Security Reckoning

- Harvard Gazette feature on vibe coding's implications (April)
- **Escape.tech study**: 5,600 vibe-coded apps → 2,000+ vulnerabilities, 400+ exposed secrets
- **53% of AI-generated code** has security issues that pass initial review
- AI code is **2.74x more likely** to introduce XSS
- **Unit42 (Palo Alto)**: "Securing Vibe Coding Tools" — treat AI code as untrusted
- Databricks: "Passing the Security Vibe Check"
- TechRxiv survey on systemic risks in autonomous development workflows
- Sources: Harvard Gazette, Escape.tech, Palo Alto Unit42, Databricks, TechRxiv, Computing.co.uk

## 8. Karpathy's Psychosis and the Agent-First Future

- **Dobby demo** (April 1): OpenClaw agent replaced 6+ home apps
- Scanned local network, reverse-engineered APIs, controls Sonos/lights/HVAC/pool/security
- WhatsApp as primary interface
- "I don't think I've typed a line of code since December"
- "State of psychosis trying to figure out what's possible"
- **OpenClaw** acquired by OpenAI in February — now the de facto agent framework
- Distinction: "agentic engineering" vs "vibe coding"
- Latest tweet: "never felt this much behind as a programmer"
- Sources: Fortune, Let's Data Science, X/Twitter

## 9. Voice Tracker — Who Said What This Week

Active voices:
- **Andrej Karpathy** — Dobby demo, "agentic engineering" framing, "never felt this behind"
- **Simon Willison** — AI state of the union on Lenny's Newsletter, "dark factories," datasette-extract release
- **Marc Andreessen** — AI layoffs "farce," silver bullet excuse, 75% overstaffed
- **Boris Cherny** (Anthropic) — Claude Code leak retraction, DMCA handling
- **Jim Farley** (Ford CEO) — "Essential economy" warning, AI eating white-collar jobs
- **Josh Gottheimer** (Congress) — Letter to Anthropic on national security
- **Charles Carmakal** (Mandiant) — 1,000+ environments impacted by TeamPCP

Check for:
- Swyx / Latent Space
- Gergely Orosz / Pragmatic Engineer
- Theo Browne
- Addy Osmani
- Steve Yegge

## 10. Model & Tool Updates (Footnotes)

- Anthropic: 300K max_tokens on Batches API, 1M context window migration (Sonnet 4.5 → 4.6)
- Google: Gemma 4 (four variants), Gemini 3.1 Pro, Gemini in Chrome, Android Auto
- GitHub: Copilot cloud agent (research/plan/code, commit signing, org controls)
- OpenAI: Acquired TBPN media show ($30M/yr revenue), reports to Chris Lehane
- Windsurf: Quota-based pricing replacement ($20/mo Pro = Cursor parity)

## 11. Jobs & Economic Impact — The Numbers

Key data points:
- 52,000 tech layoffs Q1 2026 (worst since 2023)
- Oracle: 20-30K cuts → $8-10B freed for AI infra
- AI cited in 25% of March layoffs
- Andreessen: 25-75% overstaffing claim
- CFO survey: 0.4% of roles projected cut (502K of 125M)
- Fortune: Productivity paradox — some tasks +346% time with AI
- Bloomberg: Job cuts rising with AI adoption

## 12. Signals & Radar

🔴 **Critical**
- Anthropic's security posture: two leaks in one week, Congressional scrutiny, safety policy narrowing
- Supply chain attacks now weaponize security tools (Trivy = vulnerability scanner turned attack vector)
- Axios compromise: 100M+ weekly downloads, credential theft on install

🟠 **Warning**
- AI coding tools choose vulnerable dependencies 50% more often than humans
- Oracle's 6am email as template for mass AI-driven layoffs
- DMCA overreach: 8,100 repos nuked in 24 hours

🟢 **Emerging**
- Gemma 4 under Apache 2.0 — Google's most permissive open model license
- Copilot cloud agent: from code suggestions to autonomous development workflows
- OpenClaw/Dobby: agents replacing entire app categories, not just features

🔵 **Watch**
- Claude Mythos "Capybara" tier — if leak details are accurate, represents step-change in capabilities
- Congressional interest in AI lab security practices (Gottheimer letter as precedent)
- "AI-washing" layoffs narrative gaining mainstream traction (Andreessen, Fortune, Bloomberg)

---

## Key Quotes Candidates

1. "I'm just like in the state of psychosis of trying to figure out what's possible" — Karpathy
2. "Every large company is overstaffed... AI is the silver bullet excuse" — Andreessen
3. "We know of over 1,000 impacted SaaS environments right now" — Carmakal (Mandiant)
4. "A release packaging issue caused by human error, not a security breach" — Anthropic spokesperson
5. "If Claude is replicated, we sacrifice the competitive edge" — Gottheimer
6. "I've never felt this much behind as a programmer" — Karpathy
