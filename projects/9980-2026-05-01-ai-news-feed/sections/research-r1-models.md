# R1: Model Releases & Benchmarks — April 25 to May 1, 2026

## Story: Mistral Medium 3.5 Launches — 128B Dense Open-Weight Flagship with Vibe Coding Agents
- **Date:** 2026-04-29
- **Source:** https://pulse24.ai/news/2026/4/29/23/mistral-ai-ships-medium-35-model
- **Outlet:** Pulse24 / also covered by DEV Community, TestingCatalog, AIHola
- **Key facts:**
  - 128 billion parameter dense model with 256K-token context window
  - Released as open weights under modified MIT license; self-hostable on 4 GPUs
  - Unifies instruction-following, reasoning, and coding into single weight set — replaces Medium 3.1, Magistral, and Devstral 2
  - Configurable reasoning effort per request (chat to deep multi-step)
  - SWE-Bench Verified: 77.6%; τ³-Telecom: 91.4
  - API pricing: $1.50/M input tokens, $7.50/M output tokens
  - Simultaneously launched **Vibe** remote coding agents — asynchronous parallel coding sessions from CLI or Le Chat
  - New "Work mode" in Le Chat for complex multi-step productivity tasks
- **Why it matters:** Largest open-weight dense model at launch; unifies Mistral's fragmented model lineup into a single flagship and adds agentic coding to compete with Codex/Claude Code.
- **Confidence:** high

## Story: Anthropic Ships 9 Claude Connectors for Creative Tools
- **Date:** 2026-04-28
- **Source:** https://9to5mac.com/2026/04/28/anthropic-releases-9-new-claude-connectors-for-creative-tools-including-blender-and-adobe/
- **Outlet:** 9to5Mac / Anthropic release notes
- **Key facts:**
  - Nine new Claude connectors released: Blender, Adobe Creative Cloud, Affinity (Canva), Ableton, Autodesk Fusion, SketchUp, Resolume, Splice, and one other creative tool
  - Enable Claude to automate workflows, manage 3D models, batch-process images, troubleshoot setups via native app APIs
  - Available in Claude Desktop (macOS + Windows) and API integrations for enterprise
  - No new base model — these extend Opus 4.7's capabilities into creative domains
- **Why it matters:** Expands Claude's agentic surface beyond coding into creative-professional workflows; signals Anthropic's push toward tool-use ecosystem lock-in.
- **Confidence:** high

## Story: Claude Opus 4.7 Reaches 83.5% on SWE-bench Verified — New Coding Benchmark Record
- **Date:** 2026-04-27 (leaderboard update)
- **Source:** https://www.buildfastwithai.com/blogs/best-ai-models-leaderboard-april-2026-updated
- **Outlet:** BuildFastWithAI / LMCouncil / DataLearnerAI
- **Key facts:**
  - Claude Opus 4.7 scored 83.5% on SWE-bench Verified — new #1, surpassing GPT-5.4 (76.9%) and Gemini 3.1 Pro (75.6%)
  - Also leads LM Arena / Chatbot Arena at 1503 Elo (thinking mode)
  - GPT-5.5 took #1 on Artificial Analysis Intelligence Index at 60 (composite)
  - GPT-5.5 scored 85% on ARC-AGI 2 (visual reasoning)
  - No single model dominates all benchmarks — task-dependent era
- **Why it matters:** Confirms Opus 4.7 as the coding SOTA while GPT-5.5 leads on composite/reasoning — benchmark fragmentation makes "best model" claims nuanced.
- **Confidence:** med (exact date of leaderboard update uncertain; scores confirmed by multiple aggregator sites as of late April)

## Story: Google Shuts Down Gemini Robotics 1.5 Preview, Directs to 1.6
- **Date:** 2026-04-30
- **Source:** https://ai.google.dev/gemini-api/docs/changelog
- **Outlet:** Google AI for Developers (changelog)
- **Key facts:**
  - gemini-robotics-er-1.5-preview officially shut down April 30
  - Users directed to gemini-robotics-er-1.6-preview with improved spatial and reasoning capabilities for robotics tasks
  - Part of ongoing deprecation cycle for older Gemini preview models
- **Why it matters:** Signals Google's rapid iteration on embodied-AI models; 1.6 preview is now the baseline for robotics developers.
- **Confidence:** high

