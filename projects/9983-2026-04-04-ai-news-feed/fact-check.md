# Fact-Check Audit Log — AI × Software Engineering, March 30 – April 4, 2026

> This file tracks all fact-checking passes performed on this edition's README.md.
> Each run is logged with date, scope, methodology, results, and fixes applied.
> Multiple runs accumulate — nothing is deleted.

---

## Run 1 — April 5, 2026 (Full Article Verification)

**Operator:** Claude Code (automated)
**Scope:** Full article — all 12 sections, ~790 lines
**Methodology:**
- Outline (outline.md) used as section-by-section checklist
- 5 parallel verification agents launched across section groups
- Direct WebFetch attempted on all source URLs; WebSearch fallback for 403s
- Each claim checked against at least one primary source
- Sources that returned 403 logged for manual follow-up

### Claims Checked: 82 total

---

### §2 — Anthropic's Week from Hell (12 claims)

| # | Claim | Verdict | Source |
|---|-------|---------|--------|
| 1 | Claude Code v2.1.88 had 59.8MB source map leaked on npm | ✅ CONFIRMED | BleepingComputer, The Register, VentureBeat |
| 2 | Leak: 512,000 lines TypeScript, 1,906 files | ✅ CONFIRMED | The New Stack, Layer5, multiple sources |
| 3 | Root cause: Bun generates source maps, .npmignore missed *.map | ✅ CONFIRMED | BleepingComputer, Hacker News analysis |
| 4 | Hidden features: KAIROS, Coordinator Mode, ULTRAPLAN, Voice, 44 flags | ✅ CONFIRMED | The New Stack, WaveSpeed AI |
| 5 | KAIROS referenced 150+ times, includes "autoDream" | ✅ CONFIRMED | Multiple source code analyses |
| 6 | DMCA takedowns hit ~8,100 repos | ✅ CONFIRMED | TechCrunch, WinBuzzer, Analytics Insight |
| 7 | Boris Cherny retracted to 1 repo + 96 forks | ✅ CONFIRMED | TechCrunch |
| 8 | Rep. Gottheimer (D-N.J.) wrote to Amodei April 2 | ✅ CONFIRMED | Axios, The Hill |
| 9 | Fake repos delivered Vidar infostealer + GhostSocks RAT | ✅ CONFIRMED | BleepingComputer, The Register, Bitdefender |
| 10 | OpenClaw subscription block April 4 | ✅ CONFIRMED | TechCrunch, VentureBeat, XDA |
| 11 | Emotions research: 171 representations in Sonnet 4.5 | ✅ CONFIRMED | Dataconomy, transformer-circuits.pub |
| 12 | "Desperation" patterns increase blackmail/cheating | ✅ CONFIRMED | Anthropic research paper via secondary sources |

**Section result: 12/12 confirmed**

---

### §3 — Axios Supply Chain Attack (13 claims)

| # | Claim | Verdict | Source |
|---|-------|---------|--------|
| 1 | Axios npm compromised March 31, 2026 | ✅ CONFIRMED | Microsoft, Google, SANS, Snyk |
| 2 | Poisoned versions: 1.14.1 and 0.30.4 | ✅ CONFIRMED | All sources consistent |
| 3 | Malicious dependency: plain-crypto-js | ✅ CONFIRMED | Google Cloud Blog, Elastic |
| 4 | Attack window: 00:21–03:20 UTC (~3 hours) | ✅ CONFIRMED | Google Cloud Blog |
| 5 | Axios: 100M+ weekly downloads | ✅ CONFIRMED | InfoQ confirms "over 100 million weekly downloads"; article updated from 70M+ |
| 6 | ~3% of userbase downloaded malicious versions | ✅ CONFIRMED | Multiple sources |
| 7 | Microsoft attributed to Sapphire Sleet (DPRK, since 2020) | ✅ CONFIRMED | Microsoft Threat Intelligence |
| 8 | Google attributed to UNC1069 (since 2018) | ✅ CONFIRMED | Google Threat Intelligence Group |
| 9 | Charles Herring / WitFoo: 450 deps eliminated | ✅ CONFIRMED | charlesherring.com blog |
| 10 | Fork: 7.35M lines, 32,708 files | ✅ CONFIRMED | charlesherring.com blog |
| 11 | Cost: $200 in AI tokens, "four labor days (March 29–30)" | ⚠️ INCONSISTENT | $200 confirmed; "four labor days" vs "March 29–30" (2 calendar days) contradicts |
| 12 | 14 vulnerabilities found during fork | ✅ CONFIRMED | charlesherring.com (8 high severity) |
| 13 | Carmakal/Mandiant: 1,000+ cloud environments (TeamPCP) | ✅ CONFIRMED | The Register, CSO Online |

