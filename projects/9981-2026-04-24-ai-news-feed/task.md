# Task: AI × Software Engineering — April 17–24, 2026

## Original Request

Use the AI×Software runbook to update, date from last one until today. Stories to cover beyond the ones you research, my pick:

- GPT 5.5 launch, stats, community reception
- Claude design community impressions
- Claude recognizes quality degradation (blog post)
- Claude live refreshable dashboards on Claude Cowork
- Ethan Molick & all report about AI in game industry

## Window & Previous Edition

- This edition: April 17 to April 24, 2026
- Previous edition: `projects/9982-2026-04-11-ai-news-feed/`
- Previous theme: "The Agent Takeover"
- Previous "Watch" signals (from §12):
  - Congressional oversight of AI lab security (Gottheimer letter)
  - "AI-washing" layoffs narrative going mainstream
  - OpenAI media strategy (TBPN acquisition)
  - OpenAI $122B round at $852B valuation — IPO expected later 2026
  - Microsoft threat report: agent ecosystem as attack surface
  - Dark code entering mainstream vocabulary
  - Playwright 1.59: testing infrastructure goes agent-first
  - California AI executive order enforcement

## Voices Tracked (from previous 2 editions)

- Andrej Karpathy
- Simon Willison
- Marc Andreessen
- Boris Cherny (Anthropic)
- Josh Gottheimer (Congress)
- Charles Carmakal (Mandiant)
- Jim Farley (Ford)
- Sam Altman (OpenAI)
- Gergely Orosz
- Swyx (Latent Space)
- Theo Browne
- Steve Yegge
- Kelsey Hightower
- Kent C. Dodds
- Addy Osmani
- Guillermo Rauch
- Aaron Levie
- Teresa Torres
- Martin Fowler
- DHH
- Daniel Stenberg
- Bryan Cantrill
- Chelsea Troy
- Ethan Mollick

## Must-Cover Stories (from kickoff)

- GPT 5.5 launch, stats, community reception
- Claude design community impressions
- Claude recognizes quality degradation (blog post)
- Claude live refreshable dashboards on Claude Cowork
- Ethan Mollick & report about AI in game industry

## Progress

- [x] Phase 0: Setup & task.md
- [x] Phase 1: Research (7 parallel sub-agents) — 30+ stories found, all must-covers confirmed
- [x] Phase 2: Outline — theme "The Reality Check"
- [x] Phase 3: Per-section writing (12 sections, ~8300 words)
- [x] Phase 4: README assembly (618 lines, 8304 words)
- [x] Phase 5: Explorer dashboard (704 lines) + screenshot
- [x] Phase 6: Sources (153 links) + index updated
- [x] Phase 7: Fact-check loop — 2 passes, 13 total corrections (11 + 2)
- [x] Phase 8: Editor pass — structural fixes, cross-ref correction, redundancy cut
- [x] Phase 9: Final packaging — status: draft

## Key stories shipped

- GPT-5.5 launch (§2) — TerminalBench 82.7%, 1M context, $5/$30 pricing, community reception
- Anthropic three-bug postmortem (§3) — 7 weeks of product-layer degradation, "the wrong tradeoff"
- Claude Design + Cowork Live Artifacts (§4) — Figma stock −7%, Krieger board exit, BI disruption
- Security siege (§5) — MCP RCE "by design", CanisterSprawl worm, Bitwarden CLI, Comment and Control
- SpaceX $60B Cursor option (§6) — developer tooling goes geopolitical
- Market repricing (§7) — ServiceNow −18%, IBM −7%, Meta 8K layoffs, Morgan Stanley $22B gaming thesis
- DeepSeek V4 + research (§8) — Huawei Ascend, $0.14/M, 44% agent code survival rate
- Voice tracker (§9) — 12 active voices, 1 new (Mikhail Parakhin), 13 inactive

## Fact-check log

### Pass 1 (11 corrections)
- GPT-5.5 quote: "navigate ambiguity" → "navigate through ambiguity"
- Cursor valuation: "Series C, Jan 2026" → "Series D, Nov 2025"
- DeepSeek pricing: clarified V4-Flash vs V4-Pro distinction across 5 locations
- §7 links: fixed 4 URLs pointing to 2025 articles instead of 2026

### Pass 2 (2 corrections)
- IBM stock drop: −9% → −7% across 5 locations (sources report 6-7%)
- Mollick quote: unified wording across §7, §9, §12

