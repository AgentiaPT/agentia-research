# R6: Research Papers — April 25 to May 1, 2026

## Paper: TDD Governance for Multi-Agent Code Generation via Prompt Engineering
- **Date:** 2026-04-29
- **arXiv ID:** 2604.26615
- **Authors:** Tarlan Hasanli et al.
- **Source:** https://arxiv.org/abs/2604.26615
- **Key findings:**
  - Proposes AI-native TDD framework operationalizing Test-Driven Development at prompt and workflow levels for multi-agent LLM systems
  - Introduces strict phase ordering (plan → generate → repair → validate), bounded repair loops, validation gates, and atomic mutation control
  - Separates model proposal from deterministic engine authority — LLM generates candidates, deterministic layer enforces contracts
  - Framework improves stability and reproducibility of multi-agent code generation pipelines
- **Methodology:** Encodes TDD principles as machine-readable governance manifesto; layered architecture divides AI creativity from deterministic verification; validated on multi-agent code generation workflows
- **Why it matters for practitioners:** Gives teams a concrete pattern for making LLM-driven code pipelines auditable and CI-friendly — governance-as-code for agent orchestration.
- **Confidence:** high

## Paper: Agentic AI in the Software Development Lifecycle: Architecture, Empirical Evidence, and the Reshaping of Software Engineering
- **Date:** 2026-04-29
- **arXiv ID:** 2604.26275
- **Authors:** Happy Bhati
- **Source:** https://arxiv.org/abs/2604.26275
- **Key findings:**
  - SWE-bench Verified scores rose from 1.96% (Oct 2023) to 78.4% (Apr 2026) — a 40× improvement in autonomous task resolution
  - Developer time savings in controlled studies range from 13.6% to 55.8%
  - 49% of sampled jobs in 2026 report AI used for ≥25% of tasks
  - Proposes a six-layer reference architecture for agentic SE systems and defines the "Agentic SDLC" (A-SDLC) concept
  - Identifies five open challenges: evaluation, governance, technical debt, skill redistribution, economics of attention
- **Methodology:** Survey paper consolidating empirical data 2023–2026 from Anthropic, OpenAI, DeepMind, Microsoft Research; proposes architectural taxonomy
- **Why it matters for practitioners:** Comprehensive snapshot of where agentic coding stands — useful for planning team adoption and identifying risks around technical debt.
- **Confidence:** high

## Paper: Claw-Eval-Live: A Live Agent Benchmark for Evolving Real-World Workflows
- **Date:** 2026-04-30
- **arXiv ID:** 2604.28139
- **Authors:** Chenxin Li, Zhengyang Tang et al.
- **Source:** https://arxiv.org/abs/2604.28139
- **Key findings:**
  - 105 tasks spanning CRM, HR, finance, email, helpdesk, calendar, and local workspace repair
  - Best model achieves only 66.7% pass rate; no model reaches 70%
  - Persistent failures in HR, management, and multi-system business workflows
  - Uses "double grounding" — benchmarks tied to live external demand (ClawHub Top-500 skills) AND verifiable agent actions
  - Grading combines deterministic checks with structured LLM-based judging for semantic aspects
  - Records execution traces, audit logs, service states, and workspace artifacts for reproducibility
- **Methodology:** Refreshed benchmark snapshots using public workflow-demand data; 13 SOTA models evaluated; rich evidence-based validation beyond pass/fail
- **Why it matters for practitioners:** Shows that even frontier models fail ~1/3 of realistic business workflow tasks — temper expectations for full end-to-end automation.
- **Confidence:** high

## Paper: Test Before You Deploy: Governing Updates in the LLM Supply Chain
- **Date:** 2026-04-30
- **arXiv ID:** 2604.27789
- **Authors:** Mohd Sameen Chishti, Damilare Peter Oyinloye, Jingyue Li
- **Source:** https://arxiv.org/abs/2604.27789
- **Key findings:**
  - Frames hosted LLM updates as a software supply chain governance problem — providers update silently causing behavioral drift
  - Proposes three-pronged governance framework: production contracts, risk-category-based testing, compatibility gates
  - Targeted risk-area tests catch problems that broad aggregate metrics miss
  - Validated across several LLM versions demonstrating detection of regressions invisible to standard benchmarks
- **Methodology:** Framework design + empirical validation on multiple LLM version transitions; accepted at LLMSC2026 workshop co-located with FSE 2026
- **Why it matters for practitioners:** Directly actionable — if you depend on hosted LLMs, implement compatibility gates and risk-targeted regression suites before provider updates break your product.
- **Confidence:** high

## Paper: AI-Assisted Code Review as a Scaffold for Code Quality and Self-Regulated Learning
- **Date:** 2026-04-25
- **arXiv ID:** 2604.23251
- **Authors:** Eduardo Oliveira, Michael Fu, Patanamon Thongtanunam, Sonsoles López-Pernas, Mohammed Saqr
- **Source:** https://arxiv.org/abs/2604.23251
- **Key findings:**
  - LLM-in-the-loop code review integrated into GitHub pull requests across 2 cohorts (100+ students each)
  - Iterative PR activity doubled (1176 vs 581 PRs) with AI review integration
  - Technical failures dropped to zero after AI tool/instruction refinements
  - Responsiveness to AI review comments (subsequent commits) stable at ~32–33%
  - Students used structured LLM review comments to focus discussions and improve code quality