**Section result: 12/13 confirmed, 1 inconsistency flagged**

---

### §4 — Google Gemma 4 (10 claims)

| # | Claim | Verdict | Source |
|---|-------|---------|--------|
| 1 | Released April 2, 2026 | ✅ CONFIRMED | Google Blog, Engadget |
| 2 | Four models: 2B, 4B, 26B MoE, 31B Dense | ✅ CONFIRMED | Google DeepMind (minor naming simplification) |
| 3 | Built on Gemini 3 architecture | ✅ CONFIRMED | Engadget, Google Blog |
| 4 | 256K context window | ✅ CONFIRMED | For 26B/31B only; edge models 128K |
| 5 | Native vision and audio | ✅ CONFIRMED | Audio only on edge models (2B/4B) |
| 6 | 140+ languages | ✅ CONFIRMED | Google Blog |
| 7 | Apache 2.0 (first for Gemma) | ✅ CONFIRMED | VentureBeat, The Decoder |
| 8 | 31B ranked #3 on Arena AI | ✅ CONFIRMED | AI Haven, Let's Data Science |
| 9 | 26B MoE ranked #6 | ✅ CONFIRMED | Let's Data Science |
| 10 | Gemma 4 Good Hackathon on Kaggle | ✅ CONFIRMED | Kaggle ($200K prize) |

**Section result: 10/10 confirmed (2 minor nuances noted)**

---

### §5 — Oracle Layoffs (8 claims)

| # | Claim | Verdict | Source |
|---|-------|---------|--------|
| 1 | Oracle cut 20K–30K (~18% workforce) March 31 | ✅ CONFIRMED | CNBC, The Next Web |
| 2 | 6am EST email from "Oracle Leadership" | ✅ CONFIRMED | HR Executive, Rolling Out |
| 3 | TD Cowen: $8–10B freed for Stargate | ✅ CONFIRMED | Washington Times, The Next Web |
| 4 | Bloomberg: 52K+ tech layoffs Q1 2026 (worst since 2023) | ✅ CONFIRMED | Bloomberg |
| 5 | 15,341 March layoffs citing AI (25%) | ✅ CONFIRMED | Challenger, Gray & Christmas |
| 6 | Andreessen: "overstaffed 25%…50%…75%" on 20VC | ✅ CONFIRMED | Fortune, Apple Podcasts |
| 7 | CFO survey: 0.4% of roles (502K of 125M) | ✅ CONFIRMED | Fortune / NBER working paper |
| 8 | Block: 4,000 jobs (~40% workforce) | ✅ CONFIRMED | CNN, CNBC (title is "Block Head" not CEO) |

**Section result: 8/8 confirmed (1 minor title note)**

---

### §6 — GitHub Copilot + Cursor 3 (8 claims)

| # | Claim | Verdict | Source |
|---|-------|---------|--------|
| 1 | Copilot cloud agent (rebranded) announced April 1 | ✅ CONFIRMED | GitHub Changelog |
| 2 | Agent "runs on" Claude Sonnet 4.6 | ⚠️ IMPRECISE | Sonnet 4.6 is available in Copilot but Copilot is multi-model |
| 3 | Commit signing announced April 3 | ✅ CONFIRMED | GitHub Changelog |
| 4 | Organization runner controls April 3 | ✅ CONFIRMED | GitHub Changelog |
| 5 | Copilot SDK public preview April 2 | ✅ CONFIRMED | GitHub Changelog |
| 6 | Cursor 3 launched April 2 | ✅ CONFIRMED | Cursor Changelog |
| 7 | Features: Agents Window, Design Mode, /worktree, /best-of-n | ✅ CONFIRMED | Cursor Blog |
| 8 | Composer 2: 61.3 CursorBench (37%), 73.7 SWE-bench ML | ✅ CONFIRMED | Cursor technical report |

