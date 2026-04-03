## 3. Supply Chain Siege — TeamPCP and the Axios Bomb

**March 19 – March 31 | [Palo Alto Unit42](https://unit42.paloaltonetworks.com/teampcp-supply-chain-attacks/) · [InfoQ](https://www.infoq.com/news/2026/04/axios-supply-chain/) · [The Register](https://www.theregister.com/2026/03/24/1k_cloud_environments_infected/) · [Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/03/24/detecting-investigating-defending-against-trivy-supply-chain-compromise/)**

Last week's edition covered the opening salvos of the TeamPCP campaign. This week, the full scope became clear — and then Axios fell.

### TeamPCP: When Security Tools Become Weapons

Between March 19 and March 27, threat group **TeamPCP** executed a methodical, escalating campaign that compromised four widely-used open-source projects:

| Date | Target | Vector |
|---|---|---|
| March 19 | **Trivy** (Aqua Security) | Incomplete credential rotation → force-push to 76/77 version tags |
| March 23 | **KICS** / Checkmarx AST | GitHub Actions compromise |
| March 24 | **LiteLLM** (AI gateway) | PyPI registry poisoning |
| March 27 | **Telnyx** (communications) | PyPI registry poisoning |

The attack on Trivy was particularly devastating. TeamPCP exploited an incomplete credential rotation following a minor breach in late February, then **force-pushed malicious code to 76 of 77 version tags** in the `aquasecurity/trivy-action` repository and all tags in `aquasecurity/setup-trivy`. Every CI/CD pipeline pinned to a Trivy version tag was potentially compromised.

> "We know of over 1,000 impacted SaaS environments right now that are actively dealing with this particular threat actor." — **Charles Carmakal**, Mandiant Consulting CTO, [via The Register](https://www.theregister.com/2026/03/24/1k_cloud_environments_infected/#:~:text=over%201%2C000%20impacted%20SaaS%20environments)

The irony is bitter: **the vulnerability scanner became the vulnerability**. Organizations running Trivy specifically to *detect* supply chain threats were instead *introducing* them.

### The Axios Bomb (March 31)

On the same day Anthropic leaked its source code, attackers compromised the official **Axios package on npm** — one of the most widely-used HTTP libraries in the JavaScript ecosystem, with **over 100 million downloads per week**.

The attacker gained access to the Axios maintainer's publishing credentials and released two poisoned versions (**1.14.1** and **0.30.4**) containing a hidden malicious dependency. On install, the code:

1. **Stole credentials** — cloud access keys, database passwords, API tokens
2. **Installed a Remote Access Trojan** (RAT) for persistent access

The dual version strategy (one on the 1.x branch, one on the 0.x branch) was designed to maximize coverage across both modern and legacy codebases.

### The AI Amplification Problem

A detail buried in the week's research deserves its own spotlight: a study analyzing **117,000 dependency changes** across thousands of GitHub repositories found that **AI coding agents choose package versions with known vulnerabilities 50% more often than human developers** ([Digital Today](https://www.digitaltoday.co.kr/en/view/45305/tech-insight-why-software-supply-chains-are-being-breached-quickly-amid-the-spread-of-ai-coding#:~:text=50%20percent%20more%20often%20than%20humans)).

The implications are circular: AI tools that accelerate development also accelerate the introduction of vulnerable dependencies, which then get exploited by supply chain attacks, which then require more security tooling — some of which (see: Trivy) is itself compromised.

### Why This Matters

TeamPCP's campaign represents a phase transition in supply chain attacks. Previous high-profile incidents (SolarWinds, Log4j, xz-utils) targeted general infrastructure. TeamPCP specifically targeted **security infrastructure** — the tools organizations use to protect themselves. When your vulnerability scanner is the vulnerability, the detection-defense loop breaks.
