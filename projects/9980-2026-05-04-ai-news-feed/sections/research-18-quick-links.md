# Quick Links: New AI Developer Tools (Apr 25–May 1, 2026)

## OpenAI Symphony

- **Repo:** https://github.com/openai/symphony
- **Description:** Spec and reference implementation for turning project work into isolated, autonomous Codex agent runs — teams manage work, not coding agents.
- **Key features:**
  - Monitors task boards (e.g., Linear) and spawns Codex agents per task
  - Agents deliver proof of work: CI status, PR review feedback, complexity analysis, walkthrough videos
  - Language-agnostic spec — "tell your favorite coding agent to build Symphony"
  - Reference implementation in Elixir
  - Builds on OpenAI's "harness engineering" philosophy
- **Stars/License:** ⭐ 21.1k | Apache-2.0
- **Why it matters:** Moves AI coding from "developer supervises agent" to "PM manages work queue." Symphony is OpenAI's answer to how teams actually deploy Codex at scale — not one task at a time, but as an autonomous workforce pulling from a backlog.
- **Source:** [OpenAI Harness Engineering blog post](https://openai.com/index/harness-engineering/)

---

## Microsoft APM (Agent Package Manager)

- **Repo:** https://github.com/microsoft/apm
- **Description:** Open-source dependency manager for AI agent configurations — like npm/pip but for skills, instructions, prompts, MCP servers, and plugins.
- **Key features:**
  - Single `apm.yml` manifest declares all agent context; `apm install` reproduces it everywhere
  - Transitive dependency resolution with lockfile (`apm.lock.yaml`) and integrity hashes
  - Cross-agent support: Copilot, Claude Code, Cursor, OpenCode, Codex, Gemini, Windsurf
  - `apm compile -t copilot` generates `.github/copilot-instructions.md` automatically
  - Security scanning on install (hidden Unicode detection, MCP trust boundaries)
  - Enterprise governance via `apm-policy.yml` (tighten-only inheritance, audit-mode CI gates)
  - Marketplace support, plugin authoring, `apm pack` for distribution
  - Install methods: curl, Homebrew, pip, Scoop
- **Stars/License:** ⭐ 2.2k | MIT | v0.11.0
- **Why it matters:** Solves the "works on my machine" problem for AI agent setups. Before APM, every developer manually configured their agent context. Now teams can version, share, and enforce agent configurations with the same rigor as code dependencies.
- **Source:** [APM Documentation](https://microsoft.github.io/apm/) · [GitHub Roadmap](https://github.com/orgs/microsoft/projects/2304)

---

## Microsoft AgentRC

- **Repo:** https://github.com/microsoft/agentrc
- **Description:** Reads your codebase and generates context-specific instruction files for AI coding agents, then evaluates whether they actually help.
- **Key features:**
  - **Measure:** Scores repo AI-readiness across 9 pillars and a 5-level maturity model (`agentrc readiness`)
  - **Generate:** Produces tailored instruction files via Copilot SDK — no templates, reads actual code (`agentrc instructions`)
  - **Maintain:** Evaluates instruction quality over time; CI integration catches drift (`agentrc eval`)
  - Generates `.github/copilot-instructions.md`, `.vscode/mcp.json`, eval test cases
  - Works as CLI, VS Code extension, and CI/CD pipeline quality gate
  - Batch processing across entire orgs (`agentrc batch`)
  - Automated PR creation for any repo (`agentrc pr owner/repo`)
  - Supports GitHub and Azure DevOps, monorepos, multi-root workspaces
  - Companion to APM — generates content, APM distributes it
- **Stars/License:** ⭐ 835 | MIT
- **Why it matters:** "Your repo has an AI-readiness score" is a compelling hook. As AI coding agents become standard, the repos that provide good context will get dramatically better AI output. AgentRC automates the creation and maintenance of that context — turning "context engineering" from art into measurable engineering practice.
- **Source:** [AgentRC Docs](https://github.com/microsoft/agentrc/blob/main/docs/getting-started.md) · [VS Code Custom Instructions](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)

---

*Note: Star counts captured May 4, 2026. APM and AgentRC are designed as companion tools — AgentRC generates agent context, APM packages and distributes it across teams.*