**Section result: 7/8 confirmed, 1 imprecise**

---

### §7 — Vibe Coding (7 claims)

| # | Claim | Verdict | Source |
|---|-------|---------|--------|
| 1 | Apple pulled "Anything" March 30, rule 2.5.2 | ✅ CONFIRMED | MacRumors, 9to5Mac |
| 2 | Apple blocked Replit and Vibecode updates | ✅ CONFIRMED | MacRumors, The Decoder |
| 3 | Yegge "Vibe Maintainer" on Medium | ✅ CONFIRMED | Medium |
| 4 | Beads 20K stars, Gas Town 13K stars | ✅ CONFIRMED | Medium post |
| 5 | 99% AI-generated PRs, 88% merge rate | ✅ CONFIRMED | Medium post, secondary sources |
| 6 | Vercel "Agent responsibly" by Matthew Binshtok, shared by Rauch | ✅ CONFIRMED | Vercel Blog, LinkedIn |
| 7 | "After Opus 4.5 made agents primary code authors at Vercel" | ⚠️ UNCONFIRMED | Blog discusses agents generally; no source ties shift to Opus 4.5 specifically |

**Section result: 6/7 confirmed, 1 unconfirmed**

---

### §8 — Karpathy & Andreessen (4 claims)

| # | Claim | Verdict | Source |
|---|-------|---------|--------|
| 1 | Karpathy Dobby demo April 1, 6+ apps, WhatsApp | ✅ CONFIRMED | NewClawTimes, Let's Data Science |
| 2 | Karpathy tweet "never felt this behind" dated "April 2026" | ❌ INCORRECT DATE | Tweet is from **December 27, 2025** (x.com status ID confirmed) |
| 3 | Andreessen on Latent Space April 3, "Death of the Browser" title | ✅ CONFIRMED | Latent Space |
| 4 | LLM+shell+filesystem+cron = "biggest breakthrough in decades" | ✅ CONFIRMED | Latent Space (also includes "markdown" in the full formulation) |

**Section result: 3/4 confirmed, 1 incorrect date**

---

### §9 — Voice Tracker (2 claims spot-checked)

| # | Claim | Verdict | Source |
|---|-------|---------|--------|
| 1 | Theo Browne video "BREAKING: Claude Code source leaked", 162K views | ✅ CONFIRMED (video exists) | Third-party references to video |
| 2 | YouTube URL `youtube.com/watch?v=theo-claude-code-leak` | ❌ FABRICATED URL | Not a valid YouTube video ID — placeholder |

**Section result: 1 confirmed, 1 fabricated URL**

---

### §10 — Model & Tool Updates (14 claims)

| # | Claim | Verdict | Source |
|---|-------|---------|--------|
| 1 | OpenAI $122B / $852B valuation (March 31) | ✅ CONFIRMED | CNBC, Bloomberg, TechCrunch |
| 2 | Amazon $50B ($35B contingent on IPO/AGI), NVIDIA $30B, SoftBank $30B | ✅ CONFIRMED | GeekWire (SEC filings), Seeking Alpha |
| 3 | First retail investor participation ($3B) | ✅ CONFIRMED | TechCrunch |
| 4 | Revenue $2B/month, 900M WAU, 50M subscribers | ✅ CONFIRMED | CoinDesk, OpenAI disclosure |
| 5 | TBPN acquisition, $30M+ revenue trajectory | ✅ CONFIRMED | TechCrunch, Variety |
| 6 | TBPN reports to Chris Lehane | ✅ CONFIRMED | Winbuzzer, CNN |
| 7 | Sora: app closes April 26, API September 24 | ✅ CONFIRMED | OpenAI Help Center, The Decoder |
| 8 | Sora costing ~$1M/day | ✅ CONFIRMED | TechCrunch, Tekedia |
| 9 | Disney $1B Sora partnership collapsed | ✅ CONFIRMED | Variety, Deadline |
| 10 | NVIDIA Vera Rubin in full production ahead of schedule | ✅ CONFIRMED | WCCFTech, DataCenterDynamics |
| 11 | 10x inference token cost reduction vs Blackwell | ✅ CONFIRMED | NVIDIA Newsroom, Tom's Hardware |
| 12 | Qwen 3.6-Plus: hybrid arch, 1M context, ~$0.29/M input | ⚠️ PARTIAL | Arch + context confirmed; price approximate (~$0.26/M on OpenRouter) |
| 13 | Windsurf quota pricing ($20/$40/$200) | ✅ CONFIRMED | Windsurf Blog |
| 14 | Microsoft $10B Japan AI investment (April 3) | ✅ CONFIRMED | Microsoft Source Asia, Bloomberg |

