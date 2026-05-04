# Research: Cursor SDK + Security Review

## Key Facts

- **Cursor Security Review** entered beta on April 30, 2026, for Teams and Enterprise plans
- Two always-on security agents ship together:
  - **Security Reviewer** — checks every PR for vulnerabilities, auth regressions, privacy/data-handling risks, tool auto-approvals, and prompt injection attacks; leaves inline comments with severity ratings and remediation advice
  - **Vulnerability Scanner** — scheduled full-codebase scans for known CVEs, outdated dependencies, and configuration issues; findings can push to Slack
- Both agents are customizable: triggers, tooling, output destinations, and org-specific scanning tools (SAST, SCA, secrets detection) can be plugged in via MCP servers
- Admins enable Security Review from the Cursor dashboard; usage draws from the plan's usage pool
- **Cursor SDK** entered public beta on April 29, 2026 — a TypeScript SDK (`@cursor/sdk`) exposing the full agent runtime as programmable infrastructure
- SDK execution modes: local (Node.js process), Cursor Cloud (isolated VMs with persistence), self-hosted (for compliance)
- SDK supports subagents, hooks, skills (repo-specific plugins), MCP server connections, and SSE streaming
- Compatible models include Composer 2 (optimized for coding) and GPT-5.5
- Token-based pricing (input/output tokens)
- Starter projects, CLI tools, and a public "cookbook" available on GitHub

## Timeline

- **April 29, 2026** — Cursor SDK public beta announced ([changelog](https://cursor.com/changelog/sdk-release))
- **April 30, 2026** — Cursor Security Review beta launched for Teams & Enterprise ([changelog](https://cursor.com/changelog/04-30-26))
- **Earlier in April 2026** — CVE-2026-26268 disclosed: high-severity arbitrary code execution via malicious .git hooks triggered by Cursor agents; patched in Cursor v2.5

## Sources

- [Cursor Security Review changelog (Apr 30, 2026)](https://cursor.com/changelog/04-30-26)
- [Cursor SDK changelog (Apr 29, 2026)](https://cursor.com/changelog/sdk-release)
- [MarkTechPost: Cursor Introduces a TypeScript SDK for Building Programmatic Coding Agents](https://www.marktechpost.com/2026/04/29/cursor-introduces-a-typescript-sdk-for-building-programmatic-coding-agents-with-sandboxed-cloud-vms-subagents-hooks-and-token-based-pricing/)
- [Kingy AI: Cursor SDK Review — Cursor's Coding Agent Becomes Programmable Infrastructure](https://kingy.ai/ai/cursor-sdk-review-cursors-coding-agent-becomes-programmable-infrastructure/)
- [FindSkill.ai: Cursor's New Security Reviewer Flags Prompt Injection — 4 Patterns](https://findskill.ai/blog/cursor-security-review-prompt-injection-4-patterns/)
- [Data Hogo: Cursor Code Security Scan 2026 — 50 Repos Analyzed](https://www.datahogo.com/en/blog/cursor-code-security-scan)
- [Endor Labs: Cursor Security — How to Secure AI-Generated Code in 2026](https://www.endorlabs.com/learn/cursor-security)
- [CSO Online: Critical Cursor Bug Could Turn Routine Git into RCE](https://www.csoonline.com/article/4164250/critical-cursor-bug-could-turn-routine-git-into-rce.html)

## Impact / Why It Matters

- **First major IDE to ship always-on AI security agents** — sets a new baseline for what "security built-in" means in developer tools
- **Prompt injection as a first-class vulnerability class** — the Security Reviewer explicitly flags prompt injection patterns, reflecting the new threat landscape created by AI-assisted coding
- **SDK turns Cursor from product to platform** — developers can now embed Cursor-grade coding agents in CI/CD pipelines, internal tools, and SaaS products without reimplementing sandboxing, context management, or orchestration
- **Enterprise signal** — Teams/Enterprise gating suggests Cursor is aggressively pursuing revenue from orgs already adopting AI dev tools at scale
- **Security context is timely** — released days after CVE-2026-26268 patch, signaling Cursor is responding to real exploits with preventive tooling
- **Competitive pressure** — GitHub Copilot, Windsurf, and other AI coding tools will likely need to match this security-agent paradigm
