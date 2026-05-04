# R3: Security & Vulnerabilities — April 25 to May 1, 2026

## Story: Mini Shai-Hulud — Cross-Ecosystem Supply Chain Worm Hits PyTorch Lightning & intercom-client
- **Date:** 2026-04-29 to 2026-04-30
- **Source:** https://www.aikido.dev/blog/pytorch-lightning-pypi-compromise-mini-shai-hulud
- **Outlet:** Aikido Security
- **Additional sources:**
  - https://www.kodemsecurity.com/resources/mini-shai-hulud-strikes-pytorch-lightning-and-intercom-client-inside-the-cross-ecosystem-supply-chain-attack (Kodem Security)
  - https://www.theregister.com/2026/04/30/supply_chain_attacks_sap_npm_packages (The Register)
  - https://thehackernews.com/2026/04/pytorch-lightning-compromised-in-pypi.html (The Hacker News)
  - https://github.com/intercom/intercom-node/security/advisories/GHSA-54pg-9963-v8vg (GitHub Advisory)
- **Key facts:**
  - PyTorch Lightning (`lightning` on PyPI) versions 2.6.2 and 2.6.3 compromised — 8.3M monthly downloads
  - npm `intercom-client@7.0.4` compromised at 15:00 UTC April 30, removed ~17:00 UTC (2 hours live)
  - SAP Cloud Application Programming Model npm packages also hit same day
  - Malware injected via `__init__.py`; spawned background thread downloading Bun JS runtime + 11 MB obfuscated payload (`router_runtime.js`)
  - Steals: SSH keys, AWS/GCP/Azure creds, GitHub/npm tokens, crypto wallets (BTC, LTC, XMR, DOGE), VPN creds, Discord/Slack sessions, shell histories
  - Worm propagation: harvests GitHub tokens, commits worm payloads across up to 50 branches per repo, impersonates "Anthropic Claude Code" identity in commits
  - Attribution: threat actor "TeamPCP" — linked to prior SAP-targeted npm campaigns
  - Signature string in exfil repos: "A Mini Shai-Hulud has Appeared"
- **Why it matters:** Most impactful cross-ecosystem supply chain attack of 2026 so far — affected AI/ML developer community's most popular training library with active worm propagation across GitHub repos.
- **Confidence:** high

---

## Story: Cursor IDE Sandbox Escape via Git Hooks (CVE-2026-26268) — Full Disclosure Published
- **Date:** 2026-04-28 (full technical disclosure published)
- **Source:** https://novee.security/blog/cursor-ide-cve-2026-26268-git-hook-arbitrary-code-execution/
- **Outlet:** Novee Security
- **Additional sources:**
  - https://hackread.com/cursor-ai-ide-vulnerability-code-execution-git-hooks/ (Hackread)
  - https://www.csoonline.com/article/4164250/critical-cursor-bug-could-turn-routine-git-into-rce.html (CSO Online)
  - https://www.sentinelone.com/vulnerability-database/cve-2026-26268/ (SentinelOne)
- **Key facts:**
  - CVE-2026-26268, CVSS 8.0–9.9 depending on database
  - Cursor IDE versions prior to 2.5 affected (patched February 2026, full details published April 28)
  - Attack: embedded bare git repository with malicious hooks (e.g., pre-commit) inside a project
  - Cursor's AI agent autonomously runs `git checkout`/commit operations, triggering hooks without user interaction
  - CWE-862 (Missing Authorization) — sandbox didn't restrict write access to `.git/hooks/`
  - No wild exploitation reported at disclosure time
- **Why it matters:** Demonstrates how AI coding agents autonomously performing git operations create novel attack surfaces — a single malicious repo clone leads to RCE without social engineering.
- **Confidence:** high

---

## Story: Hugging Face LeRobot Unauthenticated RCE via Pickle Deserialization (CVE-2026-25874)
- **Date:** 2026-04-28 to 2026-04-29
- **Source:** https://thehackernews.com/2026/04/critical-cve-2026-25874-leaves-hugging.html
- **Outlet:** The Hacker News
- **Additional sources:**
  - https://www.resecurity.com/en/blog/article/cve-2026-25874-hugging-face-lerobot-unauthenticated-rce-via-pickle-deserialization (Resecurity)
  - https://cyberpress.org/hugging-face-lerobot-vulnerability/ (CyberPress)
- **Key facts:**
  - CVE-2026-25874, CVSS 9.3–9.8 (Critical)
  - Unsafe `pickle.loads()` on unauthenticated gRPC channels in LeRobot PolicyServer
  - Exploitable methods: `SendPolicyInstructions`, `SendObservations`, `GetActions`
  - All versions through 0.5.1 affected; fix planned for 0.6.0 (unpatched at disclosure)
  - gRPC services use `add_insecure_port()` — no TLS/authentication by default
  - Security linter warnings about pickle usage were suppressed in codebase
  - Impact: full server compromise, lateral movement, data theft, potential physical safety risk (robotics)
