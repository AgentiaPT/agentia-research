# Research: GitHub Copilot CLI — ACP Session Controls, Headless OAuth for MCP, Slash Commands

## Key Facts

### ACP (Agent Control Protocol) Session Controls
- ACP entered **public preview** on 2026-01-28; by April 2026 it is a mature integration layer
- Start an ACP server with `copilot --acp` (stdio or TCP on a specified port)
- **Allow-All Permission Toggle**: session-wide auto-approval for tool execution and file operations — enables fully autonomous agent workflows
- **Session Backgrounding**: `Ctrl+X` then `B` sends a running task to the background without leaving the session
- **Session Resume Picker**: improved single-line session summaries for quick search/resume
- **Remote Session Control** (public preview 2026-04-13): start a session locally, monitor/steer it from GitHub.com or GitHub Mobile in real time; 60 MB stream output cap; only the initiating user can control it
- **Named Sessions**: create with `--name=NAME`, resume with `--resume=NAME`, delete individually or all at once
- ACP clients can now list and switch custom agents from the agent config UI

### Headless OAuth for MCP Servers
- Shipped in **Copilot CLI v1.0.40** (May 1, 2026)
- Adds **OAuth 2.0 `client_credentials` grant** for MCP server authentication
- Enables fully programmatic token acquisition — no browser, no human interaction
- Critical for CI/CD pipelines, containers, SSH remotes, and headless environments
- MCP server config: `~/.copilot/mcp-config.json`, per-workspace files, or CLI flags
- Complements enterprise patterns using Azure API Management + Entra ID for secure MCP exposure

### New & Updated Slash Commands (Apr–May 2026)
- `/compact` — manually trigger context compaction to reduce token usage
- `/context` — view/set working context and environment
- `/usage` — real-time session stats (tokens, requests)
- `/env` — display or modify session environment variables
- `/chronicle` — full session history and file-tracking (now available to all users)
- `/extensions` — in-session extension management with live enable/disable and hot reload
- `/clear` and `/new` now reset custom agent selection
- **Tab completion** for slash commands, arguments, subcommands, and paths (April 2026)
- **Custom slash commands in extensions** via SDK (Node.js, Python, Go, .NET)
- Slash commands exposed as "skills" in ACP clients

### Other Notable Updates (Apr 25 – May 1 Window)
- **BYOK & Local Models** (2026-04-07): bring your own API key, use local models; optional GitHub auth; all telemetry disabled in offline mode
- **Auto Model Selection** (2026-04-17): GitHub dynamically routes to the best model; billing discounts for premium models in auto mode
- **Usage Metrics** (2026-04-10): CLI activity now included in org-level usage metrics totals and feature breakdowns
- **Autopilot continuation cap**: defaults to 5 multi-turn continuations (configurable)
- `--config-dir` deprecated in favor of `COPILOT_HOME` environment variable
- Azure DevOps repo detection auto-disables the GitHub MCP server
- Faster startup via async custom CA cert loading

## Timeline

| Date | Event |
|------|-------|
| 2026-01-28 | ACP support enters public preview |
| 2026-02-25 | Copilot CLI reaches General Availability |
| 2026-04-07 | BYOK and local model support ships |
| 2026-04-10 | CLI activity added to usage metrics |
| 2026-04-13 | Remote session control (web/mobile) public preview |
| 2026-04-17 | Auto model selection support |
| 2026-04-24 | Tab completion for slash commands; named sessions |
| 2026-05-01 | v1.0.40 — headless OAuth for MCP; extension revamp; `/chronicle` GA |

## Sources

- [ACP support in Copilot CLI — public preview](https://github.blog/changelog/2026-01-28-acp-support-in-copilot-cli-is-now-in-public-preview/)
- [Remote control CLI sessions on web and mobile](https://github.blog/changelog/2026-04-13-remote-control-cli-sessions-on-web-and-mobile-in-public-preview/)
- [Auto model selection](https://github.blog/changelog/2026-04-17-github-copilot-cli-now-supports-copilot-auto-model-selection/)
- [BYOK and local models](https://github.blog/changelog/2026-04-07-copilot-cli-now-supports-byok-and-local-models/)
- [CLI activity in usage metrics](https://github.blog/changelog/2026-04-10-copilot-cli-activity-now-included-in-usage-metrics-totals-and-feature-breakdowns/)
- [Copilot CLI Weekly: Headless OAuth, Background Tasks](https://htek.dev/articles/copilot-cli-weekly-2026-05-01/)
- [Copilot CLI Weekly: Tab Completion and Named Sessions](https://htek.dev/articles/copilot-cli-weekly-2026-04-24)
- [Copilot CLI Extensions Revamp](https://dev.to/htekdev/copilot-cli-extensions-revamp-custom-slash-commands-and-full-extensibility-1f9e)
- [Steer Copilot CLI Sessions Remotely](https://dev.to/pwd9000/steer-github-copilot-cli-sessions-remotely-from-any-device-3mee)
- [copilot-cli changelog](https://github.com/github/copilot-cli/blob/main/changelog.md)
- [MCP Server Configuration — DeepWiki](https://deepwiki.com/github/copilot-cli/5.3-mcp-server-configuration)

## Impact

- **For individual developers**: The CLI is now a full agentic IDE-in-terminal — plan, execute, background tasks, switch models, and resume sessions across devices. Slash commands provide granular control without leaving the flow.
- **For CI/CD and automation**: Headless OAuth eliminates the last browser-dependency barrier for using MCP-powered tools in pipelines and containers. Combined with BYOK/local models and ACP, Copilot CLI can now run fully autonomous coding agents in headless infrastructure.
- **For enterprises**: Remote session control + usage metrics integration + Entra ID-compatible OAuth means orgs can deploy, monitor, and govern agentic CLI usage at scale.
- **For the ecosystem**: ACP as a standardized protocol + extensible slash commands + multi-language SDK means third-party tools and agents can plug into Copilot CLI without proprietary integrations.
- **Competitive signal**: GitHub is rapidly closing the gap with standalone agentic tools (Cursor, Windsurf, Claude Code) by making the terminal-native experience feature-complete — including the critical remote/mobile control dimension that competitors lack.
