## 4. Supply Chain Siege — PyTorch Lightning Hijacked, AI Coding Tools Weaponized

**April 30 | [Kodem Security](https://www.kodemsecurity.com/resources/mini-shai-hulud-strikes-pytorch-lightning-and-intercom-client-inside-the-cross-ecosystem-supply-chain-attack) · [Snyk](https://snyk.io/blog/bun-based-stealer-hits-sap-cap-js-mbt-npm-packages/) · [The Register](https://www.theregister.com/2026/04/30/supply_chain_attacks_sap_npm_packages/) · [OX Security](https://www.ox.security/blog/lightning-python-package-shai-hulud-supply-chain-attack/)**

A single campaign — **"Mini Shai-Hulud"** by TeamPCP — bridged Python and JavaScript ecosystems simultaneously, stole credentials at massive scale, and introduced a novel attack vector: **weaponizing AI coding tool configuration files for persistence.**

**PyTorch Lightning Hijack**

- **Package:** `lightning` on PyPI — **8.3 million downloads/month**
- **Compromised versions:** 2.6.2 and 2.6.3 (April 30)
- **Mechanism:** Malicious code in `__init__.py` fired a background thread on import, downloaded Bun runtime, pulled an 11 MB obfuscated JS payload
- **Stolen:** SSH keys, shell histories, `.env` files, GitHub/npm/cloud credentials (AWS, Azure, GCP), Kubernetes configs, Docker tokens, Discord/Slack sessions, crypto wallets
- **Propagation:** Used stolen GitHub tokens to inject worm payloads into up to 50 branches per repo — impersonating "Claude Code" for commits
- **Cross-ecosystem:** Modified local npm packages to propagate into Node.js
- **Impact:** [1,800+ developers affected](https://securityboulevard.com/2026/05/1800-developers-hit-in-mini-shai-hulud-supply-chain-attack-across-pypi-npm-and-php/); 1,100+ public repos found hosting exfiltrated credentials
- **Clean version:** 2.6.1 — PyPI quarantined the package

**SAP npm Packages — AI Tool Persistence**

- **Compromised:** `mbt@1.2.48`, `@cap-js/db-service@2.10.1`, `@cap-js/postgres@2.2.2`, `@cap-js/sqlite@2.2.2`
- **Target:** SAP Cloud Application Programming developers (Fortune 500 deployments)
- **Novel element — AI tool weaponization:**
  - Dropped `.claude/settings.json` leveraging "SessionStart" hook — malware re-executes every time Claude Code opens the infected repo
  - Dropped `.vscode/tasks.json` with `runOn:"folderOpen"` — malware runs when VS Code opens the folder
  - **First documented supply chain attack using AI coding agent configs as persistence mechanisms**
- **Exfiltration:** AES-256-GCM encrypted data uploaded to attacker-tagged GitHub repos under victim's own account
- **SAP response:** Security Note 3747787 issued

**Why This Is Different**

- **Legitimate packages compromised** — not lookalikes, the real thing with millions of users
- **Self-propagating** — each compromised developer becomes a vector via stolen tokens
- **AI-aware** — attackers target AI coding tool config files for persistence, knowing developers trust their IDE environments
- **Cross-ecosystem** — single campaign bridges PyPI and npm simultaneously

**Action items:**
- Pin PyTorch Lightning to ≤2.6.1; audit installs of 2.6.2/2.6.3
- Audit `.claude/` and `.vscode/tasks.json` in all repos for unauthorized entries
- Rotate all credentials if compromised packages were installed
- Review [SAP Security Note 3747787](https://me.sap.com/notes/3747787) if using CAP/MBT

---
