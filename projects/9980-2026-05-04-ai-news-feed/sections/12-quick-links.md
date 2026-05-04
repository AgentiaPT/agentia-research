## 12. Quick Links — New Tools & Frameworks

**Three repos that landed this week and deserve your attention.**

---

**OpenAI Symphony** — Autonomous Codex Orchestration

- **Repo:** [github.com/openai/symphony](https://github.com/openai/symphony)
- **Stars:** 21.1k | **License:** Apache-2.0
- **What:** Spec + Elixir reference implementation for turning task boards (Linear, Jira, GitHub Issues) into control planes for Codex agents. Agents pull tasks, work in isolated sandboxes, deliver PRs with proof of work.
- **Why it matters:** The jump from "one human supervises one agent" to "agents autonomously process backlogs." OpenAI claims 500% PR increase internally.

---

**Microsoft APM (Agent Package Manager)** — npm for AI Agent Configs

- **Repo:** [github.com/microsoft/apm](https://github.com/microsoft/apm)
- **Stars:** 2.2k | **License:** MIT | **Version:** 0.11.0
- **What:** Declare all agent context (skills, instructions, prompts, MCP servers, plugins) in one `apm.yml`. `apm install` reproduces it everywhere. Lockfile-pinned, security-scanned, policy-gated.
- **Cross-agent:** Works with Copilot, Claude Code, Cursor, OpenCode, Codex, Gemini, Windsurf
- **Key command:** `apm compile -t copilot` generates `.github/copilot-instructions.md` automatically
- **Why it matters:** Solves "works on my machine" for AI agent setups. Version, share, and enforce agent configurations with the same rigor as code dependencies.

---

**Microsoft AgentRC** — AI-Readiness Scoring for Repos

- **Repo:** [github.com/microsoft/agentrc](https://github.com/microsoft/agentrc)
- **Stars:** 835 | **License:** MIT
- **What:** Reads your codebase, scores AI-readiness across 9 pillars and a 5-level maturity model, generates tailored instruction files for AI coding agents, then evaluates whether they help.
- **Key commands:** `agentrc readiness` (score), `agentrc instructions` (generate), `agentrc eval` (measure improvement)
- **Integration:** CLI, VS Code extension, CI/CD pipeline quality gate, batch processing across orgs
- **Companion to APM:** AgentRC generates context → APM distributes it across teams
- **Why it matters:** *"Your repo has an AI-readiness score. Here's how to check it."* Turns context engineering from art into measurable practice.

---