### Pass 5 — Firecrawl fact-check (2026-04-25, §1–3 sections)

**§1 (Narrative) corrections:**
- arXiv `2504.13978` → `2604.20779` (SWE-chat paper: 44% agent code survival) — same fix applied to §8 in Pass 4, narrative section file and README table row were still using the old wrong ID
- Texas Instruments **+17%** → **~+19%** — actual close was +19.43% (largest single-day gain since 2000 per NewsBreak). Fixed in §1 section file, README narrative paragraph, §7 table, §7 prose, and §12 signals entry.
- IBM −9% in the §1 narrative table: **CONFIRMED CORRECT per Forbes source** (the linked article). The Forbes article explicitly reports −9% for IBM. The Pass 2 correction to −7% in §7 and §9 was based on other sources; the §1 narrative uses Forbes as its source which says −9%.

**§2 (GPT-5.5) corrections:**
- Quote: "navigate ambiguity" → "navigate **through** ambiguity" — verified verbatim from the OpenAI announcement page. (This was listed as fixed in Pass 1 but only applied to the README, not the section file.)

**§3 (Postmortem) corrections:**
- "**15-day overlap** between March 26 and April 10" → "**12-day overlap** between March 26 and April 7" — Bug 1 (reasoning effort) was fixed April 7; Bug 2 (cache clearing) ran until April 10. The period where BOTH bugs were simultaneously active is March 26–April 7 = 12 days. After April 7, only Bug 2 remained. Added clarifying sentence "Bug 1 was fixed April 7; Bug 2 continued alone until April 10."
- "all **affected paid** subscribers" → "all **subscribers**" — postmortem says verbatim "Today we are resetting usage limits for all subscribers."

**Confirmed correct (no changes needed):**
- GPT-5.5 codename "Spud" ✓
- "First fully retrained base model since GPT-4.5" ✓ 
- 1M token context window (API) ✓ (Codex uses 400K but API is 1M)
- Omnimodal (text, image, audio, video) ✓
- All benchmark scores: TerminalBench 82.7%, ARC-AGI 2 85%, SWE-Bench Pro 58.6%, MRCR 74.0% ✓
- ARC-AGI 2 gap "nearly 10 points" (85.0 − 75.8 = 9.2) ✓
- Pricing $5/$30 standard, $2.50/$15 Batch/Flex, $30/$180 Pro ✓
- ~40% token efficiency ✓
- Postmortem bug dates and durations ✓
- "Wrong tradeoff" quote verbatim match ✓
- ServiceNow −18% ✓, ServiceNow 22% revenue growth ✓
- VAST Data $30B valuation ✓



All 4 arXiv IDs in §8 pointed to completely unrelated papers (critical hallucinations from original research phase). Verified correct IDs using Firecrawl + web search:

| Wrong ID | Correct ID | Paper |
|---|---|---|
| 2504.13978 | **2604.20779** | SWE-chat: 44% agent code survival |
| 2504.14813 | **2604.17338** | PDB: frontier LLMs over-edit while debugging |
| 2504.14157 | **2604.18334** | CI/CD reliability: 61,837 runs, 5 bots |
| 2504.12069 | **2604.16286** | ASMR-Bench: sabotage detection AUROC 0.77 |

Additional fixes:
- **V4-Flash pricing**: Section file had "V4-Pro is $0.14/M" — corrected to "V4-Flash". V4-Pro is $1.74/M (confirmed via web search). Pricing table entry updated from "DeepSeek V4 $0.14" → "DeepSeek V4-Flash $0.14". Model updates table now shows both tiers.
- **CNBC URL**: Section file had `cnbc.com/2025/04/24/chinese-ai-lab-deepseek-releases-new-model.html` (wrong year, wrong article). Corrected to `cnbc.com/2026/04/24/deepseek-v4-llm-preview-open-source-ai-competition-china.html`.
- **Qwen 3.6-27B date**: "April 20" → "April 22" (confirmed via MarkTechPost, published 2026-04-22).
- **Qwen source link**: n1n.ai 404 → replaced with MarkTechPost (working, correct article).
- **AlphaAlign/WaltzRL source**: buildfastwithai.com/artificial-intelligence/iclr-2026-key-breakthroughs (404) → replaced with openreview.net (AlphaAlign) and iclr.cc (WaltzRL).
- **CI/CD description**: Original text described "persistent flakiness" and local-vs-CI breakage; actual paper finds agent-dependent differences (Copilot/Codex at 93–94% success) and negative correlation between frequency and success. Description updated to match actual findings.
- **PDB description**: Original text framed around "false confidence" and "introduce unnecessary changes elsewhere." Updated to match abstract language (over-editing/regeneration, precision below 45%).

