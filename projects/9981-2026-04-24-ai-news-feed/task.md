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

### Pass 3 (user-supplied correction, 2026-04-24)
- Mollick quote was paraphrased ("Not everything around me is somebody's life work anymore"); corrected to verbatim tweet text: **"One thing thing about AI, for better and worse, is that 'everything around me is somebody's life work' is no longer a true assumption going forward."**
- Source link swapped from oneusefulthing.org / blockchain.news to the original tweet: https://x.com/emollick/status/2045318277958709540
- Fixed in 3 locations: §7 prose paragraph, §9 voice-tracker table row, §12 pull-quote.
- Outstanding: the April 24 "procedural 3D harbor town simulation" reference still points at oneusefulthing.org root — needs a specific article URL when one surfaces (flagged by `scripts/extract-readme-links.py`).

## Handoff to user

- README: projects/9981-2026-04-24-ai-news-feed/README.md
- Explorer: https://agentiapt.github.io/agentia-research/projects/9981-2026-04-24-ai-news-feed/explorer.html
- Pending manual checks: none — all deferred items resolved in pass 2

## Pending commentary / decisions for user

- [ ] Add 🧑‍💻 RQuintino: commentary blocks at natural breakpoints
- [ ] Review Voice Tracker balance
- [ ] Switch status: draft → complete when ready
- [ ] Push to remote (agent does NOT push — see CLAUDE.md)
