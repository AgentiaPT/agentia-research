## 2. Project Glasswing — Anthropic Withholds Its Most Powerful Model

**April 7 | [Anthropic](https://www.anthropic.com/project/glasswing) · [The Hacker News](https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html) · [CNBC](https://www.cnbc.com/2026/04/07/anthropic-claude-mythos-ai-hackers-cyberattacks.html) · [CRN](https://www.crn.com/news/security/2026/5-things-to-know-on-anthropic-s-claude-mythos-and-project-glasswing) · [SiliconANGLE](https://siliconangle.com/2026/04/07/anthropic-debuts-project-glasswing-initiative-will-leverage-powerful-mythos-model-reinforce-software-security/)**

Seven days after [accidentally leaking 512,000 lines of Claude Code source](../9983-2026-04-04-ai-news-feed/README.md#2-anthropics-week-from-hell--claude-code-dmca-and-congressional-fire), Anthropic made the opposite announcement: it had built a model so powerful in cybersecurity that it was **too dangerous to release publicly**.

### Claude Mythos Preview

Claude Mythos Preview — Anthropic's most advanced model — was not explicitly trained as a cybersecurity tool. But as a result of general improvements in code understanding, reasoning, and autonomy, the model autonomously identified **thousands of zero-day vulnerabilities** in every major operating system and web browser. Some bugs had evaded detection for over two decades:

- **OpenBSD vulnerability** — 27 years old, undetected by human auditors and automated fuzzing
- **FreeBSD remote code execution** — 17 years old, full remote compromise
- **Multiple browser zero-days** — various ages, working exploits generated independently

Mythos generated working exploits for these vulnerabilities **independently** — no human guidance, no specific security training, just raw reasoning applied to code. This represents the biggest shift in vulnerability research since Google's Project Zero was founded in 2014.

Security experts predict that hostile actors will gain comparable AI capabilities within **6–18 months**, making Anthropic's head start a temporary window for defenders.

### The Glasswing Initiative

Rather than shipping Mythos publicly, Anthropic launched **Project Glasswing** — a cybersecurity defense initiative designed to secure critical software infrastructure for the AI era.

**Scale and scope:**
- **40+ partners** including AWS, Apple, Google, Microsoft, CrowdStrike, Cisco, NVIDIA, Palo Alto Networks, and the Linux Foundation
- **$100 million** in Claude usage credits for security researchers and maintainers
- **$4 million** in donations to open-source security organizations
- **Cyber Verification Program** — vetted access to Mythos for defensive purposes only

Partner organizations are using Mythos for vulnerability detection, penetration testing, binary analysis, and endpoint security hardening. Access is strictly limited — no public API, no general availability.

### Revenue Milestone

The same week, Anthropic surpassed OpenAI in annualized revenue for the first time:

- **Annualized revenue:** Anthropic $30B vs. OpenAI $24B
- **Enterprise customers ($1M+/yr):** Anthropic 1,000+ vs. OpenAI not disclosed
- **Fortune 10 coverage:** Anthropic 8 of 10 vs. OpenAI not disclosed
- **Primary revenue driver:** Anthropic — Claude Code + enterprise API; OpenAI — ChatGPT subscriptions

This growth was fueled by enterprise adoption — particularly Claude Code, which has become the fastest-growing developer tool in history. An IPO is being discussed for **October 2026** at a potential valuation near **$380 billion**.

### Compute Expansion

Anthropic signed expanded agreements with **Google and Broadcom** for an additional **3.5 gigawatts of TPU compute**, bringing total US-based AI infrastructure investment above $50 billion. Most new compute comes online in 2027.

> Anthropic is now running on all three major clouds: AWS, Google Cloud, and Azure.

The company that leaked everything last week is now the one guarding the internet's most critical infrastructure. The speed of that pivot — from vulnerability to fortress in seven days — is the story of the week.
