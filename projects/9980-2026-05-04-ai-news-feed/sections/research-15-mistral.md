# Research: Mistral Ships Medium 3.5 as Open-Weight Flagship

## Key Facts

- **Model**: Mistral Medium 3.5 — 128 billion parameter **dense** transformer (not MoE; every parameter active on every forward pass)
- **Context window**: 256,000 tokens
- **Multimodal**: Text + vision; vision encoder trained from scratch for variable image sizes/aspect ratios
- **Configurable reasoning**: Adjustable reasoning effort per request (fast chat → extended agentic processing)
- **Self-hosting**: Runs on as few as **four high-end GPUs**; weights downloadable from Hugging Face (`mistralai/Mistral-Medium-3.5-128B`)
- **License**: Modified MIT — allows commercial and non-commercial use; enterprises above a revenue threshold may require a commercial agreement with Mistral
- **API pricing**: **$1.50 / M input tokens**, **$7.50 / M output tokens**
- **Unifies three product lines**: Merges previous Devstral 2 (coding), Magistral (reasoning), and vision capabilities into a single checkpoint
- **Speculative decoding**: EAGLE variant available for low-latency inference
- **Languages**: Dozens supported with robust system prompt adherence

## Benchmarks

| Benchmark | Score | Context |
|-----------|-------|---------|
| SWE-Bench Verified | **77.6%** | Near Claude Sonnet 4.6 (79.6%); ahead of Qwen 3.5 397B & DeepSeek V4 Flash (~76%) |
| τ³-Telecom (agentic tool-use) | **91.4%** | Top-tier agentic task performance |
| MMLU (estimated) | ~78–79% | Comparable to Mistral Large 2; below closed-source SOTA (>91%) |
| HumanEval (estimated) | ~88–92% | Strong but trails GPT-5 (95%) and Claude 3.5 Sonnet (93.7%) |

**Positioning**: Best-in-class among open-weight models for code reasoning and agentic tasks; competitive with but slightly below absolute frontier closed-source models.

## Timeline

- **April 29, 2026** — Official release announced on Mistral AI blog
- **April 29, 2026** — Weights published on Hugging Face under modified MIT license
- **April 29, 2026** — Becomes default model in Le Chat workspace (Work mode) and powers "remote agents" in Vibe product
- **Week of April 28** — Falls within the newsletter coverage window (April 25–May 1, 2026)

## Sources

- Mistral AI official blog: [Remote agents in Vibe. Powered by Mistral Medium 3.5](https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5)
- Mistral AI docs model card: [Mistral Medium 3.5](https://docs.mistral.ai/models/model-cards/mistral-medium-3-5-26-04)
- Hugging Face model page: [mistralai/Mistral-Medium-3.5-128B](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B)
- Mistral AI changelog: [docs.mistral.ai/resources/changelogs](https://docs.mistral.ai/resources/changelogs)
- Third-party guide: [Mistral Medium 3.5 Complete Guide](https://www.aimadetools.com/blog/mistral-medium-3-5-complete-guide/)
- Dev.to review: [Mistral Medium 3.5 Review](https://dev.to/techsifted/mistral-medium-35-review-a-128b-open-weight-model-with-a-coding-agent-that-opens-prs-for-you-5a0i)

## Impact

- **Open-weight milestone**: Largest openly licensed dense model at release — gives enterprises a self-hostable alternative to closed APIs for agentic/coding workloads
- **Consolidation play**: Merging coding + reasoning + vision into one checkpoint simplifies Mistral's product line and deployment story
- **Competitive pressure**: At $1.50/$7.50 per M tokens, undercuts many proprietary APIs while offering full self-hosting freedom
- **Enterprise relevance**: Four-GPU deployability lowers the hardware bar significantly vs. MoE models requiring larger clusters
- **Agentic AI trend**: Designed explicitly for multi-step autonomous workflows — reflects the broader industry shift toward AI agents over simple chat
- **European AI leadership**: Reinforces Mistral (Paris-based) as the leading European AI lab shipping frontier-class open models
