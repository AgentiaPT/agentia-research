# Outline: The Reality Check — April 17–24, 2026

> Sync warning: every edit to README.md must be mirrored here in the same commit.

**Theme:** The Reality Check
**Thesis:** The week GPT-5.5 landed, Anthropic admitted its flagship got dumber, AI coding agents were shown to be far less reliable than benchmarks suggest, and the market started pricing in what developers have known for months — AI is reshaping everything, but the gap between promise and production is wider than anyone wants to admit.

## 1. The Week's Narrative — The Reality Check
- Convergence: GPT-5.5 launches with impressive benchmarks + Anthropic admits quality bugs + research shows 44% agent code survival + software stocks crash
- Unifying thread: The frontier keeps advancing (GPT-5.5, DeepSeek V4) but reality bites back (quality bugs, pricing pain, stock crashes)
- Deepest signal: Markets are repricing the entire SaaS sector on AI substitution risk — even beating earnings can't save you

## 2. GPT-5.5 — "A New Class of Intelligence" Meets a New Class of Pricing
- Launch details: Apr 23, 1M context, TerminalBench 82.7%, SWE-Bench Pro 58.6%
- Pricing: $5/$30 per 1M (2× GPT-5.4) — community pushback
- Comparison to Opus 4.7 (still leads SWE-Bench Pro at 64.3%)
- ARC-AGI 2: 85% — reasoning leap
- Quote candidate: "a new class of intelligence for real work" — OpenAI
- Community reception: "meaningful, if incremental"

## 3. Anthropic's Three-Bug Postmortem — When "Nerfing" Was Actually Engineering Debt
- Three overlapping product bugs (reasoning effort, cache clearing, verbosity prompt)
- Timeline: March 4 → April 20 (7 weeks of degraded experience)
- Model weights never changed — all product-layer
- Quote: "the wrong tradeoff" — Anthropic
- Community: "clients were right" + praise for transparency
- Cross-ref: previous edition covered Opus 4.7 launch (April 16)

## 4. Claude Design & Cowork Live Artifacts — Anthropic's Platform Play
- Claude Design (Apr 17): AI design companion, Figma stock -7%, Krieger board resignation
- Cowork Live Artifacts (Apr 20): refreshable dashboards, BI disruption
- Quote: Sachin Rekhi on dashboards
- "RIP frontend developers" community reaction
- Why this matters: Anthropic competing with its own API customers

## 5. The Security Siege Continues — MCP's "By Design" RCE and the First Cross-Ecosystem Worm
- MCP architectural flaw: RCE on ~200K servers, Anthropic says "by design"
- CanisterSprawl: first self-propagating cross-ecosystem supply chain worm
- Bitwarden CLI compromise: targets AI tool configs
- "Comment and Control": 3 AI coding agents leak secrets via PR injection
- Google: AI threats in the wild
- RedSun zero-day in Windows Defender
- Cross-ref: fourth consecutive week of supply chain attacks

## 6. SpaceX's $60B Cursor Option — When AI Coding Tools Become Strategic Assets
- SpaceX $60B acquisition option for Cursor
- Cursor trains on xAI Colossus
- Context: Cursor's prior valuation ~$29.3B
- VAST Data $1B raise at $30B
- Vista Equity + Google Cloud for 90+ portfolio companies
- Why this matters: developer tooling is now geopolitical

## 7. The Market Repricing — Software Stocks Crash as AI Eats SaaS
- ServiceNow -18%, IBM -7% despite beating earnings
- iShares Software ETF -6% in one day, -27% in six months
- Texas Instruments +17% (AI infra beneficiary)
- Meta 8,000 layoffs to fund AI pivot
- Valeo: 35% of validated code AI-generated
- Behaviour Interactive layoffs (gaming)
- Morgan Stanley: $22B gaming profits from AI cost cuts

## 8. DeepSeek V4 & the Open-Weight Reality Check
- DeepSeek V4: 1.6T MoE on Huawei Ascend chips
- $0.14/M input tokens (20-50× cheaper than Western APIs)
- Qwen 3.6 family expansion
- Research papers: 44% agent code survival, over-editing gap, CI/CD reliability
- ICLR 2026 safety alignment breakthroughs
- The "reality check" in AI capabilities vs production readiness

## 9. Voice Tracker
- Active ✅: Dario Amodei, Ethan Mollick, Aaron Levie, Guillermo Rauch (Vercel breach), Steve Yegge (Google two-tier), Martin Fowler (Tech Radar), DHH (Omacon), Swyx (Shopify CTO interview), Daniel Stenberg (curl AI reports), Sam Altman, Simon Willison, Gergely Orosz
- Inactive ❌: Andrej Karpathy, Kelsey Hightower, Kent C. Dodds, Theo Browne, Chelsea Troy, Addy Osmani, Bryan Cantrill, Marc Andreessen (off-topic only)
- New: Mikhail Parakhin (Shopify CTO)

## 10. Model & Tool Updates
- GPT-5.5 (OpenAI, Apr 23)
- DeepSeek V4 preview (Apr 24)
- Qwen 3.6-27B + Max-Preview (Apr 20)
- Chatbot Arena: Opus 4.7 Thinking #1 overall
- Claude Design (Apr 17)
- Claude Cowork Live Artifacts (Apr 20)
- Cohere SDK on Oracle Cloud (Apr 20)

## 11. Jobs & Economic Impact
- Meta: 8,000 layoffs (10% workforce), 6,000 roles cancelled
- Behaviour Interactive layoffs (Dead by Daylight studio)
- Quora/Poe layoffs
- Software stocks crash despite strong earnings
- Morgan Stanley: $22B gaming industry AI profit opportunity
- Valeo: 35% AI-generated code
- SpaceX/Cursor $60B deal

## 12. Signals & Radar
- 🔴 Critical: MCP "by design" RCE across 200K+ servers; CanisterSprawl first cross-ecosystem supply chain worm
- 🟠 Warning: Software stock repricing accelerating; Meta 8K layoffs set template for AI-pivot layoffs; GPT-5.5 pricing 2× increase signals API margin compression
- 🟢 Emerging: DeepSeek V4 on domestic Chinese silicon; Claude Design threatens Figma; Anthropic postmortem sets transparency precedent
- 🔵 Watch: SpaceX/Cursor $60B — developer tooling goes geopolitical; ICLR 2026 safety alignment breakthroughs; Mollick gaming benchmarks + Morgan Stanley $22B thesis

## Key Quotes candidates
- "a new class of intelligence for real work" — OpenAI (GPT-5.5 launch)
- "the wrong tradeoff" — Anthropic (postmortem)
- "RIP frontend developers" — community reaction (Claude Design)
- "I don't want AI turned on our own people" — Dario Amodei (White House)
- "If you're building agents, you basically need to throw away large parts of previous work" — Aaron Levie
- "The challenge with AI in open source security has transitioned from an AI slop tsunami into more of a plain security report tsunami" — Daniel Stenberg

## Must-cover resolution
- GPT-5.5 launch → §2
- Claude Design community impressions → §4
- Claude quality degradation postmortem → §3
- Claude Cowork Live Artifacts → §4
- Ethan Mollick + gaming AI → §7 + §12

## Pending Additions
- [ ] Verify exact quotes from paywalled sources
- [ ] Check Mollick Substack for dedicated gaming post
