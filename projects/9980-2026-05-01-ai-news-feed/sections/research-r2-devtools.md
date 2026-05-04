# R2: Developer Tools & Agentic Coding — April 25 to May 1, 2026

---

## Story: Cursor SDK Public Beta Launches — Programmatic AI Agents in TypeScript
- **Date:** 2026-04-29
- **Source:** https://www.marktechpost.com/2026/04/29/cursor-introduces-a-typescript-sdk-for-building-programmatic-coding-agents-with-sandboxed-cloud-vms-subagents-hooks-and-token-based-pricing/
- **Outlet:** MarkTechPost
- **Key facts:**
  - Cursor released public beta of `@cursor/sdk` — a TypeScript library for building programmatic coding agents
  - Supports local execution, Cursor-managed sandboxed cloud VMs, or self-hosted workers
  - Compatible with Composer-2, GPT-4, Claude, and custom model endpoints
  - Agents can open PRs, push branches, connect to MCP tools, run hooks, spawn subagents
  - Use cases: CI/CD fix automation, code review, issue triage, dependency updates, embedding agents in products
  - Install: `npm install @cursor/sdk`
  - Token-based pricing model
- **Why it matters:** Transforms Cursor from an IDE into deployable AI coding infrastructure — organizations can now embed Cursor's agents into any workflow programmatically.
- **Confidence:** high

---

## Story: GitHub Copilot in Visual Studio — April Update with Cloud Agent & Debugger Agent
- **Date:** 2026-04-30
- **Source:** https://github.blog/changelog/2026-04-30-github-copilot-in-visual-studio-april-update/
- **Outlet:** GitHub Blog / Changelog
- **Key facts:**
  - Cloud agent integration in Visual Studio 2026 — assign tasks, close IDE, get PR when done
  - Cloud agent runs via GitHub Actions-backed remote infrastructure (clone repo, execute work, submit PR)
  - New Debugger Agent validates bug fixes by running code against live runtime instrumentation
  - User-level custom agents: stored in `%USERPROFILE%/.github/agents/`, travel across projects
  - Skills discovery expanded to `.claude/skills/` and `.agents/skills/` directories
  - Copilot "coding agent" officially rebranded "Copilot cloud agent" (rebrand was April 1, but VS integration shipped April 30)
  - Chat history panel, customizable keyboard shortcuts for inline suggestions
- **Why it matters:** Visual Studio joins VS Code in having first-class autonomous cloud agent support — developers can delegate entire tasks and continue other work.
- **Confidence:** high

---

## Story: Claude Code v2.1.126 Release — Project Purge, OAuth Improvements, Windows Parity
- **Date:** 2026-05-01
- **Source:** https://code.claude.com/docs/en/changelog
- **Outlet:** Anthropic (Claude Code Docs)
- **Key facts:**
  - New `claude project purge [path]` tool deletes all Claude Code state for a project (transcripts, tasks, file history, config)
  - Supports `--dry-run`, `-y/--yes`, `-i/--interactive`, `--all`, and `--dangerously-skip-permissions` flags
  - Smarter `/model` picker reads models from gateway's `/v1/models` endpoint when `ANTHROPIC_BASE_URL` set
  - OAuth login now accepts codes pasted directly into terminal (WSL2, SSH, containers)
  - `claude_code.skill_activated` telemetry event fires for user-typed slash commands with `invocation_trigger` attribute
  - PowerShell 7 now primary shell on Windows when enabled (no longer defaults to Bash)
  - Security fixes: images >2000px auto-downscaled, concurrent credential write races fixed, session stability improvements
- **Why it matters:** Continued rapid iteration on CLI developer experience — purge command addresses project cleanup pain point; Windows parity push broadens addressable developer base.
- **Confidence:** high

---

## Story: CVE-2026-26268 — Critical RCE Vulnerability in Cursor IDE via Git Hooks
- **Date:** 2026-04-28 (public disclosure/coverage wave)
- **Source:** https://novee.security/blog/cursor-ide-cve-2026-26268-git-hook-arbitrary-code-execution/
- **Outlet:** Novee Security / CSO Online / Hackread
- **Key facts:**
  - CVSS score: 9.9 (Critical)
  - Affected: Cursor IDE versions prior to 2.5
  - Attack vector: malicious bare repository with pre-commit hook embedded in a cloned repo
  - AI agent autonomously triggers `git checkout`/`commit` → executes malicious hook without user interaction
  - Patched in Cursor v2.5 (February 2026); disclosure and coverage wave in late April
  - Highlights systemic risk of AI agents operating with elevated local filesystem/git permissions
- **Why it matters:** First high-profile CVE demonstrating how AI coding agents expand attack surface — routine git operations become RCE vectors when agents act autonomously.
- **Confidence:** high (CVE confirmed in NVD; patch shipped Feb, disclosure coverage late April)

---

## Story: Visual Studio April Update — Autonomous Cloud Agents & Debugger Agent
- **Date:** 2026-04-29
- **Source:** https://devblogs.microsoft.com/visualstudio/visual-studio-april-update-cloud-agent-integration/
- **Outlet:** Visual Studio Blog (Microsoft)
- **Key facts:**
  - "Assign a task, close the IDE, get a PR" — headline from Visual Studio Magazine
  - Cloud agents run on GitHub-hosted infrastructure; no local compute required
  - Debugger agent: reproduces bugs, instruments code, validates fixes in live runtime
  - Advanced C++ code editing tools for Copilot agent mode now GA
  - IntelliSense completions now take precedence over Copilot's inline suggestions
