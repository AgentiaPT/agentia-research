## 5. The Specification Revolution — When Specs Matter More Than Code

Multiple independent sources converged this week on the same thesis: specification quality is now the highest-leverage engineering artifact. When agents are the primary consumers of specs, precision accelerates rather than slows delivery.

### Osmani: "Stop Using /init for AGENTS.md" (March 14)
**[addyosmani.com](https://addyosmani.com/blog/agents-md/#:~:text=auto-generated%20AGENTS.md%20files%20hurt%20agent%20performance)**

Research shows auto-generated AGENTS.md files hurt agent performance and inflate costs by **20%+** — they duplicate what agents can already discover. Two papers published in early 2026 suggest the `/init` ritual may have made agents "slower, more expensive, and no more accurate."

The ACE framework (Agentic Context Engineering, ICLR 2026) outperforms static approaches by **10.6%** on agent benchmarks and **8.6%** on domain-specific tasks. Good mental model: treat AGENTS.md as a living list of codebase smells you haven't fixed yet. Human-written files help only when they contain non-discoverable information. Everything else is noise.

### Debois: "Context Is the New Code" (March 16–18, QCon London)
**[QCon London](https://qconlondon.com/presentation/mar2026/context-new-code) · [jedi.be](https://jedi.be/blog/2026/context-flywheel/#:~:text=Models%20commoditize)**

Patrick Debois — the person who coined "DevOps" — argues that context deserves the same engineering rigor as code:

> "We spent two decades building rigorous lifecycles around code. Now look at how we treat the context that drives AI coding agents: rules files copy-pasted from blog posts, prompts edited by hand, memory nobody audits. We're in the cowboy coding era of context."

He introduces the **Context Development Lifecycle** (Generate, Evaluate, Distribute, Observe) and the **Context Flywheel**: better context → better agent output → better signals → better context. Each cycle compounds.

> "Models commoditize... Tools converge... What doesn't commoditize: institutional context."

### Garg: Context Anchoring (March 17, martinfowler.com)
**[martinfowler.com](https://martinfowler.com/articles/reduce-friction-ai/context-anchoring.html)**

Rahul Garg (Principal Engineer, Thoughtworks) introduces **Context Anchoring** — maintaining a living document that captures decisions, constraints, and current state as a feature evolves. The problem it addresses: AI forgets decisions made early in conversations, leading to contradictions. Part of the [Patterns for Reducing Friction in AI-Assisted Development](https://martinfowler.com/articles/reduce-friction-ai/) series.

### Eledath: 8 Levels of Agentic Engineering (March 10, amplified March 16)
**[bassimeledath.com](https://www.bassimeledath.com/blog/levels-of-agentic-engineering#:~:text=AI%E2%80%99s%20coding%20ability%20is%20outpacing) · [Fowler (Mar 16)](https://martinfowler.com/fragments/2026-03-16.html)**

Bassim Eledath's framework: Tab Complete → Agent IDE → Context Engineering → Compounding Engineering → MCP and Skills → Harness Engineering → Background Agents → Autonomous Agent Teams. Core thesis:

> "AI's coding ability is outpacing our ability to wield it effectively, which is why SWE-bench score maxxing isn't syncing with the productivity metrics engineering leadership actually cares about"

The **"multiplayer effect"**: your output depends on your teammates' level. A level 7 wizard's PRs stall if approved by a level 2 colleague who manually reviews everything. Martin Fowler amplified it (Mar 16), comparing it to Yegge's 8-level framework.

**Why this matters:** Osmani, Debois, Garg, and Eledath are all pointing at the same thing from different angles. The old bottleneck was "how fast can we write code?" The new bottleneck is "how good are our specs, context, and harnesses?" When agents generate code at near-zero marginal cost, the quality of what you feed them becomes the differentiator.

---
