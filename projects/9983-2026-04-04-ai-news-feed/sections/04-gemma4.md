## 4. Google's Open Model Play — Gemma 4 Under Apache 2.0

**April 2 | [Google Blog](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/) · [Engadget](https://www.engadget.com/ai/google-releases-gemma-4-a-family-of-open-models-built-off-of-gemini-3-160000332.html) · [tbreak](https://tbreak.com/google-gemma-4-ai-model-launched/) · [Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/gemma-4-available-on-google-cloud)**

While Anthropic was firefighting leaks, Google shipped the most significant open model release of 2026.

### The Gemma 4 Family

Google introduced **Gemma 4** on April 2 — four open-weight models built on the Gemini 3 architecture, purpose-built for advanced reasoning and agentic workflows:

| Model | Parameters | Target |
|---|---|---|
| Gemma 4 2B Effective | 2B active | Smartphones, edge devices |
| Gemma 4 4B Effective | 4B active | Smartphones, edge devices |
| Gemma 4 26B MoE | 26B (Mixture of Experts) | Workstations |
| Gemma 4 31B Dense | 31B | Workstations, servers |

Key capabilities:
- **256K context window**
- **Native vision and audio processing**
- Fluency in **140+ languages**
- Native function calling for agentic workflows

### Performance That Punches Up

The 31B Dense model claimed **#3 on Arena AI's text leaderboard**, beating models 20× its size. The 26B MoE variant took **#6**. For on-device and local deployment, this is unprecedented — workstation-class models competing with cloud-scale systems.

### The License Shift

Previous Gemma releases used a restricted license. Gemma 4 ships under **Apache 2.0** — the most commercially permissive open-source license available. This is a strategic signal: Google is betting that broad adoption of its model architecture matters more than licensing revenue, and it positions Gemma as the default choice for developers who want open weights without legal ambiguity.

Google also launched the **Gemma 4 Good Hackathon** on Kaggle, targeting applications for communities with limited internet access and strong privacy requirements.

### Gemini 3.1 Pro

Alongside Gemma 4, Google rolled out **Gemini 3.1 Pro** with improved reasoning capabilities, available to AI Pro and Ultra subscribers. **Gemini 3 Deep Think** — the most advanced reasoning mode — is now available for Ultra subscribers. Google also expanded **Gemini in Chrome** (Windows/Mac) and pushed **Gemini to Android Auto** on April 3.

### Why This Matters

Gemma 4 under Apache 2.0 is Google's clearest statement yet that the open model race is one it intends to win. With on-device models that rival cloud models from a year ago, the "you need an API for good AI" assumption continues to erode. For software engineers, it means local AI tooling that works offline and keeps code private is no longer a compromise — it's increasingly the better option.
