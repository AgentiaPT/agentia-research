# Research: Karpathy at Sequoia Ascent 2026 — "From Vibe Coding to Agentic Engineering"

## Key Facts

- **Event:** Sequoia AI Ascent 2026, fireside chat with Stephanie Zhan
- **Date:** April 30, 2026 (written summary published same day on karpathy.bearblog.dev)
- **Core thesis:** The programming paradigm has shifted from writing code to orchestrating AI agent teams
- **Software 3.0 framework:**
  - Software 1.0 → humans write explicit code
  - Software 2.0 → humans create data/objectives, neural nets learn the program
  - Software 3.0 → programming via context window engineering (prompts, tools, examples, memory)
- **"Agentic inflection point":** December 2025 — LLMs became reliable enough for "macro" software tasks (whole features, subsystems, test orchestration) without close human supervision
- **Vibe coding vs. agentic engineering:**
  - Vibe coding = anyone builds prototypes by describing intent (raises the floor)
  - Agentic engineering = rigorous discipline for production software; engineers direct AI agents, maintain safety/reliability, exercise "taste" and judgment
- **"Jagged intelligence":** LLMs excel at tasks with verifiable solutions (code, math) but struggle with ill-defined/subjective problems
- **Key quote:** "You can outsource your thinking, but not your understanding"
- **Agent-native economy:** Software infrastructure and documentation being redesigned for AI agents rather than humans
- **MenuGen example:** App "fully engulfed" by LLMs — neural networks generate restaurant food images from prompts, reducing traditional logic to prompt engineering

## AutoResearch (Related Project)

- **Released:** March 2026 (open-sourced on GitHub: karpathy/autoresearch)
- **What:** ~630-line Python framework for autonomous ML experiment iteration
- **How it works:** AI agent modifies training code → trains for 5 min → checks validation metric (bits per byte) → keeps or discards change → loops indefinitely
- **Results:** ~700 experiments in 2 days, discovered ~20 actual improvements, 11% training efficiency gain (GPT-2 training time: 2.02h → 1.80h)
- **Throughput:** ~12 experiments/hour on a single NVIDIA GPU
- **Core files:** `program.md` (human goals), `train.py` (agent-modified), `prepare.py` (immutable setup)
- **Human role:** "Research manager" — edit a Markdown file to define objectives; agent does the iteration
- **Community impact:** Thousands of GitHub stars/forks within days; Shopify CEO Tobi Lutke reported double-digit efficiency gains

## Timeline

| Date | Event |
|------|-------|
| Mar 8, 2026 | AutoResearch open-sourced on GitHub |
| Apr 30, 2026 | Sequoia AI Ascent 2026 fireside chat |
| Apr 30, 2026 | Written summary published on karpathy.bearblog.dev |

## Sources

- Karpathy blog post: https://karpathy.bearblog.dev/sequoia-ascent-2026/
- YouTube talk: https://www.youtube.com/watch?v=96jN2OCOfLs
- VentureBeat coverage: https://venturebeat.com/technology/andrej-karpathys-new-open-source-autoresearch-lets-you-run-hundreds-of-ai
- 12 Lessons analysis: https://philippdubach.com/posts/karpathys-software-3.0-playbook/
- MindStudio 5 Predictions: https://www.mindstudio.ai/blog/karpathy-sequoia-talk-5-predictions-agentic-engineering
- GitHub repo: https://github.com/karpathy/autoresearch
- AutoResearch explainer: https://autoresearch.lol/

## Impact

- **For developers:** Role shift from code writer to agent orchestrator; "if you haven't tried these tools since late 2025, your mental model is already outdated"
- **For industry:** Validates "agentic engineering" as a real discipline, not hype — coming from one of the most respected voices in AI
- **For AI research:** AutoResearch demonstrates that autonomous agent loops can outperform manual researcher iteration for local optimizations
- **Newsletter angle:** Connects vibe coding trend (which Karpathy himself coined) to its mature successor; strong narrative arc from casual→professional AI-assisted development
- **Sequoia signal:** Major VC firm dedicating keynote slot to this thesis signals where investment dollars are flowing (agent-native infrastructure, developer tools)
