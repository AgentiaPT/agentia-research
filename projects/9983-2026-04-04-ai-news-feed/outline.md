# AI × Software Engineering — March 30 – April 4, 2026 — Outline

> **⚠️ This outline must stay in sync with README.md at all times.**
> After every content edit to the article, update this outline to reflect the change.
> See the [runbook](../../runbooks/ai-news-weekly.md) for the sync protocol.

## Theme: "The Unraveling"

The week Anthropic leaked its own future, supply chains crumbled again, Oracle cut 30,000 jobs via a 6am email, and the industry debated whether AI is actually replacing anyone at all.

---

## 1. The Week's Narrative — When the Builders Break Their Own Tools

- **Thesis:** The infrastructure of trust — from code registries to model labs to employment contracts — is fracturing under the weight of speed
- **Convergence table:** Model Security → Supply Chain → Open Models → Employment → Developer Tools → Funding
- **Unifying thread:** Tools outrunning the institutions that govern them (Anthropic npm leak = `.npmignore` missing an entry; Axios = stolen credentials; Oracle = mass email at dawn)
- **Deepest signal:** "Can any institution move this fast without dropping something critical?" — answer this week was no

## 2. Anthropic's Week from Hell — Claude Code, DMCA, and Congressional Fire

- **Act 1: Claude Code source leak (March 31)** — 59.8MB source map in v2.1.88, Bun default, 512K lines, 1,906 files
  - Hidden features: KAIROS daemon mode, Coordinator Mode, ULTRAPLAN, Voice mode
  - 44 hidden feature flags
- **Act 2: DMCA fiasco (April 1)** — 8,100 repos taken down, Boris Cherny retraction to 96 forks
  - Fastest-growing repo in GitHub history
- **Act 3: Congressional scrutiny (April 2)** — Gottheimer letter on national security, safety policy narrowing
- **Act 4: Malware exploitation** — Fake repos with Vidar infostealer + GhostSocks RAT

## 3. The Axios Bomb — North Korea Hits npm's Most-Downloaded HTTP Library

- **The attack (March 31)** — Poisoned versions 1.14.1 and 0.30.4, `plain-crypto-js` dependency
  - C2 contact → credential theft → RAT installation
  - 70M+ weekly downloads, 3% userbase hit in 3-hour window
- **North Korean attribution** — Microsoft (Sapphire Sleet) + Google (UNC1069)
- **Collateral damage** — Claude Code users who installed during window may have pulled trojanized Axios
- **TeamPCP fallout continues** — 1,000+ cloud environments (Carmakal/Mandiant)

## 4. Google's Open Model Play — Gemma 4 Under Apache 2.0

- **Gemma 4 release (April 2)** — Four models: 2B, 4B, 26B MoE, 31B Dense
  - 256K context, native vision/audio, 140+ languages, native function calling
- **Performance** — 31B ranked #3 on Arena AI, 26B MoE #6
- **License shift** — Apache 2.0 (first time, previously restricted)
- **Gemma 4 Good Hackathon** on Kaggle
- **Gemini 3.1 Pro** — improved reasoning, Deep Think for Ultra subscribers
- **Gemini in Chrome** + **Android Auto** expansion (April 3)

## 5. Oracle's 6am Email and the Great Layoff Reckoning

- **Oracle cuts 20K–30K (March 31)** — ~18% workforce, 6am email, no manager conversations
  - $8–10B freed for AI data centers (Stargate initiative)
- **Bloomberg data** — 52K tech layoffs Q1 2026, worst since 2023; AI cited in 25% of March layoffs
- **Andreessen counterpoint** — "silver bullet excuse," 25–75% overstaffed, AI not good enough until December
- **Fortune's nine reasons** — CFO survey: 0.4% roles projected cut; productivity paradox (+346% time on some tasks)

## 6. GitHub Copilot Goes Cloud-Native

- **Research, Plan, and Code (April 1)** — Rebranded from "coding agent," branch-only work, implementation plans
  - Running on Claude Sonnet 4.6
- **Commit Signing (April 3)** — Verified badge, works with "Require signed commits" branch protection
- **Organization Runner Controls (April 3)** — Default runner, lock settings
- **Copilot SDK (April 2)** — Public preview, Node/Python/Go/.NET/Java
- **Cursor 3 (April 2)** — Agents Window, Design Mode, /worktree, /best-of-n, Composer 2
  - Developer as orchestrator, not line-by-line coder

## 7. Vibe Coding Under Fire — Apple Cracks Down, Palo Alto Publishes Framework

