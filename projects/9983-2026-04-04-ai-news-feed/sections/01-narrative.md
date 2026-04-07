## 1. The Week's Narrative — When the Builders Break Their Own Tools

Last week was **the unraveling**. Anthropic leaked its flagship coding tool's 512,000-line source code through an npm packaging error, then accidentally took down 8,100 GitHub repositories trying to clean up, then received a Congressional letter questioning whether it can be trusted with national security. Meanwhile, North Korea poisoned npm's most-downloaded HTTP library, Oracle fired 30,000 people via a 6am email to fund AI data centers, Google dropped its most capable open model under Apache 2.0, and both GitHub and Cursor shipped agent-management IDEs within 24 hours of each other.

The infrastructure of trust — from code registries to model labs to employment contracts — is fracturing under the weight of speed.

| Layer | Who | What |
|---|---|---|
| **Model Security** | Anthropic | Claude Code source leaked via npm; KAIROS daemon mode revealed |
| **Supply Chain** | North Korea / DPRK | Axios (70M+ downloads/week) poisoned with RAT |
| **Open Models** | Google | Gemma 4 under Apache 2.0 — 31B model ranks #3 globally |
| **Employment** | Oracle / Bloomberg / Andreessen | 30K layoffs vs. "AI is the silver bullet excuse" |
| **Developer Tools** | GitHub / Cursor | Both ship agent-management paradigms in the same week |
| **Funding** | OpenAI | $122B round at $852B valuation — largest private raise in history |

### The Unifying Thread

Every major story this week traces back to a single tension: **the tools are outrunning the institutions that govern them**. Anthropic's leak wasn't a sophisticated attack — it was Bun generating a source map and `.npmignore` missing an entry. The Axios compromise exploited stolen maintainer credentials. Oracle didn't restructure thoughtfully — they sent a mass email at dawn. The technology is moving at frontier speed, but the operational maturity around it is stuck in 2019.

### The Deepest Signal

The Anthropic saga is the week's defining metaphor. The company that writes the most sophisticated AI safety research on Earth couldn't keep its source code from leaking through a packaging error. When Congressman Gottheimer wrote asking whether Anthropic can be trusted with models that pose national security risks, the implicit question was bigger than one company: **can any institution move this fast without dropping something critical?**

The answer, this week, was no.
