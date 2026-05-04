## 10. Model & Tool Updates

A condensed tracker of model releases, capability jumps, and developer tool updates from the past week. Organized by category for quick scanning.

### Models

- **Mistral Medium 3.5** — 128B dense parameters; scores 77.6% on SWE-Bench Verified. Notably strong at agentic coding tasks with the new "Vibe agents" capability that allows multi-step tool use without explicit orchestration. First dense model to compete with larger MoE architectures on coding benchmarks. (Cross-ref §4: Agentic Coding)

- **Claude Opus 4.7** — New coding SOTA at 83.5% SWE-Bench Verified; 1503 Elo on LM Arena (first model above 1500). Represents the current ceiling for single-model coding performance. Extended thinking and parallel tool use improvements drive the benchmark gains.

- **GPT-5.5** — Leads ARC-AGI 2 benchmark at 85%; tops Artificial Analysis composite index at 60. OpenAI's positioning as a reasoning-first model rather than a coding-first model—a strategic differentiation from Opus 4.7's coding focus.

- **DeepSeek V4** — Open weights shipped under Apache 2.0. Three variants: V4-Pro (1.6T total / 49B active parameters), V4-Flash (284B total / 13B active), and base V4. Running cost approximately 1/20th of Opus at comparable quality tiers. The open-weight release continues DeepSeek's pattern of commoditizing frontier capabilities within months of closed-model releases.

- **Gemini Robotics 1.5→1.6** — Transition announced Apr 30. The 1.6 update focuses on physical world grounding and multi-modal action planning. Part of Google's broader physical AI push alongside the Aluminum OS rumors (§12).

- **Gemini Chat-Based File Generation** — New capability allowing Gemini to generate complete documents (PDF, Word, Excel, Slides) directly in conversation. Positions Gemini as a productivity tool competing with Microsoft Copilot's Office integration.

### Developer Tools

- **Claude Code v2.1.126** — Project purge command (clean up stale context), OAuth support for enterprise SSO, and PowerShell 7 compatibility. Incremental but meaningful quality-of-life improvements for daily users.

- **Cursor SDK Public Beta + v3.2.16** — The SDK allows developers to build and deploy custom coding agents using Cursor's infrastructure. v3.2.16 adds Security Agents that scan code changes in real-time for vulnerability patterns. The SDK is the bigger story: coding agents as deployable infrastructure (§12).

- **GitHub Copilot VS Cloud Agent + Debugger Agent** — Two new agent types: Cloud Agent runs in GitHub's cloud for CI/CD-integrated coding tasks; Debugger Agent attaches to running processes to diagnose issues interactively. Expands Copilot from suggestion engine to active development participant.

### Platform

- **Anthropic Claude Connectors (9 new)** — Integrations with Blender, Adobe Creative Suite, Figma, Unity, Unreal Engine, and four others. Extends Claude's reach beyond text-and-code into creative and 3D workflows. Each connector provides domain-specific tool schemas.

- **Google Managed MCP Servers GA** — 50+ managed Model Context Protocol servers now generally available. Covers databases, APIs, cloud services, and development tools. Reduces the barrier to MCP adoption from "run your own server" to "configure and connect." Significant for enterprise adoption velocity.

- **Claude Security Public Beta** — Dedicated security analysis mode providing vulnerability scanning, threat modeling, and compliance checking. Positioned against dedicated AppSec tools (Snyk, Semgrep) rather than general coding assistants.