- **Why it matters:** Critical unpatched RCE in Hugging Face's robotics framework — combines unsafe pickle deserialization with unauthenticated network exposure, putting AI robotics deployments at immediate risk.
- **Confidence:** high

---

## Story: Anthropic Launches Claude Security (AI Vulnerability Scanner) in Public Beta
- **Date:** 2026-04-30
- **Source:** https://www.securityweek.com/anthropic-unveils-claude-security-to-counter-ai-powered-exploit-surge/
- **Outlet:** SecurityWeek
- **Additional sources:**
  - https://siliconangle.com/2026/04/30/anthropic-announces-claude-security-public-beta-find-fix-software-vulnerabilities/ (SiliconAngle)
  - https://www.infosecurity-magazine.com/news/anthropic-claude-security-for-ai/ (Infosecurity Magazine)
- **Key facts:**
  - Public beta for Claude Enterprise customers, powered by Opus 4.7 model
  - Scans entire repositories/branches; traces data flows (not just pattern matching)
  - Generates confidence-rated findings with reproduction paths and proposed patches
  - Partners embedding it: CrowdStrike, Microsoft Security, Palo Alto Networks, SentinelOne, Wiz
  - In research preview since February; reportedly found critical exploits missed by existing tools for years
  - No custom API integration needed — available via Claude.ai sidebar
- **Why it matters:** Anthropic enters the security tools market directly — positions AI as both the threat (agent vulnerabilities) and the defense (automated vuln discovery and patching).
- **Confidence:** high

---

## Story: Apple Accidentally Ships Internal CLAUDE.md Files in Support App
- **Date:** 2026-04-30
- **Source:** https://tech.yahoo.com/ai/claude/articles/apple-using-claude-inside-company-114500152.html
- **Outlet:** Yahoo Tech / original discovery by Aaron Perris on X
- **Additional sources:**
  - https://onejailbreak.com/blog/apple-accidentally-revealed-using-claude-ai/ (ONE Jailbreak)
  - https://aiproductivity.ai/news/apple-claude-md-file-apple-support-app/ (AI Productivity)
- **Key facts:**
  - Apple Support iOS app v5.13 shipped two internal CLAUDE.md configuration files
  - Reveals Apple's internal AI system codenamed "Juno AI" for support chat infrastructure
  - Shows conversation routing architecture: human customer → Apple agent → AI assistant
  - Technical details exposed: Swift actors, AsyncStream, Keychain-based session persistence, internal UI library "SAComponents"
  - Apple issued silent 5.13.1 hotfix to remove files; no public statement
  - No user data or credentials leaked — but internal engineering practices exposed
- **Why it matters:** Confirms Apple's deep integration with Anthropic's Claude Code internally; highlights the risk of AI tool configuration files leaking into production builds — a new class of accidental disclosure.
- **Confidence:** high

---

## Story: US House Launches Joint Investigation into PRC AI Model Security Risks (Cursor/Anysphere & Airbnb)
- **Date:** 2026-04-29
- **Source:** https://homeland.house.gov/2026/04/29/chairmen-garbarino-moolenaar-announce-joint-investigation-into-national-security-risks-posed-by-prc-ai-models/
- **Outlet:** US House Homeland Security Committee (official)
- **Additional sources:**
  - https://www.semafor.com/article/04/29/2026/house-committee-probes-cursor-parent-airbnb-over-chinese-ai (Semafor)
  - https://www.nextgov.com/artificial-intelligence/2026/04/house-panels-probe-airbnb-anysphere-over-use-chinese-ai-models/413207/ (Nextgov)
- **Key facts:**
  - Joint probe by Homeland Security Committee + Select Committee on China
  - Letters sent to Anysphere (Cursor IDE maker) and Airbnb
  - Focus: Cursor's Composer 2 model built on Kimi (Moonshot AI, Beijing) — linked to large-scale distillation campaigns against US frontier models
  - Concerns: unauthorized model distillation using fraudulent accounts/proxy networks, IP theft, safety guardrail stripping
  - Follows April 2026 White House memo warning of PRC industrial-scale distillation efforts
  - Risk framing: stripped models could enable weapons development, disinformation, or vuln discovery by hostile actors
- **Why it matters:** First Congressional investigation specifically targeting AI coding tools' reliance on PRC-origin models — signals potential regulatory action that could reshape AI developer tooling supply chains.
- **Confidence:** high

---

## Story: Flowise Authenticated RCE via MCP Adapters (CVE-2026-40933) — Advisory Published
- **Date:** 2026-04-25 (advisory window; GitHub advisory active)
- **Source:** https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-c9gw-hvqq-f33r
- **Outlet:** GitHub Security Advisory
- **Additional sources:**
  - https://www.wiz.io/vulnerability-database/cve/cve-2026-40933 (Wiz)
  - https://www.codeant.ai/vulnerability-database/cve-2026-40933 (CodeAnt)
