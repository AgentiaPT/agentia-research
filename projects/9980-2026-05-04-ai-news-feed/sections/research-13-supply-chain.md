# Research: Supply Chain Siege Escalates — PyTorch Lightning Hijacked + SAP npm Targeting AI Tool Credentials

## Key Facts

### PyTorch Lightning Hijack

- **Package:** `lightning` on PyPI (PyTorch Lightning) — 8.3M+ downloads/month
- **Compromised versions:** 2.6.2 and 2.6.3, published April 30, 2026
- **Attack mechanism:** Malicious code in `__init__.py` fired a background thread on import
  - Downloaded the Bun JavaScript runtime
  - Pulled an 11 MB obfuscated JS payload (`router_runtime.js`)
- **Stolen credentials:** SSH keys, shell histories, `.env` files, GitHub/npm/cloud (AWS, Azure, GCP) credentials, Kubernetes configs, Docker tokens, Discord/Slack sessions, cryptocurrency wallets
- **Propagation:** Used stolen GitHub tokens to inject worm-like payloads into up to 50 branches per repo with write access, impersonating Anthropic's "Claude Code" for commits
- **Cross-ecosystem spread:** Modified local npm packages to propagate into Node.js/JavaScript ecosystem
- **Impact:** 1,800+ public repositories found hosting exfiltrated credentials
- **Attribution:** TeamPCP group, variant of "Mini Shai-Hulud" campaign
- **Response:** PyPI quarantined the package; last clean version is 2.6.1

### SAP npm Packages Targeting AI Tool Credentials

- **Compromised packages:**
  - `mbt@1.2.48` (MTA Build Tool)
  - `@cap-js/db-service@2.10.1`
  - `@cap-js/postgres@2.2.2`
  - `@cap-js/sqlite@2.2.2`
- **Target:** SAP Cloud Application Programming Model (CAP) and MTA Build Tool users
- **Attack mechanism:** Malicious `preinstall` script downloaded Bun runtime + obfuscated credential stealer (~11.6 MB)
- **AI tool targeting (novel element):**
  - Dropped `.claude/settings.json` leveraging the "SessionStart" hook for Claude Code persistence
  - Dropped `.vscode/tasks.json` with `runOn:"folderOpen"` for VS Code persistence
  - Re-executed malware whenever infected repo opened in either tool
- **Exfiltration:** AES-256-GCM encrypted data uploaded to attacker-tagged GitHub repos under victim's own account (tagged "A Mini Shai-Hulud has Appeared")
- **Propagation:** Stole GitHub Actions secrets, republished infected npm packages, extracted secrets from CI/CD runner memory and cloud metadata services
- **SAP Advisory:** Security Note 3747787 issued
- **Attribution:** Same TeamPCP group

## Timeline

| Date | Event |
|------|-------|
| Early-mid April 2026 | SAP npm packages (`mbt`, `@cap-js/*`) compromised with Mini Shai-Hulud malware |
| April 30, 2026 | PyTorch Lightning versions 2.6.2 and 2.6.3 published with malicious payload |
| April 30, 2026 | The Register reports on ongoing SAP npm supply chain attacks |
| April 30, 2026 | Cyber News Centre publishes detailed analysis |
| Late April–Early May | PyPI quarantines `lightning` package |
| Early May 2026 | SAP issues Security Note 3747787 with mitigation guidance |
| Early May 2026 | Snyk, Kodem Security, OX Security, Phoenix Security publish technical breakdowns |

## Sources

- [Kodem Security — Mini Shai-Hulud Strikes PyTorch Lightning](https://www.kodemsecurity.com/resources/mini-shai-hulud-strikes-pytorch-lightning-and-intercom-client-inside-the-cross-ecosystem-supply-chain-attack)
- [ByteIota — PyTorch Lightning Malware: 8.3M Downloads Hit](https://byteiota.com/pytorch-lightning-malware-8-3m-downloads-hit-by-shai-hulud-attack/)
- [OX Security — Lightning Python Package Infected](https://www.ox.security/blog/lightning-python-package-shai-hulud-supply-chain-attack/)
- [StepSecurity — Obfuscated JavaScript Credential Stealer in PyPI](https://www.stepsecurity.io/blog/lightning-obfuscated-javascript-credential-stealer-bundled-in-pypi-wheel)
- [Let's Data Science — PyTorch Lightning Package Compromised](https://letsdatascience.com/news/pytorch-lightning-package-compromised-in-supply-chain-attack-473ece7e)
- [Snyk — Bun-Based Stealer Hits SAP CAP npm Packages](https://snyk.io/blog/bun-based-stealer-hits-sap-cap-js-mbt-npm-packages/)
- [Phoenix Security — Mini Shai-Hulud SAP CAP npm Worm](https://phoenix.security/mini-shai-hulud-sap-cap-mbt-npm-supply-chain-bun-credential-stealer/)
- [The Register — Supply Chain Attacks Worm Into SAP npm Packages](https://www.theregister.com/2026/04/30/supply_chain_attacks_sap_npm_packages/)
- [Cyber News Centre — SAP npm Supply-Chain Attack](https://www.cybernewscentre.com/30th-april-2026-cyber-update-sap-npm-supply-chain-attack/)
- [Pathlock — SAP npm Supply Chain Incident](https://pathlock.com/blog/security-alerts/sap-npm-supply-chain-incident-malicious-packages-impact-cap-mta/)

## Impact

### Severity: Critical

- **Scale:** Combined reach of 8M+ monthly PyPI downloads + enterprise SAP developer ecosystem
- **Novel threat:** First widely documented supply chain attacks weaponizing AI coding agent configurations (Claude Code, VS Code) for persistence
- **Cross-ecosystem:** Single campaign bridges Python (PyPI) and JavaScript (npm) ecosystems simultaneously
- **Worm behavior:** Self-propagating through stolen tokens — each compromised developer becomes a vector
- **Enterprise exposure:** SAP CAP packages used in Fortune 500 cloud deployments; CI/CD pipeline secrets at risk
- **AI tooling trust:** Demonstrates that AI coding assistants' configuration files are now attack surfaces requiring security monitoring

### Broader Supply Chain Trend Connection

- Part of escalating TeamPCP/"Mini Shai-Hulud" campaign active since 2025
- Previously targeted: Checkmarx, Bitwarden, Trivy, Aqua Security packages
- Signals shift from opportunistic typosquatting to compromising legitimate, high-traffic packages
- AI development tools (Claude Code, Copilot, VS Code) now explicitly in attacker crosshairs as persistence mechanisms
- Highlights inadequacy of current package registry security for packages with millions of downloads
