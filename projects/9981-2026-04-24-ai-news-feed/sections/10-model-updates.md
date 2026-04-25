## 10. Model & Tool Updates

### Models

- **GPT-5.5** (OpenAI, Apr 23) — 1M-token context, TerminalBench 2.0: **82.7%**, SWE-Bench Pro: **58.6%**, ARC-AGI 2: **85%**, GDPval: **84.9%**. API: $5/$30 per 1M tokens (2× GPT-5.4) — [OpenAI](https://openai.com/index/introducing-gpt-5-5/)
- **DeepSeek V4** (Apr 24) — 1.6T-param MoE (49B active), Huawei Ascend. LiveCodeBench **93.5**, MMLU-Pro **87.5**. V4-Flash **$0.14/M** · V4-Pro **$1.74/M** — [CNBC](https://www.cnbc.com/2026/04/24/deepseek-v4-llm-preview-open-source-ai-competition-china.html)
- **Qwen 3.6-27B** (Alibaba, Apr 22) — Dense open-weight, multimodal (text+vision), GGUF for llama.cpp. Qwen 3.6-Max-Preview (API) also launched — [MarkTechPost](https://www.marktechpost.com/2026/04/22/alibaba-qwen-team-releases-qwen3-6-27b-a-dense-open-weight-model-outperforming-397b-moe-on-agentic-coding-benchmarks/)
- **ChatGPT Images 2.0 / gpt-image-2** (OpenAI, Apr 21) — First image model with "Thinking Mode" reasoning before rendering. 2K resolution, batch up to 10 images, near-perfect multilingual text rendering (CJK, Indic, Cyrillic). API "gpt-image-2" available at launch. DALL·E 2 and DALL·E 3 retired May 12 — [The New Stack](https://thenewstack.io/chatgpt-images-20-openai/#:~:text=ChatGPT%20Images%202.0) · [Neurohive](https://neurohive.io/en/news/chatgpt-images-2-0-openai-launches-image-generation-model-with-reasoning-2k-resolution-and-multilingual-text/)
- **Chatbot Arena** (Apr 23–24) — Claude Opus 4.7 Thinking holds **#1 overall** (~1503 Elo). GPT-5.5 leads ARC-AGI 2. Top-6 gap: ~11 Elo — [Arena AI](https://arena.ai/leaderboard/text)

### Tools & Platforms

- **Claude Design** (Anthropic, Apr 17) — AI design companion powered by Opus 4.7 vision. Creates prototypes, decks, exports to Figma/Canva/PDF — [Anthropic](https://www.anthropic.com/news/claude-design-anthropic-labs)
- **Claude Cowork Live Artifacts** (Apr 20) — Persistent auto-refreshing dashboards. Connects Asana, Notion, Salesforce, Sheets, Slack, Gmail — [Claude Support](https://support.claude.com/en/articles/14729249-use-live-artifacts-in-claude-cowork)
- **Claude Opus 4.7 on GitHub Copilot** (Apr 16) — Replaces Opus 4.5/4.6 in Pro+ model picker. **7.5× premium request multiplier** (promotional until Apr 30). Opus 4.5/4.6 permanently retired from Copilot — [GitHub Changelog](https://github.blog/changelog/2026-04-16-claude-opus-4-7-is-generally-available/#:~:text=Claude%20Opus%204.7%20is%20generally%20available)
- **Cursor 3** (Apr 2) — Agents Window, cloud-to-local handoff, Design Mode, Composer 2 (built on Kimi K2.5 + Cursor continued pretraining/RL). BugBot at 70%+ resolution rate — [Cursor Blog](https://cursor.com/blog/cursor-3)
- **OpenAI Workspace Agents** (Apr 22) — Codex-powered persistent agents replacing GPTs for enterprise. Integrate Slack, Salesforce, Google Drive, Notion, Microsoft apps. Self-scheduling with persistent memory. Free until May 6, then credit-based — [OpenAI](https://openai.com/index/introducing-workspace-agents-in-chatgpt/) · [VentureBeat](https://venturebeat.com/orchestration/openai-unveils-workspace-agents-a-successor-to-custom-gpts-for-enterprises-that-can-plug-directly-into-slack-salesforce-and-more/)
- **Google Cloud Next '26** (Apr 22) — **$750M partner fund** for agentic AI. Agent Developer Kit (ADK) v1.0 with DAG-based orchestration. Agent Studio (low-code), Agent Registry, Agent Marketplace. **Workspace MCP Server** (preview). **TPU 8t/8i** (training/inference split). **Gemini Enterprise Agent Platform** replaces Vertex AI + Agentspace. Apple confirmed as preferred cloud provider for Gemini-powered Siri — [Google Cloud Blog](https://cloud.google.com/blog/topics/google-cloud-next/welcome-to-google-cloud-next26) · [MacRumors](https://www.macrumors.com/2026/04/22/google-gemini-powered-siri-2026/)
- **GitHub Copilot for Jira** (Apr 22) — Enhanced triggers and controls for Copilot from Jira tickets — Jira-driven issue-to-PR automation — [GitHub Blog](https://github.blog/changelog/2026-04-22-github-copilot-for-jira-our-latest-enhancements/)
- **Cohere SDK** on Oracle Cloud (Apr 20) — Command A, Command R, Embed, Rerank natively integrated with OCI Generative AI — [Oracle Blog](https://blogs.oracle.com/ai-and-datascience/cohere-sdk-is-now-natively-integrated-with-oci-ai)

### GitHub Copilot Policy Week (Apr 17–24)

A pivotal week for Copilot's commercial model:

- **Apr 17** — CLI gets auto model selection across all plans (10% usage multiplier discount) — [GitHub Changelog](https://github.blog/changelog/2026-04-17-github-copilot-cli-now-supports-copilot-auto-model-selection/)
- **Apr 20** — Paused new Pro/Pro+/Student signups; Pro+ gets **5× higher limits** than Pro; Opus models move to Pro+ only. Reason: compute costs from agentic workflows — [GitHub Blog](https://github.blog/news-insights/company-news/changes-to-github-copilot-individual-plans/) · [GitHub Community Discussion](https://github.com/orgs/community/discussions/192963)
- **Apr 22** — Public preview of **C++ Language Server** in Copilot CLI — [GitHub Changelog](https://github.blog/changelog/2026-04-22-c-code-intelligence-for-github-copilot-cli-in-public-preview/)
- **Apr 22** — Copilot Cloud Agent gets **Plan Mode** (shows plan before making changes) and **Research Mode** (broad codebase questions) — [GitHub Docs](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/research-plan-iterate)
- **Apr 24 (effective)** — GitHub will use interaction data from **Free/Pro/Pro+ users to train AI models** — opted in by default, opt-out available in settings; Business/Enterprise exempt — [InfoQ](https://www.infoq.com/news/2026/04/github-copilot-training-data/)
- **Token-based billing coming June 2026** — Per leaked documents, Microsoft plans to move **all Copilot subscribers** to token-based billing: Business $19→$30 pooled credits, Enterprise $39→$70 pooled credits (promotional rates) — [Where's Your Ed At](https://www.wheresyoured.at/exclusive-microsoft-moving-all-github-copilot-subscribers-to-token-based-billing-in-june/)
