## 10. Model & Tool Updates

### Anthropic

- **300K max_tokens** now available on the Message Batches API for Claude Opus 4.6 and Sonnet 4.6 (beta header for long-form generation)
- **1M context window migration**: Anthropic retiring the 1M context beta for Claude Sonnet 4.5 and Sonnet 4 on **April 30, 2026**. Users must migrate to Sonnet 4.6 or Opus 4.6, which support 1M tokens at standard pricing with no beta header
- Claude Code v2.1.88 pulled and re-released after source map leak (see [§2](#2-anthropics-week-from-hell--mythos-claude-code-and-congressional-fire))

### Google

- **Gemma 4** — Four open-weight models (2B, 4B, 26B MoE, 31B Dense) under Apache 2.0 (see [§4](#4-googles-open-model-play--gemma-4-under-apache-20))
- **Gemini 3.1 Pro** — Improved reasoning, rolling out to Pro and Ultra subscribers; available in NotebookLM
- **Gemini 3 Deep Think** — Advanced reasoning mode for Ultra subscribers
- **Gemini in Chrome** — Rolling out on Windows/Mac for Pro and Ultra subscribers (US, English)
- **Gemini on Android Auto** — Public rollout began April 3 for upgraded users

### GitHub

- **Copilot cloud agent** — Research/plan/code workflow (April 1), commit signing (April 3), org runner controls (April 3)
- Rebrand from "coding agent" to "cloud agent" (see [§6](#6-github-copilot-goes-cloud-native))

### OpenAI

- **$122B funding round closed** (March 31) — largest private round in history. $852B valuation. Amazon ($50B, $35B contingent on IPO/AGI milestone), NVIDIA ($30B), SoftBank ($30B). First retail investor participation ($3B). Revenue: $2B/month, 900M weekly active users, 50M subscribers. IPO expected later in 2026 ([TechCrunch](https://techcrunch.com/2026/03/31/openai-not-yet-public-raises-3b-from-retail-investors-in-monster-122b-fund-raise/) · [Bloomberg](https://www.bloomberg.com/news/articles/2026-03-31/openai-valued-at-852-billion-after-completing-122-billion-round))
- **Acquired TBPN** — daily tech talk show (April 2). $30M+ revenue trajectory. Reports to Chris Lehane. Sam Altman: *"I don't expect them to go any easier on us."* ([TechCrunch](https://techcrunch.com/2026/04/02/openai-acquires-tbpn-the-buzzy-founder-led-business-talk-show/))
- **Codex major update** (March 30) — first-class plugin system, multi-agent v2 with path-based agent addressing, pay-as-you-go team pricing (April 2). Plugin architecture positions Codex to compete with Claude Code's extension ecosystem ([OpenAI Changelog](https://developers.openai.com/codex/changelog))
- **Sora shutdown** — App closes April 26, API September 24. Was costing ~$1M/day to operate. Disney's $1B partnership collapsed. Strategic pivot: kill video generation, free compute for coding/enterprise ([TechCrunch](https://techcrunch.com/2026/03/29/why-openai-really-shut-down-sora/))
- CNBC noted M&A strategy draws questions — TBPN buy labeled "[chasing vibes](https://www.cnbc.com/2026/04/03/chasing-vibes-openai-ma-strategy-gets-more-confusing-with-tbpn-.html#:~:text=chasing%20vibes)"

### Microsoft

- **Three new in-house AI models** — speech transcription, voice generation, and an upgraded image creator. Building foundational AI independently ([VentureBeat](https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google) — *(403)*)
- **$10B Japan AI investment** (April 3, 2026–2029) — infrastructure, cybersecurity, partnerships with Sakura Internet, SoftBank, NTT Data, NEC, Fujitsu, Hitachi. Goal: train 1M AI professionals by 2030

### NVIDIA

- **Vera Rubin platform in full production** — next-gen chips entered production ahead of schedule. 10× reduction in inference token cost, 4× fewer GPUs to train MoE models vs. Blackwell. Vera Rubin NVL72: 72 GPUs in a single rack. AWS, Google Cloud, Microsoft, OCI deploying in H2 2026 ([NVIDIA](https://nvidianews.nvidia.com/news/nvidia-vera-rubin-platform))

### Alibaba

- **Qwen 3.6-Plus** (April 2) — hybrid linear-attention + sparse MoE architecture. 1M-token context window. Rivals Claude Opus 4.5 on benchmarks. Native multimodal: generates frontend pages, produces code from screenshots. Priced at ~$0.29/M input tokens — significantly cheaper than Western competitors ([Caixin Global](https://www.caixinglobal.com/2026-04-02/alibaba-releases-qwen-36-plus-ai-model-with-enhanced-coding-capabilities-102430395.html))

### Windsurf

- Completed shift from credit-based to **quota-based pricing** ($20/mo Pro = Cursor parity, $40/seat Teams, $200/mo Max)
- **GPT-5.4 Mini** available at 1x credits
- **Arena Mode** for side-by-side model comparison in the IDE

### OpenClaw

- The agent framework powering Karpathy's Dobby (see [§8](#8-karpathys-psychosis-and-the-agent-first-future))
- Acquired by OpenAI in February — rapidly becoming the de facto persistent agent framework
- Users connecting it to calendars, browsers, email, shopping, files — the "ambient OS" pattern
