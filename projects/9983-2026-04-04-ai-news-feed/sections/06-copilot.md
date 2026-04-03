## 6. GitHub Copilot Goes Cloud-Native

**April 1–3 | [GitHub Blog](https://github.blog/changelog/2026-04-01-research-plan-and-code-with-copilot-cloud-agent/) · [GitHub Changelog](https://github.blog/changelog/2026-04-03-copilot-cloud-agent-signs-its-commits/) · [GitHub Docs](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent)**

Three updates in three days signal that GitHub's Copilot is completing its transformation from "code suggestion tool" to "autonomous development workflow."

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

### Why This Matters

The three updates form a coherent story: Copilot cloud agent is being positioned as a full development peer, not a typing accelerator. Research-then-plan-then-code is how human developers work. Signed commits solve the audit trail problem. Org-level controls solve the governance problem. GitHub is systematically removing the reasons enterprises say "not yet" to agentic development.