### Pass 3 (user-supplied correction, 2026-04-24)
- Mollick quote was paraphrased ("Not everything around me is somebody's life work anymore"); corrected to verbatim tweet text: **"One thing thing about AI, for better and worse, is that 'everything around me is somebody's life work' is no longer a true assumption going forward."**
- Source link swapped from oneusefulthing.org / blockchain.news to the original tweet: https://x.com/emollick/status/2045318277958709540
- Fixed in 3 locations: §7 prose paragraph, §9 voice-tracker table row, §12 pull-quote.
- Outstanding: the April 24 "procedural 3D harbor town simulation" reference still points at oneusefulthing.org root — needs a specific article URL when one surfaces (flagged by `scripts/extract-readme-links.py`).

### Pass 6 — Firecrawl + web_search fact-check (2026-04-25, §4–12 all remaining sections)

**DOMAINS FLAGGED FOR MANUAL REVIEW (not fetched — prompt injection risk):**
| Domain | Section | Usage |
|---|---|---|
| blackswan-cybersecurity.com | §5 | RedSun threat advisory |
| beancount.io | §4 | "Vertical SaaS Survival Guide" (FABRICATED URL — beancount.io has no blog; link removed) |
| www.aibusinessreview.org | §4 | Krieger board exit article |
| www.basisreport.com | §4 | Figma stock drop article |
| enterprisezone.cc | §4 | Sachin Rekhi quote |
| www.mrlatte.net | §4 | "professional refinement" design take |
| poddtoppen.se | §9 | Swyx/Latent Space podcast URL |
| laffaz.com | §11 | Quora/Poe layoffs story (facts confirmed via web_search) |
| explore.n1n.ai | §10 | Qwen 3.6-27B (replaced with MarkTechPost) |
| blockchain.news | §9, §12 | Mollick/Altman stories |

**§4 (Claude Design / Cowork) corrections:**
- **beancount.io link removed** — beancount.io is a Python accounting tool and has no blog section. The URL `beancount.io/blog/2026/02/02/vertical-saas-survival-guide-competing-against-ai-giants` is fabricated. Changed to plain text "mandatory reading" (no link). Fixed in both §4 section file and README.
- Figma closing price $18.84, -7.28% from $20.32: **CONFIRMED** correct via officechai.com source (the cited source confirms these exact numbers).
- Mike Krieger resigned April 14 (3 days before April 17 launch): **CONFIRMED**.
- Krieger joined Figma board "in 2025": not independently verified but not disputed.

**§5 (Security) — all key facts confirmed:**
- MCP: 150M+ downloads, ~200K vulnerable servers, 7K+ public servers ✓
- CanisterSprawl StepSecurity link (pgserve URL): confirmed correct — "CanisterSprawl: pgserve Compromised on npm" is the article title ✓
- Bitwarden CLI: @2026.4.0, 93 minutes, 334 developers, sent to audit.checkmarx.cx ✓
- Oracle CPU April 21: 241 CVEs, 481 patches, 34 critical, Oracle Communications worst-hit at 139 patches ✓
- Comment and Control researchers (Aonan Guan, Zhengyu Liu, Gavin Zhong), CVSS 9.4 / $100 / $1,337 / $500 ✓

**§6 (SpaceX/Cursor) corrections:**
- **"Series C, Jan 2026"** → **"Series D, Nov 2025"** — confirmed: Cursor's Nov 2025 round was Series D at $29.3B. Pass 1 fixed the README but not the section file. Fixed now.
- **"January valuation"** → **"November 2025 valuation"** in prose — consistency fix.
- SpaceX IPO "as early as June 2026, up to $2T valuation": **CONFIRMED** ✓
- xAI Colossus ~1M H100-equivalent: **CONFIRMED** ✓
- VAST Data Series F led by Drive Capital and Access Industries, Nvidia/Fidelity/NEA: **CONFIRMED** ✓

