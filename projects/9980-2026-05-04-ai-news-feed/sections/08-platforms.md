## 8. Platform Updates — VS Code 1.118, Replit Monitoring, Anthropic Security, Mistral Medium 3.5

**April 28–30 | Multiple sources**

Four platform announcements that each represent a different vector of the agentic evolution.

### VS Code 1.118 (Apr 29)

[Release notes](https://code.visualstudio.com/updates/v1_118)

The most agent-aware VS Code release yet — six features that all serve autonomous workflows:

- **Remote Control** — track and steer ongoing Copilot CLI sessions from GitHub.com or mobile. Start a task on your laptop, monitor from your phone.
- **Codebase Search** — semantic indexing now for all workspaces + org-wide text search across GitHub repos. Agents (and humans) find code faster.
- **Dedicated Context for Skills** — skill execution isolated via `context: fork`; keeps main chat focused while subagents explore separately
- **Chronicle** — SQLite-backed chat history with `/chronicle:standup` and natural language queries. "What did I work on yesterday?" now has an answer.
- **Enterprise Policy** — fail-closed org membership gating for AI features. Admins restrict which organizations can use AI.
- **Token Efficiency** — 93% cache reuse, 20% savings from tool search, 12% faster WebSocket mode for OpenAI. Timed before June 1 usage-based billing.

### Replit App Monitoring (Apr 29)

[Replit Blog](https://replit.com/blog)

Replit closes the build → deploy → **operate** loop:

- Alerts developers via email when published apps go down, with uptime bars and analytics correlation
- One-click **"Investigate downtime with Agent"** — reads production logs + database (read-only sandbox) to pinpoint root cause
- Available on all paid plans for published apps (except Scheduled Deployments)
- Differentiator: Lovable, Bolt, and v0 stop at deploy. Replit now monitors production and debugs it with AI — the first AI-native platform to own the full lifecycle.

### Anthropic Claude Security — Public Beta (Apr 30)

[Anthropic](https://anthropic.com)

Claude Security launched for Enterprise customers (50+ seats):

- Built on **Opus 4.7** — uses LLM reasoning (not pattern-matching) to find complex logic and cross-file vulnerabilities
- Accessible at `claude.ai/security` — no API setup, no CLI; supports scheduled scans, webhooks, CSV/SARIF export
- Found **500+ vulnerabilities** in private preview that existing tools missed for years
- Partners: CrowdStrike, Palo Alto Networks, Microsoft Security, SentinelOne, Wiz
- Competes directly with Snyk and GitHub Advanced Security/CodeQL
- Advantage: deep contextual reasoning across entire codebases. Limitation: less maturity, fewer language-specific rules.

### Mistral Medium 3.5 — Open-Weight Flagship (Apr 29)

[Mistral AI](https://mistral.ai)

The French lab unifies its model lineup into one open-weight flagship:

- **128B dense** parameters — not a mixture-of-experts architecture
- **256k context window**
- **Self-hostable on 4 GPUs** (A100 80GB or equivalent)
- **Modified MIT license** — truly open weights on Hugging Face
- **API pricing:** $1.50/$7.50 per million tokens (input/output) — undercutting both GPT-5.5 ($5/$30) and Opus 4.7 ($5/$25)
- **SWE-Bench:** 77.6% — not frontier-leading but competitive, and you own the weights
- Unifies Mistral's previously fragmented coding, reasoning, and vision models into a single checkpoint

**Why this matters:** At $1.50/$7.50 with open weights, Mistral offers the "good enough and controllable" option for teams who won't pay frontier pricing or can't send code to external APIs. The 4-GPU self-hosting target makes it deployable on a single enterprise node.

---
