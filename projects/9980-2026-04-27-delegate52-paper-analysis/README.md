---
title: "Deep Dive: LLMs Corrupt Your Documents When You Delegate (DELEGATE-52)"
date: 2026-04-27
status: complete
tags: [llm-evaluation, delegation, vibe-coding, document-editing, benchmark, agentic-coding]
---

# Deep Dive: LLMs Corrupt Your Documents When You Delegate

> **Note:** This project was authored by [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (AI) with human direction and review. While factual accuracy and quality were prioritized, AI-generated content may contain errors, hallucinations, or outdated information. Sources and claims should be independently verified before relying on them.

**Paper:** [arXiv:2604.15597](https://arxiv.org/abs/2604.15597) — Laban, Schnabel, Neville (Microsoft Research, April 2026)

---

## TL;DR — What This Paper Actually Says

This paper introduces **DELEGATE-52**, a benchmark that tests whether LLMs can faithfully edit documents across 52 professional domains over long workflows (20 interactions). The key finding: **all tested LLMs degrade documents over repeated editing**, with even frontier models (Gemini 3.1 Pro, Claude 4.6 Opus, GPT 5.4) losing ~25% of document content by the end. The degradation is driven by **sparse critical failures** (not gradual decay), compounds over time, and worsens with larger documents, longer interactions, and distractor context.

---

## The Methodology — Understanding What Was Actually Tested

### The Round-Trip Relay Design

The core methodology is a **backtranslation round-trip**:

- **Forward instruction:** "Split this accounting ledger into separate files by expense category"
- **Backward instruction:** "Merge the separate files back chronologically into one file"
- A perfect model recovers the original document exactly
- The **reconstruction score (RS@k)** measures similarity between original and recovered document after k interactions
- 10 round-trips = 20 interactions total per relay

### Key Design Choices (Critical for Correct Interpretation)

- **Single-turn interactions only** — each instruction is a complete, self-contained prompt. No multi-turn conversation, no follow-up, no clarification
- **Full document regeneration** — models receive all documents as text in context and output the modified files. They regenerate entire documents each time
- **Documents are 3–5k tokens** with 8–12k tokens of distractor context
- **52 domains** — from Python and Docker to crystallography, weaving, genealogy, and music notation
- **Domain-specific similarity scoring** — not generic text similarity. A recipe gets scored on ingredients (40%), steps (40%), tips (20%). A small number change (200g → 800g) registers as a severe error
- **Real documents, not synthetic** — seed documents are real files found online
- **Each round-trip is an independent single-turn session** — no conversation memory between turns

---

## The Findings — Bullet Outline

### Main Results (Table 1)

- **All 19 models degrade** documents over 20 interactions — no exceptions
- **Average degradation across all models: ~50%** by end of simulation
- **Frontier models (Gemini 3.1 Pro, Claude 4.6 Opus, GPT 5.4):** ~25% degradation (RS@20 of 80.9%, 73.1%, 71.5%)
- **Weaker models:** much worse — GPT 5 Nano drops to 10.0%, GPT 4o to 14.7%
- **Python is the only domain** where most models (17/19) achieve lossless manipulation (RS@20 ≥ 98%)
- **Best overall model** (Gemini 3.1 Pro) is "ready" in only 11 of 52 domains

### Domain Performance (Table 2)

- **Code & Configuration** domains perform best (Python, DB Schema, Docker, Makefile)
- **Science & Engineering** varies widely — some structured domains (Circuit, Quantum) do okay, others fail
- **Creative & Media** is weak — music notation, weaving, 3D objects, audio synthesis heavily degraded
- **Structured Records** is mixed — library catalogs and accounting struggle
- **Everyday** domains (recipes, earnings, job boards) generally fail
- Models show **"severe corruption"** (≥20% degradation) in **80% of simulated conditions**

### Short-Term vs. Long-Term Performance

- **Short-term performance (2 interactions) does NOT predict long-horizon performance**
- Example: GPT 5 and Kimi K2.5 start near-identical (91.5 vs. 91.1) but diverge sharply (48.3 vs. 64.1 at RS@20)
- Gemini 3 Flash trails Mistral Large 3 early but overtakes it by end of simulation

### Agentic Tool Use (Section 4.2)

- **Tool use does NOT help** — 4 tested models actually perform *worse* with an agentic harness (6% additional degradation on average)
- GPT 5.4 with tools: 68.3% vs. 71.5% without tools
- **Why:** The agentic harness consumes 2–5x more input tokens (8–12 tool invocations per task), and longer context hurts performance
- DELEGATE-52 tasks require textual understanding, not just programmatic manipulation
- Better models increasingly use code execution (GPT 4.1: 10% vs. GPT 5.4: 45%)
- **Important caveat:** This was a "basic agentic harness" — not a state-of-the-art coding agent system

### Document Size (Section 4.3)

- **Larger documents → more degradation** across all models
- Performance gap between small and large documents **widens over time** (compounds)
- Even documents scaled to just 2x the original size show measurable additional degradation

### Length of Interaction (Section 4.4)

- Extended to **100 interactions (50 round-trips)** — degradation never plateaus
- Even GPT 5.4 drops below 60% by end of 50-round-trip relay
- First half accounts for 2–3x more loss than second half (decelerating, but never stopping)

### Distractor Effect (Section 4.5)

- Removing distractor documents improves scores by 0.4–4% after 2 interactions
- Improves by 2–8% by end of simulation (compounds over time)
- Echoes "lost in the middle" research — irrelevant context hurts

### Image Editing (Section 4.6)

- Extended to visual editing — **dramatically worse**: best models achieve 28–30% RS@20 (vs. 70–80% for text)
- Even after 2 interactions, no image model exceeds 65%

---

## Analysis: How Documents Fail

### Critical Failures — Not "Death by a Thousand Cuts"

> This is one of the paper's most important findings.

- **~80% of total degradation** comes from **critical failures** (≥10 point drop in a single round-trip)
- Models maintain near-perfect reconstruction in some rounds, then catastrophically fail in a few rounds (losing 10–30+ points at once)
- Stronger models don't avoid small errors better — they **delay critical failures** and experience them less frequently
- By 20 interactions, **38–93% of all runs** have experienced at least one critical failure (even Gemini 3.1 Pro: 38%)

### Deletion vs. Corruption

- **Weaker models** primarily fail by **deleting content** (dropping elements entirely)
- **Frontier models** primarily fail by **corrupting content** (elements present but with incorrect values)
- This is important: frontier models don't lose data — they silently alter it, which can be harder to catch

### What Makes Tasks Harder

- **Global restructuring** (split/merge, classification) is significantly harder than local operations (string manipulation)
- **Multiple coordinated operations** are harder than single operations
- **Programmatic/structured domains** (Python, DBSchema) much easier than natural language domains (Recipe, Fiction)
- High repetitiveness and structural density help performance

---

## What This Paper MEANS

- **LLMs introduce compounding errors during repeated document regeneration** — this is real and significant
- **Document fidelity is a genuine unsolved problem** — especially for non-code, non-structured domains
- **Single-domain performance doesn't generalize** — being good at Python doesn't mean being good at weaving patterns
- **Short benchmarks underestimate real-world degradation** — the compounding effect means 2-interaction tests miss critical failures
- **Agentic tool use is not a magic fix** (at least with basic harnesses) — more tokens consumed can worsen results
- **LLMs tend to fail catastrophically, not gradually** — a "looks fine for 6 rounds then corrupts severely" pattern is dangerous
- **Frontier models corrupt rather than delete** — the errors are subtler and harder to detect
- **Rapid progress is real:** GPT 4o → GPT 5.4 went from 14.7% to 71.5% in 16 months

---

## What This Paper Does NOT Mean

### ❌ "AI coding tools are broken"
The paper explicitly shows **Python is the one domain where most models are ready** (17/19 achieve ≥98% reconstruction). Code is the easiest domain, not the hardest. The headline "25% corruption" is across *all 52 domains*, most of which are far from typical coding.

### ❌ "You can't use LLMs for development"
The benchmark tests full-document regeneration across exotic domains (crystallography, weaving, music notation). Real coding agents don't work this way — they make targeted edits, have compilers/linters/tests, and work in a domain (code) where LLMs demonstrably excel.

### ❌ "Agentic systems don't help"
The paper tested a **basic** agentic harness with file read/write and code execution. It explicitly disclaims: *"this is not an optimized state-of-the-art agent system; future work could explore more sophisticated harnesses."* Modern coding agents (Claude Code, Cursor, etc.) use diff-based editing, test feedback loops, compiler validation, and much more sophisticated orchestration.

### ❌ "25% of your code disappears every session"
The 25% figure is averaged across **52 domains** (including crystallography, weaving, music notation) over **20 sequential interactions** with **full document regeneration each time**. In real coding, agents make surgical edits to specific files, not regenerating entire codebases.

### ❌ "This invalidates vibe coding"
The paper actually *motivates* its work by referencing vibe coding as an emerging paradigm. It doesn't say delegation is impossible — it says current models aren't reliable *delegates* across all domains. Python coding is the one bright spot.

### ❌ "Longer conversations always produce worse code"
The benchmark chains **independent** single-turn sessions with full regeneration. It doesn't test the kind of multi-turn, iterative refinement that happens in real agentic workflows where errors can be caught and corrected.

---

## Why Your 12K-Line Vela App Doesn't Suffer This Problem

This is the key practical question. Here's why real-world agentic coding (like editing a large app with Claude Code through many iterations) doesn't match the paper's catastrophic degradation scenario:

### 1. Surgical Edits vs. Full Document Regeneration

**DELEGATE-52:** The model receives the entire document and must *output the entire modified document*. Every token gets regenerated, creating opportunities for error at every position.

**Real agentic coding:** Tools like Claude Code use **diff-based editing** — specifying exact `old_str → new_str` replacements. Only the targeted code changes. The other 11,900 lines are never touched, never regenerated, never at risk.

### 2. Executable Verification Loop

**DELEGATE-52:** No verification. The model's output is accepted as-is and fed into the next round. Silent corruption compounds unchecked.

**Real agentic coding:** After every change, the code gets:
- **Compiled/built** — syntax errors caught immediately
- **Linted** — style and static analysis catches issues
- **Tested** — existing test suites validate behavior
- **Run** — the app either works or it doesn't

If a change breaks something, the agent **sees the error and fixes it**. This feedback loop is the single biggest difference.

### 3. Code Is the Easiest Domain

The paper itself shows Python is the **one domain where 17/19 models achieve ≥98% reconstruction** even under the harsh benchmark conditions. Code has:
- Formal syntax that constrains valid outputs
- Unambiguous semantics (it either runs or it doesn't)
- Rich training data (more code training data than crystallography data)
- Standard patterns and conventions that models know well

### 4. Version Control as a Safety Net

**DELEGATE-52:** Changes cascade forward with no rollback possibility. Once a document is corrupted, all subsequent edits build on the corrupted version.

**Real agentic coding:** Git provides:
- Full history of every change
- Ability to diff and review exactly what changed
- Rollback to any previous state
- Branch-based isolation for experiments

### 5. Task Structure Is Different

**DELEGATE-52:** Tasks require complete document transformations — "split this ledger into separate files by category" requires understanding and perfectly reproducing every line.

**Real agentic coding:** Tasks are typically:
- "Add a new feature to component X" (additive)
- "Fix this bug in function Y" (targeted)
- "Refactor this module" (structural, but still localized)

You're rarely asking an agent to "rewrite all 12,000 lines in a different format and then convert them back."

### 6. Incremental Complexity vs. Round-Trip Reversal

**DELEGATE-52:** Tasks are paired forward/backward transformations. The *reversal* is where models struggle — reconstructing exactly what was there before.

**Real agentic coding:** Work is **monotonically forward**. You add features, fix bugs, refactor — you almost never need to perfectly reverse a complex transformation. Each change *adds* to the codebase rather than requiring perfect reconstruction.

### 7. Domain Familiarity

**DELEGATE-52:** Tests 52 domains including crystallography (.cif files), weaving patterns, ham radio logs, EDIFACT messages — domains with tiny representation in training data.

**Real coding:** TypeScript/JavaScript, HTML, CSS, React, standard web frameworks — among the **most represented domains** in LLM training data.

### 8. Context Management

**DELEGATE-52:** Includes 8–12k tokens of distractor context alongside the working document, which the paper shows compounds degradation.

**Real agentic coding:** Sophisticated context management — agents read only the files they need, search for specific functions, and don't carry irrelevant documents in context.

### Summary Table

| Factor | DELEGATE-52 | Real Agentic Coding (Vela) |
|--------|-------------|---------------------------|
| Edit granularity | Full document regeneration | Surgical diff-based edits |
| Verification | None | Build + lint + test + run |
| Domain | 52 domains (most niche) | Code (LLM's strongest domain) |
| Error recovery | None — errors compound | Feedback loop catches & fixes |
| Version control | None | Full git history |
| Task type | Reversible transformations | Forward-only feature work |
| Context | 8–12k distractor tokens | Targeted file reading |
| Training data | Many low-resource domains | High-resource code domain |

---

## Practical Implications for AI-Assisted Development

### What you should actually worry about:

- **Silent value corruption in non-code files** — config files, data files, documentation with precise numbers
- **Long autonomous runs without checkpoints** — the paper shows degradation is non-linear; set up verification gates
- **Overgeneralizing from code success** — just because your agent handles TypeScript well doesn't mean it handles your YAML configs, SQL migrations, or data files with equal fidelity
- **Not having tests** — if you're "vibe coding" without a test suite, you're closer to the paper's scenario than you think
- **Complex global restructurings** — major refactors that touch many files simultaneously are the highest-risk operation

### What you probably don't need to worry about:

- **Normal feature development** in well-known programming languages with test coverage
- **Incremental changes** to existing codebases with build/test feedback loops
- **Short, focused agent sessions** with clear verification between tasks

---

## Fact-Check Notes

All claims in this analysis have been verified against the actual paper text (arXiv:2604.15597v1). Key verifications:

- ✅ **"25% corruption for frontier models"** — Verified. Abstract states "corrupt an average of 25% of document content by the end of long workflows" for frontier models. Table 1 confirms: Gemini 3.1 Pro (80.9% = 19.1% loss), Claude 4.6 Opus (73.1% = 26.9% loss), GPT 5.4 (71.5% = 28.5% loss). Average: ~24.8% — checks out.

- ✅ **"Python is the only domain where most models are ready"** — Verified. Section 4.1: "Python is the only domain (out of 52) where most models are ready." Table 2 shows 17/19 models pass the ≥98% threshold for Python.

- ✅ **"80% of degradation from critical failures"** — Verified. Section 5 Analysis: "These sparse critical failures explain about 80% of total document degradation."

- ✅ **"Basic agentic harness tested, not SOTA"** — Verified. Section 4.2: "We note this is not an optimized state-of-the-art agent system; future work could explore more sophisticated harnesses."

- ✅ **"Agents use 2–5x more tokens"** — Verified. Section 4.2: "they invoke 8-12 tools on average to complete a task, consuming 2-5x more input tokens than the no-tool alternative."

- ✅ **"Better models use more code execution"** — Verified. Section 4.2: "better models rely more on code execution (10% for GPT 4.1 vs. 45% for GPT 5.4)."

- ✅ **"GPT 4o to GPT 5.4 improvement in 16 months"** — Verified. Section 6: "16 months separate the GPT 4o and GPT 5.4 models... benchmark performance increased from 14.7% to 71.5%."

- ✅ **"Single-turn sessions"** — Verified. Limitations Section 8: "Our simulations use single-turn sessions where each instruction fully specifies a task without needing clarification."

- ✅ **"Extending to 100 interactions shows no plateau"** — Verified. Section 4.4: "degradations continue to accumulate in longer relays, with none of the models showing signs of plateauing."

- ✅ **"Frontier models corrupt rather than delete"** — Verified. Section 5: "weaker models' degradation originates primarily from content deletion, while frontier models' degradation is attributable to corruption of content."

---

## Sources

- Laban, P., Schnabel, T., Neville, J. (2026). [LLMs Corrupt Your Documents When You Delegate](https://arxiv.org/abs/2604.15597#:~:text=even%20frontier%20models). arXiv:2604.15597.
- [DELEGATE-52 GitHub Repository](https://github.com/microsoft/DELEGATE52)
- [DELEGATE-52 Dataset on HuggingFace](https://huggingface.co/datasets/microsoft/DELEGATE52)
