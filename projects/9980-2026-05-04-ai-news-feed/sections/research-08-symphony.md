# Research: OpenAI Open-Sources Symphony — Spec for Codex Orchestration

## Key Facts

- **What it is**: Symphony is an open-source specification (primarily a `SPEC.md` file) that turns issue trackers (e.g., Linear) into control planes for Codex coding agents
- **Purpose**: Moves teams from manually supervising coding agents to managing work at the ticket/task level — agents autonomously pick up issues, implement them, and shepherd PRs to merge
- **Architecture**: A long-running daemon/service that:
  - Polls an issue tracker on a fixed cadence
  - Creates isolated per-issue workspaces
  - Spawns Codex agent sessions per task
  - Monitors CI, rebases, resolves conflicts, retries flaky checks
  - Restarts crashed/stalled agents
  - Dispatches with bounded concurrency and exponential backoff
- **Key design choice**: Symphony is a *spec*, not a monolithic tool — the repo contains `SPEC.md` (the language-agnostic specification) plus a reference implementation in Elixir
- **Origin story**: OpenAI team built a repo with zero human-written code using Codex; hit a ceiling at 3–5 concurrent sessions per engineer due to context-switching overhead; Symphony was the solution
- **Impact claimed**: 500% increase in landed PRs in first 3 weeks on some internal teams
- **Repository**: github.com/openai/symphony — 21.1k stars, 1.9k forks, 6 contributors, Apache 2.0 license
- **Languages**: Elixir (95.5%), Python (3%), CSS (1.2%)
- **Reference implementation**: Elixir-based (in `elixir/` directory)
- **Key concept — "Harness Engineering"**: Symphony builds on OpenAI's prior concept of making repositories "agent-friendly" with automated tests, guardrails, and `WORKFLOW.md` files that version the agent prompt alongside the code
- **Authors**: Alex Kotliarskyi, Victor Zhu, and Zach Brock (OpenAI)

## Technical Details

- **WORKFLOW.md**: A per-repo file with YAML front matter + prompt body that defines how agents should behave in that repository — versioned with the code
- **State machine model**: Uses Linear ticket statuses as states; agents transition tickets through stages (e.g., → In Progress → Human Review → Merging → Done)
- **DAG execution**: Tasks can have dependencies; agents only start on unblocked tasks, enabling natural parallel execution
- **Self-filing**: Agents can create new issues when they discover improvements outside current scope
- **Objectives over transitions**: Evolved from rigid state machines to giving agents goals + tools (gh CLI, CI log readers, Chrome DevTools) and letting them reason about next steps
- **Non-goals**: Not a web UI, not a distributed job scheduler, not a sandbox — it's a scheduler/runner that reads tickets and dispatches agents
- **Recovery**: Supports restart recovery without persistent database; reconciles state on boot

## Problems It Solves

1. **Human attention bottleneck** — Engineers could only manage 3–5 interactive Codex sessions before context-switching degraded productivity
2. **Session-centric workflow** — Decouples work from sessions/PRs; tickets can represent larger units of work spanning multiple repos
3. **Last-mile CI friction** — Watches CI, rebases, resolves conflicts, retries flaky checks automatically
4. **Exploration cost** — Drops the perceived cost of speculative tasks to near-zero; non-engineers (PMs, designers) can file work directly
5. **Agent supervision overhead** — Eliminates need to manually steer/nudge agents mid-task

## Limitations (per OpenAI)

- Agents can miss the mark when given ticket-level autonomy (lost ability to nudge mid-flight)
- Not every task fits — ambiguous problems or those requiring strong judgment still need interactive sessions
- Higher PR volume doesn't equal higher quality; review/testing burden scales with output
- Enterprises need audit trails, security policies, identity integration before adopting at scale

## Timeline

| Date | Event |
|------|-------|
| ~Oct 2025 | OpenAI team begins building repo with zero human code |
| Mar 4, 2026 | Initial commit to github.com/openai/symphony (repo created with SPEC.md, LICENSE, README) |
| Mar 27, 2026 | GitHub Actions workflow pinning |
| Apr 27, 2026 | Latest commits: SPEC.md clarification (RFC 2119 language), Elixir implementation updates |
| Apr 27, 2026 | Blog post published: "An open-source spec for Codex orchestration: Symphony" |
| Apr 28, 2026 | InfoWorld coverage; wider industry attention |

## Sources

- OpenAI blog post (Apr 27, 2026): https://openai.com/index/open-source-codex-orchestration-symphony/
- InfoWorld article by Prasanth Aby Thomas (Apr 28, 2026): https://www.infoworld.com/article/4164173/openais-symphony-spec-pushes-coding-agents-from-prompts-to-orchestration.html
- GitHub repository: https://github.com/openai/symphony (21.1k ⭐, Apache 2.0)

## Impact

- **For enterprises**: Shifts AI from personal coding aid to shared engineering infrastructure — "a lightweight operating system for software delivery" (Greyhound Research)
- **For the ecosystem**: Establishes an open standard for agent orchestration that any tool can implement (spec-first design means it's not locked to OpenAI's stack)
- **Analyst view (Forrester)**: "Value increases when agents are embedded into workflows and governed at scale rather than invoked interactively by individuals"
- **Cautionary notes**: Industry analysts warn that generation scales effortlessly but validation does not; 500% PR increase should prompt caution around review quality, escaped defects, and junior engineer development
- **Competitive context**: Positions OpenAI/Codex as the orchestration layer for software delivery, potentially ahead of GitHub Copilot's workspace features and other coding agents that remain session-focused
- **Open questions**: Legacy toolchain integration, ownership of agent decisions, traceability, separation of duties remain unresolved for enterprise adoption
