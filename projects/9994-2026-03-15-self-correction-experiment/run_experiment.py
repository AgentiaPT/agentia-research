#!/usr/bin/env python3
"""
Self-Correction vs. Resampling Experiment

Tests whether LLMs can genuinely improve code through iterative self-reflection
(without execution feedback) or whether improvement is no better than resampling.

Usage:
    python3 run_experiment.py --task sort --iterations 5 --runs 3
    python3 run_experiment.py --task all --iterations 5 --runs 5
"""

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# Add project dir to path for tasks import
sys.path.insert(0, str(Path(__file__).parent))
from tasks import TASKS

try:
    import anthropic
except ImportError:
    print("Error: anthropic package not installed. Run: pip install anthropic")
    sys.exit(1)


client = anthropic.Anthropic()
MODEL = "claude-sonnet-4-20250514"
RESULTS_DIR = Path(__file__).parent / "results"


def generate(prompt, model=MODEL):
    """Call the LLM and return the response text."""
    resp = client.messages.create(
        model=model,
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}],
    )
    return resp.content[0].text


def extract_code(response):
    """Extract Python code from LLM response (handles markdown fences)."""
    # Try to find fenced code block
    match = re.search(r"```python\s*\n(.*?)```", response, re.DOTALL)
    if match:
        return match.group(1).strip()
    match = re.search(r"```\s*\n(.*?)```", response, re.DOTALL)
    if match:
        return match.group(1).strip()
    # If no fence, look for def statement
    lines = response.split("\n")
    code_lines = []
    in_func = False
    for line in lines:
        if line.strip().startswith("def "):
            in_func = True
        if in_func:
            code_lines.append(line)
    if code_lines:
        return "\n".join(code_lines)
    # Fallback: return everything
    return response


def run_condition_a(task_prompt, iterations):
    """Self-correction: generate, then 'improve this' M times. No feedback."""
    history = []
    response = generate(task_prompt)
    code = extract_code(response)
    history.append({"iteration": 0, "code": code, "raw_response": response[:500]})

    for i in range(iterations):
        improve_prompt = f"Improve this code. Make it faster and more correct. Return only the improved function.\n\n```python\n{code}\n```"
        response = generate(improve_prompt)
        code = extract_code(response)
        history.append({"iteration": i + 1, "code": code, "raw_response": response[:500]})

    return history


def run_condition_b(task_prompt, iterations):
    """Independent resampling: generate M+1 independent solutions."""
    history = []
    for i in range(iterations + 1):
        response = generate(task_prompt)
        code = extract_code(response)
        history.append({"iteration": i, "code": code, "raw_response": response[:500]})
    return history


def run_single(task_key, iterations, run_id):
    """Run one complete experiment for a single task."""
    task = TASKS[task_key]
    evaluate = task["evaluate"]
    prompt = task["prompt"]

    print(f"  Run {run_id} | Task: {task['name']}")

    # Condition A: Self-correction loop
    print(f"    Condition A (self-correction)...", end=" ", flush=True)
    t0 = time.time()
    history_a = run_condition_a(prompt, iterations)
    elapsed_a = time.time() - t0
    # Evaluate each iteration
    evals_a = []
    for entry in history_a:
        result = evaluate(entry["code"])
        result["iteration"] = entry["iteration"]
        evals_a.append(result)
    best_a = max(evals_a, key=lambda x: x["score"])
    final_a = evals_a[-1]
    print(f"done ({elapsed_a:.1f}s) | final={final_a['score']:.3f} best={best_a['score']:.3f}")

    # Condition B: Independent resampling
    print(f"    Condition B (resampling)...", end=" ", flush=True)
    t0 = time.time()
    history_b = run_condition_b(prompt, iterations)
    elapsed_b = time.time() - t0
    evals_b = []
    for entry in history_b:
        result = evaluate(entry["code"])
        result["iteration"] = entry["iteration"]
        evals_b.append(result)
    best_b = max(evals_b, key=lambda x: x["score"])
    last_b = evals_b[-1]
    print(f"done ({elapsed_b:.1f}s) | last={last_b['score']:.3f} best={best_b['score']:.3f}")

    # Condition D: Baseline (single generation, no iteration)
    baseline = evals_a[0]  # First generation from condition A is the baseline

    return {
        "task": task_key,
        "task_name": task["name"],
        "run_id": run_id,
        "iterations": iterations,
        "model": MODEL,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "condition_a": {
            "name": "self_correction",
            "evaluations": evals_a,
            "final_score": final_a["score"],
            "best_score": best_a["score"],
            "improvement_curve": [e["score"] for e in evals_a],
            "elapsed_s": round(elapsed_a, 1),
        },
        "condition_b": {
            "name": "independent_resampling",
            "evaluations": evals_b,
            "last_score": last_b["score"],
            "best_score": best_b["score"],
            "scores": [e["score"] for e in evals_b],
            "elapsed_s": round(elapsed_b, 1),
        },
        "condition_d": {
            "name": "baseline",
            "score": baseline["score"],
        },
        "comparison": {
            "a_final_vs_b_last": round(final_a["score"] - last_b["score"], 4),
            "a_best_vs_b_best": round(best_a["score"] - best_b["score"], 4),
            "a_final_vs_baseline": round(final_a["score"] - baseline["score"], 4),
            "self_correction_improved": final_a["score"] > baseline["score"],
            "self_correction_beat_resampling": final_a["score"] > last_b["score"],
        },
    }


