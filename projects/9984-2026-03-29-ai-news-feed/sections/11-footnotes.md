## 11. Model & Tool Updates — Footnotes

### OpenAI Shuts Down Sora
**March 24 | [TechCrunch](https://techcrunch.com/2026/03/24/openais-sora-was-the-creepiest-app-on-your-phone-now-its-shutting-down/) · [CNN](https://edition.cnn.com/2026/03/24/tech/openai-sora-video-app-shutting-down) · [CNBC](https://www.cnbc.com/2026/03/24/openai-shutters-short-form-video-app-sora-as-company-reels-in-costs.html) · [Variety](https://variety.com/2026/digital/news/openai-shutting-down-sora-video-disney-1236698277/)**

Sam Altman announced the shutdown of Sora, just six months after launch. The numbers: **$15 million/day** in inference costs against only **$2.1 million in total lifetime revenue**. Disney, which had signed a three-year deal and committed **$1 billion** to OpenAI, terminated its partnership. Compute redirected toward robotics and the mysterious successor codenamed **"Spud."** Multiple competitors (Runway Gen-4, Kling 3.0, Google Veo 3.1) had already matched or exceeded Sora's quality.

### JetBrains 2026.1 — The Agentic IDE Wave
**March 26 | [JetBrains Blog](https://blog.jetbrains.com/idea/2026/03/intellij-idea-2026-1/) · [DevClass](https://www.devclass.com/ai-ml/2026/03/26/jetbrains-shifts-to-agentic-dev-with-central-retires-pair-programming/5211637)**

JetBrains shipped 2026.1 across IntelliJ IDEA, GoLand, CLion, and other IDEs with a major theme: **open AI agent integration**.

- **Agent Client Protocol (ACP)** support — Cursor, Copilot, Codex, Claude Agent, and dozens of external agents now work natively via one-click install from the new ACP Registry
- **Junie CLI** (Beta) — LLM-agnostic coding agent usable from terminal, any IDE, CI/CD, and GitHub/GitLab
- **BYOK** (Bring Your Own Key) — connect personal OpenAI or Anthropic accounts without a JetBrains AI subscription
- **Code With Me sunset** — 2026.1 is the last version to support the human pair programming feature, as JetBrains shifts fully to agentic development with its upcoming **"Central"** platform

The Code With Me sunset is symbolically loaded: JetBrains is retiring its *human* pair programming tool to make room for *agent* pair programming. The transition from human-to-human collaboration to human-to-agent collaboration is now explicit in product strategy.

### AI Bots Surpass Human Internet Traffic
**March 26 | [CNBC](https://www.cnbc.com/2026/03/26/ai-bots-humans-internet.html) · [TechCrunch](https://techcrunch.com/2026/03/19/online-bot-traffic-will-exceed-human-traffic-by-2027-cloudflare-ceo-says/)**

HUMAN Security's State of AI Traffic report confirmed automated traffic has officially eclipsed human users. Key numbers: automated traffic grew **23.5% YoY** vs. 3.1% for humans. AI agent traffic exploded **7,851%**. LLM traffic (ChatGPT, Claude, Gemini) grew **187%** in 2025. Cloudflare CEO Matthew Prince predicted bot traffic will exceed human traffic by 2027 — it arrived early.

### Google Gemini — Chat History Import & Free Code Assist
**March 26 | [Bloomberg](https://www.bloomberg.com/news/articles/2026-03-26/google-gemini-adds-tool-to-make-it-easier-to-switch-from-chatgpt) · [Google Blog](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-code-assist-free/)**

Google released tools letting Gemini users upload chat history from ChatGPT and Claude — a direct play to capture switchers. Separately, **Gemini Code Assist became fully free** for individual developers with **180,000 code completions/month** (vs. typical 2,000 on free tiers), working across VS Code, JetBrains, and Android Studio.

### Cursor
**[Fortune](https://fortune.com/2026/03/21/cursor-ceo-michael-truell-ai-coding-claude-anthropic-venture-capital/) · [WinBuzzer](https://winbuzzer.com/2026/03/20/cursor-unveils-composer-2-for-cheaper-ai-coding-xcxwbn/)**

- **Composer 2 model** (March 20) — Cursor's own AI model for multi-file edits, priced below rivals
- **Self-hosted cloud agents** (March 25) — code, build outputs, and secrets stay on internal machines
- **Bugbot Autofix** — graduated from reviewer to fixer, **35%+ of suggestions merged**
- **$2B annualized revenue** (Feb 2026), doubling from $1B in 3 months. 2M+ total users, 1M+ paying

### Windsurf
**[Windsurf Changelog](https://windsurf.com/changelog)**

- Now owned by **Cognition AI** after ~$250M acquisition (Dec 2025)
- **Pricing change** (March 19) — credit-based to quota-based billing with daily/weekly refresh limits, triggering significant user backlash
- 1M+ active users, 70M+ lines of AI-written code daily

### Model Releases
- **Mistral Voxtral TTS** (March 26) — open-source text-to-speech, 9 languages, small enough for a smartwatch — [TechCrunch](https://techcrunch.com/2026/03/26/mistral-releases-a-new-open-source-model-for-speech-generation/)
- **NVIDIA Nemotron 3** — open-weight leader at 60.47% SWE-bench Verified — [NVIDIA](https://nvidianews.nvidia.com/news/nvidia-debuts-nemotron-3-family-of-open-models)
- **Xiaomi MiMo-V2-Pro** — 1T parameters, 1M context, agent-focused
- **Alibaba Qwen 3.5 Small** — 9B model scores 81.7 on GPQA Diamond, Apache 2.0

### Copilot Updates
- **Agentic Code Review** (March 5) — full project context analysis, auto-generates fix PRs
- **Coding agent** starts 50% faster, adds semantic code search
- **Student plan** updated (March 13) with new model lineup
- **CLI v1.0.12** (March 26) — lower memory, `/undo` command, multi-session support

### Claude Code Rate Limit Controversy
**March 26 | [MacRumors](https://www.macrumors.com/2026/03/26/claude-code-users-rapid-rate-limit-drain-bug/)**

Users flooded GitHub and Reddit reporting sessions burning out in minutes instead of hours. Anthropic confirmed they were **"adjusting 5-hour session limits during peak hours."** The rate limit controversy coincided with the Auto Mode launch, creating a perception gap: Anthropic shipped autonomous capabilities while simultaneously throttling the resources needed to use them.

### Policy
- **White House National AI Policy Framework** (March 20) — 7 pillars, federal preemption of state laws, industry-led standards — [White House](https://www.whitehouse.gov/wp-content/uploads/2026/03/03.20.26-National-Policy-Framework-for-Artificial-Intelligence-Legislative-Recommendations.pdf)
- **EU AI Act** — Council agreed March 13 to streamline rules, extending high-risk AI timeline by 16 months — [EU Council](https://www.consilium.europa.eu/en/press/press-releases/2026/03/13/council-agrees-position-to-streamline-rules-on-artificial-intelligence/)
