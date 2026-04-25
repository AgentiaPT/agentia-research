## 8. Supply Chain: The Siege Continues

**April 5–11 | [The Register](https://www.theregister.com/2026/04/11/trivy_axios_supply_chain_attacks/) · [CodeRoasis](https://coderoasis.com/cve-2025-62718-the-axios-crisis-a-critical-ssrf-vuln-a-north-korean-supply-chain-attack-and-why-every-node-js-developer-needs-to-act-right-now/) · [InfoQ](https://www.infoq.com/news/2026/04/trivy-supply-chain-attack/)**

The supply chain siege that dominated last week's headlines continues with new developments and a fresh attack on a developer utility.

### Axios CVE Published (April 9)

The North Korean attack on Axios — [covered last week](../9983-2026-04-04-ai-news-feed/README.md#3-the-axios-bomb--north-korea-hits-npms-most-downloaded-http-library) as a breaking story — received a formal CVE designation this week:

- **CVE:** CVE-2025-62718
- **CVSS:** 9.3 (Critical)
- **Type:** Server-Side Request Forgery (SSRF) in NO_PROXY handling
- **Attribution:** UNC1069 (North Korean state-sponsored)
- **Blast radius:** ~600,000 downloads during 3-hour poisoning window

The CVE formalizes what was already known: the compromised Axios versions (1.14.1, 0.30.4) distributed a cross-platform RAT through a malicious `plain-crypto-js` dependency. Organizations are still auditing CI/CD pipelines and rotating secrets.

### CPU-Z Supply Chain Attack (April 9–10)

A **new** supply chain attack hit the official **CPUID website** — the distributor of CPU-Z, HWMonitor, and other popular system utilities. For approximately 6 hours, the site served trojanized ZIP archives containing a malicious DLL (`CRYPTBASE.dll`, Zig-compiled) with an **Alien RAT variant** backdoor.

This attack is notable because it targets **desktop software distributed through a vendor's own website** — not a package registry. The vector was web infrastructure compromise, not credential theft. Thousands of users downloading CPU utilities during the window were potentially exposed.

CPUID remediated the breach and published IoCs (Indicators of Compromise) for affected users.

### Trivy/TeamPCP Ongoing

The [TeamPCP campaign](../9984-2026-03-29-ai-news-feed/README.md#1-the-supply-chain-reckoning--litellm-trivy-and-the-teampcp-campaign) continues with active remediation across **1,000+ cloud environments**. Vulnerable package versions have been pulled, but the propagation through CI/CD pipelines means organizations are still discovering compromised downstream dependencies.

### Adobe Acrobat Reader (CVE-2026-34621)

A prototype pollution vulnerability in Adobe Acrobat Reader (CVSS 8.6) was confirmed to be **actively exploited in the wild** this week. Attackers are using maliciously crafted PDFs to achieve remote code execution. The widespread use of Acrobat in enterprise document workflows amplifies the supply chain risk — a single malicious PDF in a shared drive or email attachment can compromise a workstation.

### The Pattern

Three consecutive weeks of major supply chain attacks (TeamPCP → Axios → CPU-Z) across three different vectors (CI/CD credential theft → npm account compromise → website infrastructure). The attack surface is widening, the actors are diversifying, and the pace isn't slowing.