**§7 (Market) corrections:**
- **Texas Instruments +17% → ~+19%** (×2 in section file: table and prose) — actual close April 23 was +19.43%
- **IBM CNBC URL had wrong year 2025** → replaced with `cnbc.com/2026/04/22/ibm-q1-earnings-report-2026.html`
- **ServiceNow Forbes URL had wrong year 2025** (Derek Saul article) → replaced with `forbes.com/sites/aliciapark/2026/04/23/ai-fears-keep-hammering-software-stocks...`
- **USNews software selloff URL was wrong** (2025 tariff article) → replaced with `money.usnews.com/investing/news/articles/2026-04-23/us-software-stocks-slide-as-ibm-servicenow-results-reignite-ai-disruption-fears`
- **Meta CNBC URL had wrong year 2025** → replaced with `cnbc.com/2026/04/23/meta-will-cut-10percent-of-workforce-as-it-pushes-more-into-ai.html`
- **Valeo Google Cloud URL had wrong year 2025** → replaced with `googlecloudpresscorner.com/2026-04-22-Valeo-and-Google-Cloud-Expand-...`
- IBM 9.5% revenue growth: **CONFIRMED** ✓
- Meta: 8K layoffs + 6K cancelled = 14K total, headcount 79K→71K, May 20 start, 16 weeks + 2/year severance: **CONFIRMED** ✓
- Valeo 35% AI code, 100K employees on Gemini Workspace: **CONFIRMED** ✓
- Morgan Stanley: $22B profits, ~50% cost cuts, $275B global gaming spend, Tencent/Sony/Roblox: **CONFIRMED** ✓
- Behaviour Interactive ~1,200 employees pre-layoff: **CONFIRMED** ✓

**§10 (Model Updates) corrections:**
- **Qwen date Apr 20 → Apr 22** (same as §8 fix, model table section file not previously updated)
- **explore.n1n.ai URL replaced with MarkTechPost URL** (known, trusted domain)

**§11 (Jobs) corrections:**
- **Texas Instruments +17% → ~+19%** in market signals table

**§9 (Voices) / §12 (Signals) — confirmed correct:**
- Dario Amodei quote/CNBC URL: **CONFIRMED** ✓
- Aaron Levie quote/Yahoo Tech: **CONFIRMED** ✓
- Martin Fowler blog: **CONFIRMED** ✓
- Daniel Stenberg blog: **CONFIRMED** ✓
- Comment and Control VentureBeat URL: used in both §5 and §12 (same article)



### Pass 7 — Reputable alternatives for all flagged domains (2026-04-25)

| Old domain | New source | Verified |
|---|---|---|
| `blackswan-cybersecurity.com` [18] | BleepingComputer "Recently leaked Windows zero-days now exploited in attacks" | ✓ confirmed (§5 + README) |
| `www.basisreport.com` | Gizmodo "Anthropic Launches Claude Design, Figma Stock Immediately Nosedives" | ✓ confirmed (§4 + README) |
| `www.aibusinessreview.org` | TechCrunch "Anthropic CPO leaves Figma's board after reports he will offer a competing product" | ✓ confirmed (§4 + README) |
| `enterprisezone.cc` (×2) | LinkedIn profile link for Sachin Rekhi + class link removed (no indexed primary source exists) | attribution kept |
| `www.mrlatte.net` | SmashingMagazine "The UX Designer's Nightmare: When Production-Ready Becomes A Design Deliverable" (Apr 22) | ✓ confirmed (§4 + README) |
| `poddtoppen.se` (×2) | latent.space/p/shopify (confirmed: Apple Podcasts also confirmed same episode title) | ✓ confirmed (§9 + README) |
| `laffaz.com` | **No reputable alternative found** — link removed, plain text attribution kept | (§11 + README) |
| `blockchain.news` Morgan Stanley gaming (§7) | money.usnews.com "Gaming Industry Could Unlock $22 Billion..." | ✓ confirmed (§7 + README) |
| `blockchain.news` Mollick quote (§9, §12) | x.com/emollick/status/2045318277958709540 (already in README §12 from Pass 3) | ✓ confirmed (§9) |
| `blockchain.news` Mollick GPT-5.5 benchmark (§9 + README) | oneusefulthing.org/p/sign-of-the-future-gpt-55 (confirmed URL from archive) | ✓ confirmed |
| `blockchain.news` Sam Altman "jakub-coded" (§9 + README) | openai.com/index/introducing-gpt-5-5/ + wording updated (tweet claim unverifiable; "jakub-coded" phrasing removed) | ✓ cleaned |



- [ ] Add 🧑‍💻 RQuintino: commentary blocks at natural breakpoints
- [ ] Review Voice Tracker balance
- [ ] Switch status: draft → complete when ready
- [ ] Push to remote (agent does NOT push — see CLAUDE.md)
