# AI × Software Engineering — April 5–11, 2026 — Outline

> **⚠️ This outline must stay in sync with README.md at all times.**
> After every content edit to the article, update this outline to reflect the change.
> See the [runbook](../../runbooks/ai-news-weekly.md) for the sync protocol.

## Theme: "The Fortress"

The week the industry chose defense over disruption. Anthropic withheld its most powerful model for cybersecurity. The Big Three united against Chinese model copying. OpenAI published a policy paper on robot taxes. Meta abandoned open source. And someone threw a Molotov cocktail at Sam Altman's house.

---

## 1. The Week's Narrative — The Fortress

- **Thesis:** After weeks of unraveling (leaks, supply chain attacks, layoffs), the industry pivoted to defense on every front — technological, economic, legal, and physical
- **Convergence table:** Cybersecurity (Mythos/Glasswing) → Model Defense (anti-copying alliance) → Economic (robot tax) → Legal (Musk trial) → Physical (Altman attack) → Market (Meta goes closed)
- **Unifying thread:** Every major actor chose to build walls this week
- **Deepest signal:** The company that leaked its source code last week now withholds its most powerful model as too dangerous to release — the fastest pivot from vulnerability to fortress in tech history

## 2. Project Glasswing — Anthropic Withholds Its Most Powerful Model

- **Claude Mythos Preview (April 7)** — "Too dangerous to release" model
  - Autonomously found thousands of zero-day vulnerabilities in every major OS and browser
  - Bugs dating back 17-27 years (FreeBSD RCE, OpenBSD 27-year bug)
  - Generated working exploits independently
  - Biggest shift in vulnerability research since Google's Project Zero (2014)
- **Project Glasswing** — cybersecurity defense initiative
  - 40+ partners: AWS, Apple, Google, Microsoft, CrowdStrike, Cisco, NVIDIA, Palo Alto, Linux Foundation
  - $100M in usage credits + $4M to open-source security organizations
  - Cyber Verification Program for vetted access
- **Revenue milestone** — Anthropic surpasses OpenAI ($30B vs $24B annualized)
  - 1,000+ enterprise customers spending $1M+/year each
  - 8 of Fortune 10 using Anthropic
  - IPO discussed for October 2026, ~$380B valuation
- **Compute deals** — 3.5 GW of TPU compute from Google/Broadcom ($50B+ total US AI infrastructure)

## 3. The Anti-Distillation Alliance — Big Three Unite Against Chinese Model Copying

- **Frontier Model Forum goes operational (April 7)** — OpenAI, Anthropic, Google + Microsoft
  - Real-time attack intelligence sharing (modeled on cybersecurity ISACs)
  - Targeting: DeepSeek, Moonshot AI, MiniMax
  - Anthropic flagged 16M adversarial distillation attacks from 24,000 fake accounts
- **$1B AI Frontier Fund** — watermarking, detection, legal action
- **Coordinated lobbying** for stricter export controls and legislative protection
- **Context:** DeepSeek-R1 release sparked suspicions of training via adversarial distillation

## 4. Meta Goes Closed — Muse Spark and the End of Open-Source AI

- **Muse Spark launch (April 8)** — Meta's first proprietary model
  - Built by Meta Superintelligence Labs (MSL), led by Alexandr Wang (ex-Scale AI CEO)
  - Natively multimodal (text + images from pretraining)
  - Three reasoning modes: Instant, Thinking, Contemplating (parallel sub-agents)
  - 10x more efficient than Llama 4 Maverick
  - Health & wellness focus: physician collaboration, nutritional scanning
- **Business model shift** — no open source, private preview API only, Meta account required
- **Stock impact** — 9% jump, Meta AI app near top of App Store
- **$115-135B capex** announced for AI infrastructure
- **Strategic context** — Llama 4 benchmark controversy, Scale AI acquisition ($14.3B)
- **Significance** — Google's Gemma 4 becomes the last major Apache 2.0 frontier model

## 5. OpenAI's Robot Tax — The Intelligence Age Policy Blueprint

- **"Industrial Policy for the Intelligence Age" (April 6)** — OpenAI's policy paper
  - Robot tax on automated labor (comparable rates to displaced human workers)
  - Public wealth fund seeded by AI company contributions (Alaska Permanent Fund model)
  - Four-day workweek pilot programs at full pay
  - Automatic safety nets triggered by AI displacement metrics
  - Tax base shift from payroll to capital gains/corporate income
  - AI access framed as a fundamental right
- **Musk trial escalation (April 7)** — seeks Altman/Brockman ouster
  - Trial date: April 27, Oakland federal court
  - $134-150B damages sought (to nonprofit, not Musk)
  - Core claim: OpenAI betrayed nonprofit mission
- **Altman Molotov cocktail attack (April 10)** — physical violence against AI leaders
  - 4 AM attack on SF home, suspect arrested near OpenAI HQ
  - Suspect (Daniel Moreno-Gama, 20, from Texas) had list of AI executives
  - Federal charges: attempted murder, arson, destructive devices
  - Altman blog post: "de-escalate the rhetoric... fewer explosions in fewer homes"

## 6. Claude Managed Agents — Anthropic's Infrastructure Play

- **Public beta launch (April 8)** — composable APIs for production agents
  - $0.08 per agent runtime hour + standard token pricing
  - Architecture: brain (reasoning) + hands (sandbox execution) + session (event log)
  - Credential management, stateful sessions, error recovery
  - Compresses months of agent infrastructure work to days
