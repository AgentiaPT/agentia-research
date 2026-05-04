## 6. The Tooling Arms Race — Codex, Claude Code, Cursor, Copilot All Ship Major Updates

**April 28–30 | Multiple sources**

Four competing AI coding platforms shipped significant updates within 72 hours. Every tool is racing from "code assistant" to "autonomous project teammate."

### OpenAI Codex — Persistent Goals, Memory, 90+ Plugins (Apr 30)

[Releasebot](https://releasebot.io/updates/openai/codex) · [Digital Applied](https://www.digitalapplied.com/blog/openai-codex-for-almost-everything-release-guide) · [BigHatGroup](https://www.bighatgroup.com/blog/openai-codex-enterprise-ai-automation-april-2026/)

- **`/goal` command** — persistent workflows surviving across sessions. "Keep test coverage above 80%" becomes a standing instruction.
- **Cross-session memory** (preview, enterprise-first) — remembers project context between sessions without re-prompting
- **90+ new plugins** — Atlassian, CircleCI, GitLab, Notion, Linear — reads from and writes to actual team tools
- **In-app browser annotation** — mark elements for visual context in frontend work
- **SSH remote dev** (alpha) — connect to remote machines for builds/testing/deployment

### Claude Code — /ultrareview, plugin-prune, MCP alwaysLoad (Apr 20–28)

[Anthropic Docs](https://docs.anthropic.com/en/docs/claude-code) · [Changelog](https://docs.anthropic.com/en/docs/claude-code/changelog) · [UltraReview guide](https://www.claudedirectory.org/blog/ultrareview-claude-code-guide)

- **`/ultrareview`** — cloud multi-agent code review with verification pass; parallel agents check each other's work
- **`plugin prune`** — cleans orphaned plugin dependencies (v2.1.121, Apr 28)
- **Windows PowerShell native** — full support without Git Bash since v2.1.84
- **`alwaysLoad` MCP** — MCP tools load instantly at session start (v2.1.121)
- **PostToolUse hooks expansion** — hook into any tool completion for custom workflows

### Cursor — SDK + Security Review (Apr 29–30)

[Cursor SDK blog](https://authorityaitools.com/blog/cursor-sdk-launch-april-2026) · [Security Review changelog](https://cursor.com/changelog/04-30-26) · [CVE-2026-26268](https://nvd.nist.gov/vuln/detail/cve-2026-26268)

- **Cursor SDK** (`@cursor/sdk`, Apr 29) — TypeScript SDK exposing the full agent runtime; local, cloud, or self-hosted. Supports subagents, hooks, MCP servers, SSE streaming.
- **Security Review** (Apr 30, Teams/Enterprise) — two always-on agents:
  - **PR Security Reviewer** — flags vulnerabilities, auth regressions, prompt injection on every PR
  - **Vulnerability Scanner** — scheduled full-codebase scans
- First major IDE treating **prompt injection as a first-class vulnerability class**
- Released days after patching CVE-2026-26268 (git hook RCE)

### GitHub Copilot CLI — ACP Sessions, Headless OAuth, Slash Commands (Apr 29–May 1)

[GitHub Blog](https://github.blog) · [GitHub Docs](https://docs.github.com/en/copilot) · [VS Code 1.118 notes](https://code.visualstudio.com/updates/v1_118)

- **ACP session controls** — allow-all permissions, backgrounding (`Ctrl+X B`), named sessions, remote steering from GitHub.com/mobile
- **Headless OAuth** (v1.0.40, May 1) — `client_credentials` grant for MCP servers; no browser needed in CI/containers
- **New slash commands:** `/compact`, `/context`, `/usage`, `/env`, `/chronicle`, `/extensions` with hot reload
- **Auto model selection** — CLI picks optimal model per task; BYOK/local models supported
- **Extension SDK** — multi-language extension authoring with tab completion

### The Pattern

Every platform shipped the same three capabilities within days:

- **Persistence** — agents remembering across sessions (Codex memory, Claude alwaysLoad, Copilot named sessions)
- **Orchestration** — managing multiple sub-agents or external tools (Claude ultrareview, Cursor subagents, Symphony)
- **Security** — hardening against new attack surfaces (Cursor Security Review, Anthropic Claude Security, Copilot headless OAuth)

The race is no longer "who writes better completions." It's who builds the most capable autonomous engineer — and secures it first.

---
