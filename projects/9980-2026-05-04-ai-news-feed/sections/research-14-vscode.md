# Research: VS Code 1.118 Release (April 29, 2026)

## Key Facts

- **Release date**: April 29, 2026 (version 1.118)
- **Theme**: Expanding where you can work with Copilot agents and making them more efficient

### Remote Control for Copilot CLI Sessions (Experimental)
- Monitor and steer ongoing Copilot CLI sessions from GitHub.com or the GitHub mobile app
- Respond to approvals, check progress, and steer work from another device while the session keeps running in background
- Enable via `github.copilot.chat.cli.remote.enabled` setting; activate with `/remote on` in CLI chat
- Eliminates the need to be at your machine when the agent pauses for approval

### Codebase Search & Context
- **Semantic indexing now available in ALL workspaces** — previously limited to GitHub/ADO repos only
- Searches by meaning (e.g., "authentication" finds `login`, `signIn`, `verifyCredentials`, `OAuth token exchange`)
- Non-GitHub workspaces may require a few minutes to build initial index
- **GitHub text search (`githubTextSearch` tool)**: grep-style exact-match search across GitHub repos or entire orgs
- Complements existing `githubRepo` semantic search tool for code outside current workspace

### Dedicated Context for Skills (Experimental)
- Skills can now run in a dedicated subagent context isolated from main conversation
- Prevents multi-step tool calls and large reference material from crowding main chat context
- Configured via `context: fork` in `SKILL.md` frontmatter
- Requires `github.copilot.chat.skillTool.enabled` setting

### Chronicle — Chat Session Insights (Experimental)
- Tracks chat interactions in a local SQLite database (session metadata, branches, repos, timestamps, files touched, PR/issue references)
- `/chronicle:standup` — generates standup report from last 24 hours, grouped by feature/branch
- `/chronicle:tips` — analyzes 7 days of usage for personalized prompting/workflow tips
- `/chronicle [query]` — free-form natural language queries against session history
- Requires `github.copilot.chat.localIndex.enabled` setting

### Enterprise Control — Approved Account Organizations Policy
- New `ChatApprovedAccountOrganizations` device policy gates AI feature activation on approved GitHub org membership
- Fail-closed behavior: chat features not activated until user is signed into an approved org account
- Useful for enterprises enforcing account-based policies consistently across chat entry points

### Token Efficiency Improvements
- **Prompt caching**: 93%+ of each request reused from cache in ongoing sessions; ~10x lower billing rate for cached tokens on Anthropic models
- **Tool search tool**: splits toolset into ~30 always-available core tools (~88% of calls) + deferred tools loaded on demand; up to **20% token savings** on Anthropic models; rolling out to GPT-5.4 and GPT-5.5
- **Agentic search tool**: fine-tuned small model handles codebase exploration independently; up to 20% token savings
- **Agentic execution tool**: offloads terminal command execution to smaller model; filters verbose output before returning to main agent; capped at 10 terminal calls per invocation
- **WebSocket mode for OpenAI models**: persistent connection reduces latency; makes OpenAI models **12% faster**

### Other Notable Changes
- **VS Code Agents app** (Insiders): companion app for parallel agent sessions; now accessible from title bar; web client at insiders.vscode.dev/agents; Claude agent available alongside Copilot CLI/Cloud
- **Copilot added as Git co-author by default** for chat/agent workflows
- **Workspace `.mcp.json` files**: declare MCP servers at workspace level with automatic deduplication
- **Sandboxing**: read access no longer automatically enabled for all `$HOME` paths; strengthened isolation

## Timeline

| Date | Event |
|------|-------|
| April 27, 2026 | GitHub announces Copilot moving to usage-based billing (effective June 1, 2026) |
| April 29, 2026 | VS Code 1.118 released |
| June 1, 2026 | Copilot usage-based billing takes effect |

## Sources

- [VS Code 1.118 Release Notes](https://code.visualstudio.com/updates/v1_118#:~:text=Welcome%20to%20the%201.118%20release)
- [GitHub Copilot usage-based billing announcement](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/)
- [VS Code Agents documentation](https://aka.ms/VSCode/Agents/docs)
- [How Copilot understands your workspace](https://code.visualstudio.com/docs/copilot/reference/workspace-context)

## Impact

- **Developer workflow**: Remote control for CLI sessions is a significant quality-of-life improvement for developers who start long-running agent tasks and step away — particularly relevant for mobile-first workflows
- **Cost reduction timing**: Token efficiency improvements (20% savings, 93% cache reuse, WebSocket 12% speed boost) arrive just before usage-based billing kicks in June 1 — clearly designed to soften the billing transition
- **Enterprise adoption**: The new org-gating policy addresses a key enterprise blocker — IT admins can now enforce which accounts access AI features before any chat UI appears
- **Search paradigm shift**: Semantic indexing for all workspaces (not just GitHub repos) democratizes AI-powered code search to any development environment
- **Agent ecosystem maturation**: The Agents companion app, dedicated skill contexts, and Chronicle represent VS Code's evolution from "editor with AI" to "AI-native development environment"
