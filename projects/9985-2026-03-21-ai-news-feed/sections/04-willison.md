## 4. Simon Willison — Defining Agentic Engineering

Simon Willison published five posts in seven days — the most prolific voice this week, and increasingly the practitioner defining the vocabulary for how professionals use AI coding tools.

### Pragmatic Summit Fireside (March 14)
**[simonwillison.net](https://simonwillison.net/2026/Mar/14/pragmatic-summit/#:~:text=tests%20are%20no%20longer%20even%20remotely%20optional)**

Fireside chat at the Pragmatic Summit in San Francisco, hosted by Eric Lui (Statsig). Willison described the stages of AI adoption for developers, from occasional ChatGPT questions to "that moment where the agent writes more code than you do."

On tests:

> "I see people who are writing code with coding agents and they're not writing any tests at all. That's a terrible idea."

> "They're free now. They're effectively free. I think tests are no longer even remotely optional."

On TDD specifically — a revealing admission from someone who resisted it for decades:

> "I hated [test-first TDD] throughout my career" — but getting agents to do it is fine since he doesn't care if the agent spins around for a few minutes.

On security: reiterated the **"lethal trifecta"** — when a model can access private data, is exposed to malicious instructions, and has an exfiltration vector. Now "standard vocabulary among CISOs evaluating AI agents." Top recommendation: sandboxing.

On open source: "agents love open source" — great at recommending libraries and stitching things together. But projects are flooded with junk contributions; people are trying to "convince GitHub to disable pull requests entirely."

### NICAR Workshop — Coding Agents for Data Analysis (March 16)
**[simonwillison.net](https://simonwillison.net/2026/Mar/16/coding-agents-for-data-analysis/) · [Workshop handout](https://simonw.github.io/nicar-2026-coding-agents/)**

Three-hour workshop at NICAR 2026 for data journalists — demonstrating Claude Code and OpenAI Codex for data exploration, analysis, and cleaning. Participants burned **$23** of Codex tokens total. Exercises used Python, SQLite, and Datasette.

Key insight: coding agents aren't just for developers. They can explore data, run statistical summaries, spot outliers, find correlations, scrape websites, and handle JavaScript-rendered pages. Highlight: had Claude Code vibe-code interactive Leaflet heat map visualizations for a trees database.

### GPT-5.4 Mini and Nano (March 17)
**[simonwillison.net](https://simonwillison.net/2026/Mar/17/mini-and-nano/)**

Coverage of OpenAI's new smaller models. GPT-5.4-nano outperforms previous GPT-5 mini at max reasoning effort. New mini is **2x faster** than predecessor. GPT-5.4-nano is cheaper than Gemini 3.1 Flash-Lite. Simon tested by having Codex produce pelican-riding-bicycle SVGs across reasoning effort levels. The nano can describe **76,000 photos for $52**.

### OpenAI/Astral Analysis (March 19)
**[simonwillison.net](https://simonwillison.net/2026/Mar/19/openai-acquiring-astral/)**

Questioned whether it's a talent or product acquisition — Astral's business product (pyx, private PyPI registry) conspicuously absent from announcements. Noted OpenAI's broader acquisition spree: Promptfoo, OpenClaw, Crixet. Flagged that if things go south, it tests "how viable the forking exit strategy really is."

### Turbo Pascal Deconstructed (March 20)
**[simonwillison.net](https://simonwillison.net/2026/Mar/20/turbo-pascal/)**

Had Claude decompile and annotate Borland's 1985 Turbo Pascal 3.02 binary (**39,731 bytes** — a full IDE + compiler). Built an interactive artifact with labeled segments and reconstructed, annotated source code — done in regular claude.ai chat, not Claude Code.

### The Vocabulary Question

Willison's distinction between "agentic engineering" and "vibe coding" is [becoming industry standard](https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/#:~:text=professional%20software%20engineers%20using%20coding%20agents):

- **Vibe coding**: "coding where you pay no attention to the code at all" — the original Karpathy definition
- **Agentic engineering**: "professional software engineers using coding agents to improve and accelerate their work by amplifying their existing expertise"

Addy Osmani's [crisper version](https://addyosmani.com/blog/agentic-engineering/#:~:text=Vibe%20coding%20%3D%20YOLO): "Vibe coding = YOLO. Agentic engineering = AI does the implementation, human owns the architecture, quality, and correctness."

On the one-year anniversary of coining "vibe coding" (Feb 4, 2026), Karpathy himself endorsed this: "my current favorite [alternative term] is agentic engineering."

---
