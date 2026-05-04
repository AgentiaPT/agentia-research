## 9. OpenAI Symphony — From Prompts to Orchestration

**April 28 | [OpenAI](https://openai.com/index/open-source-codex-orchestration-symphony/) · [GitHub](https://github.com/openai/symphony) · [InfoWorld](https://www.infoworld.com/article/4164173/openais-symphony-spec-pushes-coding-agents-from-prompts-to-orchestration.html)**

OpenAI open-sourced **Symphony** — a *specification* for turning existing task management tools into control planes for autonomous Codex agents.

**What It Is**

A daemon that:

1. **Polls task boards** (Linear, Jira, GitHub Issues) for work items
2. **Spawns isolated Codex agent workspaces** — one per task, sandboxed
3. **Monitors CI** — tracks whether agent-submitted work passes tests
4. **Shepherds PRs to merge** — agents deliver proof of work: CI status, review feedback, complexity analysis

Mental model: your PM assigns tasks to a board. Symphony treats each ticket as a work order for an autonomous agent. Humans review output, not process.

**Technical Details**

- **Language-agnostic spec** — `SPEC.md` defines the protocol; any agent framework can implement it
- **Reference implementation** in Elixir (chosen for supervision trees and fault tolerance)
- **Apache 2.0** license
- **~20k+ GitHub stars** in the first weeks
- OpenAI claims **500% increase in PRs** internally after adoption

**Why It Matters**

The shift: from "developer supervises one agent on one task" to "PM manages a queue that agents pull from autonomously." Symphony eliminates the 3–5 session context-switching ceiling limiting current AI coding tools. Instead of babysitting, you backlog.

Competes with Claude Code's `/ultrareview` and Cursor's subagent architecture — but at a different layer. Symphony doesn't care which agent does the work. It's the orchestration spec, not the executor.

---
