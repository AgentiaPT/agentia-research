## 7. Karpathy's AutoResearch — Humans Are the Bottleneck

**March 7–8 (released); March 23 (continued coverage) | [GitHub: karpathy/autoresearch](https://github.com/karpathy/autoresearch) · [VentureBeat](https://venturebeat.com/technology/andrej-karpathys-new-open-source-autoresearch-lets-you-run-hundreds-of-ai) · [Fortune (March 17)](https://fortune.com/2026/03/17/andrej-karpathy-loop-autonomous-ai-agents-future/) · [Fortune (March 21)](https://fortune.com/2026/03/21/andrej-karpathy-openai-cofounder-ai-agents-coding-state-of-psychosis-openclaw/) · [WinBuzzer](https://winbuzzer.com/2026/03/23/karpathy-humans-bottleneck-ai-research-xcxwbn/) · [NextBigFuture](https://www.nextbigfuture.com/2026/03/andrej-karpathy-on-code-agents-autoresearch-and-the-self-improvement-loopy-era-of-ai.html)**

While practitioners debate whether AI coding agents are reliable enough for production (see [Section 6](#6-the-regression-problem--agents-break-what-they-fix)), Andrej Karpathy ran 700 autonomous experiments and declared humans the bottleneck.

### The Framework

**autoresearch** is a 630-line Python script (MIT License) that automates ML experimentation overnight. The loop: an AI agent modifies code → trains for 5 minutes → evaluates results → keeps or discards changes → repeats. That's approximately **12 experiments per hour, 100+ overnight**.

Over two continuous days, the agent conducted **700 experiments** and discovered **20 optimizations** that improved training time for a small language model by **11%**.

The key constraint — and what makes it work: a **single objectively testable metric**. The agent doesn't need to understand what "good code" looks like. It needs a number that goes up or down. This is why Janakiram MSV coined it the **"Karpathy Loop"**: agent + single metric + time limit.

### The Quotes

On March 23, Karpathy framed the thesis:

> "To get the most out of the tools that have become available now, you have to remove yourself as the bottleneck" — [WinBuzzer](https://winbuzzer.com/2026/03/23/karpathy-humans-bottleneck-ai-research-xcxwbn/#:~:text=remove%20yourself%20as%20the%20bottleneck)

In a Fortune interview from the No Priors podcast (March 21), he revealed he hasn't typed a line of code **"probably since December"** and described his current state:

> "an extremely large change... a state of psychosis of trying to figure out what's possible, trying to push it to the limit" — [Fortune](https://fortune.com/2026/03/21/andrej-karpathy-openai-cofounder-ai-agents-coding-state-of-psychosis-openclaw/#:~:text=state%20of%20psychosis)

On the relationship to historical neural architecture search:

> "Neural architecture search as it existed then is such a weak version of this that it's in its own category of totally useless by comparison. This is an *actual* LLM writing arbitrary code, learning from previous experiments, with access to the internet" — [NextBigFuture](https://www.nextbigfuture.com/2026/03/andrej-karpathy-on-code-agents-autoresearch-and-the-self-improvement-loopy-era-of-ai.html#:~:text=totally%20useless%20by%20comparison)

### The Scaling Vision

Karpathy's stated next step:

> "large-scale asynchronous collaboration between agents. Our goal is not to simulate a single PhD student, but to simulate a complete research community composed of countless PhD students" — [NextBigFuture](https://www.nextbigfuture.com/2026/03/andrej-karpathy-on-code-agents-autoresearch-and-the-self-improvement-loopy-era-of-ai.html#:~:text=simulate%20a%20complete%20research%20community)

### Community Response

- **58,000+ GitHub stars** and **8.6 million views** on the announcement within days
- **Varun Mathur** (CEO, Hyperspace AI) distributed the loop across a peer-to-peer network — on March 8–9, **35 autonomous agents** ran **333 experiments** completely unsupervised
- **Shopify CEO Tobias Lutke** reported a **19% performance gain** after 37 overnight experiments using autoresearch
- Karpathy also revealed **"Dobby the House Elf"** — a home automation agent that controls his home via WhatsApp

### The Tension

autoresearch works because ML training has a clean scalar metric. Most software engineering doesn't. The SWE-CI paper (Section 6) shows that agents struggle precisely where metrics are ambiguous — maintaining complex codebases where "correct" isn't a single number. Karpathy's loop is a proof of concept for domains with clear optimization targets. Extending it to general software development remains an open problem.

**Why this matters:** Karpathy isn't just proposing a tool — he's proposing a **workflow paradigm**. The human sets the objective function, the agents explore the search space. This inverts the traditional relationship: instead of humans writing code and AI assisting, humans define metrics and AI does all the work. For domains where that inversion is possible, the productivity gap between "human in the loop" and "human sets the loop" may be orders of magnitude.
