## 1. The Week's Narrative — When the Builders Break Their Own Tools

Last week was **the unraveling**. The company building one of the world's most capable AI models accidentally leaked its next-generation model's specifications, then leaked its flagship coding tool's source code, then accidentally took down 8,100 GitHub repositories trying to clean up, then received a Congressional letter questioning whether it can be trusted with national security. Meanwhile, a threat actor turned the industry's own vulnerability scanners into attack vectors, Oracle fired 30,000 people via a 6am email to fund AI data centers, and the most prolific open-source AI advocate on Earth said he hasn't typed a line of code since December.

The infrastructure of trust — from code registries to model labs to employment contracts — is fracturing under the weight of speed.

| Layer | Who | What |
|---|---|---|
| **Model Security** | Anthropic | Leaked Mythos specs + Claude Code source in one week |
| **Supply Chain** | TeamPCP / Axios attackers | Compromised security scanners + npm's most-downloaded HTTP library |
| **Open Models** | Google | Gemma 4 under Apache 2.0 — most capable open model family yet |
| **Employment** | Oracle / Bloomberg / Andreessen | 30K layoffs vs. "AI is the silver bullet excuse" |
| **Developer Tools** | GitHub / Karpathy | Copilot goes autonomous; Karpathy replaces apps with one agent |
| **Code Quality** | Multiple studies | 53% of AI code has security holes; 2.74× more XSS |

### The Unifying Thread

Every major story this week traces back to a single tension: **the tools are outrunning the institutions that govern them**. Anthropic's leaks weren't sophisticated attacks — they were configuration errors and packaging mistakes. TeamPCP didn't need zero-days — they exploited incomplete credential rotations. Oracle didn't restructure thoughtfully — they sent a mass email at dawn. The technology is moving at frontier speed, but the operational maturity around it is stuck in 2019.

### The Deepest Signal

The Anthropic saga is the week's defining metaphor. The company that writes the most sophisticated AI safety research on Earth couldn't keep its own model specifications or source code from leaking through a misconfigured CMS and a fat-fingered npm publish. When Congressman Gottheimer wrote asking whether Anthropic can be trusted with models that pose "unprecedented cybersecurity risks," the implicit question was bigger than one company: **can any institution move this fast without dropping something critical?**

The answer, this week, was no.
