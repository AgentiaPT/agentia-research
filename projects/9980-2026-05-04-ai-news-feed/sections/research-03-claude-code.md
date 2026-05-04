# Research: Claude Code April Update

## Key Facts

### /ultrareview (Public Preview — Week of Apr 20–24)
- Cloud-based, multi-agent code review launched as `/ultrareview` slash command
- Uploads branch or PR to a secure cloud sandbox; multiple specialized AI agents analyze in parallel (security, logic, performance, edge cases)
- Includes a **verification pass** — a separate agent reproduces each finding in isolation; only confirmed bugs are reported
- Runs asynchronously; user can close terminal and check progress via `/tasks`
- Takes ~5–10 minutes vs. seconds for local `/review`; designed for critical pre-merge moments
- Pricing: Pro/Max users got 3 free runs until May 5, 2026; billed per run afterward ($5–$20 depending on repo size)
- Only supports GitHub PRs; not available on Bedrock, Vertex, Foundry, or zero-data-retention orgs
- Requires v2.1.86+ and active Claude.ai login

### plugin prune (v2.1.121 — Apr 28)
- New command `claude plugin prune` removes orphaned auto-installed plugin dependencies
- `plugin uninstall --prune` now cascades removal of lingering dependencies
- Addresses buildup of unused libraries on shared dev machines

### Windows Without Git Bash (PowerShell Tool — v2.1.84+, late March / early April)
- Native PowerShell support as opt-in shell tool; no longer requires Git Bash or WSL
- Resolves path translation errors (C:\ vs /c/), CLI flag incompatibilities, and inability to run native Windows scripts
- Automatic fallback: if Git for Windows is absent, Claude Code uses PowerShell automatically (v2.1.120+)
- Supports direct registry, Event Log, and Azure AD interactions
- Configurable via `{ "defaultShell": "powershell" }` in settings.json

### MCP "alwaysLoad" Configuration (v2.1.121 — Apr 28)
- New `alwaysLoad: true` option in MCP server config
- All tools from that server are immediately available at session start — bypasses deferred ToolSearch loading
- Eliminates surprise "benching" of custom tools by deferral logic
- Critical for teams relying on the same MCP tooling every session

### Other Notable April Features
- **Opus 4.7 released (mid-April)**: new default "xhigh" effort level; +13% coding benchmark; 3× vision improvement
- **Auto Mode for Max users**: runs complex tasks without repetitive permission prompts
- **NO_FLICKER rendering engine**: flicker-free terminal output
- **/powerup interactive tutorials**: guided onboarding system
- **/team-onboarding**: easier team setup with admin-guided access controls
- **PostToolUse hooks expanded**: can now replace output for ALL tool types, not just MCP
- **/skills filter**: type-to-filter search box for long skill lists
- **Quality postmortem (Apr 23)**: Anthropic disclosed three changes that degraded quality (effort default switched to medium, session memory bug, verbosity-reducing prompt change); all reverted; usage limits reset for subscribers
- **Deprecation notice**: Claude Sonnet 4 and Opus 4 (original) retiring June 15, 2026 — migrate to 4.6+ models

## Timeline
- **Mar 26**: v2.1.84 — PowerShell tool preview ships
- **Apr 1**: v2.1.90 — /powerup tutorials, NO_FLICKER rendering
- **Apr 9**: v2.1.98 — Vertex AI wizard, monitor tool, sandbox
- **Apr 10**: v2.1.101 — /team-onboarding, OS CA cert trust
- **Apr 20–24 (Week 17)**: /ultrareview enters public research preview; Opus 4.7 ships
- **Apr 23**: Anthropic publishes quality postmortem; reverts three problematic changes
- **Apr 28**: v2.1.121 — alwaysLoad MCP, plugin prune, PostToolUse for all tools, memory leak fixes
- **Apr 28**: v2.1.122 — Bedrock service tier selection, PR URL session lookup, further bugfixes

## Sources
- [Claude Code Week 17 (Apr 20–24) — Official Docs](https://code.claude.com/docs/en/whats-new/2026-w17)
- [Claude Code Changelog — All Release Notes (2026)](https://claudefa.st/blog/guide/changelog)
- [Claude Code v2.1.121 Release Notes — ClaudeWorld](https://claude-world.com/articles/claude-code-21121-release/)
- [Claude Code v2.1.122 Release Notes — Build This Now](https://www.buildthisnow.com/blog/guide/development/claude-code-v2-1-122-whats-new)
- [Claude Code v2.1.121 — NewReleases.io / GitHub](https://newreleases.io/project/github/anthropics/claude-code/release/v2.1.121)
- [Claude Code v2.1.120–123 (Apr 28–29) — Authority AI Tools](https://authorityaitools.com/blog/claude-code-2-1-120-april-2026-update)
- [Claude Code PowerShell Tool Guide — ClaudeLab](https://claudelab.net/en/articles/claude-code/claude-code-powershell-tool-windows-guide)
- [An Update on Recent Claude Code Quality Reports — Anthropic Engineering](https://www.anthropic.com/engineering/april-23-postmortem)
- [Claude Code /ultrareview — Multi-Agent Cloud Review](https://www.claudedirectory.org/blog/ultrareview-claude-code-guide)
- [Opus 4.7 Feature Guide — Pasquale Pillitteri](https://pasqualepillitteri.it/en/news/925/claude-opus-4-7-complete-guide-features)
- [Claude Code MCP Always-Load, Plugin Pruning — SmarterWork](https://www.smarterwork.ai/updates/claude-code-v21121-mcp-always-load-plugin-pruning-ux-fixes)
- [State of AI Code Review — April 2026 Recap (DEV Community)](https://dev.to/lewiska/state-of-ai-code-review-april-2026-recap-5acb)

## Impact / Why It Matters
- **/ultrareview** represents a shift from single-pass AI review to multi-agent verification — directly addresses the trust gap in AI-generated code by having agents cross-check each other
- **Plugin prune** is a small but meaningful DevEx improvement for teams with heavy plugin usage; reduces "works on my machine" drift
- **Windows PowerShell support** removes the last major friction point for Windows developers — Claude Code is now fully cross-platform without workarounds
- **alwaysLoad MCP** is significant for enterprise teams building standardized toolchains — guarantees tool availability eliminates a class of "where did my tool go?" support tickets
- **Quality postmortem transparency** sets an industry precedent: Anthropic publicly disclosed internal decisions that hurt quality and gave concrete remediation — builds developer trust
- The breadth of the April update (new model, new review paradigm, Windows parity, extensibility) positions Claude Code as the most rapidly iterating AI coding tool in the market