- **Methodology:** Mixed-methods: GitHub activity metrics, surveys, reflective reports; repeated cross-sectional comparison across 2023–2024 cohorts
- **Why it matters for practitioners:** Evidence that AI code review works as a learning scaffold — ~1/3 of comments lead to action, and PR volume doubles without quality drops.
- **Confidence:** high

## Paper: RecursiveMAS: Recursive Multi-Agent Systems
- **Date:** 2026-04-28
- **arXiv ID:** 2604.25917
- **Authors:** Xiyuan Yang et al.
- **Source:** https://arxiv.org/abs/2604.25917
- **Key findings:**
  - Multi-agent collaboration via latent-space recursive computation instead of text exchanges
  - ~8.3% better average accuracy vs SOTA single/multi-agent baselines on math, science, medicine, search, and code tasks
  - 1.2×–2.4× end-to-end inference speedup
  - 34.6%–75.6% reduction in token usage
  - Only 0.31% of total parameters trained (RecursiveLink modules); main LLM parameters frozen
  - Validated on 4 collaboration patterns across 9 benchmarks
- **Methodology:** Inner-outer loop optimization — inner trains individual agents for latent thought generation, outer co-optimizes coordination; gradient-based credit assignment across recursion rounds
- **Why it matters for practitioners:** If multi-agent coding pipelines are in your roadmap, latent-space communication could slash token costs by 50%+ while improving accuracy.
- **Confidence:** high

## Paper: DEFault++: Automated Fault Detection, Categorization, and Diagnosis for Transformer Architectures
- **Date:** 2026-04-28
- **arXiv ID:** 2604.28118
- **Authors:** Sigma Jahan, Saurabh Singh Rajput, Tushar Sharma, Mohammad Masudur Rahman
- **Source:** https://arxiv.org/abs/2604.28118
- **Key findings:**
  - Hierarchical diagnostic system for transformer-specific faults at 3 levels: detection, categorization (12 categories), root cause (45 mechanisms)
  - AUROC for fault detection: >0.96
  - Macro-F1 for categorization and root cause identification: 0.85
  - Developer study: correct repair actions increased from 57.1% to 83.3% when using DEFault++
  - DEFault-bench: 3,739 labeled mutation-based fault instances across 7 transformer models and 9 tasks
- **Methodology:** Fault Propagation Graphs (FPG) derived from transformer structure; prototype matching + supervised contrastive learning for diagnosis; DEForm mutation technique for synthetic fault generation
- **Why it matters for practitioners:** As teams fine-tune and deploy custom transformers, this tool can diagnose attention/projection faults that standard debuggers miss.
- **Confidence:** high

## Paper: From Mirage to Grounding: Towards Reliable Multimodal Circuit-to-Verilog Code Generation
- **Date:** 2026-04-28
- **arXiv ID:** 2604.27969
- **Authors:** Guang Yang, Xing Hu et al.
- **Source:** https://arxiv.org/abs/2604.27969
- **Key findings:**
  - Addresses hallucination in LLM-generated hardware description code (Verilog) from circuit diagrams
  - Multimodal approach combining circuit image understanding with code generation
  - Focus on grounding — reducing "mirage" outputs where generated code looks correct but doesn't match circuit semantics
- **Methodology:** Multimodal AI pipeline (vision + code generation) with grounding mechanisms for hardware/software co-design verification
- **Why it matters for practitioners:** Extends LLM code generation reliability concerns beyond software into hardware description languages — relevant for chip design automation teams.
- **Confidence:** med (limited metrics available from search results)

---

## Search queries used
1. `arXiv papers AI software engineering LLM coding agents April 2026`
2. `arXiv 2604 LLM code generation benchmark evaluation April 25-30 2026`
3. `"TDD Governance" multi-agent code generation arXiv 2026 Hasanli`
4. `arXiv AI software testing automation developer productivity April 2026 new paper`
5. `arXiv 2604.26275 "Agentic AI in Software Development Lifecycle" April 2026`
6. `arXiv 2604.28139 "Claw-Eval-Live" agent evaluation April 2026`
7. `arXiv April 28 29 30 2026 LLM coding agent benchmark new paper software engineering`
8. `arXiv "Test Before You Deploy" LLM supply chain governance April 2026 Chishti`
9. `arXiv cs.SE April 25 26 27 28 2026 new submissions code LLM agent`
10. `arXiv 2604.25917 RecursiveMAS multi-agent systems April 2026`
11. `arXiv April 2026 "code review" OR "pull request" OR "developer productivity" LLM AI new paper 2604`
12. `arXiv 2604 "code generation" OR "software engineering" OR "coding benchmark" April 25-May 1 2026`
13. `arXiv 2604.28118 DEFault++ transformer fault detection April 2026`