## Story: Gemini App Adds Chat-Based File Generation (PDF, Word, Excel, Slides)
- **Date:** 2026-04-29 (approx., "late April")
- **Source:** https://releasebot.io/updates/google/gemini
- **Outlet:** Releasebot / af.net
- **Key facts:**
  - Gemini chat interface now generates and exports PDFs, Word, Excel, Google Docs, Sheets, and Slides directly
  - Consumer-facing feature across Gemini app
  - Alongside: Google TV Gemini features for image/video generation and "Remix" function
- **Why it matters:** Moves Gemini from chat-only to direct document-output tool; competes with ChatGPT's Canvas and Claude's Artifacts.
- **Confidence:** med (exact date given as "late April" by aggregator; no precise day confirmed)

## Story: DeepSeek V4 Open-Source Adoption Wave — Benchmarks Confirm Top-3 Open Model
- **Date:** 2026-04-25 to 2026-04-30 (post-release adoption period)
- **Source:** https://felloai.com/deepseek-v4/
- **Outlet:** FelloAI / Codersera / MIT Technology Review / ABC News
- **Key facts:**
  - V4-Pro: 1.6T total params, 49B active; V4-Flash: 284B total, 13B active — both 1M context
  - Released under Apache 2.0/MIT on Hugging Face (April 24 was release day)
  - Cost: ~1/20th of Claude Opus 4.7 for comparable workloads
  - On code/reasoning leaderboards, V4-Pro entered top 3 among open models — just below GPT-5.5
  - Deprecation: deepseek-chat/deepseek-reasoner routes to V4-Flash until July 24 retirement
  - Huawei Ascend + Nvidia support confirmed
  - Previous edition covered the "preview" announcement; this week the open-source weights shipped and community benchmarking validated claims
- **Why it matters:** With Apache 2.0 licensing and 1/20th the cost of Western frontier models, V4 resets the price-performance floor for self-hosted enterprise AI.
- **Confidence:** med (release itself was April 24 — covered last week as "preview"; the open-weight availability and independent benchmarks are the new April 25+ developments)

---

## 403 / Paywalled

- https://pulse24.ai/news/2026/4/29/23/mistral-ai-ships-medium-35-model — connection refused
- https://9to5mac.com/2026/04/28/anthropic-releases-9-new-claude-connectors-for-creative-tools-including-blender-and-adobe/ — fetch failed
- https://dev.to/techsifted/mistral-medium-35-review-a-128b-open-weight-model-with-a-coding-agent-that-opens-prs-for-you-5a0i — fetch failed
- https://ai.google.dev/gemini-api/docs/changelog — fetch failed

All key facts were confirmed via multiple corroborating web search results despite individual page fetch failures.

---

## Out-of-window items dropped

| Item | Date | Reason |
|------|------|--------|
| GPT-5.5 launch | April 23 | Previous edition |
| DeepSeek V4 preview announcement | April 24 | Previous edition (open-source wave is new) |
| Claude Opus 4.7 release | April 16 | Previous edition |
| Qwen 3.6-27B | April 22 | Previous edition |
| Qwen 3.6-Max-Preview | April 20 | Out of window |
| Kimi K2.6 release | April 20 | Out of window |
| Gemma 4 release | April 2 | Out of window |
| Meta Llama 5 release | April 8 | Out of window |
| Cohere-Aleph Alpha merger announcement | April 24 | One day before window |
| Cohere Transcribe ASR model | March 31 | Out of window |
| Cohere legacy model retirements | April 4 | Out of window |
| Gemini Deep Research agent previews | April 21 | Out of window |
| Gemini Embedding-2 GA | April 22 | Out of window |

---

## Search queries used

1. `OpenAI new model release April 2026`
2. `Anthropic Claude model update April 28 29 30 2026`
3. `Google Gemini model release April 25-May 1 2026`
4. `Meta Llama new model release April 2026`
5. `Mistral AI model release late April 2026`
6. `DeepSeek model update April 25 26 27 28 29 30 2026`
7. `Qwen model release April 25-May 1 2026`
8. `AI model benchmark leaderboard results April 28 29 30 May 1 2026`
9. `Cohere AI model release April 2026`
10. `"Kimi K2.6" OR "GLM-5" OR "MiniMax" model release April 2026`
11. `Gemma 4 Google release April 2026`
12. `Cohere Aleph Alpha merger announcement date April 2026`
13. `Qwen 3.6 Max-Preview release date late April 2026`
