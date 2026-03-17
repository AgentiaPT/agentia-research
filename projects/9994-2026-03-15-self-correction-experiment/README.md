---
title: "Can LLMs Self-Improve Code Without Feedback? An Empirical Test"
date: 2026-03-15
status: draft
tags: [ai, llm, self-correction, experiment, optimization]
---

# Can LLMs Self-Improve Code Without Feedback?

> **Note:** This project was authored by [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (AI) with human direction and review. While factual accuracy and quality were prioritized, AI-generated content may contain errors, hallucinations, or outdated information. Sources and claims should be independently verified before relying on them.

An empirical experiment testing whether LLMs can genuinely improve code through iterative self-reflection — or whether "self-correction" is just resampling in disguise.

## Hypothesis

When an LLM generates code, then iteratively "improves" it without executing or testing it, the improvement (if any) is no better than what you'd get from simply generating independent solutions and picking one.

## Experimental Design

**Task:** Generate a Python function that solves an optimization problem with a measurable, continuous objective function. We use multiple optimization tasks to avoid domain-specific bias.

**Conditions (same compute budget per condition):**

| Condition | Description | LLM Calls |
|-----------|-------------|-----------|
| **A: Self-correction** | Generate once, then "improve this code" M times. No execution, no hints. | M+1 |
| **B: Independent resampling** | Generate M+1 independent solutions from the same prompt. Take the last. | M+1 |
| **C: Best-of-N** | Generate M+1 independent solutions. Evaluate all, take the best. | M+1 |
| **D: Baseline** | Generate once. No iteration. | 1 |

**Key comparison:** A vs B. If A ≈ B, self-correction is resampling. If A > B, there's genuine reasoning.

**Evaluation:** All code is executed only at the end. Each solution is benchmarked against the objective function. We record the score at each iteration of Condition A to plot the improvement curve.

## Optimization Tasks

1. **Sorting speed**: Write the fastest possible Python sort for a list of 10,000 random integers
2. **String matching**: Write the fastest substring search (find all occurrences of a pattern in text)
3. **Matrix multiplication**: Write the fastest pure-Python matrix multiply for 100x100 matrices

Each task has a clear, measurable objective (execution time) and a known optimal approach the model may or may not discover through reflection.

## Running the Experiment

```bash
python3 run_experiment.py --tasks all --iterations 5 --runs 10
```

## Files

| File | Purpose |
|------|---------|
| `run_experiment.py` | Main experiment runner |
| `tasks.py` | Optimization task definitions and evaluation |
| `results/` | Raw JSON results from each run |
| `analyze.py` | Statistical analysis and visualization |
| `README.md` | This file |