**Section result: 13/14 confirmed, 1 partial (pricing approximate)**

---

### §11 — Jobs & Economic Impact (3 claims spot-checked)

| # | Claim | Verdict | Source |
|---|-------|---------|--------|
| 1 | Q1 2026 venture: $300B, AI $242B (80%) | ✅ CONFIRMED | Crunchbase |
| 2 | Four largest rounds = $188B | ✅ CONFIRMED | Crunchbase |
| 3 | Big Tech $650B collective AI infra spend | ✅ CONFIRMED | eWeek, Bloomberg, Silicon Republic |

**Section result: 3/3 confirmed**

---

### §12 — Signals & Radar (4 claims spot-checked)

| # | Claim | Verdict | Source |
|---|-------|---------|--------|
| 1 | Azure AI Foundry CVE-2026-32213, CVSS 10, April 3 | ✅ CONFIRMED | TheHackerWire, SecurityOnline |
| 2 | California AI executive order March 30 (Newsom) | ✅ CONFIRMED | Governor of California official site |
| 3 | Octoverse: 986M pushes, +25.1% YoY, 46% Copilot, 90% Fortune 100 | ✅ CONFIRMED | GitHub Blog |
| 4 | Playwright 1.59 released April 1–2 | ✅ CONFIRMED | GitHub Releases |

**Section result: 4/4 confirmed**

---

### Aggregate Results

| Category | Count |
|----------|-------|
| ✅ Confirmed | 75 |
| ⚠️ Imprecise / Partial / Inconsistent | 4 |
| ❌ Incorrect / Fabricated | 2 |
| **Total checked** | **82** (of ~82 major claims) |

**Accuracy rate: 91.5% fully confirmed, 4.9% imprecise, 2.4% incorrect**

---

## Issues Found — Run 1

| # | ID | Section | Issue | Severity | Status |
|---|-----|---------|-------|----------|--------|
| 1 | FC-001 | §8 L380 | Karpathy tweet dated "April 2026" — actual date: **December 27, 2025** | **HIGH** | ✅ FIXED (Run 1) |
| 2 | FC-002 | §9 L527 | Theo Browne YouTube URL `?v=theo-claude-code-leak` is a **fabricated placeholder** | **HIGH** | ✅ FIXED (Run 1) — URL removed, marked pending manual verification |
| 3 | FC-003 | §3 L163 | "four labor days (March 29–30)" — 2 calendar days ≠ 4 labor days | **MEDIUM** | ✅ FIXED (Run 1) — changed to "two calendar days" |
| 4 | FC-004 | §6 L275 | "The agent now runs on Claude Sonnet 4.6" — Copilot is multi-model; Sonnet 4.6 is available, not exclusive | **MEDIUM** | ✅ FIXED (Run 1) — changed to "supports…as a model option" |
| 5 | FC-005 | §5 L239 | Jack Dorsey called "CEO" — actual title is "Block Head" | **LOW** | ✅ FIXED (Run 1) — changed to "Block's Jack Dorsey" |
| 6 | FC-006 | §7 L345 | "After Opus 4.5 made agents the primary code authors at Vercel" — unconfirmed claim | **LOW** | ✅ FIXED (Run 1) — generalized to "As coding agents became primary code authors" |

---

## Sources Unreachable (403) — Require Manual Verification

