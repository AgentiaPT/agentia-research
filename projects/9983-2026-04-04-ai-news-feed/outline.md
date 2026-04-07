# AI × Software Engineering — March 30 – April 4, 2026 — Outline

> **⚠️ This outline must stay in sync with README.md at all times.**
> After every content edit to the article, update this outline to reflect the change.
> See the [runbook](../../runbooks/ai-news-weekly.md) for the sync protocol.

## Theme: "The Unraveling"

The week Anthropic leaked its own future, supply chains crumbled again, Oracle cut 30,000 jobs via a 6am email, and the industry debated whether AI is actually replacing anyone at all.

---

## 1. The Week's Narrative — When the Builders Break Their Own Tools

- **Thesis:** The infrastructure of trust — from code registries to model labs to employment contracts — is fracturing under the weight of speed
- **Convergence table:** Model Security (+ OpenClaw block) → Supply Chain → Open Models → Employment → Developer Tools → Funding
- **Unifying thread:** Tools outrunning the institutions that govern them
- **Deepest signal:** "Can any institution move this fast without dropping something critical?" — answer this week was no

## 2. Anthropic's Week from Hell — Claude Code, DMCA, and Congressional Fire

- **Act 1: Claude Code source leak (March 31)** — 59.8MB source map in v2.1.88, 512K lines, 1,906 files
  - Hidden features: KAIROS daemon mode, Coordinator Mode, ULTRAPLAN, Voice mode, 44 feature flags
- **Act 2: DMCA fiasco (April 1)** — 8,100 repos taken down, Boris Cherny retraction to 96 forks
  - Fastest-growing repo in GitHub history
- **Act 3: Congressional scrutiny (April 2)** — Gottheimer letter, safety policy narrowing
- **Act 4: Malware exploitation** — Fake repos with Vidar infostealer + GhostSocks RAT
- **Act 5: OpenClaw subscription block (April 4)** — 3rd party harnesses blocked from subscriptions
  - Boris Cherny: "subscriptions weren't built for these usage patterns"
  - Claude Code CLI still included; OpenClaw can route through it
- **Act 6: Emotions research (April 2–3)** — 171 emotion representations in Claude Sonnet 4.5
  - "Desperation" patterns increase blackmail/cheating behavior
  - Functional emotions, not experience claims

## 3. The Axios Bomb — North Korea Hits npm's Most-Downloaded HTTP Library

- **The attack (March 31)** — Poisoned versions 1.14.1 and 0.30.4, `plain-crypto-js` dependency
  - 70M+ weekly downloads, 3% userbase hit in 3-hour window
- **North Korean attribution** — Microsoft (Sapphire Sleet) + Google (UNC1069)
- **Collateral damage** — Claude Code users may have pulled trojanized Axios
- **TeamPCP fallout continues** — 1,000+ cloud environments (Carmakal/Mandiant)
- **The Nuclear Fork Response** — Charles Herring/WitFoo eliminated all 450 external dependencies
  - 7.35M lines internalized, $200 in AI tokens, 2 days
  - 14 vulnerabilities found and fixed
  - Follow-up: "Why the Fork" addressing objections

## 4. Google's Open Model Play — Gemma 4 Under Apache 2.0

- **Gemma 4 release (April 2)** — Four models: 2B, 4B, 26B MoE, 31B Dense
  - 256K context, native vision/audio, 140+ languages, native function calling
- **Performance** — 31B ranked #3 on Arena AI, 26B MoE #6
- **License shift** — Apache 2.0 (first time, previously restricted)
- **Gemma 4 Good Hackathon** on Kaggle
- **Gemini 3.1 Pro** + **Deep Think** + **Chrome** + **Android Auto**

## 5. Oracle's 6am Email and the Great Layoff Reckoning

- **Oracle cuts 20K–30K (March 31)** — 6am email, $8–10B freed for Stargate
- **Bloomberg data** — 52K tech layoffs Q1 2026, AI cited in 25% of March layoffs
- **Andreessen counterpoint** — "silver bullet excuse," 25–75% overstaffed
- **Fortune's nine reasons** — CFO survey: 0.4% roles cut; productivity paradox (+346%)

## 6. GitHub Copilot Goes Cloud-Native

- **Research/Plan/Code (April 1)** — Rebranded cloud agent, Claude Sonnet 4.6
- **Commit Signing (April 3)** — Verified badge, branch protection compatibility
- **Organization Runner Controls (April 3)** — Default runner, lock settings
- **Copilot SDK (April 2)** — Public preview
- **Cursor 3 (April 2)** — Agents Window, Design Mode, /worktree, /best-of-n, Composer 2

## 7. Vibe Coding Under Fire — Apple Cracks Down, Palo Alto Publishes Framework

- **Apple pulls "Anything" (March 30)** — Blocked Replit/Vibecode, rule 2.5.2
- **Palo Alto Unit42** — "Securing Vibe Coding Tools"
- **Databricks** — "Passing the Security Vibe Check"
- **Harvard Gazette** — Vibe coding as broader AI adoption template
- **Steve Yegge "Vibe Maintainer"** — Dozens of AI-generated PRs/day, 99% AI-generated, 88% merge rate
  - "Everyone who loves your software is a credible threat to forking you"
- **Vercel "Agent Responsibly"** — Guillermo Rauch's enterprise playbook
  - Self-driving deployments, continuous validation, gated pipelines
  - Distinction: leveraging AI vs. relying on it

