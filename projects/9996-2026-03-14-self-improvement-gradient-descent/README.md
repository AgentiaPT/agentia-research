---
title: "Iterative Self-Improvement at Inference Time vs. Gradient Descent During Training"
date: 2026-03-14
status: complete
tags: [ai, llm, self-improvement, gradient-descent, inference-time]
---

# Iterative Self-Improvement at Inference Time vs. Gradient Descent During Training

> **Note:** This project was authored by [Claude Code](https://claude.ai/claude-code) (AI) with human direction and review. While factual accuracy and quality were prioritized, AI-generated content may contain errors, hallucinations, or outdated information. Sources and claims should be independently verified before relying on them.

## A Theoretical Investigation

**Date**: 2026-03-14
**Status**: Complete research survey

---

## Table of Contents

1. [The Formal Analogy: Self-Critique Loops as Gradient Descent](#1-the-formal-analogy-self-critique-loops-as-gradient-descent)
2. [In-Context Learning as Implicit Gradient Descent](#2-in-context-learning-as-implicit-gradient-descent)
3. [The Information-Theoretic Argument: Can Fixed Weights Produce Genuinely Better Outputs?](#3-the-information-theoretic-argument)
4. [Activation Space Exploration via Re-Prompting](#4-activation-space-exploration-via-re-prompting)
5. [The Verifier-Generator Gap](#5-the-verifier-generator-gap)
6. [Sampling Theory: Iterative Refinement as Search](#6-sampling-theory-iterative-refinement-as-search)
7. [MCMC, Simulated Annealing, and Optimization Analogies](#7-mcmc-simulated-annealing-and-optimization-analogies)
8. [Context Window as Working Memory](#8-context-window-as-working-memory)
9. [Synthesis: A Unified View](#9-synthesis-a-unified-view)

---

## 1. The Formal Analogy: Self-Critique Loops as Gradient Descent

### The Core Question

When an LLM generates an output, critiques it, and refines it iteratively, is this process formally analogous to gradient descent on a loss function? The answer is: partially yes, with important caveats.

### Self-Refine: The Empirical Foundation

Madaan et al. (2023) introduced **Self-Refine**, the canonical framework for iterative self-improvement:

> "Like humans, large language models (LLMs) do not always generate the best output on their first try. Motivated by how humans refine their written text, we introduce Self-Refine, an approach for improving initial outputs from LLMs through iterative feedback and refinement."
> -- [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651#:~:text=Like%20humans%2C%20large%20language%20models)

The key property: **"Self-Refine does not require any supervised training data, additional training, or reinforcement learning, and instead uses a single LLM as the generator, refiner, and feedback provider."** This single-model constraint is what makes the gradient descent analogy both tempting and problematic.

### The Formal Connection: In-Context Alignment

The most rigorous theoretical treatment comes from Wang et al. (2024), presented at NeurIPS 2024:

> "LLMs are capable of improving their abilities purely by self-correction, i.e., correcting previous responses through self-examination."
> -- [A Theoretical Understanding of Self-Correction through In-context Alignment](https://arxiv.org/abs/2405.18634#:~:text=LLMs%20are%20capable%20of%20improving)

This paper formalizes self-correction as an **in-context alignment task** and demonstrates that the self-correction process operates through mechanisms analogous to in-context gradient descent. The work goes beyond previous theories on simplified linear transformers by showing the roles of **softmax attention, multi-head attention, and the MLP block** in enabling self-correction in realistic architectures.

### FormalGrad: Projected Gradient Descent

A direct analogy was drawn by FormalGrad (2025), which:

> "approximates the solution by alternating gradient proposals (soft updates) and formal verification (hard constraints), akin to projected gradient descent in continuous optimization."
> -- [FormalGrad: Integrating Formal Methods with Gradient-Based LLM Refinement](https://arxiv.org/html/2508.10059v1#:~:text=approximates%20the%20solution%20by%20alternating)

This frames the critique step as computing a "gradient direction" and the refinement step as taking a step in that direction, with verification acting as a projection back onto the feasible set.

### The Critical Limitation: Huang et al.'s Counterargument

Huang et al. (2024, ICLR) challenged the self-correction narrative:

> "LLMs struggle to self-correct their responses without external feedback, and at times, their performance even degrades after self-correction."
> -- [Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/abs/2310.01798#:~:text=LLMs%20struggle%20to%20self-correct)

This finding suggests the analogy breaks down in a crucial way: in gradient descent, the loss function provides an **objective signal**. In intrinsic self-correction, the model uses the same parameters to both generate and evaluate, meaning the "gradient" may point in the wrong direction.

---

## 2. In-Context Learning as Implicit Gradient Descent

### The Von Oswald et al. Result

Von Oswald et al. (2023, ICML) provided the foundational theoretical result:

> "Training Transformers on auto-regressive objectives is closely related to gradient-based meta-learning formulations."
> -- [Transformers learn in-context by gradient descent](https://arxiv.org/abs/2212.07677#:~:text=training%20Transformers%20on%20auto-regressive%20objectives)

Their central claim is that **"trained Transformers become mesa-optimizers i.e. learn models by gradient descent in their forward pass."** They demonstrated:

> "equivalence of data transformations induced by 1) a single linear self-attention layer and by 2) gradient-descent (GD) on a regression loss."
> -- [arxiv.org/abs/2212.07677](https://arxiv.org/abs/2212.07677#:~:text=equivalence%20of%20data%20transformations)

Crucially, they showed that **"when training self-attention-only Transformers on simple regression tasks either the models learned by GD and Transformers show great similarity or, remarkably, the weights found by optimization match the construction."**

Beyond matching gradient descent, the transformers **"surpass the performance of plain gradient descent by learning an iterative curvature correction"** -- suggesting they implement something closer to second-order optimization (like Newton's method) rather than plain SGD.

### The Akyurek et al. Result

Independently, Akyurek et al. (2023, ICLR) proved the same core result:

> "Neural sequence models, especially transformers, exhibit a remarkable capacity for in-context learning. They can construct new predictors from sequences of labeled examples (x, f(x)) presented in the input without further parameter updates. We investigate the hypothesis that transformer-based in-context learners implement standard learning algorithms implicitly, by encoding smaller models in their activations, and updating these implicit models as new examples appear in the context."
> -- [What learning algorithm is in-context learning? Investigations with linear models](https://arxiv.org/abs/2211.15661#:~:text=Neural%20sequence%20models%2C%20especially%20transformers)

They proved **"by construction that transformers can implement learning algorithms for linear models based on gradient descent and closed-form ridge regression"** and showed that **"trained in-context learners closely match the predictors computed by gradient descent, ridge regression, and exact least-squares regression, transitioning between different predictors as transformer depth and dataset noise vary."**

### What This Means for Self-Improvement

The Von Oswald/Akyurek result establishes that transformers can implement optimization algorithms **within a single forward pass** using the context window. Each layer of the transformer can be interpreted as performing one step of gradient descent on an implicit loss function. When we extend this to iterative self-refinement (multiple forward passes with critique), we get **multiple optimization trajectories** where each pass can be seen as performing additional gradient steps on the implicit objective -- but with the crucial difference that the "training data" (the critique) is itself model-generated.

---

## 3. The Information-Theoretic Argument

### Can Fixed Weights Produce Genuinely Better Outputs?

This is perhaps the deepest theoretical puzzle. If all knowledge is encoded in the model's fixed parameters, how can iteration at inference time produce outputs that are genuinely better than what the model could produce in a single pass?

### The Fundamental Limit

From an information-theoretic perspective:

> "Each floating-point parameter can only encode a finite number of bits at a given precision, and the compression of knowledge and capabilities faces insurmountable limits, which is analogous to how lossless compression algorithms cannot compress data below its entropy."
> -- [On the Fundamental Limits of LLMs at Scale](https://arxiv.org/html/2511.12869v1#:~:text=each%20floating-point%20parameter%20can%20only%20encode)

### The Resolution: Latent Knowledge Unlocking

Recent work provides a compelling resolution. The paper "Reasoning Unlocks LLM Parametric Knowledge" demonstrates:

> "enabling reasoning substantially expands the capability boundary of the model's parametric knowledge recall, unlocking correct answers that are otherwise effectively unreachable."
> -- [Reasoning Unlocks LLM Parametric Knowledge](https://www.emergentmind.com/papers/2603.09906#:~:text=enabling%20reasoning%20substantially%20expands)

Two mechanisms drive this:

1. **Computational buffer effect**: "the model uses the generated reasoning tokens to perform latent computation independent of their semantic content." Even nonsense filler text improves accuracy, suggesting the model uses extra tokens for internal computation.

2. **Factual priming via self-retrieval**: "generating topically related facts acts as a semantic bridge that facilitates correct answer retrieval." The model's own intermediate outputs serve as retrieval cues for knowledge stored in its parameters.

### The Sampling Perspective

A key insight from "Reasoning with Sampling" (2025):

> "the posttrained distribution is simply a 'sharper' version of the base model distribution, instead of placing mass on reasoning traces the base model is unlikely to generate."
> -- [Reasoning with Sampling: Your Base Model is Smarter Than You Think](https://arxiv.org/html/2510.14901v1#:~:text=the%20posttrained%20distribution%20is%20simply)

This suggests the knowledge is always present in the weights -- iteration and reasoning don't create new information but rather **navigate to regions of the output distribution where the correct answer has non-zero but low probability**. The model is not generating new knowledge; it is performing search over its own capabilities.

### The Formal Boundary

The boundary is not as fixed as it appears:

> "The boundary of an LLM's parametric knowledge is not fixed by its static parameterization, but is substantially influenced by the generative inference protocol."

This means the effective capability of a model with fixed weights is a function of **how** inference is conducted, not just **what** the weights encode.

---

## 4. Activation Space Exploration via Re-Prompting

### How Critique Navigates the Model's Capability Space

When we re-prompt a model with its own output plus a critique, we are effectively providing a **different input** that activates different regions of the model's parameter space:

> "Each prompt acts as a directional force, guiding the model's trajectory through latent space."
> -- [Navigating LLM Latent Spaces](https://theseocommunity.com/resources/best-of/mastering-llm-conversations-navigating-latent-space-with-strategic-prompts#:~:text=Each%20prompt%20acts%20as%20a%20directional%20force)

### Linear Directions in Representation Space

Research has shown that:

> "it is possible to locate linear directions in LLMs' internal representations that correspond to high-level semantic concepts such as truth or honesty, sycophancy, power and morality, or factual knowledge."

This means that when a critique says "this reasoning has an error in step 3," it is literally steering the model's activations along directions corresponding to concepts like "correctness" and "careful reasoning."

### Concept Guidance and Activation Steering

**Concept guidance** has emerged as a technique to control language model behavior by probing hidden representations for concept vectors and using them to perturb activations at inference time. When self-critique is viewed through this lens, the critique text acts as an implicit activation steering signal, pushing the model's internal representations toward "higher quality" regions of the activation space.

### LatentPrompt: Systematic Exploration

LatentPrompt (2025) provides a framework for systematic navigation:

> LatentPrompt is "a model-agnostic framework for prompt optimization that leverages latent semantic space to automatically generate, evaluate, and refine candidate prompts, beginning with seed prompts embedded in continuous latent space and systematically exploring this space to identify prompts that maximize task-specific performance."
> -- [LatentPrompt: Optimizing Prompts in Latent Space](https://arxiv.org/html/2508.02452v1#:~:text=a%20model-agnostic%20framework%20for%20prompt%20optimization)

This makes the optimization analogy explicit: prompt refinement is literally gradient-free optimization in the continuous latent space of the model.

---

## 5. The Verifier-Generator Gap

### The Computational Complexity Foundation

The hypothesis that verification is computationally easier than generation is rooted in one of the deepest questions in computer science: P vs. NP. If P != NP, then there exist problems where checking a solution is polynomially easier than finding one.

Noam Brown (OpenAI) coined the term **"Generator-Verifier Gap"** and framed it as the key to inference-time scaling:

> "When verifying a solution is easier than generating it (think Chess moves, coding, math), scaling up inference time compute gets better results."
> -- [Simons Institute](https://x.com/SimonsInstitute/status/1839354223521374581#:~:text=When%20verifying%20a%20solution%20is%20easier)

### Why This Matters for Self-Improvement

If the generator-verifier gap exists for LLMs, then a model can productively critique its own outputs because:

1. **The critique task is easier than the generation task.** Identifying that a proof step is wrong is easier than producing the correct proof step.
2. **More inference-time compute can be productively applied.** With a verifier, you can sample many candidates and select the best.
3. **The gap determines where scaling helps.** Brown's framework predicts that domains with large generator-verifier gaps (math, coding, chess) benefit most from inference-time compute, while domains with small gaps (factual recall) benefit less.

### OpenAI's "Let's Verify Step by Step"

Lightman et al. (2023) empirically validated this with **process reward models**:

> Process supervision -- providing feedback at each individual reasoning step -- "significantly outperforms outcome supervision for training models to solve problems from the challenging MATH dataset."
> -- [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050#:~:text=significantly%20outperforms%20outcome%20supervision)

This shows that step-level verification (which has a large generator-verifier gap) is more effective than outcome-level verification (where the gap is smaller).

### The Skeptical View

However, the assumption that LLMs exhibit a generator-verifier gap has been challenged:

> "verification of correctness should be easier than generation -- a rather classical argument from computational complexity -- which should be irrelevant to LLMs to the extent that what they are doing is approximate retrieval"
> -- [On the self-verification limitations of large language models](https://openreview.net/forum?id=4O0v4s3IzY#:~:text=verification%20of%20correctness%20should%20be%20easier)

The researchers found **"significant performance collapse with self-critique and significant performance gains with sound external verification,"** suggesting that the generator-verifier gap may only hold when the verifier is **external** (or at least uses a different model or different capabilities than the generator).

---

## 6. Sampling Theory: Iterative Refinement as Search

### The Fundamental Framing

Iterative refinement can be understood as search over the model's output distribution. Rather than taking a single sample from p(output | prompt), self-refinement implements an adaptive search process that explores the distribution more thoroughly.

### Base Models Are Smarter Than You Think

A key 2025 result demonstrates:

> "sampling directly from the base model can achieve single-shot reasoning capabilities on par with those from RL."
> -- [Reasoning with Sampling](https://arxiv.org/html/2510.14901v1#:~:text=sampling%20directly%20from%20the%20base%20model)

> "existing base models are much more capable at single-shot reasoning than current sampling methods reveal."
> -- [arxiv.org/html/2510.14901v1](https://arxiv.org/html/2510.14901v1#:~:text=existing%20base%20models%20are%20much%20more%20capable)

This implies the bottleneck is not the model's knowledge but the **search strategy** over its output distribution.

### Power Distributions and Implicit Planning

When sampling from p^alpha (the distribution raised to a power), the effect is:

> "encourages sampling tokens which have fewer but higher likelihood 'future paths', as opposed to tokens with several lower likelihood completions."
> -- [arxiv.org/html/2510.14901v1](https://arxiv.org/html/2510.14901v1#:~:text=encourages%20sampling%20tokens%20which%20have%20fewer)

This is **implicit forward-looking behavior** through distributional reweighting -- the model effectively plans ahead by concentrating probability mass on tokens that lead to high-quality completions.

### Best-of-N as Simple Search

Best-of-N (BoN) sampling is the simplest form of search: generate N candidates, score them, return the best. More sophisticated approaches like **iterative deepening sampling** use:

> "a novel algorithmic framework that iteratively increases the sampling budget following a geometric progression, while incorporating self-reflection mechanisms at each expansion step."
> -- [Iterative Deepening Sampling](https://arxiv.org/html/2502.05449v1#:~:text=a%20novel%20algorithmic%20framework)

### Test-Time Compute Scaling

Snell et al. (2024) established the theoretical foundation:

> "if an LLM is allowed to use a fixed but non-trivial amount of inference-time compute, how much can it improve its performance on a challenging prompt?"
> -- [Scaling LLM Test-Time Compute Optimally](https://arxiv.org/abs/2408.03314#:~:text=if%20an%20LLM%20is%20allowed%20to%20use)

Their compute-optimal scaling strategy uses two mechanisms: **(1) searching against dense, process-based verifier reward models; and (2) updating the model's distribution over a response adaptively, given the prompt at test time.**

The practical result: **"test-time compute can be used to outperform a 14x larger model"** in FLOPs-matched evaluations.

---

## 7. MCMC, Simulated Annealing, and Optimization Analogies

### LLMRefine: Explicit Simulated Annealing

Xu et al. (2023) directly frame iterative LLM refinement as simulated annealing:

> "We formulate the iterative refinement procedure into a local search problem."
> -- [LLMRefine](https://arxiv.org/html/2311.09336v3#:~:text=We%20formulate%20the%20iterative%20refinement)

The goal is **"searching for the highest scoring output according to the feedback model."** Their simulated annealing approach:

- At high temperatures: accepts potentially worse candidates (exploration)
- At low temperatures: becomes greedy (exploitation)
- **"SA combines the strengths of both alternative search procedures"** by balancing exploration vs. exploitation

Results: **"win/lose ratios are 1.56 and 1.38 respectively, indicating SA has superior performance against AA and greedy."**

### MCMC Sampling from Sharpened Distributions

Recent work uses MCMC to sample from sharpened sequence-level probability distributions of autoregressive language models:

> Grammar-constrained decoding "iteratively refines samples through local proposals that are always constraint-satisfying, with a framework that balances computational cost and sampling fidelity as the chain converges toward the true grammar-aligned distribution."
> -- [Constrained Sampling for Language Models](https://arxiv.org/html/2506.05754v1#:~:text=iteratively%20refines%20samples)

### LLMs as Markov Chains

Sarrof et al. (2024) established a rigorous Markov chain framework:

> "MC(V_K*, Q_f) is an ergodic unichain and has a unique stationary distribution."
> -- [Large Language Models as Markov Chains](https://arxiv.org/html/2410.02724v1#:~:text=is%20an%20ergodic%20unichain)

> "The stationary distribution is the long-term equilibrium of the Markov chain defined by the LLM and can be interpreted as a proxy of its understanding of natural language in its token space."
> -- [arxiv.org/html/2410.02724v1](https://arxiv.org/html/2410.02724v1#:~:text=The%20stationary%20distribution%20is%20the%20long-term)

This provides a formal convergence guarantee: iterative generation converges to a unique distribution, with convergence rate depending on context window size K and temperature. Higher temperatures lead to faster mixing but potentially lower-quality equilibria.

### The Optimization Landscape Analogy

| Concept | Gradient Descent (Training) | Iterative Self-Improvement (Inference) |
|---|---|---|
| **State** | Model weights | Output text in context |
| **Objective** | Training loss | Implicit quality function |
| **Update rule** | Gradient step | Critique + refinement |
| **Step size** | Learning rate | Degree of revision |
| **Convergence** | To loss minimum | To quality plateau (or oscillation) |
| **Exploration** | Stochastic gradients, noise | Temperature, sampling |
| **Constraints** | Regularization | Prompt structure, instructions |
| **Second-order** | Adam, natural gradient | Detailed critique, multi-aspect feedback |

---

## 8. Context Window as Working Memory

### Extending Computational Class

Merrill and Sabharwal (2024, ICLR) proved the foundational result about how chain-of-thought (using the context window as a scratchpad) extends computational power:

> "Does such intermediate generation fundamentally extend the computational power of a decoder-only transformer? We show that the answer is yes."
> -- [The Expressive Power of Transformers with Chain of Thought](https://arxiv.org/abs/2310.07923#:~:text=Does%20such%20intermediate%20generation%20fundamentally)

The amount of extension depends on how many intermediate tokens are generated:

- **Logarithmic steps**: "push the limits of standard transformers only slightly"
- **Linear steps**: "adds a clear new ability (under standard complexity conjectures): recognizing all regular languages" and keeps decoders "within context-sensitive languages"
- **Polynomial steps**: "make them recognize exactly the class of polynomial-time solvable problems" -- the **first exact characterization of a type of transformers in terms of standard complexity classes**

### The Serial Computation Gap

Standard transformers are fundamentally parallel processors. Chain of thought fills a critical gap:

> "CoT empowers the model with the ability to perform inherently serial computation, which is otherwise lacking in transformers, especially when depth is low."

With T steps of chain-of-thought, **"constant-depth transformers using constant-bit precision and O(log n) embedding size can solve any problem solvable by boolean circuits of size T."**

### Working Memory as Computation Extension

The context window serves as working memory in multiple ways:

1. **Scratchpad**: Intermediate results that would overflow the model's fixed-depth computation can be externalized to the context.
2. **Self-retrieval**: Previously generated tokens serve as retrieval cues for knowledge in the parameters.
3. **State tracking**: The context maintains state across what would otherwise be stateless forward passes.
4. **Iterative deepening**: Each self-critique cycle adds more "working memory" about what went wrong, enabling the model to attend to failure modes on subsequent passes.

### Self-Notes: Explicit Working Memory

Lanchantin et al. (2023) introduced **Self-Notes**, where:

> "Self-Notes can act as both explicit intermediate reasoning steps and working memory for state-tracking."
> -- [Learning to Reason and Memorize with Self-Notes](https://arxiv.org/pdf/2305.00833#:~:text=Self-Notes%20can%20act%20as%20both)

---

## 9. Synthesis: A Unified View

### The Core Theoretical Picture

Bringing together all eight dimensions, here is a unified theoretical framework for understanding iterative self-improvement at inference time:

**Layer 1: Computational Equivalence (Weak Form)**
In-context learning in transformers implements gradient descent on implicit loss functions (Von Oswald et al., Akyurek et al.). Self-critique loops extend this by performing multiple "optimization steps" across forward passes, with the critique serving as a noisy gradient signal.

**Layer 2: The Search Interpretation**
Iterative refinement is fundamentally **search over the model's output distribution**. The model's weights define a vast space of possible outputs; single-pass generation samples from this space once, while iterative refinement performs guided search. The generator-verifier gap determines whether this search can be productive.

**Layer 3: The Information-Theoretic Bound**
No genuinely new information is created. All improvements come from better navigating existing knowledge in the weights. But this is not a trivial constraint -- the "effective knowledge boundary" of a model is substantially larger than what single-pass generation accesses. Reasoning unlocks parametric knowledge that is otherwise unreachable.

**Layer 4: The Computational Extension**
Chain-of-thought and context-window-as-scratchpad provably extend the computational class of transformers. With polynomial intermediate tokens, transformers can solve any problem in P. Self-improvement loops leverage this extended computation to solve problems that would be impossible in a single forward pass.

**Layer 5: The Optimization Landscape**
The refinement process navigates an optimization landscape where:
- The "position" is the current output
- The "gradient" is the critique
- The "objective" is the implicit quality function
- **Simulated annealing** provides the right framework when exploration-exploitation tradeoffs matter
- **MCMC** provides convergence guarantees to a stationary distribution
- The process can get stuck (self-correction failure) when the model's verifier and generator share the same biases

### Key Tensions and Open Questions

1. **Intrinsic vs. extrinsic feedback**: The analogy to gradient descent is strongest when an external verifier provides the critique signal. When the model critiques itself, the "gradient" may be systematically biased, leading to performance degradation rather than improvement.

2. **Convergence vs. oscillation**: Unlike gradient descent with a convex loss, self-refinement has no convergence guarantees in general. The Markov chain framework suggests convergence to a stationary distribution, but this distribution may not correspond to "high quality."

3. **Diminishing returns**: Empirically, most improvement happens in the first 1-3 refinement steps. This is consistent with the optimization analogy (early steps make large improvements, later steps are marginal) but also with the information-theoretic bound (the model quickly exhausts its ability to recombine existing knowledge).

4. **The depth-breadth tradeoff**: Is it better to refine one output deeply (gradient descent analogy) or sample many outputs and select the best (best-of-N / search analogy)? Snell et al. show this depends on problem difficulty -- easy problems benefit from breadth, hard problems from depth.

5. **Emergent vs. retrievable knowledge**: When reasoning "unlocks" knowledge, is this genuinely emergent recombination, or is it retrieval of patterns seen during training? The distinction matters for understanding the fundamental limits of self-improvement.

---

## Source Index

### Foundational Papers

| Paper | Authors | Venue | Key Contribution |
|---|---|---|---|
| [Transformers learn in-context by gradient descent](https://arxiv.org/abs/2212.07677) | Von Oswald et al. | ICML 2023 | Transformers implement GD in forward pass |
| [What learning algorithm is in-context learning?](https://arxiv.org/abs/2211.15661) | Akyurek et al. | ICLR 2023 | ICL implements GD, ridge regression |
| [Self-Refine](https://arxiv.org/abs/2303.17651) | Madaan et al. | NeurIPS 2023 | Iterative self-feedback framework |
| [Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/abs/2310.01798) | Huang et al. | ICLR 2024 | Limits of intrinsic self-correction |
| [The Expressive Power of Transformers with Chain of Thought](https://arxiv.org/abs/2310.07923) | Merrill & Sabharwal | ICLR 2024 | CoT extends computational class to P |
| [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050) | Lightman et al. | ICLR 2024 | Process reward models for verification |

### Theoretical Frameworks

| Paper | Authors | Key Contribution |
|---|---|---|
| [A Theoretical Understanding of Self-Correction through In-context Alignment](https://arxiv.org/abs/2405.18634) | Wang et al. | Self-correction as in-context alignment (NeurIPS 2024) |
| [Scaling LLM Test-Time Compute Optimally](https://arxiv.org/abs/2408.03314) | Snell et al. | Compute-optimal inference scaling |
| [Large Language Models as Markov Chains](https://arxiv.org/html/2410.02724v1) | Sarrof et al. | LLMs have unique stationary distributions |
| [On the Fundamental Limits of LLMs at Scale](https://arxiv.org/html/2511.12869v1) | -- | Information-theoretic bounds on LLM capacity |
| [FormalGrad](https://arxiv.org/html/2508.10059v1) | -- | Self-refinement as projected gradient descent |

### Sampling and Search

| Paper | Authors | Key Contribution |
|---|---|---|
| [Reasoning with Sampling](https://arxiv.org/html/2510.14901v1) | -- | Base models are smarter than sampling reveals |
| [Reasoning Unlocks LLM Parametric Knowledge](https://www.emergentmind.com/papers/2603.09906) | -- | Reasoning expands effective knowledge boundary |
| [LLMRefine](https://arxiv.org/html/2311.09336v3) | Xu et al. | Simulated annealing for text refinement |
| [Constrained Sampling for Language Models](https://arxiv.org/html/2506.05754v1) | -- | MCMC for grammar-constrained decoding |
| [Iterative Deepening Sampling](https://arxiv.org/html/2502.05449v1) | -- | Geometric budget expansion with self-reflection |

### Verification and Self-Correction

| Paper | Key Contribution |
|---|---|
| [On the self-verification limitations of LLMs](https://openreview.net/forum?id=4O0v4s3IzY) | Self-critique causes performance collapse |
| [When Can LLMs Actually Correct Their Own Mistakes?](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00713/125177/) | Critical survey of self-correction capabilities |
| [LatentPrompt](https://arxiv.org/html/2508.02452v1) | Prompt optimization in latent semantic space |

### Context and Computation

| Paper | Key Contribution |
|---|---|
| [Learning to Reason and Memorize with Self-Notes](https://arxiv.org/pdf/2305.00833) | Self-Notes as working memory |
| [Chain of Thought Empowers Transformers to Solve Inherently Serial Problems](https://openreview.net/forum?id=3EWTEy9MTM) | CoT enables serial computation in parallel architectures |