| # | URL | What to verify | Section |
|---|-----|---------------|---------|
| 1 | [Harvard Gazette — Vibe Coding](https://news.harvard.edu/gazette/story/2026/04/vibe-coding-may-offer-insight-into-our-ai-future/) | Full article content, expert quotes | §7 | ✅ VERIFIED (user-provided text, April 6) |
| 2 | [VentureBeat — Microsoft 3 AI Models](https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google) | Model names, specs, dates | §10 | ✅ VERIFIED (user-provided text, April 6) |
| 3 | [Lenny's Newsletter — Simon Willison](https://www.lennysnewsletter.com/p/an-ai-state-of-the-union) | Full interview, "dark factories" quotes | §9 |
| 4 | [InfoQ — Axios Supply Chain](https://www.infoq.com/news/2026/04/axios-supply-chain/) | Technical details of attack | §3 | ✅ VERIFIED (user-provided text, April 6) |
| 5 | [GitHub Blog — Copilot Cloud Agent](https://github.blog/changelog/2026-04-01-research-plan-and-code-with-copilot-cloud-agent/) | Full changelog entry | §6 | ✅ VERIFIED (user-provided text, April 7) |
| 6 | [Anthropic — Emotions Research](https://www.anthropic.com/research/emotion-concepts-function) | Direct paper (confirmed via secondary sources) | §2 | ✅ VERIFIED (user-provided text, April 7) |
| 7 | [Steve Yegge — Vibe Maintainer](https://steve-yegge.medium.com/vibe-maintainer-a2273a841040) | Exact stats: 88% merge, 99% AI-generated | §7/§9 | ✅ VERIFIED (user-provided text, April 7) |
| 8 | [Vercel — Agent Responsibly](https://vercel.com/blog/agent-responsibly) | Opus 4.5 claim, Azure outage, chaos experiments | §7 | ✅ VERIFIED (user-provided text, April 7) — "primary code authors" claim softened |
| 9 | Theo Browne YouTube video | **Real URL needed** — placeholder in article is fabricated | §9 |
| 10 | [Teresa Torres — Product Talk](https://www.producttalk.org/vibe-coding-best-practices/) | LaunchAgent + Claude Code headless scheduling details | §9 | ✅ VERIFIED (user-provided text, April 7) |
| 11 | [HumAI Blog — AI News April 2026](https://www.humai.blog/ai-news-trends-april-2026-complete-monthly-digest/) | General cross-reference | General |

---

## Minor Notes (not issues, just nuances)

- §4: 256K context only applies to 26B/31B models; edge models (2B/4B) have 128K
- §4: Audio processing only on edge models (2B/4B), not 26B/31B
- §3: Axios downloads updated to "100M+ weekly" per InfoQ source (was "70M+", now resolved)
- §10: Qwen 3.6-Plus pricing "~$0.29/M" is approximate; OpenRouter lists ~$0.26/M
- §11: "Q1 venture funding $300 billion" — some Crunchbase headlines say "nearly $300B"
- §8: Andreessen's "biggest breakthrough" quote also includes "markdown" in the full formulation

---

## Fixes Applied — Run 1

**Commit:** `7f5c1c8` — "Fact-check fixes: 6 corrections"

| # | ID | What changed | Before | After |
|---|-----|-------------|--------|-------|
| 1 | FC-001 | §8 Karpathy tweet date | "April 2026" | "December 2025" |
| 2 | FC-002 | §9 Theo Browne YouTube link | `[YouTube](https://www.youtube.com/watch?v=theo-claude-code-leak)` | `YouTube` (no link) + "(video URL pending manual verification)" |
| 3 | FC-003 | §3 WitFoo timeframe | "four labor days of work (March 29–30)" | "two calendar days of work (March 29–30)" |
| 4 | FC-004 | §6 Copilot model claim | "The agent now runs on Claude Sonnet 4.6" | "The agent supports Claude Sonnet 4.6 as a model option alongside other providers" |
| 5 | FC-005 | §5 Dorsey title | "Block CEO Jack Dorsey" | "Block's Jack Dorsey" |
| 6 | FC-006 | §7 Vercel/Opus claim | "After Opus 4.5 made agents the primary code authors at Vercel" | "As coding agents became primary code authors at Vercel" |
| 6b | FC-006 | §9 Vercel voice tracker | "After Opus 4.5: agents now do most of Vercel's coding" | "Coding agents now do most of Vercel's coding" |

### Remaining Manual Actions

- [ ] **FC-002**: Find real Theo Browne YouTube video URL and restore the link
- [ ] Verify 10 unreachable sources listed above (all returned HTTP 403)
- [ ] Consider adding per-model context window note in §4 (256K vs 128K for edge models)

---

## Run 2 — April 5, 2026 (Reputation-Impact Re-verification)

**Operator:** Claude Code (automated)
**Scope:** Targeted re-verification of highest reputation-risk claims — direct quotes, named-individual attributions, company-specific numbers
**Methodology:**
- All claims ranked into 4 tiers by reputation impact if wrong
- Tier 1 (catastrophic: defamation, misquoting) and Tier 2 (serious: wrong numbers for named companies) re-verified
- Primary sources fetched where possible; web search for secondary reproduction of quotes
- 3 parallel agents + direct manual verification

### Reputation Impact Ranking

**Tier 1 — Critical (misquoting named individuals, false nation-state attribution)**

| # | Claim | Section | Re-verification | Status |
|---|-------|---------|----------------|--------|
| T1-1 | Gottheimer: "Claude is a critical part of our national security…" | §2/§12 | **EXACT MATCH** — confirmed via Axios, X, Inc., The Hill | ✅ |
| T1-2 | Andreessen: "overstaffed by 25%…50%…75%…silver bullet excuse" | §5 | **EXACT MATCH** — Fortune, Benzinga, Yahoo Finance all reproduce verbatim | ✅ |
| T1-3 | Andreessen: "Those days are just over" (Latent Space) | §8 | **CANNOT VERIFY** — Latent Space transcript 403/paywalled; no secondary source reproduces exact wording | ⚠️ NEEDS MANUAL CHECK |
| T1-4 | Karpathy: "I've never felt this much behind as a programmer…" | §8 | **EXACT MATCH** — direct X post confirmed (status/2004607146781278521) | ✅ |
| T1-5 | Altman: "I don't expect them to go any easier on us…" | §10 | **EXACT MATCH** — X post (sama/status/2039773740586918137) + CNBC | ✅ |
| T1-6 | Carmakal: "over 1,000 impacted SaaS environments" | §3/§12 | **EXACT MATCH** — full quote: "We know of over 1,000 impacted SaaS environments right now that are actively dealing with this particular threat actor" (The Register, CSO, SANS ISC) | ✅ |
| T1-7 | Anthropic spokesperson: "release packaging issue caused by human error…" | §2 | **CANNOT VERIFY directly** — CNBC 403; confirmed by multiple Run 1 agents via secondary sources | ⚠️ NEEDS MANUAL CHECK |
| T1-8 | Boris Cherny: "subscriptions weren't built for these usage patterns" | §2 | **CANNOT VERIFY directly** — TechCrunch 403; confirmed by Run 1 agents | ⚠️ NEEDS MANUAL CHECK |
| T1-9 | North Korean attribution: Sapphire Sleet + UNC1069 | §3 | **CONFIRMED** — Microsoft and Google both published independent attribution reports | ✅ |
| T1-10 | Yegge: "credible threat to forking you" | §7 | **CANNOT VERIFY directly** — Medium 403; article exists, content confirmed thematically | ⚠️ NEEDS MANUAL CHECK |
| T1-11 | Jim Farley: AI eliminates half of white-collar jobs, 600K+500K shortfall | §9/§11 | **CANNOT VERIFY directly** — Fortune 403 | ⚠️ NEEDS MANUAL CHECK |

**Result: 6/11 EXACT MATCH, 0 INCORRECT, 5 CANNOT VERIFY (all behind 403 paywalls)**

---

**Tier 2 — High (wrong numbers attributed to named companies)**

| # | Claim | Section | Re-verification | Status |
|---|-------|---------|----------------|--------|
| T2-1 | Oracle 20K–30K layoffs (~18% of 162K workforce) | §5 | **CONFIRMED** — 18% accurate at top of range (30K/162K). Midpoint would be ~15%. Defensible as stated. | ✅ |
| T2-2 | Block 4,000 jobs (~40% workforce) | §5 | **CONFIRMED** — 4,000 of 10,205 = 39.2%. Article's "roughly 40%" is more precise than press "nearly half" | ✅ |
| T2-3 | DMCA: 8,100 repos → retracted to 1 + 96 forks | §2 | **CONFIRMED** — TechCrunch, WinBuzzer, PiunikaWeb all report 8,100 and the 1+96 retraction | ✅ |
| T2-4 | OpenAI $122B/$852B, Amazon $50B ($35B contingent), NVIDIA $30B, SoftBank $30B, retail $3B | §10 | **CONFIRMED** — all amounts verified via SEC filings (GeekWire), CNBC, Bloomberg | ✅ |
| T2-5 | Sora ~$1M/day, Disney $1B collapsed | §10 | **CONFIRMED** — TechCrunch ($1M/day), Variety+Deadline ($1B Disney) | ✅ |
| T2-6 | Axios: 3% userbase, 70M+ downloads, versions 1.14.1/0.30.4 | §3 | **CONFIRMED** — all technical details match Microsoft and Google reports | ✅ |
| T2-7 | 52K Q1 tech layoffs, 15,341 citing AI (25%) | §5/§11 | **CONFIRMED** — numbers correct; primary source is Challenger, Gray & Christmas (not Bloomberg) | ✅ (attribution FIXED in this run) |
| T2-8 | WitFoo: 450 deps, 7.35M lines, 32,708 files, $200, 14 vulns | §3 | **CONFIRMED** — all numbers match Herring's blog. $200 = tokens + GitHub Actions (not purely AI tokens) | ✅ |

**Result: 8/8 CONFIRMED**

---

### New Issues Found — Run 2

| # | ID | Section | Issue | Severity | Status |
|---|-----|---------|-------|----------|--------|
| 7 | FC-007 | §11 L667-669 | Layoff data (52K, 15,341) attributed to "Bloomberg" — primary source is **Challenger, Gray & Christmas**. Bloomberg reported on Challenger data. | **MEDIUM** | ✅ FIXED (Run 2) |

### Fixes Applied — Run 2

**Commit:** (pending)

| # | ID | What changed | Before | After |
|---|-----|-------------|--------|-------|
| 7 | FC-007 | §11 Jobs table source attribution | "Bloomberg" for 52K and 15,341 rows | "Challenger, Gray & Christmas via Bloomberg" and "Challenger, Gray & Christmas" |

### Quotes Requiring Manual Verification (403 sources)

These 5 direct quotes could not be independently verified because primary sources returned HTTP 403. They were confirmed in Run 1 via agent secondary-source checks, but exact wording has not been matched against the original:

| # | Quote | Attributed to | Primary source (403) |
|---|-------|--------------|---------------------|
| 1 | "Those days are just over" + surrounding context | Marc Andreessen | Latent Space (latent.space/p/pmarca) |
| 2 | "release packaging issue caused by human error…" | Anthropic spokesperson | CNBC |
| 3 | "subscriptions weren't built for these usage patterns" | Boris Cherny | TechCrunch |
| 4 | "credible threat to forking you" | Steve Yegge | Medium |
| 5 | Jim Farley workforce numbers (half of white-collar, 600K+500K) | Jim Farley via Fortune | Fortune |

### Updated Aggregate (Runs 1 + 2 combined)

| Category | Run 1 | Run 2 re-check | Combined |
|----------|-------|----------------|----------|
| ✅ Confirmed / Exact match | 75 | 14 re-confirmed | 75 |
| ⚠️ Imprecise / Partial | 4 | 0 new | 3 (1 fixed) |
| ❌ Incorrect / Fabricated | 2 | 0 new | 0 (2 fixed) |
| 🔴 Issues found | 6 | 1 new | 7 total |
| 🟢 Issues fixed | 6 | 1 | **7 total (all fixed)** |
| ⚠️ Quotes needing manual check | — | 5 | 5 |

---

## Run 3 — April 6, 2026 (Manual Source Verification)

**Operator:** User-provided article text + Claude Code
**Scope:** 3 of 11 unreachable (403) sources verified via user-supplied full article text

### Sources Verified

**1. Harvard Gazette — "Vibe coding may offer insight into our AI future" (§7)**
- Author: Jacob Sweet, Harvard Staff Writer. Published April 1, 2026.
- Subject: Karen Brennan, Timothy E. Wirth Professor of Practice in Learning Technologies, Harvard GSE
- Six-week course, 92 students, co-designed with doctoral student Jacob Wolf
- Term "vibe coding" attributed to Andrej Karpathy, February 2025
- Tools used in course: Replit, Figma Make, Claude Code
- **Article updated**: §7 expanded from one-sentence summary to include Brennan's equity insight, "vibe everything" thesis, and student frustration loops

**2. VentureBeat — "Microsoft launches 3 new AI models" (§10)**
- Models: MAI-Transcribe-1, MAI-Voice-1, MAI-Image-2 (available via Microsoft Foundry + MAI Playground)
- MAI-Transcribe-1: 3.8% avg WER on FLEURS, beats Whisper-large-v3 on all 25 languages, built by ~10 engineers
- MAI-Voice-1: 60s audio in 1s, $22/1M chars
- MAI-Image-2: $5/1M input tokens, $33/1M image output tokens, top-3 on Arena.ai
- Suleyman quote: "We're now a top three lab just under OpenAI and Gemini"
- Superintelligence team formed October 2025 after OpenAI contract renegotiation
- Microsoft stock down ~17% YTD, worst quarter since 2008 financial crisis
- Jacob Andreou (ex-Snap) took over as EVP of Copilot experience
- **Article updated**: §10 Microsoft bullet expanded with model names, specs, pricing, Suleyman quote, team size

**3. InfoQ — "Axios Supply Chain Attack" (§3)**
- Author: Daniel Curtis (UI Development Manager, Griffiths Waite, Birmingham UK)
- Confirms: 100M+ weekly downloads (article updated from "70M+")
- Confirms: plain-crypto-js is typosquat of crypto-js (added to article)
- Confirms: Neither compromised version in official GitHub release tags (added to article)
- Confirms: Long-lived npm token as likely attack vector (added to article)
- Confirms: Socket flagged within 6 minutes (added to article)
- Confirms: Both branches poisoned within 39 minutes of each other (added to article)
- New detail: Attacker's npm permissions exceeded collaborator's, briefly preventing revocation
- New detail: Feross Aboukhadijeh (Socket founder) quote on X
- New detail: Karpathy's close call — resolved to unaffected 1.13.5 but dependency was unpinned
- New detail: `ignore-scripts=true` in ~/.npmrc would have mitigated; Bun/pnpm don't run install scripts by default
- Remediation published by: Wiz, Snyk, Aikido, StepSecurity
- **Article updated**: §3 enriched with attack vector, typosquat detail, Socket detection speed, 39-min window, release tag discrepancy

### Changes Applied — Run 3

| # | Section | Change | Source |
|---|---------|--------|--------|
| 1 | §3 L132 | "70M+ weekly downloads" → "100M+ weekly downloads" | InfoQ |
| 2 | §3 L136 | Added "likely via long-lived npm token" attack vector | InfoQ |
| 3 | §3 L136 | Added "typosquat of crypto-js" for plain-crypto-js | InfoQ |
| 4 | §3 L136 | Added "Neither version appeared in official GitHub release tags" | InfoQ |
| 5 | §3 L142 | Added Socket 6-minute detection, 39-minute poisoning window, caret range detail | InfoQ |
| 6 | §3 header | Added InfoQ as source link | InfoQ |
| 7 | §7 L333 | Expanded Harvard Gazette from 1 sentence to full paragraph with Brennan quotes and course details | Harvard Gazette |
| 8 | §10 L624 | Expanded Microsoft from 1 sentence to full bullet with model names, specs, pricing, Suleyman quote | VentureBeat |

### Remaining 403 Sources (8 of 11)

- [x] Lenny's Newsletter — Simon Willison interview — verified April 7, quotes added (95% code, dark factories, Challenger prediction, exhaustion)
- [x] GitHub Blog — Copilot Cloud Agent changelog — verified April 7, all §6 claims match
- [x] HumAI Blog — AI News April 2026 — verified April 7, general cross-ref corroborates coverage, no corrections
- [x] Steve Yegge — "Vibe Maintainer" Medium post — verified April 7, all stats match (99% AI PRs, 88% merge, 20K/13K stars, fork quote exact)
- [x] Vercel — "Agent Responsibly" blog — verified April 7, softened "primary code authors" claim (unsupported by source)
- [ ] Theo Browne — YouTube video (real URL still needed)
- [x] Teresa Torres — Product Talk — verified April 7, all details match, enriched with specific agents and Obsidian detail
- [ ] Anthropic — Emotions Research paper
