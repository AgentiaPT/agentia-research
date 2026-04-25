## 5. The Security Siege Continues — MCP's "By Design" RCE and the First Cross-Ecosystem Worm

Last week we called supply-chain attacks [the siege that won't lift](../9982-2026-04-11-ai-news-feed/README.md#7-supply-chain-the-siege-continues). This week the siege escalated: a protocol-level flaw that Anthropic *refuses to patch*, the first self-propagating worm that jumps ecosystems, and three marquee AI coding agents caught leaking secrets through PR titles. Four consecutive weeks. No end in sight.

---

### MCP: Remote Code Execution "By Design"

OX Security disclosed on April 20 that the **STDIO transport** in Anthropic's Model Context Protocol passes user-controlled input straight to a shell — no sanitization, no allow-list, no escape. The result: arbitrary command execution on any host running an MCP server.

> "Input sanitization and restricting what commands are supplied is the responsibility of downstream developers, not the protocol itself."
> — [Anthropic's response](https://thehackernews.com/2026/04/anthropic-mcp-design-vulnerability.html#:~:text=responsibility%20of%20downstream%20developers)

**Blast radius:** **150 M+ downloads**, **~200 K vulnerable server instances**, and **7 000+ publicly exposed servers** — spanning LiteLLM, LangChain, Flowise, Cursor, Windsurf, and Claude Code itself [\[1\]](https://thehackernews.com/2026/04/anthropic-mcp-design-vulnerability.html#:~:text=150%20million%20downloads) [\[2\]](https://www.csoonline.com/article/4159889/rce-by-design-mcp-architectural-choice-haunts-ai-agent-ecosystem.html#:~:text=by%20design) [\[3\]](https://www.infosecurity-magazine.com/news/systemic-flaw-mcp-expose-150/#:~:text=150%20Million%20Downloads).

OX identified four exploitation paths: unauthenticated UI injection, hardening bypasses, zero-click prompt injection (Windsurf), and malicious marketplace packages. CVEs have been assigned for Windsurf, LiteLLM, GPT Researcher, Flowise, and others — but **no protocol-level fix exists** [\[4\]](https://gbhackers.com/anthropic-mcp-hit-by-critical-vulnerability/#:~:text=no%20protocol-level%20fix).

---

### CanisterSprawl: The First Cross-Ecosystem Supply-Chain Worm

On April 21, researchers documented **CanisterSprawl** — a self-propagating worm that jumps between npm and PyPI. It steals publish tokens from infected machines, uses them to trojanize packages the victim maintains, and coordinates via **decentralized command-and-control hosted on Internet Computer Protocol (ICP) canisters** — making takedowns nearly impossible [\[5\]](https://thehackernews.com/2026/04/canistersprawl-self-propagating-worm.html#:~:text=self-propagating%20worm) [\[6\]](https://www.endorlabs.com/learn/canistersprawl-the-first-cross-ecosystem-supply-chain-worm#:~:text=decentralized%20C2) [\[7\]](https://blog.gitguardian.com/three-supply-chain-campaigns-hit-npm-pypi-and-docker-hub-in-48-hours/#:~:text=CanisterSprawl).

- **Vector:** Stolen npm/PyPI publish tokens
- **Propagation:** Automatic — trojanizes victim's own packages
- **C2:** ICP canisters (no centralized server to seize)
- **Ecosystems:** npm → PyPI (bidirectional)

This is the threat model the industry warned about and never built defenses for: **worm-speed propagation across package registries with no single point of takedown**.

---

### Bitwarden CLI: 93 Minutes, 334 Developers, AI Creds Gone

On April 22, attackers compromised a Bitwarden engineer's GitHub account, poisoned a GitHub Actions workflow via OIDC Trusted Publishing, and shipped `@bitwarden/cli@2026.4.0` to npm. The malicious version lived for **93 minutes** before removal [\[7\]](https://thehackernews.com/2026/04/bitwarden-cli-compromised-in-ongoing.html#:~:text=93-minute) [\[8\]](https://www.stepsecurity.io/blog/bitwarden-cli-hijacked-on-npm-bun-staged-credential-stealer-targets-developers-github-actions-and-ai-tools#:~:text=Bun-Staged%20Credential%20Stealer).

What made this different: the stealer **explicitly targeted AI tool configurations** — `~/.claude.json`, Cursor configs, Codex CLI settings, MCP server credentials, and Aider tokens. It's the first npm compromise designed to harvest AI assistant credentials at scale [\[9\]](https://www.mend.io/blog/compromised-bitwarden-cli-npm-worm-ai-poisoning/#:~:text=AI%20Assistants) [\[10\]](https://www.endorlabs.com/learn/shai-hulud-the-third-coming----inside-the-bitwarden-cli-2026-4-0-supply-chain-attack#:~:text=AI%20tool%20credentials).

Stolen secrets were encrypted with AES-256-GCM and sent to `audit.checkmarx.cx` — a domain impersonating the legitimate Checkmarx security firm. **334 developers** confirmed affected.

---

### "Comment and Control": Three AI Agents, One Injection, All Your Secrets

Researchers Aonan Guan, Zhengyu Liu, and Gavin Zhong demonstrated that **Claude Code**, **Gemini CLI**, and **GitHub Copilot Agent** all exfiltrate repository secrets when a malicious instruction is embedded in a PR title, issue body, or issue comment [\[11\]](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026#:~:text=Comment%20and%20Control) [\[12\]](https://www.securityweek.com/claude-code-gemini-cli-github-copilot-agents-vulnerable-to-prompt-injection-via-comments/#:~:text=prompt%20injection%20via%20comments) [\[13\]](https://cybersecuritynews.com/prompt-injection-via-github-comments/#:~:text=pull%20request%20titles%2C%20issue%20bodies%2C%20and%20issue%20comments).

The attack requires **zero infrastructure** — no C2 server, no malware. The entire attack loop runs within GitHub itself: an attacker writes a malicious PR title or issue comment, the AI agent reads and processes it as trusted context, and posts its own API keys into a PR comment. This is the **first public cross-vendor demonstration** of a single prompt injection pattern defeating multiple major AI agents simultaneously.

- **Claude Code (Anthropic)** — CVSS **9.4**, Bounty: $100, Public Advisory: None
- **Gemini CLI (Google)** — CVSS **9.3**, Bounty: $1,337, Public Advisory: None
- **Copilot Agent (GitHub)** — Bounty: $500, Public Advisory: None

All three share the same architectural flaw: **untrusted GitHub data flows into an AI agent that holds production secrets and unrestricted tool access**. All three vendors **patched silently** — no CVEs, no advisories. Users on older versions remain exposed [\[14\]](https://www.theregister.com/2026/04/15/claude_gemini_copilot_agents_hijacked/#:~:text=patched%20quietly).

---

### Google Confirms: Prompt Injection Is in the Wild

Google's Threat Intelligence team, partnering with DeepMind, published a large-scale study of indirect prompt injection payloads found across the Common Crawl corpus [\[14\]](https://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html#:~:text=AI%20threats%20in%20the%20wild). Most are low-impact (SEO manipulation, tone hijacking), but the team documented functional payloads attempting **data exfiltration**, **financial fraud** (fake PayPal/Stripe instructions for payment-capable agents), and **destructive actions** (file deletion targeting privileged dev tools) [\[15\]](https://www.helpnetsecurity.com/2026/04/24/indirect-prompt-injection-in-the-wild/#:~:text=indirect%20prompt%20injection).

The finding that matters: attackers are now sharing **injection templates** — organized toolkits, not one-off experiments [\[16\]](https://www.infosecurity-magazine.com/news/researchers-10-wild-indirect/#:~:text=10%20In-the-Wild).

---

### RedSun: Windows Defender Becomes the Attack Vector

Disclosed April 17, **RedSun** is an unpatched zero-day in Windows Defender's remediation engine. An attacker combines NTFS directory junctions, opportunistic locks, and the Cloud Files API to trick Defender into overwriting a system binary (`TieringEngineService.exe`) with attacker-controlled code — **as SYSTEM** [\[17\]](https://www.bleepingcomputer.com/news/microsoft/new-microsoft-defender-redsun-zero-day-poc-grants-system-privileges/#:~:text=RedSun%20zero-day) [\[18\]](https://www.bleepingcomputer.com/news/security/recently-leaked-windows-zero-days-now-exploited-in-attacks/#:~:text=RedSun).

No admin rights needed. No kernel exploit. Works on fully patched April 2026 systems. **No official fix as of April 24** [\[19\]](https://thehackernews.com/2026/04/three-microsoft-defender-zero-days.html#:~:text=Three%20Microsoft%20Defender%20Zero-Days).

---

### Rapid-Fire Patch Table

- **Three ecosystems, 48 hours** (Apr 21–23) — GitGuardian documented three coordinated supply-chain campaigns hitting **npm, PyPI, and Docker Hub** in a single weekend: compromised **Checkmarx KICS** Docker images and VS Code extensions harvesting GitHub tokens, **xinference** on PyPI with credential-stealing payloads across three malicious releases, and CanisterSprawl on npm (covered above). All three targeted the same thing: **developer secrets** — API keys, cloud creds, SSH keys, CI/CD tokens [\[22\]](https://blog.gitguardian.com/three-supply-chain-campaigns-hit-npm-pypi-and-docker-hub-in-48-hours/#:~:text=Three%20supply%20chain%20attacks%20hit%20npm%2C%20PyPI%2C%20and%20Docker%20Hub)
- **Oracle CPU** (Apr 21) — **241 CVEs**, 481 patches, 34 critical; Oracle Communications worst-hit (139 patches) [\[23\]](https://blogs.oracle.com/security/april-2026-critical-patch-update-released#:~:text=Critical%20Patch%20Update)
- **AI security tools hijacked** (Apr 21) — Compromised at **90+ organizations** via trojanized scanning integrations [\[24\]](https://thehackernews.com/2026/04/ai-security-tools-hijacked.html#:~:text=AI%20security%20tools)
- **RedSun + BlueHammer** (Apr 17) — Two Defender 0-days; BlueHammer (CVE-2026-33825) patched, RedSun still open [\[19\]](https://thehackernews.com/2026/04/three-microsoft-defender-zero-days.html#:~:text=Three%20Microsoft%20Defender%20Zero-Days)

---

### Lovable: When Your No-Code AI Builder Exposes Everything

On April 20, a security researcher disclosed that **all public Lovable projects' chat history and source code could be accessed by any authenticated user** — a classic Broken Object-Level Authorization (BOLA) vulnerability. The regression was [introduced in February 2026](https://lovable.dev/blog/our-response-to-the-april-2026-incident#:~:text=February%202026%20%E2%80%94%20Backend%20regressions) when backend changes re-enabled public access paths that had been locked down.

To Lovable's credit, the response was fast: **fix shipped within 2 hours**, all current public projects made private (except official templates), and a [detailed remediation timeline published](https://lovable.dev/blog/our-response-to-the-april-2026-incident#:~:text=We%20shipped%20a%20fix%20within%20two%20hours). Private projects and Lovable Cloud were never impacted. But the incident is a cautionary tale for anyone evaluating no-code AI app builders — when the platform generates your code *and* hosts your conversations about it, the blast radius of a single authorization bug is far wider than a traditional SaaS breach.

---

### EU AI Act: The Compliance Clock Is Ticking

The regulatory dimension of AI security sharpened this week. **EU AI Act Annex III high-risk obligations take effect August 2, 2026** — meaning agents performing credit scoring, resume filtering, or healthcare-benefit decisions must implement **Article 12-compliant automatic logging**: every agent action recorded, retained, and auditable. Penalties: up to **€15 million or 3% of global annual revenue** ([Help Net Security](https://www.helpnetsecurity.com/2026/04/16/eu-ai-act-logging-requirements/#:~:text=EU%20AI%20Act%20logging%20requirements)). A possible Digital Omnibus delay may push some obligations for *existing* deployed systems to December 2027, but **new deployments face the August deadline** ([EU Digital Strategy](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)).

Separately, the **EU Commission allocated €63.2 million** under the Digital Europe Programme for AI in health and online safety — the first major funding tranche under the act's provisions.

For engineering teams: if your agents touch any Annex III high-risk domain, **build verifiable action logs now**. The August deadline is 14 weeks away.

---

### Why This Matters

The pattern is no longer "supply-chain attacks are increasing." The pattern is **convergence**: supply-chain worms now target AI tool credentials specifically (Bitwarden), protocols designed for AI agents ship RCE by design (MCP), AI agents themselves become exfiltration channels (Comment and Control), and even no-code AI platforms expose user data through basic authorization failures (Lovable). Google's research confirms prompt injection payloads are being industrialized in the wild. And now **regulation is arriving**: the EU AI Act's logging requirements turn security from a best practice into a legal obligation with nine-figure penalties.

Treat prompt injection like SQL injection — defense in depth from design through deployment. The attackers have figured out that **the AI toolchain is the new high-value target**, the defenders haven't caught up, and the regulators are about to start fining.
