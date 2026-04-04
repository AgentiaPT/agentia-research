## 6. GitHub Copilot Goes Cloud-Native

**April 1–3 | [GitHub Blog](https://github.blog/changelog/2026-04-01-research-plan-and-code-with-copilot-cloud-agent/) · [GitHub Changelog](https://github.blog/changelog/2026-04-03-copilot-cloud-agent-signs-its-commits/) · [GitHub Docs](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent)**

After last week's [data training backlash](../9984-2026-03-29-ai-news-feed/README.md#4-the-data-training-backlash--github-copilot-opts-you-in), GitHub pivoted to shipping capability. Three updates in three days signal that Copilot is completing its transformation from "code suggestion tool" to "autonomous development workflow."

### Research, Plan, and Code (April 1)

**Copilot cloud agent** (rebranded from "coding agent") is no longer limited to pull-request workflows. The agent can now:

- **Work on a branch without creating a PR** — giving developers flexibility over how and when to advance work
- **Produce an implementation plan** for review before writing any code
- **Research** a codebase and answer questions about architecture and conventions

This is the shift from "suggest code when I type" to "understand the problem, plan the approach, execute the solution." The agent now runs on **Claude Sonnet 4.6**.

### Commit Signing (April 3)

Every commit made by Copilot cloud agent is now **cryptographically signed**. Signed commits appear as **Verified** on GitHub, confirming the commit was genuinely made by the agent and hasn't been tampered with. Critically, this means Copilot now works in repositories with the **"Require signed commits"** branch protection rule — previously a blocker for agentic workflows in security-conscious organizations.

### Organization Runner Controls (April 3)

Organization admins can now:
- Set a **default runner** used automatically across all repositories without per-repo configuration
- **Lock the runner setting** so individual repositories can't override the organization default

This addresses the enterprise deployment gap: IT teams can standardize how Copilot's agent runs across the organization while maintaining central control.

### Copilot SDK (April 2)

GitHub also released the **Copilot SDK in public preview** — building blocks to embed Copilot's agentic capabilities into external apps. Available for Node.js/TypeScript, Python, Go, .NET, and Java. This opens Copilot's agent infrastructure to the broader developer tools ecosystem.

### Cursor 3: The Agent Management IDE (April 2)

The same week, **Cursor shipped its biggest update ever** — a ground-up redesign centered on managing multiple AI agents rather than writing code directly ([Cursor Blog](https://cursor.com/blog/cursor-3)):

- **Agents Window** — run many agents in parallel across repos and environments (local, worktrees, cloud, SSH)
- **Design Mode** — annotate and target UI elements in a browser view, giving agents pixel-precise feedback
- **/worktree** — creates isolated git worktrees so agent changes don't conflict
- **/best-of-n** — runs the same task across multiple models in parallel worktrees, then compares outcomes
- **Composer 2** — frontier coding model scoring 61.3 on CursorBench (37% improvement) and 73.7 on SWE-bench Multilingual

Cursor 3 represents a philosophical shift: **the developer becomes an orchestrator supervising multiple agents**, not a line-by-line coder.

### Why This Matters

GitHub and Cursor both shipped agent-management paradigms in the same week. The convergence is clear: AI development tools are no longer autocomplete engines — they're autonomous workflow platforms. The developer's job is shifting from "write code" to "direct agents, review output, maintain architecture." Research-plan-code (Copilot), multi-agent orchestration (Cursor 3), and signed commits (both) all point to the same future.
