## 8. Platform Updates — VS Code 1.118, Replit Monitoring, Anthropic Security, Mistral Medium 3.5

**April 28–30 | Multiple sources**

Four platform announcements representing different vectors of the agentic evolution.

### VS Code 1.118 — The "Every Token Counts" Release (Apr 29)

[Release notes](https://code.visualstudio.com/updates/v1_118) · [Visual Studio Magazine](https://visualstudiomagazine.com/articles/2026/04/30/vs-code-curbs-token-use-ahead-of-copilots-controversial-usage-based-billing-switch.aspx)

The most significant VS Code release in the context of [Section 5's billing earthquake](#5-github-copilots-billing-earthquake--from-flat-subscriptions-to-pay-per-token). With usage-based billing arriving June 1, VS Code 1.118 ships an aggressive token efficiency overhaul — explicitly citing the billing change in its release notes.

**Token Efficiency**

- **93% prompt cache reuse** — strategic cache breakpoints at system prompt, tools list, and last-two-messages boundaries mean repeated context billed at ~10× lower rates. Cache-stable prompts eliminate byte drift that previously reset caches mid-session.
- **Tool search tool (20% token savings)** — splits toolset into ~30 always-available (covering 88% of calls) and deferred tools loaded on-demand via semantic search. Default for Anthropic models; rolling out for GPT-5.4/5.5.
- **Agentic search + execution tools** — specialist small models handle codebase exploration and terminal execution, replacing expensive frontier-model token usage. Execution tool filters verbose output before returning to main agent.
- **WebSocket mode (12% faster for OpenAI)** — persistent connection sends only delta input per turn; server retains conversation state.

**Combined impact:** A heavy agentic session consuming 200+ credits under naive billing could cost 40–60% less through caching and delegation alone.

**Other Key Features**

- **Chronicle (experimental)** — SQLite-backed local index of all chat sessions. Commands: `/chronicle:standup` (24h activity by branch), `/chronicle:tips` (7-day usage analysis), `/chronicle [query]` (natural language search). Chat history becomes queryable institutional memory.
- **Remote Control** — track and steer Copilot CLI sessions from GitHub.com or mobile.
- **Dedicated Context for Skills** — skill execution isolated via `context: fork`; subagents explore without polluting main chat.
- **Enterprise Policy** — fail-closed org membership gating for AI features.

### Replit App Monitoring (Apr 29)

[Replit Blog](https://blog.replit.com/app-monitoring) · [Replit Docs](https://docs.replit.com/updates/2026/05/01/changelog)

Replit closes the build → deploy → **operate** loop:

- Alerts when published apps go down, with uptime bars and analytics correlation
- One-click **"Investigate downtime with Agent"** — reads production logs + database (read-only sandbox) to pinpoint root cause
- Available on all paid plans for published apps (except Scheduled Deployments)
- Lovable, Bolt, and v0 stop at deploy. Replit now monitors production and debugs it with AI — first AI-native platform owning the full lifecycle.

### Anthropic Claude Security — Public Beta (Apr 30)

[Claude Blog](https://claude.com/blog/claude-security-public-beta) · [SecurityWeek](https://www.securityweek.com/anthropic-unveils-claude-security-to-counter-ai-powered-exploit-surge/) · [CRN](https://www.crn.com/news/security/2026/anthropic-launches-claude-security-5-things-to-know)

- Built on **Opus 4.7** — uses LLM reasoning (not pattern-matching) for complex logic and cross-file vulnerabilities
- Accessible at `claude.ai/security` — no API setup; supports scheduled scans, webhooks, CSV/SARIF export
- Found **500+ vulnerabilities** in private preview that existing tools missed for years
- Partners: CrowdStrike, Palo Alto Networks, Microsoft Security, SentinelOne, Wiz
- Competes directly with Snyk and GitHub Advanced Security/CodeQL
- Advantage: deep contextual reasoning across codebases. Limitation: fewer language-specific rules.

### Mistral Medium 3.5 — Open-Weight Flagship (Apr 29)

[Mistral AI](https://mistral.ai) · [MarktechPost](https://www.marktechpost.com/2026/05/02/mistral-ai-launches-remote-agents-in-vibe-and-mistral-medium-3-5-with-77-6-swe-bench-verified-score/) · [DataNorth](https://datanorth.ai/news/mistral-medium-3-5-release)

- **128B dense** parameters (not mixture-of-experts)
- **256k context window**
- **Self-hostable on 4 GPUs** (A100 80GB or equivalent)
- **Modified MIT license** — open weights on Hugging Face
- **API pricing:** $1.50/$7.50 per million tokens — undercutting GPT-5.5 ($5/$30) and Opus 4.7 ($5/$25)
- **SWE-Bench Verified:** 77.6% — competitive, and you own the weights
- Unifies Mistral's previously fragmented coding, reasoning, and vision models into one checkpoint

At $1.50/$7.50 with open weights, Mistral offers the "good enough and controllable" option for teams that won't pay frontier pricing or can't send code to external APIs. The 4-GPU target makes it deployable on a single enterprise node.

---
