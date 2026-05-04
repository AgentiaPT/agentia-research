## 12. Quick Links — New Tools & Frameworks

**Two repos that landed this week and deserve your attention.**

---

**Microsoft APM (Agent Package Manager)** — npm for AI Agent Configs

- **Repo:** [github.com/microsoft/apm](https://github.com/microsoft/apm)
- **Stars:** 2.2k | **License:** MIT | **Version:** 0.11.0
- **What:** Declare all agent context (skills, instructions, prompts, MCP servers, plugins) in one `apm.yml`. `apm install` reproduces it everywhere. Lockfile-pinned, security-scanned, policy-gated.
- **Cross-agent:** Works with Copilot, Claude Code, Cursor, OpenCode, Codex, Gemini, Windsurf
- **Key command:** `apm compile -t copilot` generates `.github/copilot-instructions.md` automatically

---

**Microsoft AgentRC** — AI-Readiness Scoring for Repos

- **Repo:** [github.com/microsoft/agentrc](https://github.com/microsoft/agentrc)
- **Stars:** 835 | **License:** MIT
- **What:** Reads your codebase, scores AI-readiness across 9 pillars and a 5-level maturity model, generates tailored instruction files for AI coding agents, then evaluates whether they help.
- **Key commands:** `agentrc readiness` (score), `agentrc instructions` (generate), `agentrc eval` (measure improvement)
- **Integration:** CLI, VS Code extension, CI/CD pipeline quality gate, batch processing across orgs
- **Companion to APM:** AgentRC generates context → APM distributes it across teams

---