- **Early adopters** — Notion, Asana, Sentry, Rakuten
- **Advisor Tool** — different Claude models in different roles within workflows
- **Competitive context** — vs OpenAI Assistants API, Google Vertex AI agents

## 7. The Regulatory Wave — 19 New AI Laws and Apple's Crackdown

- **19 AI bills passed into law** in two weeks (late March/early April)
  - Data transparency, user protections, deepfake restrictions, app store accountability
  - California and New York leading
- **Apple vs. Grok** — threatens removal of Musk's xAI chatbot over deepfake generation
  - Demanded formal content moderation plan
- **App Store AI spam** — 557K app submissions (24% increase), review delays
  - Top 1% capture 92% of in-app revenue
- **Follow-up**: California AI executive order (from last edition's "watch")

## 8. Supply Chain: The Siege Continues

- **Axios CVE published (April 9)** — CVE-2025-62718 (CVSS 9.3), SSRF vulnerability
  - North Korean attribution confirmed (UNC1069)
  - 600K downloads during 3-hour poisoning window
- **CPU-Z supply chain attack (April 9-10)** — official CPUID website compromised
  - Trojanized ZIPs with Alien RAT variant, 6-hour window
- **Trivy/TeamPCP continued fallout** — ongoing remediation in 1,000+ cloud environments
- **Adobe Acrobat Reader** — CVE-2026-34621 (CVSS 8.6), prototype pollution → RCE via PDFs

## 9. Voice Tracker

### Active (✅)
| Voice | Key Topic | Source |
|---|---|---|
| Sam Altman | Molotov attack response, "Building the Future" talk, robot tax paper | CNBC, Blog, TechCrunch |
| Dario Amodei (implied) | Glasswing announcement, Mythos decision | Anthropic |
| Elon Musk | Seeks Altman ouster, $134B damages | CNBC, Bloomberg |
| Evan Spiegel | Snap layoffs, AI generates 65% of code | CNBC, Fast Company |
| Alexandr Wang | Muse Spark launch, Meta Superintelligence Labs | Meta Blog |

### Inactive (❌)
| Voice | Notes |
|---|---|
| Andrej Karpathy | No major new statements this week |
| Simon Willison | Technical commentary, no headline takes |
| Marc Andreessen | Latent Space from previous week referenced |
| Gergely Orosz | No specific this-week items found |
| Steve Yegge | Not active this week |
| Kelsey Hightower | Nutanix .NEXT keynote was last week |

## 10. Model & Tool Updates

- **Anthropic** — Claude Mythos Preview (restricted), Claude Managed Agents (public beta), $30B revenue run rate
- **Meta** — Muse Spark (proprietary, multimodal, 3 reasoning modes, private API)
- **Zhipu AI** — GLM-5.1 (744B open-source, trained without NVIDIA hardware, surpasses GPT-5.4 in coding)
- **OpenAI** — "Robot tax" policy paper, Musk trial escalation, $122B round completed
- **Google** — Broadcom/Anthropic compute deal (3.5 GW TPU)
- **Claude Code** — 80.8% SWE-bench, 1M-token context beta, fastest-growing dev tool

## 11. Jobs & Economic Impact

- **Snap**: 1,000 jobs (16% workforce), AI generates 65% of code, $500M annualized savings
- **GoPro**: 23% workforce reduction
- **Pendo**: 10% (~90 people)
- **OpenAI robot tax** — proposes government robot tax, public wealth fund, 4-day workweek
- **Anthropic**: Surpassed OpenAI in revenue ($30B vs $24B), 1,000+ enterprise customers at $1M+
- **Meta**: $115-135B capex commitment, proprietary pivot
- **Capital surge**: Q1 VC hit $300B (2x previous year)

## 12. Signals & Radar

### 🔴 Critical
- Claude Mythos: AI model too dangerous to release — first major "capability suppression" decision
- Molotov cocktail attack on Sam Altman's home — AI debate turns physically violent
- 16M adversarial distillation attacks on US AI models from Chinese firms

### 🟠 Warning
- Meta abandons open source — Muse Spark closes the door on Llama's legacy
- 19 new AI bills passed into law in two weeks
- Musk trial (April 27) could force OpenAI structural changes, $134B damages

### 🟢 Emerging
- Claude Managed Agents at $0.08/hr — agent infrastructure becomes a commodity
- GLM-5.1: open-source 744B model trained without NVIDIA hardware
- OpenAI's robot tax: an AI company proposing to tax its own technology

### 🔵 Watch
- Anthropic IPO (October 2026, ~$380B valuation)
- CPU-Z supply chain attack: developer utility websites as attack vectors
- AI-generated app spam overwhelming App Store review processes
- Physical security of AI executives becoming an industry concern

### Key Quotes (6-7)
1. Altman — "de-escalate the rhetoric... fewer explosions in fewer homes, figuratively and literally"
2. Anthropic (on Mythos) — "too dangerous for public release" / capability that "greatly surpasses humans"
3. Evan Spiegel — AI generates "more than 65% of all new code at Snap"
4. Musk (court filing) — seeks removal of Altman as officer, $134B to nonprofit
5. OpenAI policy paper — "AI access as a fundamental right"