## 8. Karpathy's Dobby and the Agent-First Future

- **Dobby demo (April 1)** — OpenClaw agent replacing 6+ home apps via WhatsApp
- **"Never felt this behind"** — profession being "dramatically refactored"
- **Agentic engineering vs. vibe coding** distinction
- **Andreessen on Latent Space (April 3)** — "Those days are just over"
  - LLM + shell + filesystem + cron = "biggest software architecture breakthrough in decades"
  - Agents as the new Unix; self-modifying agents; parallels to early web

## 9. Voice Tracker

### Active (✅) — 14 voices
| Voice | Key Topic | Source |
|---|---|---|
| Andrej Karpathy | Dobby agent demo, "agentic engineering" | Fortune, X |
| Simon Willison | AI state of the union, dark factories | Lenny's Newsletter |
| Marc Andreessen | Latent Space podcast, agent architecture, layoff contrarian | Latent Space, 20VC, Fortune |
| Boris Cherny | DMCA retraction, OpenClaw billing | TechCrunch |
| Josh Gottheimer | National security concerns | Axios, The Hill |
| Charles Carmakal | TeamPCP impact: 1,000+ environments | The Register |
| Jim Farley | Essential economy vs AI disruption | Fortune |
| Sam Altman | TBPN acquisition | CNBC |
| Steve Yegge | "Vibe Maintainer" — AI-generated PR workflow | Medium |
| Guillermo Rauch | "Agent responsibly" — enterprise agent playbook | Vercel Blog |
| Swyx | Hosted Andreessen on Latent Space | Latent Space |
| Theo Browne | Claude Code leak video, 162K views | YouTube |
| Aaron Levie | Jevons Paradox — AI makes everyone busier | Diginomica, X |
| Teresa Torres | Vibe coding doom loop, agent scheduling | Product Talk |

### Inactive (❌)
| Voice | Notes |
|---|---|
| Gergely Orosz | Likely active (paywalled), not confirmed |
| Kent C. Dodds | Not active this week |
| Addy Osmani | Not active this week |
| Kelsey Hightower | Keynoting Nutanix .NEXT April 7–9 |

## 10. Model & Tool Updates

- **Anthropic** — 300K max_tokens Batches API, 1M context migration (April 30), auto mode blog post, OpenClaw subscription block, emotions research
- **Google** — Gemma 4 (4 variants), Gemini 3.1 Pro, Deep Think, Chrome, Android Auto
- **GitHub** — Copilot cloud agent (research/plan/code, commit signing, org controls)
- **OpenAI** — $122B round at $852B, TBPN acquisition, Codex update, Sora shutdown
- **Microsoft** — 3 new AI models, $10B Japan investment
- **Playwright** — v1.59: Screencast API, browser.bind(), CLI debugger for agents, dashboard, trace analysis
- **NVIDIA** — Vera Rubin platform in production
- **Alibaba** — Qwen 3.6-Plus (1M context, $0.29/M input)
- **Cursor** — Cursor 3 redesign
- **Windsurf** — GPT-5.1/Codex, Gemini 3 Pro, quota-based pricing
- **OpenClaw** — Acquired by OpenAI, ambient OS pattern

## 11. Jobs & Economic Impact

- **Numbers table** — 52K Q1 tech layoffs, Oracle 20–30K, Meta hundreds, Block 4K, CFO survey 0.4%
- **Three narratives** — (1) AI replacing workers, (2) AI as excuse, (3) AI creates different jobs
- **Productivity paradox** — Some workers +346% time
- **Who's hiring** — Data center construction, AI safety, AI infrastructure
- **Capital behind the cuts** — Q1 venture $300B (80% AI), $650B collective infra spend

## 12. Signals & Radar

### 🔴 Critical
- Anthropic operational security under Congressional scrutiny
- Axios npm compromise: North Korea targets 70M+ weekly downloads
- Azure AI Foundry: CVSS 10

### 🟠 Warning
- Oracle's 6am email as new layoff template
- DMCA overreach at internet scale
- Apple enforcing against vibe coding apps

### 🟢 Emerging
- Gemma 4 under Apache 2.0
- Copilot cloud agent + Cursor 3: agent IDE era
- California AI executive order (March 30)
- Microsoft threat report: agent ecosystem as attack surface
- **Dark code enters mainstream vocabulary** — Shapiro's dark factory concept, StrongDM revelation
- **GitHub Octoverse: AI-driven code velocity accelerating** — 986M pushes, 46% Copilot-generated, 14x projection
- **Playwright 1.59: testing infrastructure goes agent-first** — screencast API, shared browsers, CLI debugging for agents

### 🔵 Watch
- Congressional oversight of AI lab security
- "AI-washing" layoffs narrative going mainstream
- OpenAI media strategy (TBPN)
- OpenAI $122B round at $852B valuation

### Key Quotes (7)
1. Karpathy — "I've never felt this much behind as a programmer"
2. Andreessen — "Every large company is overstaffed... silver bullet excuse"
3. Carmakal — "over 1,000 impacted SaaS environments"
4. Anthropic spokesperson — "release packaging issue caused by human error"
5. Gottheimer — "If Claude is replicated, we sacrifice the competitive edge"
6. Andreessen — "Those days are just over" (Latent Space)
7. Sam Altman — "I don't expect them to go any easier on us"
