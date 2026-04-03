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

- **Acquired TBPN** — daily tech talk show hosted by John Coogan and Jordi Hays (April 2). On track for $30M+ revenue in 2026. Reports to Chris Lehane (strategy org). Editorial independence pledged. Sam Altman: *"I don't expect them to go any easier on us."* ([TechCrunch](https://techcrunch.com/2026/04/02/openai-acquires-tbpn-the-buzzy-founder-led-business-talk-show/))
- **Codex-only seats** — New pricing tier for API-focused teams ([TipRanks](https://www.tipranks.com/news/the-fly/ai-daily-openai-acquires-tbpn-rolls-out-codex-only-seats-thefly-news))
- CNBC noted OpenAI's M&A strategy draws questions — the TBPN buy labeled as "[chasing vibes](https://www.cnbc.com/2026/04/03/chasing-vibes-openai-ma-strategy-gets-more-confusing-with-tbpn-.html#:~:text=chasing%20vibes)" by some analysts

### Microsoft

- **Three new in-house AI models** — speech transcription, voice generation, and an upgraded image creator. Signals Microsoft building foundational AI independently, not just relying on OpenAI partnership ([VentureBeat](https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google) — *(403, details from search snippets)*)

### Windsurf

- Completed shift from credit-based to **quota-based pricing** ($20/mo Pro = Cursor parity, $40/seat Teams, $200/mo Max)
- **GPT-5.4 Mini** available at 1x credits
- **Arena Mode** for side-by-side model comparison in the IDE

### OpenClaw

- The agent framework powering Karpathy's Dobby (see [§8](#8-karpathys-psychosis-and-the-agent-first-future))
- Acquired by OpenAI in February — rapidly becoming the de facto persistent agent framework
- Users connecting it to calendars, browsers, email, shopping, files — the "ambient OS" pattern