- **Why it matters:** Microsoft extends the "fire-and-forget" agent paradigm to Visual Studio proper — blurring the line between IDE and autonomous task runner.
- **Confidence:** high

---

## Story: Google Cloud Managed MCP Servers GA — 50+ Servers Available
- **Date:** 2026-04-28 (GA at Cloud Next '26; release notes confirm late April)
- **Source:** https://cloud.google.com/blog/products/ai-machine-learning/google-managed-mcp-servers-are-available-for-everyone
- **Outlet:** Google Cloud Blog
- **Key facts:**
  - 50+ Google-managed MCP servers now generally available
  - Cover services across Google Cloud (BigQuery, Cloud Storage, Firestore, Vertex AI, etc.)
  - Supported by Gemini CLI, Claude, ChatGPT, LangChain, and other MCP clients
  - Built-in Cloud IAM, audit logging, centralized discovery via Agent Registry
  - No local server hosting required — remote MCP endpoints available by default when Cloud product is enabled
  - Protocol governed by Linux Foundation's Agentic AI Foundation (AAIF)
- **Why it matters:** First major cloud provider to ship fully managed MCP infrastructure at scale — establishes MCP as the enterprise standard for AI-to-tool connectivity.
- **Confidence:** high

---

## Story: ACP (Agent Client Protocol) Session Management Stabilized
- **Date:** 2026-04-22–23
- **Source:** https://agentclientprotocol.com/updates
- **Outlet:** Agent Client Protocol (JetBrains / Zed)
- **Key facts:**
  - April 23: "Session Close" method stabilized — IDEs can cleanly cancel in-progress agent tasks
  - April 22: "Session Resume" stabilized — clients reconnect to existing agent sessions without replaying history
  - New Transports Working Group formed for WebSocket/HTTP remote agent communication
  - ACP Registry now has 40+ compatible agents (Codex, Claude, Gemini, Copilot, etc.)
  - JetBrains Air tool orchestrates multiple ACP-compatible agents concurrently
- **Why it matters:** ACP is becoming the "LSP for AI agents" — session management stability is a prerequisite for enterprise adoption of multi-agent workflows.
- **Confidence:** med (dates April 22-23 are just outside our window; included as context since impact spans into our week)

---

## Story: Cursor v3.2.16 — Security Review Agents (Beta)
- **Date:** ~2026-04-29
- **Source:** https://cursor.com/changelog
- **Outlet:** Cursor (official changelog)
- **Key facts:**
  - Two new always-on security agents on higher-tier plans:
    - **Security Reviewer**: checks every PR for vulnerabilities, leaves inline comments + suggested remediations
    - **Vulnerability Scanner**: scheduled codebase scans, findings deliverable via Slack
  - Integrates with existing SAST/SCA tooling
  - Version 3.2.16 as of April 29, 2026
- **Why it matters:** AI coding tools adding security-by-default workflows — shifts left on vulnerability detection without requiring separate toolchain.
- **Confidence:** med (synthesized from multiple sources; exact date inferred from version tracking)

---

## 403 / Paywalled

- GitHub Blog changelog entries for April 25-30 required login for some details
- CSO Online CVE-2026-26268 full article partially paywalled
- Cursor official changelog (cursor.com/changelog) loaded but details sparse without scrolling/JS rendering

---

## Out-of-window items dropped

| Item | Date | Reason |
|------|------|--------|
| Cursor 3.0 launch | 2026-04-02 | Before window; covered in previous edition |
| Cursor 3.1 Tiled Layout | 2026-04-13 | Before window |
| Windsurf 2.0 launch / Agent Command Center | 2026-04-15 | Before window |
| GitHub Copilot signup pause | 2026-04-20 | Before window; covered in previous edition |
| Copilot "cloud agent" rebrand | 2026-04-01 | Before window |
| Microsoft Agent Framework 1.0 GA | 2026-04-03 | Before window |
| VS Code 1.116 built-in Copilot | 2026-04-17 | Before window |
| ACP Session Close/Resume | 2026-04-22-23 | Borderline; included with caveat |

---

## Search queries used

1. `GitHub Copilot updates April 2026 new features`
2. `Cursor IDE update April 28 2026`
3. `Claude Code updates April 25-May 1 2026`
4. `VS Code AI features April 2026 release`
5. `Windsurf IDE AI coding April 2026 update`
6. `JetBrains AI assistant April 2026 update`
7. `MCP model context protocol servers new April 2026`
8. `agentic coding developer tools news April 28 29 30 2026`
9. `Cursor SDK public beta April 29 2026`
10. `Windsurf 2.0 launch date April 2026 "Agent Command Center"`
11. `Microsoft Agent Framework 1.0 release April 2026`
12. `"GitHub Copilot" "cloud agent" Visual Studio April 2026`
13. `CVE-2026-26268 Cursor IDE vulnerability April 2026`
14. `Google MCP servers generally available April 2026`
15. `"GitHub Copilot" "cloud agent" rebrand April 2026 date announcement`
16. `JetBrains "Agent Client Protocol" ACP April 2026`
