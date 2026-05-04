## 5. The Tooling Arms Race — Codex, Claude Code, Cursor, Copilot All Ship Major Updates

**April 28–30 | Multiple sources**

Four competing AI coding platforms shipped significant updates within 72 hours of each other. The pattern is clear: every tool is racing from "code assistant" to "autonomous project teammate."

### OpenAI Codex — Persistent Goals, Memory, 90+ Plugins (Apr 30)

[Releasebot](https://releasebot.dev) · [WindowsReport](https://windowsreport.com) · [TestingCatalog](https://testingcatalog.com)

- **`/goal` command** — define persistent workflows that survive across sessions and days. "Keep test coverage above 80%" becomes a standing instruction the agent checks every run.
- **Cross-session memory** (preview, enterprise-first) — Codex remembers project context, decisions, and patterns between sessions without re-prompting
- **90+ new plugins** — Atlassian (Jira/Confluence), CircleCI, GitLab, Notion, Linear — Codex now reads from and writes to the tools teams actually use
- **In-app browser annotation** — mark elements in a browser view; Codex understands visual context for frontend work
- **SSH remote dev** (alpha) — connect Codex to remote machines for builds, testing, deployment
- **Framing shift:** OpenAI explicitly marketing Codex as a "workspace agent" / "project teammate" — not a code assistant

### Claude Code — ultrareview, plugin-prune, MCP alwaysLoad (Apr 20–28)

[Anthropic Docs](https://docs.anthropic.com) · [Changelog](https://docs.anthropic.com/en/docs/claude-code/changelog)

- **`/ultrareview`** — cloud multi-agent code review with a verification pass; launches parallel review agents that check each other's work. Public preview.
- **`plugin prune`** — cleans orphaned plugin dependencies (v2.1.121, Apr 28)
- **Windows PowerShell native** — full support without Git Bash since v2.1.84
- **`alwaysLoad` MCP** — MCP tools load instantly at session start; no more waiting for lazy initialization (v2.1.121)
- **PostToolUse hooks expansion** — hook into any tool completion for custom workflows

### Cursor — SDK + Security Review (Apr 29–30)

- **Cursor SDK** (`@cursor/sdk`, Apr 29) — TypeScript SDK exposing the full agent runtime; runs local, cloud, or self-hosted. Supports subagents, hooks, MCP servers, SSE streaming.
- **Security Review** (Apr 30, Teams/Enterprise) — two always-on agents:
  - **PR Security Reviewer** — flags vulnerabilities, auth regressions, prompt injection risks on every PR
  - **Vulnerability Scanner** — scheduled full-codebase scans
- First major IDE to treat **prompt injection as a first-class vulnerability class**
- Released days after patching CVE-2026-26268 (git hook remote code execution)

### GitHub Copilot CLI — ACP Sessions, Headless OAuth, Slash Commands (Apr 29–May 1)

[GitHub Blog](https://github.blog) · [docs.github.com](https://docs.github.com)

- **ACP session controls** — allow-all permissions, backgrounding (`Ctrl+X B`), named sessions, remote steering from GitHub.com or mobile
- **Headless OAuth** (v1.0.40, May 1) — `client_credentials` grant for MCP servers; no browser needed in CI/containers/headless environments
- **New slash commands:** `/compact`, `/context`, `/usage`, `/env`, `/chronicle`, `/extensions` with hot reload
- **Auto model selection** — CLI picks the optimal model per task; BYOK/local models supported
- **Extension SDK** — multi-language extension authoring with tab completion

### The Pattern

Every platform shipped the same three capabilities within days:

- **Persistence** — agents that remember across sessions (Codex memory, Claude Code alwaysLoad, Copilot named sessions)
- **Orchestration** — managing multiple sub-agents or external tools (Claude ultrareview, Cursor subagents, Symphony)
- **Security** — hardening against the new attack surfaces (Cursor Security Review, Anthropic Claude Security, Copilot headless OAuth)

The race is no longer "who writes better code completions." It's who builds the most capable autonomous software engineer — and who secures it first.

---
