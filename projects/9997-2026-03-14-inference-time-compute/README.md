---
title: "Inference-Time Compute Scaling in Large Language Models"
date: 2026-03-14
status: complete
tags: [ai, llm, inference-time-compute, scaling, research-survey]
---

# Inference-Time Compute Scaling in Large Language Models

> **Note:** This project was authored by [Claude Code](https://claude.ai/claude-code) (AI) with human direction and review. While factual accuracy and quality were prioritized, AI-generated content may contain errors, hallucinations, or outdated information. Sources and claims should be independently verified before relying on them.

**A Research Survey -- March 2026**

---

## 1. What Is Inference-Time Compute Scaling?

Inference-time compute scaling (also called "test-time compute" or "test-time scaling") refers to the practice of allocating additional computational resources *during inference* -- when a model is generating its response -- rather than during training. Instead of making a model smarter by training it longer on more data (training-time scaling), you make it smarter by letting it "think" longer on each problem.

The core insight is deceptively simple: **a model that spends more compute at inference time can outperform a much larger model that answers immediately.**

### Training-Time vs. Inference-Time Scaling

| Dimension | Training-Time Scaling | Inference-Time Scaling |
|---|---|---|
| **When** | Before deployment (pre-training, fine-tuning) | During each query/response |
| **What scales** | Model parameters, dataset size, training FLOPs | Tokens generated, search iterations, samples |
| **Cost profile** | Fixed upfront cost, amortized over all queries | Per-query cost, varies by difficulty |
| **Governed by** | Chinchilla scaling laws (Hoffmann et al., 2022) | Emerging inference scaling laws |
| **Analogy** | Studying harder for an exam | Taking more time on each exam question |

The pivotal realization is that these two forms of scaling are **not interchangeable** -- they have different efficiency profiles depending on problem difficulty, and the optimal strategy combines both.

---

## 2. The Key Papers

### 2.1 "Let's Verify Step by Step" (OpenAI, May 2023)

**Authors:** Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, Karl Cobbe

**Paper:** [arXiv:2305.20050](https://arxiv.org/abs/2305.20050#:~:text=process%20supervision%20significantly%20outperforms%20outcome%20supervision)

This paper established the foundation for process reward models (PRMs) -- a critical ingredient in inference-time scaling. The core question: when training a reward model to evaluate LLM reasoning, should you judge only the final answer (outcome supervision) or every intermediate step (process supervision)?

> "We conduct our own investigation, finding that process supervision significantly outperforms outcome supervision for training models to solve problems from the challenging MATH dataset. Our process-supervised model solves 78% of problems from a representative subset of the MATH test set."
>
> -- [Lightman et al., 2023](https://arxiv.org/abs/2305.20050#:~:text=process%20supervision%20significantly%20outperforms%20outcome%20supervision)

**Key contributions:**

- **Process supervision >> outcome supervision** for mathematical reasoning
- **PRM800K dataset released** -- 800,000 step-level human feedback labels
- **Active learning** significantly improves the efficacy of process supervision
- Established that step-level verification enables better search at inference time -- if you can evaluate each reasoning step, you can prune bad paths early

**Why it matters for inference-time compute:** PRMs are the "verifiers" that make inference-time search effective. Without a reliable way to evaluate intermediate reasoning steps, generating multiple solution paths at inference time yields diminishing returns. This paper showed that step-level feedback is both feasible and dramatically more effective.

---

### 2.2 "Scaling LLM Test-Time Compute Optimally" (UC Berkeley / Google DeepMind, August 2024)

**Authors:** Charlie Snell, Jaehoon Lee, Kelvin Xu, Aviral Kumar

**Paper:** [arXiv:2408.03314](https://arxiv.org/abs/2408.03314#:~:text=scaling%20LLM%20test-time%20compute%20optimally) | Accepted to ICLR 2025

This is the landmark paper that rigorously formalized inference-time compute scaling. The central research question:

> "If an LLM is allowed to use a fixed but non-trivial amount of inference-time compute, how much can it improve its performance on a challenging prompt?"

**Two mechanisms studied:**

1. **Search against process-based verifier reward models** -- generating multiple candidate solutions and using a PRM to select the best
2. **Adaptive distribution updating** -- modifying the model's token distributions at test time based on the specific prompt

**Key findings:**

- A compute-optimal strategy **improves efficiency by more than 4x** compared to best-of-N baselines:

  > "improving the efficiency of test-time compute scaling by more than 4x compared to a best-of-N baseline"
  >
  > -- [Snell et al., 2024](https://arxiv.org/html/2408.03314v1#:~:text=improving%20the%20efficiency%20of%20test-time%20compute%20scaling%20by%20more%20than%204x)

- In FLOPs-matched evaluations, **smaller models with test-time compute outperform 14x larger models** on problems where base success rates are non-trivial

- **Difficulty matters enormously:**
  - Easy to intermediate questions: test-time compute often outperforms additional pretraining
  - Most challenging questions: additional pretraining remains more effective
  - This means "test-time and pretraining compute are not 1-to-1 exchangeable"

- **Strategy depends on difficulty:**
  - Easy questions benefit more from sequential revisions
  - Hard questions benefit from beam search over multiple paths
  - The optimal approach is adaptive: select the strategy based on estimated question difficulty

---

### 2.3 "Inference Scaling Laws" (Tsinghua / Microsoft, August 2024)

**Authors:** Yangzhen Wu, Zhiqing Sun, Shanda Li, Sean Welleck, Yiming Yang

**Paper:** [arXiv:2408.00724](https://arxiv.org/abs/2408.00724#:~:text=scaling%20inference%20compute%20with%20inference%20strategies)

This paper established empirical inference scaling laws across multiple strategies:

> "Scaling inference compute with inference strategies can be more computationally efficient than scaling model parameters."
>
> -- [Wu et al., 2024](https://arxiv.org/abs/2408.00724#:~:text=scaling%20inference%20compute%20with%20inference%20strategies%20can%20be%20more%20computationally%20efficient)

**Strategies evaluated:** greedy search, majority voting, best-of-N, weighted voting, and two tree search algorithms.

**Critical finding:** The Llemma-7B model paired with tree search **consistently outperformed the Llemma-34B model** across inference strategies on MATH benchmarks -- a nearly 5x parameter difference overcome by smarter inference.

---

### 2.4 OpenAI o1 and o3 (September 2024 -- January 2025)

**Source:** [OpenAI -- "Learning to Reason with LLMs"](https://openai.com/index/learning-to-reason-with-llms/#:~:text=performance%20consistently%20improves)

OpenAI's o1 (September 2024) and o3 (December 2024) are the highest-profile embodiments of inference-time compute scaling. These models generate extended chains of thought before producing answers, spending variable amounts of compute depending on problem difficulty.

**Key characteristics:**

- Performance consistently improves with both more RL training (train-time compute) **and** more time spent thinking (test-time compute)
- A **15x increase in inference-time compute equates to a 10x increase in train-time compute** -- demonstrating the efficiency advantage
- o3 generates **multiple candidate chains of thought** and uses search algorithms (beam search, MCTS-like methods) to evaluate and select the best reasoning path
- o3-mini introduced "Adaptive Thinking" with Low/Medium/High reasoning effort levels

**Benchmark results for o3:**
- AIME 2024: ~97%
- GPQA Diamond (PhD-level science): ~87.7%

---

### 2.5 DeepSeek-R1 (January 2025)

**Authors:** DeepSeek-AI

**Paper:** [arXiv:2501.12948](https://arxiv.org/abs/2501.12948#:~:text=reasoning%20abilities%20of%20LLMs%20can%20be%20incentivized%20through%20pure%20reinforcement%20learning) | Published in Nature, Vol. 645, pp. 633-638 (2025)

DeepSeek-R1 demonstrated that reasoning capabilities can emerge **purely from reinforcement learning** without supervised fine-tuning on human-written chain-of-thought demonstrations:

> "Reasoning abilities of LLMs can be incentivized through pure reinforcement learning (RL), obviating the need for human-labeled reasoning trajectories."
>
> -- [DeepSeek-AI, 2025](https://arxiv.org/abs/2501.12948#:~:text=reasoning%20abilities%20of%20LLMs%20can%20be%20incentivized%20through%20pure%20reinforcement%20learning)

**The "Aha Moment":** DeepSeek-R1-Zero exhibited a remarkable emergent behavior during training. The model spontaneously learned to pause, reconsider, and restart its reasoning -- inserting reflective commentary like "Wait, wait. Wait. That's an aha moment I can flag here" before reworking a problem. This behavior was **not explicitly programmed** -- it emerged naturally from the RL training loop.

**Emergent behaviors observed:**
- Extended thinking: response length naturally grew from minimal to thousands of reasoning tokens
- Self-verification: the model revisited and reevaluated previous steps autonomously
- Alternative exploration: spontaneous exploration of multiple solution pathways

**Benchmark results:**
- AIME 2024: 79.8% (pass@1); 86.7% with majority voting
- MATH-500: 97.3%
- Codeforces: 2,029 Elo rating (96.3rd percentile)

**Critical insight:** The "thinking time" of DeepSeek-R1-Zero showed consistent improvement throughout training. The model's output length grew organically as performance improved, suggesting that extended reasoning naturally emerges as an optimal strategy when rewarded for correctness.

---

## 3. Why Does More "Thinking" Produce Better Outputs?

There is no single theoretical explanation. Instead, several complementary mechanisms contribute:

### 3.1 The Search Perspective

The most compelling framework treats inference-time compute as **search over a solution space**. A harder problem has a larger space of possible reasoning paths, most of which lead to wrong answers. More compute = more paths explored = higher probability of finding a correct one.

Noam Brown (OpenAI) articulated this powerfully at the TED AI Conference (October 2024):

> "It turned out that having a bot think for just 20 seconds in a hand of poker got the same boosting performance as scaling up the model by 100,000x and training it for 100,000 times longer."
>
> -- [Noam Brown, TED AI 2024](https://venturebeat.com/ai/openai-noam-brown-stuns-ted-ai-conference-20-seconds-of-thinking-worth-100000x-more-data#:~:text=20%20seconds%20in%20a%20hand%20of%20poker)

Brown drew on his experience building poker AIs (Libratus, Pluribus). Human players spent time deliberating while bots acted instantly. Adding "thinking time" (inference-time search) was the breakthrough that led to superhuman poker play -- and the same principle generalizes to language models.

However, Brown also identified a crucial prerequisite:

> "If you try to do the reasoning paradigm on top of GPT-2, I don't think it would have gotten you almost anything."
>
> -- [Noam Brown, Latent Space podcast](https://www.latent.space/p/noam-brown#:~:text=if%20you%20try%20to%20do%20the%20reasoning%20paradigm%20on%20top%20of%20GPT-2)

The foundation must exist first. Extended thinking only helps if the model already has the knowledge and capabilities to reason -- analogous to how asking a pigeon to think harder about chess won't help.

### 3.2 The Decomposition Perspective

Chain-of-thought reasoning works because it **decomposes complex problems into simpler sub-problems** that the model can solve individually. Studies have shown performance drops significantly as reasoning depth increases -- from ~68% accuracy at depth-1 to ~43% at depth-5. By breaking multi-step problems into explicit intermediate steps, each step stays within the model's reliable capability range.

### 3.3 The Contextual Maintenance Perspective

Transformers process all tokens in context simultaneously. When a model writes out intermediate reasoning steps, those steps become part of the context for subsequent generation. This effectively gives the model an **external working memory** -- the reasoning trace itself serves as a scratchpad that maintains context across a long derivation.

### 3.4 The Token Probability Guidance Perspective

A more mechanistic view: LLMs may not truly "reason" in a traditional sense. When triggered to produce step-by-step output, the probability distribution over next tokens gets directed toward patterns that resemble the multi-step reasoning seen in training data. The explicit reasoning tokens effectively condition the model into a "reasoning mode" where subsequent token predictions are more likely to be correct.

### 3.5 The Verification and Error Correction Perspective

With more tokens and more time, models can:
- **Detect errors** in their own reasoning and backtrack
- **Verify intermediate results** before proceeding
- **Explore alternative approaches** when one path seems unlikely to succeed

DeepSeek-R1-Zero's emergent self-correction behavior is the strongest evidence for this: the model learned to insert "wait" moments and reconsider its approach entirely, without any explicit training to do so.

---

## 4. Chain-of-Thought Reasoning and Output Quality

### The Foundational Paper

**"Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"** (Wei et al., January 2022)

[arXiv:2201.11903](https://arxiv.org/abs/2201.11903#:~:text=chain%20of%20thought%20prompting%20improves%20performance)

> "We explore how generating a chain of thought -- a series of intermediate reasoning steps -- significantly improves the ability of large language models to perform complex reasoning."
>
> -- [Wei et al., 2022](https://arxiv.org/abs/2201.11903#:~:text=generating%20a%20chain%20of%20thought)

**Headline result:**

> "Prompting a 540B-parameter language model with just eight chain of thought exemplars achieves state of the art accuracy on the GSM8K benchmark of math word problems, surpassing even finetuned GPT-3 with a verifier."

**Critical finding -- emergence:** Chain-of-thought reasoning is an **emergent property of model scale**. The benefits only materialize with sufficiently large models (approximately 100B+ parameters). Smaller models produce incoherent chains of thought that hurt rather than help performance.

### The Mechanism: More Tokens = More Compute

Cameron Wolfe summarizes the core dynamic in [Demystifying Reasoning Models](https://cameronrwolfe.substack.com/p/demystifying-reasoning-models#:~:text=longer%20CoT):

> "Longer CoT = more tokens = more compute."

Each additional token generated is a forward pass through the model. By generating thousands of reasoning tokens before answering, reasoning models effectively perform orders of magnitude more computation per query than standard models. The reasoning trace is not merely decorative -- it is the mechanism through which additional compute is allocated.

---

## 5. Inference-Time Compute Techniques

### 5.1 Best-of-N Sampling

**Mechanism:** Generate N independent completions from the model, then select the best one using a reward model or verifier.

**Strengths:** Simple to implement, embarrassingly parallel, works with any base model.

**Weaknesses:** Scales poorly -- diminishing returns as N increases; wasteful because most samples are discarded; requires a reliable verifier.

**Empirical baseline:** The Snell et al. (2024) paper treats best-of-N as the baseline and shows their compute-optimal strategy achieves the same performance with **4x less compute**.

### 5.2 Self-Consistency (Wang et al., 2022)

**Paper:** [arXiv:2203.11171](https://arxiv.org/abs/2203.11171#:~:text=self-consistency%20boosts%20the%20performance)

> "Self-consistency first samples a diverse set of reasoning paths instead of only taking the greedy one, and then selects the most consistent answer by marginalizing out the sampled reasoning paths."
>
> -- [Wang et al., 2022](https://arxiv.org/abs/2203.11171#:~:text=samples%20a%20diverse%20set%20of%20reasoning%20paths)

**Core intuition:**

> "A complex reasoning problem typically admits multiple different ways of thinking leading to its unique correct answer."

**Benchmark improvements over standard CoT:**

| Benchmark | Improvement |
|---|---|
| GSM8K | +17.9% |
| SVAMP | +11.0% |
| AQuA | +12.2% |
| StrategyQA | +6.4% |
| ARC-challenge | +3.9% |

Self-consistency is essentially majority voting over diverse reasoning paths. It trades inference compute (generating multiple paths) for accuracy, without any additional training.

### 5.3 Tree-of-Thought (Yao et al., NeurIPS 2023)

**Paper:** [arXiv:2305.10601](https://arxiv.org/abs/2305.10601#:~:text=deliberate%20problem%20solving)

Tree-of-Thought (ToT) generalizes chain-of-thought by treating reasoning as an **explicit tree search**. Instead of generating a single linear chain of reasoning, the model:

1. Generates multiple candidate "thoughts" (reasoning steps) at each node
2. Self-evaluates each candidate
3. Uses search algorithms (BFS, DFS) to explore the tree
4. Backtracks when paths seem unproductive

**Dramatic result on Game of 24:**
- GPT-4 with standard CoT: **4%** success rate
- GPT-4 with Tree-of-Thought: **74%** success rate

This 18.5x improvement demonstrates that structured search over reasoning paths can unlock capabilities that exist within the model but are inaccessible through greedy generation.

### 5.4 Process Reward Models + Beam Search

Combining PRMs (from "Let's Verify Step by Step") with beam search creates a powerful inference-time scaling strategy. The model generates multiple partial solutions, the PRM scores each step, and beam search prunes unpromising paths while expanding promising ones. This is believed to be close to what OpenAI's o1/o3 models do internally.

### 5.5 Sequential Revision / Iterative Refinement

The model generates an initial answer, then refines it through multiple rounds of self-critique and revision. Each revision is additional inference compute. The s1 paper (January 2025) introduced "wait tokens" -- special tokens that force the model to continue thinking rather than outputting a final answer, providing a simple mechanism for controlling inference-time compute allocation.

### 5.6 Comparison of Approaches

From Sebastian Raschka's analysis in [The State of LLM Reasoning Model Inference](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling#:~:text=inference-time%20compute%20scaling):

Inference-time techniques divide into two categories:
- **Parallel scaling** (best-of-N, majority voting, self-consistency): generate multiple independent completions and aggregate
- **Sequential scaling** (chain-of-thought, iterative refinement, budget forcing): generate more tokens in a single completion

No single technique universally dominates. The optimal strategy depends on task type, difficulty level, and available compute budget.

---

## 6. Empirical Scaling Results

### 6.1 The Core Scaling Relationship

Across multiple studies, a consistent pattern emerges: **performance improves monotonically with inference-time compute, but with diminishing returns.** The curve resembles a logarithmic function -- large gains early, gradually flattening.

### 6.2 Small Models Can Beat Large Ones

The most striking empirical result from the literature:

> A **1B parameter model can outperform a 405B Llama 3 model** that lacks inference-time scaling, with appropriate compute allocation.
>
> -- Reported in a February 2025 paper, cited by [Raschka](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling#:~:text=1B%20parameter%20model%20can%20outperform)

From Snell et al. (2024): a smaller model with compute-optimal test-time scaling **outperforms a 14x larger model** in FLOPs-matched comparisons on problems of easy-to-moderate difficulty.

From Wu et al. (2024): **Llemma-7B with tree search consistently outperforms Llemma-34B** across MATH benchmarks.

### 6.3 The Difficulty Dependency

This is perhaps the most important nuanced finding. The benefit of inference-time compute is **not uniform across problem difficulties:**

- **Easy problems:** Test-time compute is highly effective; even simple strategies like self-consistency yield large gains
- **Medium problems:** Compute-optimal strategies with adaptive allocation provide the best cost-performance tradeoff
- **Very hard problems:** Additional pretraining (bigger model) remains more effective than inference-time compute. The model cannot "think" its way to knowledge it doesn't have.

This creates a practical implication: the optimal system uses a **difficulty-aware router** that allocates more inference compute to medium-difficulty problems and routes truly hard problems to larger/better-trained models.

### 6.4 The Cost-Performance Tradeoff

As Raschka notes:

> "Inference-time compute scaling increases the inference costs, so whether to use a small model with substantial inference scaling or training a larger model and using it with less or no inference scaling is a math that has to be worked out."
>
> -- [Raschka, 2025](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling#:~:text=inference-time%20compute%20scaling%20increases%20the%20inference%20costs)

The economics depend critically on the **inference-to-pretraining token ratio**. For a model that handles billions of queries, amortizing training cost is cheap and inference dominates. For self-improvement pipelines or low-volume applications, inference-time compute may be more economical.

### 6.5 Noam Brown's Limit Cases

Brown identified two practical ceilings for inference-time scaling:

1. **Economic constraint:** As inference extends from seconds to minutes to hours, costs accumulate. There's a spending ceiling per query.
2. **Iteration speed:** Longer reasoning creates wall-clock delays. With evaluations taking weeks, experimental iteration slows dramatically -- what Brown calls "actually the strongest case for long timelines."

---

## 7. Synthesis: Where the Field Stands

### The New Scaling Paradigm

The field has shifted from a single scaling axis (train bigger models on more data) to a **two-dimensional scaling surface** with training-time and inference-time compute as orthogonal axes. The frontier of capability is no longer just about model size -- it's about the optimal allocation of total compute between training and inference.

### Open Questions

1. **Theoretical foundations:** Why does inference-time search work so well remains empirically observed rather than theoretically proven. There is no equivalent of the Chinchilla scaling laws for inference-time compute.

2. **Verifier quality:** All search-based methods depend on reliable verifiers. Current PRMs are trained on mathematical reasoning; generalizing to open-ended tasks is an active research area.

3. **Emergent reasoning ceiling:** DeepSeek-R1-Zero showed reasoning can emerge from pure RL, but is there a ceiling? Can RL alone produce reasoning capabilities beyond what exists in the pretraining data?

4. **Compute allocation:** The difficulty-adaptive routing problem is unsolved in general. How do you estimate problem difficulty before solving it?

5. **Diminishing returns:** All empirical curves show flattening. Is there a hard ceiling on what inference-time compute can achieve for a given model, or can new techniques unlock further gains?

### The Broader Implication

The inference-time compute paradigm represents a fundamental shift in how we think about AI capability. Rather than building ever-larger monolithic models, the frontier is moving toward **systems that adaptively allocate computation based on problem difficulty** -- thinking fast on easy problems and slow on hard ones. This mirrors human cognition (Kahneman's System 1 vs. System 2) and may represent a more natural and economically sustainable path to increasingly capable AI systems.

---

## Sources

- [Lightman et al., "Let's Verify Step by Step" (2023)](https://arxiv.org/abs/2305.20050)
- [Snell et al., "Scaling LLM Test-Time Compute Optimally" (2024)](https://arxiv.org/abs/2408.03314)
- [Wu et al., "Inference Scaling Laws" (2024)](https://arxiv.org/abs/2408.00724)
- [Wei et al., "Chain-of-Thought Prompting Elicits Reasoning in LLMs" (2022)](https://arxiv.org/abs/2201.11903)
- [Wang et al., "Self-Consistency Improves Chain of Thought Reasoning" (2022)](https://arxiv.org/abs/2203.11171)
- [Yao et al., "Tree of Thoughts: Deliberate Problem Solving with LLMs" (2023)](https://arxiv.org/abs/2305.10601)
- [DeepSeek-AI, "DeepSeek-R1: Incentivizing Reasoning via RL" (2025)](https://arxiv.org/abs/2501.12948)
- [OpenAI, "Learning to Reason with LLMs" (2024)](https://openai.com/index/learning-to-reason-with-llms/)
- [Noam Brown, TED AI Conference (2024)](https://venturebeat.com/ai/openai-noam-brown-stuns-ted-ai-conference-20-seconds-of-thinking-worth-100000x-more-data)
- [Noam Brown, Latent Space Podcast (2024)](https://www.latent.space/p/noam-brown)
- [Cameron Wolfe, "Demystifying Reasoning Models" (2024)](https://cameronrwolfe.substack.com/p/demystifying-reasoning-models)
- [Sebastian Raschka, "State of LLM Reasoning and Inference Scaling" (2025)](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling)
