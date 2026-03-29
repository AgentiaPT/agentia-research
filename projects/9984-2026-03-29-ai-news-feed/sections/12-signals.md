## 12. Signals & Radar

### Critical Signals 🔴

| Signal | Evidence |
|--------|----------|
| **Supply chain attacks now chain through security tools** | TeamPCP weaponized Trivy (a security scanner) to backdoor LiteLLM. The tools meant to protect the ecosystem became the attack vector. |
| **Frontier model details leaked via basic misconfiguration** | Anthropic's CMS default exposed ~3,000 internal documents including Claude Mythos. No sophisticated attack — just a setting left on "public." |

### Warning Signals 🟠

| Signal | Evidence |
|--------|----------|
| **75% agent regression rate in long-term maintenance** | SWE-CI paper shows agents that pass all tests still break codebases over time. Only Claude Opus exceeds 50% zero-regression. |
| **Platform data defaults eroding developer trust** | GitHub opted all Copilot users into training data collection. 172 downvotes, near-universal community backlash. |
| **Rate limit throttling undermines autonomous capabilities** | Anthropic shipped Auto Mode while simultaneously throttling session limits during peak hours. |
| **Sora's $15M/day cost collapse** | OpenAI shut down Sora after six months — inference costs 7x higher than total lifetime revenue. Economics of large generative models remain brutal. |

### Emerging Signals 🟢

| Signal | Evidence |
|--------|----------|
| **AI pentesting for vibe-coded apps** | Lovable + Aikido: automated security testing integrated into the build flow. $100/test. |
| **Reasoning-blind classifiers for agent safety** | Claude Code Auto Mode uses a classifier that can't see the agent's reasoning — preventing self-justification of dangerous actions. |
| **Autonomous research loops entering production** | Karpathy's autoresearch: 700 experiments, 11% speedup. Shopify CEO reports 19% gains. Varun Mathur ran 35 agents on 333 experiments unsupervised. |
| **Three-agent architecture for sustained coding** | Anthropic's Planner/Generator/Evaluator pattern enables 6-hour coherent sessions at $200. |
| **Agent coordination > agent generation** | Osmani: "Not generation, but coordination" is the hard problem. Three focused agents outperform one generalist. |
| **Human pair programming → agent pair programming** | JetBrains sunsets Code With Me, replaces with ACP agent integration. The product strategy is now explicit. |

### Watch Signals 🔵

| Signal | Evidence |
|--------|----------|
| **Anthropic IPO timeline** | Bloomberg reports October 2026 consideration. |
| **Pentagon appeal in Ninth Circuit** | Government has 7 days to appeal Judge Lin's injunction. Precedent for AI company usage restrictions at stake. |
| **Mythos/Capybara general availability** | Anthropic working to make it "much more efficient" before release. Timeline unknown. |
| **AI bots > human traffic** | HUMAN Security confirms automated traffic eclipsed human users. AI agent traffic grew 7,851% YoY. |
| **Google's free Gemini Code Assist** | 180K completions/month free — 90x the typical free tier. Pricing pressure on Copilot, Cursor, Windsurf. |

---

## Key Quotes of the Week

> "To get the most out of the tools that have become available now, you have to remove yourself as the bottleneck"
> — **Andrej Karpathy** · [WinBuzzer](https://winbuzzer.com/2026/03/23/karpathy-humans-bottleneck-ai-research-xcxwbn/)

> "Nothing in the governing statute supports the Orwellian notion that an American company may be branded a potential adversary and saboteur of the U.S. for expressing disagreement with the government"
> — **Judge Rita F. Lin** · [NPR](https://www.npr.org/2026/03/26/nx-s1-5762971/judge-temporarily-blocks-anthropic-ban)

> "When asked to evaluate work they've produced, agents tend to respond by confidently praising the work — even when, to a human observer, the quality is obviously mediocre"
> — **Anthropic Engineering** · [Anthropic](https://www.anthropic.com/engineering/harness-design-long-running-apps)

> "Almost nobody's figured out how to make everything work together as smoothly as possible... And that's the actual hard problem here. Not generation, but coordination"
> — **Addy Osmani** · [O'Reilly AI CodeCon](https://talks.addy.ie/oreilly-codecon-march-2026/)

> "Powerful technologies rarely yield simple consequences"
> — **Martin Fowler** · [martinfowler.com](https://martinfowler.com/fragments/2026-03-26.html)

> "AI assisted PRs are now only allowed for accepted issues. Drive-by AI PRs will be closed without question. Bad AI drivers will be banned from all future contributions"
> — **Mitchell Hashimoto** · [X](https://x.com/mitchellh/status/2014433315261124760)

> "Old skills are losing leverage, and nobody has the answers — not even the people who've been doing this for 30 years"
> — **Kent Beck** · [Tidy First?](https://tidyfirst.substack.com/p/nobody-knows)

---

## Voice Tracker Table

| Voice | Active This Week | Key Topic | Source |
|-------|-----------------|-----------|--------|
| Simon Willison | ✅ Mar 22–27 | Supply chain cooldown, LiteLLM response, Auto Mode | [simonwillison.net](https://simonwillison.net/) |
| Addy Osmani | ✅ Mar 26 | Code Agent Orchestra, O'Reilly AI CodeCon | [addyosmani.com](https://addyosmani.com/blog/code-agent-orchestra/) |
| Martin Fowler | ✅ Mar 24, 26 | Anthropic AI study, ADRs, "both booster and doomer" | [martinfowler.com](https://martinfowler.com/) |
| Andrej Karpathy | ✅ Mar 23 | AutoResearch, "humans are bottleneck", "state of psychosis" | [WinBuzzer](https://winbuzzer.com/2026/03/23/karpathy-humans-bottleneck-ai-research-xcxwbn/) |
| Kent Beck | ✅ ~Mar 25 | "Nobody Knows" / Still Burning series | [tidyfirst.substack.com](https://tidyfirst.substack.com/) |
| Kelsey Hightower | ✅ Mar 23–26 | KubeCon EU Amsterdam | [CNCF](https://www.cncf.io/) |
| Daniel Stenberg | ✅ Mar 22, 26, 27 | NTLM beast, curl meeting, HTTP/3 talk | [daniel.haxx.se](https://daniel.haxx.se/) |
| Mitchell Hashimoto | 📌 Earlier Mar | Ghostty AI bug fix ($4.14), Vercel board, AI PR policy | [X](https://x.com/mitchellh/) |
| Steve Yegge | ❌ | (Mar 11: Pragmatic Engineer podcast, "eight levels") | — |
| Gergely Orosz | ❌ | (Mar 11: Steve Yegge interview) | — |
| Ethan Mollick | ❌ | (Mar 12: "Shape of the Thing") | — |
| Grady Booch | ❌ | (Mar 19: InfoWorld profile) | — |
| Patrick Debois | ❌ | (Mar: Sonar Summit, Context Flywheel) | — |
| Charity Majors | ❌ | (Mar 9: SRECon, "clarity is the scarce resource") | — |
| Dave Farley | ❌ | (Feb: Aviator podcast, "bigger than agile") | — |
| DHH | ❌ | — | — |
| ThePrimeagen | ❌ | (Mar 20: The Standup #050) | — |
| Bryan Cantrill | ❌ | — | — |
| Jaana Dogan | ❌ | — | — |
| Mike Mason | ❌ | — | — |
| Max Woolf | ❌ | — | — |
| Chelsea Troy | ❌ | — | — |
| Clive Thompson | 📌 Earlier Mar | (Mar 12: NYT Magazine "Coding After Coders") | — |
