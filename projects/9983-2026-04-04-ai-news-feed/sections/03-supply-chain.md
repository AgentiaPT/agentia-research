## 3. The Axios Bomb — North Korea Hits npm's Most-Downloaded HTTP Library

**March 31 | [Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/04/01/mitigating-the-axios-npm-supply-chain-compromise/) · [Google Cloud](https://cloud.google.com/blog/topics/threat-intelligence/north-korea-threat-actor-targets-axios-npm-package) · [The Hacker News](https://thehackernews.com/2026/04/google-attributes-axios-npm-supply.html)**

On March 31 — the same day Anthropic leaked its source code — attackers compromised the official **Axios package on npm**, one of the most widely-used HTTP libraries in the JavaScript ecosystem with **over 70 million downloads per week**.

### The Attack

Between 00:21 and 03:20 UTC, the attacker gained access to the Axios maintainer's publishing credentials, changed the maintainer's email to an attacker-controlled account, and released two poisoned versions (**1.14.1** and **0.30.4**) containing a hidden malicious dependency (`plain-crypto-js`). On install, the code:

1. **Contacted C2 servers** and downloaded OS-specific payloads (macOS, Windows, Linux)
2. **Stole credentials** — cloud access keys, database passwords, API tokens
3. **Installed a Remote Access Trojan** (RAT) for persistent access

The dual version strategy (one on the 1.x branch, one on the 0.x branch) was designed to maximize coverage across both modern and legacy codebases. Roughly **3% of the Axios userbase** downloaded the malicious versions during the three-hour window.

### North Korean Attribution

Both Microsoft and Google independently attributed the attack to **North Korean state actors**:

- Microsoft identified the infrastructure as belonging to **Sapphire Sleet**, a DPRK group active since 2020 focused on cryptocurrency and financial targets
- Google attributed it to **UNC1069**, a financially motivated North Korea-nexus threat actor active since at least 2018

### Collateral Damage

Users who installed or updated Claude Code via npm on March 31 between 00:21 and 03:29 UTC may have pulled a trojanized version of Axios containing a cross-platform RAT — making Anthropic's own tool briefly a malware delivery vector.

### TeamPCP Fallout Continues

Meanwhile, the [TeamPCP supply chain campaign covered last week](../9984-2026-03-29-ai-news-feed/README.md#1-the-supply-chain-reckoning--litellm-trivy-and-the-teampcp-campaign) (Trivy → KICS → LiteLLM → Telnyx) continued to cause damage. Mandiant's CTO Charles Carmakal reported **1,000+ cloud environments** actively dealing with the threat actor ([The Register](https://www.theregister.com/2026/03/24/1k_cloud_environments_infected/)), and Microsoft published detailed [mitigation guidance](https://www.microsoft.com/en-us/security/blog/2026/03/24/detecting-investigating-defending-against-trivy-supply-chain-compromise/).

### Why This Matters

The Axios attack raises the stakes beyond TeamPCP. This wasn't a security tool compromise or an obscure package — it was one of npm's most-downloaded libraries, targeted by a nation-state actor. When North Korea is poisoning JavaScript's HTTP layer, every `npm install` is a potential attack surface.