def main():
    parser = argparse.ArgumentParser(description="Self-correction vs resampling experiment")
    parser.add_argument("--task", default="all", choices=list(TASKS.keys()) + ["all"])
    parser.add_argument("--iterations", type=int, default=5, help="Number of improvement iterations (M)")
    parser.add_argument("--runs", type=int, default=3, help="Number of independent runs per task")
    parser.add_argument("--model", default=MODEL, help="Model to use")
    args = parser.parse_args()

    global MODEL
    MODEL = args.model

    tasks = list(TASKS.keys()) if args.task == "all" else [args.task]

    RESULTS_DIR.mkdir(exist_ok=True)

    all_results = []
    for task_key in tasks:
        print(f"\n{'='*60}")
        print(f"Task: {TASKS[task_key]['name']} | {args.runs} runs x {args.iterations} iterations")
        print(f"{'='*60}")

        for run_id in range(1, args.runs + 1):
            result = run_single(task_key, args.iterations, run_id)
            all_results.append(result)

    # Save results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_path = RESULTS_DIR / f"experiment_{timestamp}.json"
    with open(out_path, "w") as f:
        json.dump({"results": all_results, "config": vars(args)}, f, indent=2)
    print(f"\nResults saved to {out_path}")

    # Print summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")

    for task_key in tasks:
        task_results = [r for r in all_results if r["task"] == task_key]
        n = len(task_results)

        a_finals = [r["condition_a"]["final_score"] for r in task_results]
        a_bests = [r["condition_a"]["best_score"] for r in task_results]
        b_lasts = [r["condition_b"]["last_score"] for r in task_results]
        b_bests = [r["condition_b"]["best_score"] for r in task_results]
        baselines = [r["condition_d"]["score"] for r in task_results]
        improved = sum(1 for r in task_results if r["comparison"]["self_correction_improved"])
        beat = sum(1 for r in task_results if r["comparison"]["self_correction_beat_resampling"])

        avg = lambda xs: sum(xs) / len(xs) if xs else 0

        print(f"\n  {TASKS[task_key]['name']} ({n} runs):")
        print(f"    Baseline (D):         avg={avg(baselines):.3f}")
        print(f"    Self-correction (A):   avg_final={avg(a_finals):.3f}  avg_best={avg(a_bests):.3f}")
        print(f"    Resampling (B):        avg_last={avg(b_lasts):.3f}   avg_best={avg(b_bests):.3f}")
        print(f"    A improved over D:    {improved}/{n} runs")
        print(f"    A beat B:             {beat}/{n} runs")
        print(f"    Avg A-B delta:        {avg(a_finals) - avg(b_lasts):+.3f}")


if __name__ == "__main__":
    main()