- **Apple pulls "Anything" (March 30)** — Blocked Replit/Vibecode updates, App Store rule 2.5.2
- **Palo Alto Unit42** — "Securing Vibe Coding Tools," treat AI code as untrusted
- **Databricks** — "Passing the Security Vibe Check," guardrails not abandonment
- **Harvard Gazette** — Vibe coding as window into broader AI adoption patterns

## 8. Karpathy's Dobby and the Agent-First Future

- **Dobby demo (April 1)** — OpenClaw agent replacing 6+ home apps via WhatsApp
  - Scanned network, reverse-engineered APIs (Sonos, lights, HVAC, pool, security, shades)
- **"Never felt this behind"** — profession being "dramatically refactored"
- **Agentic engineering vs. vibe coding** distinction

## 9. Voice Tracker

### Active (✅)
| Voice | Key Topic | Source |
|---|---|---|
| Andrej Karpathy | Dobby agent demo, "agentic engineering" | Fortune, X |
| Simon Willison | AI state of the union, dark factories | Lenny's Newsletter |
| Marc Andreessen | AI layoffs as "silver bullet excuse" | 20VC, Fortune |
| Boris Cherny | Claude Code DMCA retraction | TechCrunch |
| Josh Gottheimer | National security concerns re: Anthropic | Axios, The Hill |
| Charles Carmakal | TeamPCP impact: 1,000+ environments | The Register |
| Jim Farley | Essential economy vs AI disruption | Fortune |
| Sam Altman | TBPN acquisition | CNBC |

### Inactive (❌)
| Voice | Notes |
|---|---|
| Gergely Orosz | No specific items this week |
| Swyx | AIE Europe prep, no episode |
| Theo Browne | Active on T3 Chat, no major AI takes |
| Steve Yegge | (listed as inactive — NEEDS UPDATE) |
| Addy Osmani | (listed as inactive — NEEDS UPDATE) |

## 10. Model & Tool Updates

- **Anthropic** — 300K max_tokens Batches API, 1M context window migration (April 30 deadline)
- **Google** — Gemma 4 (4 variants), Gemini 3.1 Pro, Deep Think, Chrome, Android Auto
- **GitHub** — Copilot cloud agent (research/plan/code, commit signing, org controls)
- **OpenAI** — $122B round at $852B, TBPN acquisition, Codex major update, Sora shutdown
- **Microsoft** — 3 new AI models (speech/voice/image), $10B Japan investment
- **NVIDIA** — Vera Rubin platform in production
- **Alibaba** — Qwen 3.6-Plus (1M context, $0.29/M input)
- **Cursor** — Cursor 3 redesign
- **Windsurf** — GPT-5.1/Codex, Gemini 3 Pro, quota-based pricing
- **OpenClaw** — Acquired by OpenAI, ambient OS pattern

## 11. Jobs & Economic Impact

- **Numbers table** — 52K Q1 tech layoffs, Oracle 20–30K, Meta hundreds, Block 4K, CFO survey 0.4%
- **Three narratives** — (1) AI replacing workers, (2) AI as excuse, (3) AI creates different jobs
- **Productivity paradox** — Some workers +346% time on tasks with AI
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

### 🔵 Watch
- Congressional oversight of AI lab security
- "AI-washing" layoffs narrative going mainstream
- OpenAI media strategy (TBPN)
- OpenAI $122B round at $852B valuation

### Key Quotes (6)
1. Karpathy — "I've never felt this much behind as a programmer"
2. Andreessen — "Every large company is overstaffed... silver bullet excuse"
3. Carmakal — "over 1,000 impacted SaaS environments"
4. Anthropic spokesperson — "release packaging issue caused by human error"
5. Gottheimer — "If Claude is replicated, we sacrifice the competitive edge"
6. Sam Altman — "I don't expect them to go any easier on us"

---

## Pending Additions (from user highlights, April 5)

These stories need to be integrated into the article and this outline updated:

- [ ] Latent Space pod with Marc Andreessen → §8 or §9
- [ ] GitHub 14x code commits forecast → §6 or §10
- [ ] Claude blocks OpenClaw subscriptions → §2 or §10
- [ ] Nuclear fork (Charles Herring, 400+ repos) → §3
- [ ] Anthropic emotions research → §2 or §10
- [ ] Claude auto mode blog post → §2 or §10
- [ ] Playwright 1.59 (AI-first testing) → §10
- [ ] Dark code / dark code factories → §7 or §12
- [ ] Steve Yegge "Vibe Maintainer" → §7 or §9
- [ ] Agent responsibly by Vercel → §7 or §12
