## 8. Platform Updates — VS Code 1.118, Replit Monitoring, Anthropic Security, Mistral Medium 3.5

**April 28–30 | Multiple sources**

Four platform announcements that each represent a different vector of the agentic evolution.

### VS Code 1.118 — The "Every Token Counts" Release (Apr 29)

[Release notes](https://code.visualstudio.com/updates/v1_118) · [Visual Studio Magazine](https://visualstudiomagazine.com/articles/2026/04/30/vs-code-curbs-token-use-ahead-of-copilots-controversial-usage-based-billing-switch.aspx)

The most significant VS Code release in the context of [Section 5's billing earthquake](#5-github-copilots-billing-earthquake--from-flat-subscriptions-to-pay-per-token). With usage-based billing arriving June 1, VS Code 1.118 ships an aggressive token efficiency overhaul — explicitly acknowledging the billing change in its release notes. The message is clear: Microsoft is simultaneously raising the price of tokens AND giving you tools to use fewer of them.

**Token Efficiency — The Headline Story**

The release notes open this section by directly citing the April 27 billing announcement. Three major optimizations ship together:

- **93% prompt cache reuse** — strategic cache breakpoints at system prompt, tools list, and last-two-messages boundaries mean repeated context is billed at ~10× lower rates (particularly for Anthropic models). Cache-stable system prompts and tools registration eliminate byte drift that previously reset caches mid-session.
- **Tool search tool (20% token savings)** — splits the agent's toolset into ~30 always-available tools (covering 88% of calls) and deferred tools loaded on-demand via semantic search. Already default for Anthropic models; rolling out for GPT-5.4/5.5 via Responses API.
- **Agentic search + execution tools** — two new specialist small models handle codebase exploration and terminal execution respectively, replacing expensive frontier-model token usage for these tasks. The execution tool filters verbose terminal output before returning to the main agent — no more paying premium tokens to read 500 lines of test output.
- **WebSocket mode (12% faster for OpenAI)** — persistent connection sends only delta input per turn; server retains conversation state. Reduces request size and latency in multi-turn agent workflows.

**Combined impact:** A heavy agentic coding session that might have consumed 200+ credits under naive billing could now cost 40–60% less through caching and delegation alone. This positions VS Code as the "cost-aware IDE" — the billing system penalizes waste, and the editor actively eliminates it.

**Other Key Features**

- **Chronicle (experimental)** — SQLite-backed local index of all chat sessions: metadata, files touched, PRs referenced. Commands: `/chronicle:standup` (24h activity grouped by branch), `/chronicle:tips` (7-day usage analysis for prompt improvement), `/chronicle [query]` (free-form natural language search across history). Your chat history becomes queryable institutional memory.
- **Remote Control** — track and steer ongoing Copilot CLI sessions from GitHub.com or mobile.
- **Dedicated Context for Skills** — skill execution isolated via `context: fork`; subagents explore without polluting main chat context.
- **Enterprise Policy** — fail-closed org membership gating for AI features.

### Replit App Monitoring (Apr 29)

[Replit Blog](https://blog.replit.com/app-monitoring) · [Replit Docs](https://docs.replit.com/updates/2026/05/01/changelog)

Replit closes the build → deploy → **operate** loop:

- Alerts developers via email when published apps go down, with uptime bars and analytics correlation
- One-click **"Investigate downtime with Agent"** — reads production logs + database (read-only sandbox) to pinpoint root cause
- Available on all paid plans for published apps (except Scheduled Deployments)
- Differentiator: Lovable, Bolt, and v0 stop at deploy. Replit now monitors production and debugs it with AI — the first AI-native platform to own the full lifecycle.

### Anthropic Claude Security — Public Beta (Apr 30)

[Claude Blog](https://claude.com/blog/claude-security-public-beta) · [SecurityWeek](https://www.securityweek.com/anthropic-unveils-claude-security-to-counter-ai-powered-exploit-surge/) · [CRN](https://www.crn.com/news/security/2026/anthropic-launches-claude-security-5-things-to-know)

Claude Security launched for all Enterprise customers:

- Built on **Opus 4.7** — uses LLM reasoning (not pattern-matching) to find complex logic and cross-file vulnerabilities
- Accessible at `claude.ai/security` — no API setup, no CLI; supports scheduled scans, webhooks, CSV/SARIF export
- Found **500+ vulnerabilities** in private preview that existing tools missed for years
- Partners: CrowdStrike, Palo Alto Networks, Microsoft Security, SentinelOne, Wiz
- Competes directly with Snyk and GitHub Advanced Security/CodeQL
- Advantage: deep contextual reasoning across entire codebases. Limitation: less maturity, fewer language-specific rules.

### Mistral Medium 3.5 — Open-Weight Flagship (Apr 29)

[Mistral AI](https://mistral.ai) · [MarktechPost](https://www.marktechpost.com/2026/05/02/mistral-ai-launches-remote-agents-in-vibe-and-mistral-medium-3-5-with-77-6-swe-bench-verified-score/) · [DataNorth](https://datanorth.ai/news/mistral-medium-3-5-release)

The French lab unifies its model lineup into one open-weight flagship:

- **128B dense** parameters — not a mixture-of-experts architecture
- **256k context window**
- **Self-hostable on 4 GPUs** (A100 80GB or equivalent)
- **Modified MIT license** — truly open weights on Hugging Face
- **API pricing:** $1.50/$7.50 per million tokens (input/output) — undercutting both GPT-5.5 ($5/$30) and Opus 4.7 ($5/$25)
- **SWE-Bench Verified:** 77.6% — not frontier-leading but competitive, and you own the weights
- Unifies Mistral's previously fragmented coding, reasoning, and vision models into a single checkpoint

**Why this matters:** At $1.50/$7.50 with open weights, Mistral offers the "good enough and controllable" option for teams who won't pay frontier pricing or can't send code to external APIs. The 4-GPU self-hosting target makes it deployable on a single enterprise node.

---
