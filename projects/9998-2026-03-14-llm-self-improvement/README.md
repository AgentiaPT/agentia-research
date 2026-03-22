---
title: "Why LLMs Improve When They Critique and Refine Their Own Outputs"
date: 2026-03-14
status: complete
tags: [ai, llm, self-refinement, self-correction, constitutional-ai]
explorers:
  - file: research.html
    title: The Paradox of Self-Improvement
    description: Interactive research essay on why LLMs produce better output when forced to critique and refine their own work
    screenshot: research-screenshot.png
---

# Why LLMs Improve When They Critique and Refine Their Own Outputs

> ✨ This project was authored by [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (AI) with human direction and review. While factual accuracy and quality were prioritized, AI-generated content may contain errors, hallucinations, or outdated information. Sources and claims should be independently verified before relying on them.

A deep research survey on self-refinement, self-correction, and iterative improvement in large language models.

---

## 1. Self-Refine (Madaan et al., 2023)

**Paper:** [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651#:~:text=Like%20humans%2C%20large%20language%20models) (NeurIPS 2023)

### Core Idea

A single LLM acts as generator, critic, and refiner in an iterative loop -- no additional training, no reinforcement learning, no extra models. The process mirrors how humans revise their own writing.

### Mechanism

1. **Generate** an initial output
2. **Feedback**: the same LLM critiques the output
3. **Refine**: the LLM revises based on its own feedback
4. Repeat steps 2-3 until a stopping criterion is met (up to 4 iterations)

### Key Results

> "Like humans, large language models (LLMs) do not always generate the best output on their first try."
> -- [Madaan et al., 2023](https://arxiv.org/abs/2303.17651#:~:text=Like%20humans%2C%20large%20language%20models)

- **~20% absolute improvement** on average across 7 tasks compared to single-pass generation
- Improvements ranged from **5% to 40%** depending on the task
- **Sentiment Reversal**: improved by at least 21.6 points
- **Code Optimization**: score improved from 22.0 to 28.8
- Evaluated on GPT-3.5, ChatGPT, and GPT-4 -- even GPT-4 improved with self-refinement
- Human evaluators and automatic metrics consistently preferred Self-Refine outputs

### The 7 Tasks Evaluated

Review rewriting, acronym generation, story generation, code rewriting, response generation, constrained generation, and toxicity removal.

### Why It Matters

Self-Refine demonstrated that the capacity for improvement already exists within the model's weights. The same model that generates a mediocre first draft can, when prompted to critique it, identify specific flaws and produce better output. No external oracle is needed.

---

## 2. Constitutional AI (Anthropic, Bai et al., 2022)

**Paper:** [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073#:~:text=harmless%20AI%20assistant%20that%20engages) (Anthropic)

### Core Idea

Train harmless AI assistants through self-improvement, using only a set of principles ("a constitution") rather than extensive human feedback labels. The model critiques and revises its own outputs guided by constitutional principles.

### Two-Phase Training Process

**Phase 1 -- Supervised Self-Critique:**

> "sample from an initial model, then generate self-critiques and revisions, and then finetune the original model on revised responses."
> -- [Bai et al., 2022](https://arxiv.org/abs/2212.08073#:~:text=sample%20from%20an%20initial%20model)

The model generates a response to a harmful prompt, then critiques its own response against a randomly selected constitutional principle, then rewrites the response to comply. The revised responses become training data.

**Phase 2 -- RL from AI Feedback (RLAIF):**

The model evaluates pairs of its own responses, choosing which is better. These AI-generated preferences train a reward model, which then guides reinforcement learning. This replaces human labelers with the model's own judgment.

### Key Results

- Produces **"a harmless but non-evasive AI assistant that engages with harmful queries by explaining its objections to them"** rather than simply refusing
- Both phases **"can leverage chain-of-thought style reasoning to improve the human-judged performance and transparency of AI decision making"**
- The RL-CAI assistant was **preferred by crowdworkers** over assistants trained with human feedback labels
- Makes it **"possible to control AI behavior more precisely and with far fewer human labels"**
- Follow-up implementations showed CAI can boost harmlessness metrics by ~40%

### Why It Matters

Constitutional AI shows that self-critique is not just a test-time trick -- it can be baked into training itself. The model's ability to evaluate its own outputs against principles creates a scalable alignment technique that reduces dependence on human annotators.

---

## 3. Reflexion (Shinn et al., 2023)

**Paper:** [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366#:~:text=reinforce%20language%20agents%20not%20by%20updating%20weights) (NeurIPS 2023)

### Core Idea

> "a novel framework to reinforce language agents not by updating weights, but instead through linguistic feedback"
> -- [Shinn et al., 2023](https://arxiv.org/abs/2303.11366#:~:text=reinforce%20language%20agents%20not%20by%20updating%20weights)

Agents verbally reflect on task feedback and store reflective text in an episodic memory buffer to improve subsequent attempts.

### Architecture

Three components work together:

1. **Actor**: generates text/actions based on observations
2. **Evaluator**: scores the actor's output (e.g., binary success/failure)
3. **Self-Reflection**: an LLM generates verbal reinforcement cues using the reward signal, current trajectory, and persistent memory

The self-reflective feedback acts as a "semantic gradient signal" -- it gives the agent a concrete direction for improvement rather than just a scalar reward.

### Key Results

- **HumanEval (coding)**: 91% pass@1 accuracy, surpassing GPT-4's 80%
- **AlfWorld (sequential decision-making)**: completed 130 out of 134 tasks with ReAct + Reflexion
- **HotPotQA**: ~20 point improvement in exact-match accuracy over baseline
- Achieves state-of-the-art on multiple code generation benchmarks

### Why It Matters

Reflexion shows that "verbal reinforcement" -- the model telling itself in natural language what it did wrong and what to try next -- can substitute for weight updates. The model doesn't learn in the traditional sense (no gradient descent), but it effectively learns within its context window by accumulating reflective experience.

---

## 4. The "Revision" Capability: Why Can Models Improve Text They Already Generated?

### The Generation-Verification Gap

The most compelling theoretical explanation comes from what Noam Brown calls **"a generator verifier gap"**:

> "I view it as the kinds of problems where there is a benefit from being able to consider more options and think for longer. You might call it...a generator verifier gap."
> -- [Noam Brown, Sequoia Capital podcast](https://sequoiacap.com/podcast/training-data-noam-brown/#:~:text=generator%20verifier%20gap)

This concept has deep roots in computational complexity theory. The P vs NP question captures precisely this asymmetry: **verifying a solution is often computationally easier than generating one**. In the LLM context:

- **Generating** a perfect response in one pass requires the model to make every token-level decision correctly in sequence
- **Evaluating** whether a completed response has problems is a different, often easier task
- **Revising** a specific identified flaw is easier than generating the whole thing from scratch

### Why Revision Works Mechanically

When a model reads its own output and is asked to critique it, several things change computationally:

1. **Different attention patterns**: During generation, the model attends to the prompt and its own partial output. During critique, it attends to the complete output as a whole, enabling global coherence assessment that wasn't possible during autoregressive generation.

2. **Different prompt context**: The critique prompt frames the task as evaluation rather than generation, activating different learned behaviors from training data (the model has seen many examples of reviews, critiques, and editorial feedback).

3. **Full-sequence visibility**: Autoregressive generation is inherently local -- each token is predicted based only on preceding tokens. Critique has access to the full output, enabling detection of issues like logical inconsistencies, repetition, or structural problems that emerge only at the sequence level.

4. **Task decomposition**: Revision breaks a hard problem (generate perfect output) into two easier sub-problems (identify what's wrong, then fix that specific thing).

### The Exponential Divergence Problem

Yann LeCun has formalized why single-pass generation is inherently limited:

> "I have claimed that Auto-Regressive LLMs are exponentially diverging diffusion processes... Let e be the probability that any generated token exits the tree of 'correct' answers. Then the probability that an answer of length n is correct is (1-e)^n"
> -- [Yann LeCun](https://x.com/ylecun/status/1640122342570336267#:~:text=exponentially%20diverging%20diffusion%20processes)

This mathematical argument explains why revision helps: if each token has a small probability of being wrong, longer outputs become increasingly likely to contain errors. Revision provides an opportunity to catch and fix these accumulated errors after the full sequence exists.

---

## 5. Is This Truly "Self-Improvement" or Accessing Different Parts of the Weight Space?

### The Skeptical View: It's Not Real Self-Improvement

**Huang et al. (2023)** directly challenged the self-improvement narrative in their paper [Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/abs/2310.01798#:~:text=LLMs%20struggle%20to%20self-correct):

> "LLMs struggle to self-correct their responses without external feedback, and at times, their performance even degrades after self-correction."
> -- [Huang et al., 2023](https://arxiv.org/abs/2310.01798#:~:text=LLMs%20struggle%20to%20self-correct)

Key findings:
- On GSM8K math problems, **self-correction consistently decreased performance**
- Models changed correct answers to wrong ones **more often** than they fixed actual errors
- LLMs are poorly calibrated -- they express high confidence in wrong answers and doubt correct ones
- **"Intrinsic self-correction"** (without external feedback) largely does not work for reasoning tasks

### The Nuanced View: Different Tasks, Different Results

The critical distinction is between:

- **Tasks with verifiable outputs** (code that compiles, text matching criteria): self-correction works well because the model gets a reliable signal
- **Open-ended reasoning** (math, logic): self-correction often fails because the model cannot reliably distinguish correct from incorrect reasoning
- **Subjective quality** (writing style, tone, engagement): self-refinement works well because "better" is genuinely subjective and the model's second opinion is valid

### What's Actually Happening in the Weights

The most accurate framing is that self-refinement **activates different capabilities that coexist within the same weight space**:

- **Generation mode**: The model samples from learned distributions, optimizing for fluency and plausibility
- **Evaluation mode**: When prompted to critique, different attention patterns activate, engaging the model's learned understanding of quality criteria
- **Revision mode**: The model applies targeted edits guided by specific feedback, a more constrained generation task

These are not separate "modes" in a hard-coded sense -- they emerge from the fact that the model was trained on data containing generation, evaluation, and revision. The weights encode all three capabilities; the prompt determines which is activated.

### SCoRe: Teaching Real Self-Correction via RL

Google DeepMind's **SCoRe** ([Self-Correction via Reinforcement Learning](https://arxiv.org/abs/2409.12917#:~:text=self-correction%20via%20reinforcement%20learning), 2024) showed that genuine self-correction can be trained:

> SCoRe uses "a multi-turn online reinforcement learning approach that significantly improves an LLM's self-correction ability using entirely self-generated data"

Key results:
- **15.6 percentage point improvement** on MATH benchmark
- **9.1 percentage point improvement** on HumanEval
- Two-stage training prevents the model from learning to just "produce the best first-attempt response and only minorly edit it"
- Importantly, **reduced instances where the model changed correct answers to incorrect ones** -- the exact failure mode Huang et al. identified

---

## 6. What Happens Computationally When a Model Reads Its Own Output?

### The Attention Mechanism Perspective

When a transformer processes its own previous output for critique:

1. **Query-Key-Value computation**: Each token in the critique context generates query vectors that attend over the full original output. The attention scores create a weighted representation emphasizing the most relevant parts of the output for evaluation.

2. **Layer-by-layer refinement**: In early layers, the model builds syntactic and local semantic representations. In deeper layers, it constructs abstract representations that can capture logical structure, argument flow, and factual consistency.

3. **Specialized heads**: Research shows that different attention heads specialize -- some track syntactic dependencies, others semantic relationships, others long-range coherence. During critique, the heads tracking coherence and consistency become more informative than during generation.

4. **Residual stream accumulation**: Through the residual connections, each layer adds its analysis to a growing representation. By the final layer, the model has built a rich, multi-level understanding of the output that was never available during token-by-token generation.

### The Key Asymmetry

During **generation**, the model commits to each token sequentially with no ability to revise earlier decisions. During **critique**, the model sees the complete output and can reason about global properties (coherence, completeness, accuracy) that only emerge from the full sequence.

This is analogous to the difference between writing a chess move and evaluating a board position -- the same neural network can do both, but evaluation benefits from seeing the complete state.

---

## 7. Theoretical Frameworks for Why Iterative Refinement Works

### Framework 1: The Generation-Verification Gap Hypothesis

The [Generation-Verification Gap Hypothesis](https://www.emergentmind.com/topics/generation-verification-gap-hypothesis#:~:text=generation-verification%20gap) formalizes the observation that:

- Some hypothesis classes are **generatable but not predictable** (VC dimension and Closure dimension govern distinct properties)
- This gap "is not solely an artifact of flawed practice but often reflects real, intrinsic limitations"
- The practical implication: interleaving verification with generation -- as Self-Refine does -- partially closes this gap

### Framework 2: Test-Time Compute Scaling

Noam Brown's research demonstrates that more computation at inference time translates directly to better performance:

> "It turned out that having a bot think for just 20 seconds in a hand of poker got the same boosting performance as scaling up the model by 100,000x and training it for 100,000 times longer"
> -- [Noam Brown, TED AI Conference 2024](https://venturebeat.com/ai/openai-noam-brown-stuns-ted-ai-conference-20-seconds-of-thinking-worth-100000x-more-data#:~:text=20%20seconds%20of%20thinking)

The crucial insight is that this is general-purpose, not domain-specific:

> "the way that it's thinking for longer is actually quite general and can be used for a lot of different domains"
> -- [Noam Brown, Sequoia Capital](https://sequoiacap.com/podcast/training-data-noam-brown/#:~:text=quite%20general)

Brown also articulated the System 1/System 2 framing:

> "you need a certain level of intellectual ability, just in terms of System 1 in order to benefit from System 2"
> -- [Noam Brown, Latent Space podcast](https://www.latent.space/p/noam-brown#:~:text=System%201%20in%20order%20to%20benefit%20from%20System%202)

This explains why self-refinement works better with stronger models: the base capability (System 1) must be sufficient for the deliberative process (System 2) to help.

### Framework 3: Iterative Narrowing of the Solution Space

Each refinement iteration narrows the search space:

- **Iteration 0**: Generate from the full distribution of possible outputs
- **Iteration 1**: Critique identifies specific problems, constraining the space to outputs that fix those problems
- **Iteration 2**: Further critique identifies remaining issues, narrowing further
- Diminishing returns occur naturally as the easy improvements are captured first

This mirrors gradient descent conceptually -- each step moves toward a better solution, with the critique serving as an approximate gradient in natural language.

### Framework 4: Ensemble Effect via Sequential Sampling

Self-refinement can be viewed as a form of sequential ensembling. Each iteration samples from a slightly different conditional distribution (conditioned on the critique), and the final output benefits from having effectively consulted multiple "versions" of the model's judgment. This is similar to how majority voting over multiple samples improves accuracy, but structured through the critique-revision loop.

---

## 8. Expert Opinions

### Noam Brown (OpenAI)

Brown's work on poker AI and OpenAI's o1 model provides the most direct evidence for why iterative reasoning helps. His key insight: the same model that plays mediocre poker in real-time plays vastly better when given time to search and reconsider.

> "One way to think about reasoning is there are some problems that benefit from being able to think about it for longer."
> -- [Noam Brown](https://sequoiacap.com/podcast/training-data-noam-brown/#:~:text=benefit%20from%20being%20able%20to%20think)

He envisions scaling this dramatically:

> "We're going to get them thinking instead of three minutes, they're for three hours, and then three days, and then three weeks"
> -- [Noam Brown, Latent Space](https://www.latent.space/p/noam-brown#:~:text=three%20hours%2C%20and%20then%20three%20days)

And notes that models are getting better at using this time:

> "these models are becoming more efficient in the way they're thinking, and so they're able to do more with the same amount of test-time compute"
> -- [Noam Brown, Latent Space](https://www.latent.space/p/noam-brown#:~:text=more%20efficient%20in%20the%20way%20they%27re%20thinking)

### Yann LeCun (Meta)

LeCun remains skeptical that autoregressive self-correction can overcome the fundamental limitations of the architecture:

> "Auto-Regressive LLMs can't plan (and can't really reason)."
> -- [Yann LeCun on X](https://x.com/ylecun/status/1702027572077326505#:~:text=Auto-Regressive%20LLMs%20can%27t%20plan)

He views the error accumulation problem as fundamental, and argues that iterative refinement within the autoregressive paradigm is a bandage, not a cure. His proposed alternative: **world models** that learn from interaction with the environment, enabling genuine planning and reasoning rather than pattern-matched self-critique.

### Ilya Sutskever (Safe Superintelligence Inc.)

At NeurIPS 2024, Sutskever acknowledged the power of reasoning-time computation while noting its implications:

> "AI systems that reason will be able to correct themselves, much like autocorrect -- but far grander."
> -- [Ilya Sutskever, NeurIPS 2024](https://dlyog.com/papers/one_internet_v1#:~:text=autocorrect)

But he also warned:

> "The more it reasons, the more unpredictable it becomes"
> -- [Ilya Sutskever, NeurIPS 2024](https://deepnewz.com/ai-modeling/ilya-sutskever-neurips-2024-ai-s-reasoning-power-to-make-technology-less-8008fa08#:~:text=unpredictable)

Sutskever's view suggests that self-correction and reasoning are genuinely powerful capabilities, not illusions -- but they come with the cost of reduced predictability, which has profound safety implications.

---

## 9. The Mirror Problem: Human vs. LLM Self-Revision Without External Feedback

The core question in LLM self-improvement has a deeper analogue: **can any information-processing system reliably improve its own outputs without external validation?** The cognitive science evidence suggests the answer is more uncomfortable than the AI literature acknowledges -- because humans are far worse at this than we assume.

### The Parallel Failure Modes

When an LLM generates output, critiques it, and revises -- all without external feedback -- it faces a fundamental problem: the same weights that produced the original error are evaluating whether the error exists. The cognitive science literature reveals that humans face a structurally identical problem.

**Dunning-Kruger and the Metacognitive Blind Spot.** In their landmark review, Dunning, Heath, and Suls found that "people's self-views hold only a tenuous to modest relationship with their actual behavior and performance" -- with correlations between self-assessed and actual ability being consistently moderate to meager across domains including health, education, and workplace performance ([Dunning et al., 2004](https://journals.sagepub.com/doi/10.1111/j.1529-1006.2004.00018.x#:~:text=tenuous%20to%20modest%20relationship)). The core mechanism: the skills required to produce a competent response are the same skills required to recognize that a response is incompetent. This is not merely a human cognitive bias -- it is a structural property of any system that uses the same process for generation and evaluation.

**The Writer's Blind Spot.** The proofreading literature provides a vivid demonstration. When writers re-read their own text, their brains process what they *intended* to write rather than what appears on the page -- a form of [top-down perceptual completion](https://smallbluedog.com/proofreading-our-own-work-overcoming-autocorrect.html#:~:text=proofreading%20blind%20spots) where the mental model overrides the sensory input. Writing guides universally recommend temporal distance -- "put it in a drawer for a week" -- as the primary remedy. This works not because new information arrives, but because the writer's internal model partially decays, allowing perception to dominate over expectation.

**WYSIATI and Post-Hoc Rationalization.** Kahneman's WYSIATI principle -- "What You See Is All There Is" -- describes how System 1 constructs a coherent story from available information without recognizing what is missing: "You build the best possible story from the information available to you, and if it is a good story, you believe it" ([Kahneman, 2011](https://en.wikipedia.org/wiki/Thinking,_Fast_and_Slow#:~:text=You%20build%20the%20best%20possible%20story)). This applies directly to self-revision: when a system (human or LLM) re-evaluates its own output, it tends to construct a post-hoc rationalization of *why the output is correct* rather than genuinely searching for flaws. Both humans and LLMs exhibit a striking pattern: high confidence in probabilistic outputs that happens to be the most likely prediction, treated post-hoc as near-certainty. The revision process then becomes confirmation rather than genuine evaluation.

**The AI-Metacognition Paradox.** A 2025 study by Fernandes et al. found that when humans use AI to complete reasoning tasks, the Dunning-Kruger effect *disappears* -- but not in the way you'd hope. Performance improved by 3 points, but participants overestimated their performance by 4 points. Worse, "higher AI literacy correlated with lower metacognitive accuracy" -- those who knew more about AI were *more* confident but *less* accurate in judging their own performance ([Fernandes et al., 2025](https://www.sciencedirect.com/science/article/pii/S0747563225002262#:~:text=overestimated%20their%20task%20performance)). The researchers concluded: "current AI tools are not fostering metacognition and users are not learning about their mistakes." This suggests that AI-assisted self-evaluation may compound the calibration problem rather than solve it.

### Where Humans Have a Genuine Architectural Advantage

**The Error-Related Negativity (ERN).** The human brain possesses dedicated error-detection circuitry that operates semi-independently from the generation process. The ERN -- a sharp negative ERP component generated in the anterior cingulate cortex -- fires within 80-150 milliseconds of an erroneous response, often *before conscious awareness of the error* ([Wikipedia: ERN](https://en.wikipedia.org/wiki/Error-related_negativity#:~:text=80%20to%20150%20milliseconds)). Research shows the ERN reflects "an internal comparison, by the anterior cingulate cortex, of two signals: an unconscious representation of the ongoing action and a conscious representation of the intended one." Critically, ERN amplitude increases with growing error awareness in multiple studies, linking this preconscious signal to eventual conscious error detection ([Wessel et al., 2011](https://pmc.ncbi.nlm.nih.gov/articles/PMC3328124/#:~:text=enlarged%20ERN%20for%20reported%20vs.%20non-reported%20errors)).

An LLM has no architectural equivalent. Its "evaluation" of its own output uses the same transformer layers, the same attention mechanism, and the same weights that generated the output. There is no separate error-detection circuit that can fire independently.

**Somatic Markers: The Embodied Error Signal.** Damasio's somatic marker hypothesis proposes that emotional processes -- experienced as bodily feelings -- guide decision-making by associating physiological responses with past outcomes ([Damasio, 1996](https://pubmed.ncbi.nlm.nih.gov/8941953/#:~:text=somatic%20marker)). The "gut feeling" that something is wrong is a real neural signal processed in the ventromedial prefrontal cortex and amygdala -- architecturally separate from the language and reasoning systems. When a human re-reads their work and experiences unease without being able to articulate why, this is the somatic marker system providing an independent evaluation channel. LLMs have no embodied experience, no emotional valence, and no equivalent of "this feels wrong but I can't say why."

**Multi-System Cross-Checking.** The dual-process framework (Stanovich & West) describes how System 2 can override System 1 responses by detecting conflicts between intuitive outputs and normative rules. De Neys (2012) showed that even children as young as 7-8 implicitly register logical-normative violations during heuristic-biased tasks -- evidenced by prolonged response times and error-related EEG signals. However, the override failure rate is substantial: adults frequently fail to override System 1 biases even when they possess the analytical competence, particularly under fatigue, time pressure, or competing cognitive demands.

**Incubation and Unconscious Restructuring.** Perhaps the strongest human advantage: the ability to restructure a problem representation without any new information. Sio and Ormerod's meta-analysis of 117 studies (3,606 participants) found a positive incubation effect with a median effect size of d = 0.26 and a mean of d = 0.41 ([Sio & Ormerod, 2009](https://pubmed.ncbi.nlm.nih.gov/19210055/#:~:text=positive%20incubation%20effect)). Baird et al. (2012) demonstrated that engaging in an undemanding task during incubation (which maximizes mind wandering) "led to substantial improvements in performance on previously encountered problems" -- improvements that were not attributable to explicitly directed thoughts about the task ([Baird et al., 2012](https://journals.sagepub.com/doi/abs/10.1177/0956797612446024#:~:text=substantial%20improvements%20in%20performance)).

The sleep data is even more striking. Wagner et al. (2004) found that approximately 60% of participants discovered a hidden rule after sleeping, versus 23% in groups that did not sleep. Cai et al. (2009) reported that REM sleep groups improved by almost 40% on creativity tasks ([Ritter & Dijksterhuis, 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC3990058/#:~:text=60%25%20discovered%20the%20rule)).

The key mechanism: "conscious thought may be focused and convergent, whereas unconscious thought may be more associative and divergent" ([Ritter & Dijksterhuis, 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC3990058/#:~:text=conscious%20thought%20may%20be%20focused%20and%20convergent)). During incubation, the brain doesn't just rest -- it actively reorganizes the problem representation, forming novel associations that were previously suppressed by goal-directed thinking.

An LLM's weights are frozen between agentic loop iterations. It cannot restructure its internal representation of a problem. It can only re-approach the same fixed representation with different input context.

### The Developmental Parallel: Scale Thresholds in Both Systems

A striking parallel emerges between cognitive development in children and model scale in LLMs. De Neys (2012) found that **conflict detection -- the ability to implicitly notice when a heuristic response violates logical norms -- is absent in young children (third graders) and develops through adolescence** ([De Neys, 2012](https://journals.sagepub.com/doi/abs/10.1177/1745691611429354#:~:text=conflict%20sensitivity)). Third graders were "fully confident that their response was correct and did not show any sensitivity to their errors."

In LLMs, the pattern is remarkably similar: **self-correction requires a minimum model scale**. Research shows a threshold around 3.8B parameters for moral self-correction to emerge, and models below 22B parameters generally cannot self-correct effectively. For small models (335M-775M parameters), self-correction "does not contribute to improvement and even leads to worse performance" ([Smaller LLMs Can Do Moral Self-Correction, 2024](https://arxiv.org/html/2410.23496#:~:text=3.8B)). This maps directly to Noam Brown's observation: "you need a certain level of intellectual ability, just in terms of System 1 in order to benefit from System 2."

Both systems require a minimum "base capability" before self-monitoring becomes effective. Below that threshold, the self-correction process either does nothing or actively degrades performance -- in both children and small LLMs.

### When Introspection Makes Things Worse

Wilson and Schooler (1991) demonstrated that **analyzing reasons can actually reduce the quality of decisions**. When students were asked to introspect about why they preferred certain strawberry jams, their preferences diverged from expert ratings -- while students who simply chose without analysis aligned better with experts. The mechanism: "analyzing reasons can focus people's attention on nonoptimal criteria" ([Wilson & Schooler, 1991](https://pubmed.ncbi.nlm.nih.gov/2016668/#:~:text=nonoptimal%20criteria)). Introspection activated surface-level, easily verbalizable attributes at the expense of holistic judgment.

This directly parallels Huang et al.'s finding that LLM self-correction on reasoning tasks makes performance *worse*. The model's "critique" focuses attention on surface features of the reasoning (does it look right?) rather than deep logical structure (is it right?), and the revision process introduces new errors while "fixing" things that weren't broken. In both systems, forced introspection without reliable evaluation criteria degrades rather than improves output.

### Why the Human Advantage Is Smaller Than It Appears

Despite these architectural differences, the empirical evidence suggests humans are only **modestly better** at self-revision without external feedback:

| Dimension | Humans | LLMs | Advantage |
|-----------|--------|------|-----------|
| **Self-assessment accuracy** | "Tenuous to modest" correlation with actual performance (Dunning et al.) | Poor calibration; changes correct answers to wrong ones as often as vice versa (Huang et al.) | Slight human edge |
| **Error detection without feedback** | ERN fires preconsciously, but often fails to reach awareness; override failure is common | No dedicated error circuit; relies on attention asymmetry | Moderate human edge |
| **Incubation / restructuring** | d = 0.26-0.41 effect; 60% vs 23% insight after sleep | No equivalent; frozen weights between passes | Strong human edge |
| **Confirmation bias in revision** | WYSIATI; post-hoc rationalization; neural amplification of confirmatory evidence | Same-weights evaluation; plausible-sounding but empty critiques | Similar failure mode |
| **Task-dependent success** | Good at surface quality; poor at own reasoning errors | Good at surface quality; poor at own reasoning errors | Strikingly parallel |
| **Post-hoc rationalization** | Choice-supportive bias; confidence increases after decision; WYSIATI | 80-100% expressed confidence regardless of accuracy; RLHF amplifies | Same failure pattern |
| **Improvement with external feedback** | Dramatic improvement | Dramatic improvement | Both systems need it |

A 2025 meta-analysis of 41 studies (4,813 participants) comparing AI-generated and human-provided feedback found "no statistically significant differences in learning performance" (Hedge's g = 0.25) -- suggesting the two systems are empirically comparable as external evaluators, even if their internal self-evaluation mechanisms differ ([Educational Psychology Review, 2025](https://www.tandfonline.com/doi/full/10.1080/01443410.2025.2553639#:~:text=no%20statistically%20significant%20differences)).

### Counterpoint: Structured Introspection Can Work

The convergence thesis has exceptions. A 2024 study showed that LLMs can self-correct without external feedback by masking key conditions in the original question and constructing verification questions -- yielding +6.8 exact match on open-domain QA, +14.1 on arithmetic reasoning, and +9.6 on commonsense reasoning ([EMNLP 2024](https://aclanthology.org/2024.emnlp-main.714/#:~:text=key%20condition%20verification)). The key: instead of asking "is this right?", the model is prompted to verify specific conditions that must hold for the answer to be correct. This transforms vague self-assessment into structured verification -- a form of self-generated external signal.

Similarly, human decision-making improves when introspection is structured. Rather than asking "am I right?", techniques like red-teaming, pre-mortem analysis ("assume this failed -- why?"), and checklists channel self-evaluation into concrete, verifiable sub-questions. The lesson is not that introspection is useless, but that **unstructured** introspection is unreliable. Both humans and LLMs benefit when self-evaluation is decomposed into specific, answerable sub-questions rather than holistic "is this good?" assessment.

### Scoring the Gap: A Tier Framework

Rating human vs LLM self-revision capability without external feedback (1-10 scale, 10 = perfect self-correction):

| Capability | Humans | LLMs | Gap |
|------------|--------|------|-----|
| Surface error detection (typos, grammar, style) | 6/10 | 5/10 | Small |
| Logical reasoning self-correction | 3/10 | 2/10 | Small |
| Creative quality improvement | 5/10 | 4/10 | Small |
| Calibration (knowing what you don't know) | 4/10 | 2/10 | Moderate |
| Problem restructuring (insight) | 5/10 | 1/10 | Large |
| Embodied/emotional error signal | 5/10 | 0/10 | Large |
| **Overall intrinsic self-revision** | **~4.5/10** | **~2.5/10** | **Moderate** |
| **With external feedback** | **8/10** | **8/10** | **None** |

The gap is real but moderate (~2 points on a 10-point scale). It comes almost entirely from incubation/restructuring and embodied signals -- capabilities with no LLM equivalent. On the dimensions that matter most for knowledge work (reasoning, calibration), both systems score poorly. The equalizer is external feedback, where both jump to ~8/10.

### The Uncomfortable Convergence

The pattern across both systems is consistent: **self-revision without external feedback is an inherently limited operation for any information-processing system.** The limitations are not incidental bugs -- they are structural consequences of using the same process for generation and evaluation.

Even *external* human review is surprisingly unreliable: a study of peer reviewers found they "failed to identify two thirds of the major errors" in manuscripts, detecting a median of only 3 out of 9 deliberately inserted errors ([Schroter et al., 2008](https://pmc.ncbi.nlm.nih.gov/articles/PMC2586872/#:~:text=two%20thirds)). If trained external reviewers miss 66% of major errors, the self-review baseline is substantially worse.

Archer (2010) argued there is "no evidence for the effectiveness of self-assessment" in isolation, recommending a shift from "individualized, internalized self-assessment to self-directed assessment utilizing and filtering external feedback" ([Frontiers in Psychology, 2011](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2011.00312/full#:~:text=no%20evidence%20for%20the%20effectiveness%20of%20self-assessment)). This recommendation -- aimed at human learners -- applies equally to LLMs.

The real differentiator is not the capacity for self-revision, but the **quality of the verification signal**:

- **No signal** (pure intrinsic self-correction): Both humans and LLMs are unreliable. Performance can degrade.
- **Weak signal** (human intuition, ERN, "feels wrong"): Modest improvement. Humans have a genuine but limited edge here.
- **Incubation signal** (unconscious restructuring): Humans have an advantage with no LLM equivalent. Effect sizes are real but moderate (d ≈ 0.3).
- **Strong signal** (tests pass, code compiles, external review): Both systems improve dramatically. This is where the real gains live.

The implication for agentic AI systems is clear: **invest in verification infrastructure, not in self-critique sophistication.** The Reflexion architecture (Section 3), SCoRe (Section 5), and tool-augmented approaches like CRITIC all support this conclusion. The path to reliable self-improvement -- for both humans and machines -- runs through external feedback, not through introspection.

### Post-Hoc Rationalization: The Shared Failure Mode

Perhaps the deepest parallel between human and LLM self-revision is the tendency to treat probabilistic outputs as certainties after the fact.

**In humans:** When a person makes a decision under uncertainty, the brain rapidly constructs a causal narrative explaining *why* that decision was correct -- even when it was essentially a weighted coin flip. This is [choice-supportive bias](https://en.wikipedia.org/wiki/Choice-supportive_bias#:~:text=retroactively%20ascribe%20positive%20attributes): "the tendency to retroactively ascribe positive attributes to an option one has selected." After a difficult choice between equally attractive options, people increase the perceived attractiveness of the chosen option and decrease the attractiveness of the rejected one -- the "spreading of alternatives" first documented by Brehm (1956). Confidence increases *after* the decision, not before it.

The neural mechanism is now understood. Rollwage et al. (2020) used MEG to show that "holding high confidence in a decision leads to a striking modulation of post-decision neural processing, such that integration of confirmatory evidence is amplified while disconfirmatory evidence processing is abolished" ([Nature Communications, 2020](https://www.nature.com/articles/s41467-020-16278-6#:~:text=integration%20of%20confirmatory%20evidence%20is%20amplified%20while%20disconfirmatory%20evidence%20processing%20is%20abolished)). The brain literally gates out information that contradicts a confident decision. The revision process becomes an exercise in defending the original output rather than genuinely evaluating it -- not as a cognitive shortcut, but as a neural mechanism.

**In LLMs:** The pattern is structurally identical but mechanistically different. LLMs exhibit "a consistent tendency to exhibit high expressed confidence in their responses, with scores typically ranging between 80% and 100%, regardless of their actual accuracy" ([1up.ai](https://1up.ai/blog/why-llms-suck-at-confidence-scoring/#:~:text=80%25%20and%20100%25)). The training process optimizes for fluency and coherence, not truthful reasoning -- so an LLM presents answers confidently because that style was optimal for next-token prediction, even when the content is incorrect. RLHF makes this worse: reinforcement learning methods induce systematic overconfidence compared to supervised fine-tuning ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12396779/#:~:text=overconfidence)). When asked to evaluate their own output, LLMs generate plausible-sounding justifications for why the output is good, with "critiques" that are often superficial or miss the actual errors.

**The convergence:** Both systems convert probabilistic, uncertain outputs into confident-seeming certainties through post-hoc rationalization. For humans, this serves an adaptive function -- maintaining decision confidence enables action. For LLMs, it is an artifact of training objectives that reward confident-sounding text. In both cases, the revision process is compromised: the same system that generated a high-confidence wrong answer generates high-confidence reasoning for why that answer is correct.

**The institutional insight:** The human advantage here is not that humans avoid this trap -- they don't. It's that humans have evolved **social and institutional structures** (peer review, editorial processes, legal adversarial systems, scientific replication) that externalize the verification function. These structures exist precisely *because* human self-evaluation is unreliable.

The AI parallel is already emerging. Multi-agent debate -- where multiple LLM agents independently generate proposals and deliberate on each other's reasoning -- is essentially an artificial institution. Du et al. (2023) showed this approach "significantly enhances mathematical and strategic reasoning" and "reduces fallacious answers and hallucinations" because "agents often identify and remove one another's uncertain or inconsistent facts" ([Du et al., 2023](https://arxiv.org/abs/2305.14325#:~:text=identify%20and%20remove)). This is the LLM equivalent of peer review: externalizing the critic by creating synthetic adversarial perspectives. The lesson from both cognitive science and AI research converges: reliable self-improvement requires externalizing the critic, not perfecting the self-critic. Tetlock's superforecasters provide the definitive human case study: amateur forecasters beat intelligence analysts with classified information -- not through superior intrinsic judgment, but because "keeping score provides feedback and therefore an opportunity to learn" ([Tetlock, 2015](https://longnow.org/seminars/02015/nov/23/superforecasting/#:~:text=keeping%20score)). The external scoring signal, not the forecaster's self-assessment, drove improvement. This may be the single most important insight for agentic AI design.

### A Proposed Definitive Test

Can we prove that intrinsic self-correction (without external information) is no better than random chance? The experiment is straightforward:

1. **Task:** A large set of reasoning problems with known correct answers (e.g., GSM8K, MATH, or logic puzzles).
2. **Condition A (Self-correction):** The model generates an answer, then is prompted to critique and revise it. Record the final answer.
3. **Condition B (Random replacement):** The model generates an answer, then generates a *completely independent* second answer to the same problem (no access to the first answer). Record the second answer.
4. **Condition C (Baseline):** The model generates a single answer. No revision.
5. **Measure:** Compare accuracy across conditions. If self-correction works, A > B > C. If self-correction is no better than resampling, A ≈ B. If self-correction degrades performance (Huang et al.'s finding), A < C.

The critical comparison is **A vs B**. If the model's self-critique is genuinely identifying errors and improving outputs, condition A should outperform condition B (random resampling). If A ≈ B, then self-correction is just variance -- the model is essentially sampling again from the same distribution, not genuinely improving. Early evidence from decomposition analyses suggests this may be the case for reasoning tasks: on GSM8K-Complex, the strongest model (DeepSeek) achieves only a 17% intrinsic correction rate, while weaker models correct 1.6-1.7x more errors -- suggesting that "correction" may be noise rather than signal ([Decomposing LLM Self-Correction, 2025](https://web3.arxiv.org/pdf/2601.00828#:~:text=17%25)).

The same experiment can be run with humans: give subjects a math test, then ask half to review and revise (Condition A) and half to simply redo the problems from scratch without seeing their first answers (Condition B). If human self-revision on reasoning tasks is also no better than fresh attempts, it would confirm the convergence thesis -- that the limitation is structural, not architectural.

**A concrete test using code generation:** Code is the ideal domain because it has an objective verification signal (does it pass the test suite?) but we can deliberately *withhold* that signal to test pure intrinsic self-correction.

1. Give the model a coding problem from HumanEval or MBPP with hidden test cases.
2. **Condition A (Self-correction loop):** Generate code, then simply ask the model to "improve this code" M times -- no structured critique, no hints, no execution. Just the bare instruction to improve. Record the final version.
3. **Condition B (Independent resampling):** Generate M+1 independent solutions to the same problem. Take the last one. Same compute budget, no self-critique.
4. **Condition C (Majority vote):** Generate M+1 independent solutions and select by majority vote (self-consistency). Same compute budget.
5. **Condition D (With execution feedback):** Generate code, run it against tests, feed errors back, revise. The control condition showing what external feedback enables.
6. Run all solutions against the hidden test suite. Compare pass rates.

```python
# Self-correction vs. resampling on code generation
import anthropic

client = anthropic.Anthropic()

def generate(prompt, model="claude-sonnet-4-20250514"):
    return client.messages.create(model=model, max_tokens=2048,
        messages=[{"role": "user", "content": prompt}]).content[0].text

results = {"self_correct": [], "resample": [], "majority": [], "with_tests": []}

for problem in humaneval_problems:
    prompt = f"Write a Python function:\n{problem['prompt']}"

    # Condition A: pure self-correction — no guidance, no structure
    code_a = generate(prompt)
    for _ in range(M):
        code_a = generate(f"Improve this code:\n{code_a}")  # no hints, no critique prompt
    results["self_correct"].append(passes_tests(code_a, problem["tests"]))

    # Condition B: independent resampling
    samples = [generate(prompt) for _ in range(M + 1)]
    results["resample"].append(passes_tests(samples[-1], problem["tests"]))

    # Condition C: majority vote
    passing = [s for s in samples if passes_tests(s, problem["tests"])]
    results["majority"].append(len(passing) > len(samples) // 2)

    # Condition D: with execution feedback (the real signal)
    code_d = generate(prompt)
    for _ in range(M):
        success, output = run_tests(code_d, problem["tests"])
        if success: break
        code_d = generate(f"This code failed:\n{code_d}\nError:\n{output}\nFix it.")
    results["with_tests"].append(passes_tests(code_d, problem["tests"]))
```

**Predicted outcomes based on existing evidence:**

- **D >> A** (with-feedback dominates self-correction) — well-established by CRITIC, Reflexion, SCoRe.
- **A ≈ B** (self-correction ≈ resampling) — this is the key hypothesis. If confirmed, intrinsic self-correction on code is just variance.
- **C > A** (majority vote > self-correction) — if true, the compute spent on self-critique is better spent on independent sampling. This would have profound implications for agentic loop design.
- **C < D** (majority vote < execution feedback) — external signals remain essential.

This experiment could be run in an afternoon with a single API key. The result would either validate or refute the claim that LLMs can genuinely improve code through intrinsic self-reflection.

**An even cleaner test — optimization with a measurable objective:** Ask the model to write code that optimizes a measurable quantity (e.g., "write the fastest possible Python function to compute Fibonacci numbers"). The objective function is execution time — completely objective, no ambiguity. Critically: **no code is executed during the loop.** The model only generates code, reflects on it, and generates a new version. Save every iteration's output but *evaluate only at the end* by benchmarking all versions. Plot performance vs. iteration number. If the curve is flat or random, intrinsic self-correction adds nothing. If it improves monotonically, the model is genuinely reasoning about performance without any feedback signal. This avoids the pass/fail binary of HumanEval and gives a continuous metric.

**What existing evidence suggests:** Emerging work on ReflexiCoder (2025) shows that models *trained* for self-correction via RL can outperform resampling, achieving 95.73% on HumanEval through internal iteration without execution feedback ([ReflexiCoder, 2025](https://arxiv.org/html/2603.05863#:~:text=95.73)). But models relying on *prompting alone* for self-correction often fail to improve -- "naive prompting for self-correction may reduce performance." This mirrors the SCoRe finding from Section 5: genuine self-correction can be trained but doesn't emerge naturally from prompting. The distinction between trained self-correction and prompted self-correction may be the key variable our experiment would test. CorrectBench (2025) provides a systematic framework for exactly this kind of comparison across intrinsic, external, and fine-tuned self-correction strategies ([CorrectBench, 2025](https://arxiv.org/html/2510.16062v1#:~:text=effectiveness%20of%20self-correction%20strategies)).

**The convergence ceiling.** Even when self-correction does help, it hits a hard limit fast. Research shows most practical value comes from 1-2 rounds, with effectiveness following an exponential decay. GPT-4 shows complete loss of debugging effectiveness by the third iteration. The ceiling is set by the model's shared blind spots: "errors that the model cannot recognize as errors are blind spots shared by both generator and critic" -- the same weights, the same gaps ([Iterative Self-Correction, Emergent Mind](https://www.emergentmind.com/topics/iterative-self-correction#:~:text=blind%20spots)). This is the computational version of Dunning-Kruger: you can't evaluate what you can't perceive.

---

## Synthesis: What We Know and What Remains Uncertain

### What the evidence supports

1. **Self-refinement reliably improves output quality** on tasks where the model can meaningfully evaluate its own output (writing, code, structured generation). The ~20% improvement from Self-Refine is robust across tasks and models.

2. **Self-correction fails on pure reasoning** without external feedback. The Huang et al. finding is clear: models cannot reliably identify their own reasoning errors. They're as likely to "fix" correct answers as wrong ones.

3. **The generation-verification gap is real but task-dependent.** For code (does it compile?), verification is strictly easier. For mathematical proofs, the gap may be smaller. For creative writing, "verification" is subjective and the model's critique is genuinely informative.

4. **Training for self-correction works.** SCoRe demonstrates that RL can teach models to genuinely improve on second attempts, reducing the pathological "correct-to-wrong" flips.

5. **Test-time compute scales.** Brown's 20-seconds-equals-100,000x result is perhaps the most striking empirical finding in this space.

6. **Humans and LLMs share the same fundamental limitation.** Self-revision without external feedback is inherently unreliable for any information-processing system. Humans have modest architectural advantages (prediction-error circuits, multi-system cross-checking, incubation/restructuring), but the empirical performance gap on self-evaluation tasks is smaller than the architectural differences suggest. Both systems degrade without external feedback and improve dramatically with it.

### What remains uncertain

- **Where exactly is the knowledge stored?** When a model improves its output, is it accessing latent knowledge that poor sampling missed the first time? Or is the critique genuinely adding new information through the evaluation framing?

- **Does self-refinement hit a ceiling?** Diminishing returns are observed, but it's unclear if this is a fundamental limit or a function of current model capabilities.

- **Is LeCun right about the architecture?** If autoregressive generation is fundamentally exponentially divergent, then self-correction is fighting an exponential with a linear process. World models might genuinely be necessary for reliability.

- **Can self-improvement compound?** If a model improves its output, and then improves its improvement, can this compound indefinitely? Or does it converge to a fixed point determined by the model's underlying capability?

- **Is the human-LLM gap on self-evaluation closing or fixed?** Humans have architectural advantages (ERN, incubation), but these provide modest empirical gains. As LLMs gain access to more diverse evaluation strategies (tool use, multi-agent debate, verifier models), the effective gap may narrow further -- even without matching the human architecture.

- **Can post-hoc rationalization be trained away?** Both humans and LLMs convert uncertain outputs into confident certainties. Calibration training helps LLMs; metacognitive training helps humans. But neither fully solves the problem. Is this a fundamental property of generative systems?

---

## Sources

- [Self-Refine: Iterative Refinement with Self-Feedback (Madaan et al., 2023)](https://arxiv.org/abs/2303.17651)
- [Self-Refine Project Page](https://selfrefine.info/)
- [Constitutional AI: Harmlessness from AI Feedback (Bai et al., 2022)](https://arxiv.org/abs/2212.08073)
- [Anthropic Constitutional AI Research Page](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback)
- [Reflexion: Language Agents with Verbal Reinforcement Learning (Shinn et al., 2023)](https://arxiv.org/abs/2303.11366)
- [Reflexion - Prompt Engineering Guide](https://www.promptingguide.ai/techniques/reflexion)
- [Large Language Models Cannot Self-Correct Reasoning Yet (Huang et al., 2023)](https://arxiv.org/abs/2310.01798)
- [When Can LLMs Actually Correct Their Own Mistakes? (TACL Survey)](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00713/125177/When-Can-LLMs-Actually-Correct-Their-Own-Mistakes)
- [Training Language Models to Self-Correct via Reinforcement Learning / SCoRe (Google DeepMind, 2024)](https://arxiv.org/abs/2409.12917)
- [Google Publishes LLM Self-Correction Algorithm SCoRe (InfoQ)](https://www.infoq.com/news/2024/10/google-deepmind-score/)
- [Generation-Verification Gap Hypothesis (Emergent Mind)](https://www.emergentmind.com/topics/generation-verification-gap-hypothesis)
- [Noam Brown - Scaling Test-Time Compute (Latent Space)](https://www.latent.space/p/noam-brown)
- [Noam Brown - Teaching LLMs to Reason (Sequoia Capital)](https://sequoiacap.com/podcast/training-data-noam-brown/)
- [Noam Brown at TED AI (VentureBeat)](https://venturebeat.com/ai/openai-noam-brown-stuns-ted-ai-conference-20-seconds-of-thinking-worth-100000x-more-data)
- [Yann LeCun on Autoregressive LLMs (X/Twitter)](https://x.com/ylecun/status/1640122342570336267)
- [Yann LeCun on LLM Planning Limitations (X/Twitter)](https://x.com/ylecun/status/1702027572077326505)
- [Ilya Sutskever NeurIPS 2024 - End of Pre-Training](https://dlyog.com/papers/one_internet_v1)
- [Ilya Sutskever on Reasoning and Unpredictability](https://deepnewz.com/ai-modeling/ilya-sutskever-neurips-2024-ai-s-reasoning-power-to-make-technology-less-8008fa08)
- [Flawed Self-Assessment: Implications for Health, Education, and the Workplace (Dunning, Heath, Suls, 2004)](https://journals.sagepub.com/doi/10.1111/j.1529-1006.2004.00018.x)
- [Error Awareness and the Error-Related Negativity: Evaluating the First Decade of Evidence (Wessel, 2012)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3328124/)
- [The Role of the ACC in Prediction Error and Signaling Surprise (Alexander & Brown, 2019)](https://onlinelibrary.wiley.com/doi/full/10.1111/tops.12307)
- [Does Incubation Enhance Problem Solving? A Meta-Analytic Review (Sio & Ormerod, 2009)](https://pubmed.ncbi.nlm.nih.gov/19210055/)
- [Inspired by Distraction: Mind Wandering Facilitates Creative Incubation (Baird et al., 2012)](https://journals.sagepub.com/doi/abs/10.1177/0956797612446024)
- [Creativity: The Unconscious Foundations of the Incubation Period (Ritter & Dijksterhuis, 2014)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3990058/)
- [In Search of Our True Selves: Feedback as a Path to Self-Knowledge (Frontiers, 2011)](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2011.00312/full)
- [Choice-Supportive Bias (Wikipedia)](https://en.wikipedia.org/wiki/Choice-supportive_bias)
- [Confidence Drives a Neural Confirmation Bias (Nature Communications, 2020)](https://www.nature.com/articles/s41467-020-16278-6)
- [Token Probabilities to Mitigate LLM Overconfidence (PMC, 2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12396779/)
- [Thinking, Fast and Slow (Kahneman, 2011) - WYSIATI](https://en.wikipedia.org/wiki/Thinking,_Fast_and_Slow)
- [Thinking Too Much: Introspection Can Reduce the Quality of Preferences (Wilson & Schooler, 1991)](https://pubmed.ncbi.nlm.nih.gov/2016668/)
- [Bias and Conflict: A Case for Logical Intuitions (De Neys, 2012)](https://journals.sagepub.com/doi/abs/10.1177/1745691611429354)
- [Smaller Large Language Models Can Do Moral Self-Correction (2024)](https://arxiv.org/html/2410.23496)
- [AI vs Human Feedback Meta-Analysis (Educational Psychology Review, 2025)](https://www.tandfonline.com/doi/full/10.1080/01443410.2025.2553639)
- [Self-Correction in LLMs (Communications of the ACM)](https://cacm.acm.org/news/self-correction-in-large-language-models/)
- [The Somatic Marker Hypothesis and Prefrontal Cortex (Damasio, 1996)](https://pubmed.ncbi.nlm.nih.gov/8941953/)
- [What Errors Do Peer Reviewers Detect? (Schroter et al., 2008)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2586872/)
- [LLMs Can Self-Correct with Key Condition Verification (EMNLP, 2024)](https://aclanthology.org/2024.emnlp-main.714/)
- [Somatic Marker Hypothesis (Wikipedia)](https://en.wikipedia.org/wiki/Somatic_marker_hypothesis)
- [Improving Factuality and Reasoning through Multiagent Debate (Du et al., 2023)](https://arxiv.org/abs/2305.14325)
- [AI Makes You Smarter But None the Wiser (Fernandes et al., 2025)](https://www.sciencedirect.com/science/article/pii/S0747563225002262)
- [Confidence Drives a Neural Confirmation Bias (Rollwage et al., 2020)](https://www.nature.com/articles/s41467-020-16278-6)
- [Decomposing LLM Self-Correction (2025)](https://web3.arxiv.org/pdf/2601.00828)
- [ReflexiCoder: Self-Correction via RL for Code Generation (2025)](https://arxiv.org/html/2603.05863)
- [CorrectBench: Benchmarking Self-Correction in LLMs (2025)](https://arxiv.org/html/2510.16062v1)
- [Superforecasting: The Art and Science of Prediction (Tetlock, 2015)](https://longnow.org/seminars/02015/nov/23/superforecasting/)
- [Iterative Self-Correction: Convergence and Blind Spots (Emergent Mind)](https://www.emergentmind.com/topics/iterative-self-correction)