- **Key facts:**
  - CVE-2026-40933, CVSS 10.0 (Critical)
  - Flowise versions through 3.0.13 affected; patched in 3.1.0
  - Unsafe serialization of stdio commands in MCP adapter — command injection via custom MCP server config
  - Authenticated users can specify arbitrary commands (e.g., `npx -c "touch /tmp/pwn"`) bypassing sanitization
  - Part of broader MCP architectural vulnerability family (10+ CVEs in April across LiteLLM, LangChain, LangFlow, etc.)
- **Why it matters:** Highest-severity CVE in the MCP ecosystem wave — shows that even "authenticated" RCE in AI workflow builders represents critical risk given shared/multi-tenant deployments.
- **Confidence:** high (Note: exact publication date within late April; advisory active in our window)

---

## Story: Google Antigravity IDE Prompt Injection → RCE (Patched, Disclosed in April)
- **Date:** 2026-04-28 (THN/CSO coverage publication)
- **Source:** https://thehackernews.com/2026/04/google-patches-antigravity-ide-flaw.html
- **Outlet:** The Hacker News
- **Additional sources:**
  - https://www.pillar.security/blog/prompt-injection-leads-to-rce-and-sandbox-escape-in-antigravity (Pillar Security — original research)
  - https://www.csoonline.com/article/4161382/prompt-injection-turned-googles-antigravity-file-search-into-rce.html (CSO Online)
- **Key facts:**
  - Prompt injection in `find_by_name` tool's Pattern parameter → injected `-X` (exec-batch) flag to `fd` binary
  - Works even under Antigravity's Strict/Secure Mode — native tools execute before sandbox constraints enforced
  - Attack chain: stage script in workspace → inject exploit via prompt/content → agent executes payload (zero user interaction after injection)
  - Patched February 28, 2026 (Pillar Security responsible disclosure January 2026)
  - No CVE assigned at publication time
  - Systemic risk pattern: trusted native tool operations bypass agent security sandboxes
- **Why it matters:** Landmark demonstration that prompt injection can achieve full RCE in AI IDEs — even "secure mode" failed because native tools aren't subject to sandbox constraints.
- **Confidence:** high (patch older, but public disclosure/coverage falls in our window)

---

## 403 / Paywalled

- Infosecurity Magazine full articles (partial access only; key facts corroborated via other sources)
- SecurityWeek Claude Security deep-dive (summary available; full feature analysis paywalled)

---

## Out-of-window items dropped

| Item | Date | Reason |
|------|------|--------|
| PraisonAI CVE-2026-34938 (CVSS 10.0 sandbox escape) | 2026-04-03 | Disclosed 3 weeks before window |
| MCP RCE "by design" 200K+ servers (OX Security) | 2026-04-15–16 | Covered in previous edition (Apr 17-24) |
| Vercel breach via Context.ai/ShinyHunters | 2026-04-19–24 | Disclosure and expanded findings end before Apr 25 |
| CanisterSprawl supply chain worm | Pre Apr-25 | Covered in previous edition |
| Lovable BOLA data exposure | Pre Apr-25 | Covered in previous edition |
| Bitwarden CLI credential harvest | Pre Apr-25 | Covered in previous edition |
| Oracle CPU April 21 (241 CVEs) | 2026-04-21 | Pre-window |
| OpenClaw CVE-2026-33579 | Early April | Part of "tsunami" cluster, pre-window |
| "AI Agent Vulnerability Tsunami" (Hexon blog) | Early April | Six CVEs disclosed early April, pre-window |

---

## Search queries used

1. `AI security vulnerabilities CVE April 2026`
2. `prompt injection attack April 2026`
3. `npm PyPI malware supply chain attack April 2026`
4. `MCP security vulnerability April 28 29 30 2026`
5. `AI data breach April 2026`
6. `"Mini Shai-Hulud" PyTorch Lightning supply chain attack April 29 2026`
7. `AI agent vulnerability PraisonAI CVE-2026-34938 sandbox escape`
8. `SAP npm supply chain attack worm April 30 2026 "intercom-client"`
9. `Flowise CVE-2026-40933 MCP RCE April 2026`
10. `Google Antigravity AI IDE prompt injection RCE CVE 2026`
11. `Vercel breach ShinyHunters Context.ai OAuth April 2026 date`
12. `CVE-2026-34938 PraisonAI disclosure date published April 2026`
13. `"AI agent vulnerability tsunami" hexon.bot "six critical CVEs" April 2026 date`
14. `AI security news April 28 29 30 May 1 2026`
15. `Cursor IDE CVE-2026-26268 git hook vulnerability April 2026`
16. `Anthropic "Claude Security" vulnerability scanner launch April 30 2026`
17. `Hugging Face LeRobot RCE vulnerability CVE April 2026`
18. `Apple Claude.md documentation leaked support app April 30 2026`
19. `US House investigation PRC AI models national security April 29 2026 Anysphere`
