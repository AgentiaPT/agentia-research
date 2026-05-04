## 8. OpenAI Symphony — From Prompts to Orchestration

**April 28 | [OpenAI](https://openai.com/index/open-source-codex-orchestration-symphony/) · [GitHub](https://github.com/openai/symphony) · [InfoWorld](https://www.infoworld.com/article/4164173/openais-symphony-spec-pushes-coding-agents-from-prompts-to-orchestration.html)**

OpenAI open-sourced **Symphony** — not a product, but a *specification* for how teams can turn their existing task management tools into control planes for autonomous Codex agents.

**What It Is**

Symphony is a daemon that:

1. **Polls task boards** (Linear, Jira, GitHub Issues) for work items
2. **Spawns isolated Codex agent workspaces** — one per task, sandboxed
3. **Monitors CI** — agents submit work, Symphony tracks whether tests pass
4. **Shepherds PRs to merge** — agents deliver proof of work: CI status, review feedback, complexity analysis, walkthrough videos

The mental model: your project manager assigns tasks to a ticket board. Symphony treats each ticket as a work order for an autonomous agent. Humans review the output, not the process.

**Technical Details**

- **Language-agnostic spec** — `SPEC.md` defines the protocol; any agent framework can implement it
- **Reference implementation** in Elixir (chosen for supervision trees and fault tolerance)
- **Apache 2.0** license
- **21.1k GitHub stars** in the first week
- OpenAI claims **500% increase in PRs** internally after adopting the workflow

**Why It Matters**

The shift is fundamental: from "developer supervises one agent completing one task" to "PM manages a queue of tasks that agents pull from autonomously." Symphony eliminates the 3–5 session context-switching ceiling that currently limits AI coding tools. Instead of babysitting, you backlog.

This directly competes with Claude Code's `/ultrareview` and Cursor's subagent architecture — but at a different layer. Symphony doesn't care which agent does the work. It's the orchestration spec, not the executor.

---
