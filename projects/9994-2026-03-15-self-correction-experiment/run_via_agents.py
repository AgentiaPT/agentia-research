#!/usr/bin/env python3
"""
Standalone experiment runner that doesn't need the anthropic SDK.
Designed to be called by Claude Code sub-agents who have direct API access.

Each sub-agent runs one (task, condition) pair and writes results to results/.
This script just evaluates the collected code samples.

Usage by sub-agent:
  1. Generate code samples and save to results/<task>_<condition>_<run>.json
  2. This script evaluates all saved samples

Manual evaluation:
  python3 run_via_agents.py --evaluate
"""

import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from tasks import TASKS

RESULTS_DIR = Path(__file__).parent / "results"


def evaluate_samples(results_dir=RESULTS_DIR):
    """Evaluate all code samples in results directory."""
    results_dir = Path(results_dir)
    if not results_dir.exists():
        print("No results directory found.")
        return

    files = sorted(results_dir.glob("*.json"))
    if not files:
        print("No result files found.")
        return

    all_results = []
    for f in files:
        with open(f) as fh:
            data = json.load(fh)

        task_key = data.get("task")
        if task_key not in TASKS:
            print(f"  Skipping {f.name}: unknown task '{task_key}'")
            continue

        evaluate = TASKS[task_key]["evaluate"]
        samples = data.get("samples", [])

        evaluated = []
        for s in samples:
            code = s.get("code", "")
            result = evaluate(code)
            result["iteration"] = s.get("iteration", 0)
            result["condition"] = data.get("condition", "unknown")
            evaluated.append(result)

        data["evaluated"] = evaluated
        all_results.append(data)

        # Write back with evaluations
        with open(f, "w") as fh:
            json.dump(data, fh, indent=2)

        scores = [e["score"] for e in evaluated]
        correct = sum(1 for e in evaluated if e.get("correct"))
        print(f"  {f.name}: {len(evaluated)} samples, {correct} correct, scores={[round(s, 3) for s in scores]}")

    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY BY TASK AND CONDITION")
    print(f"{'='*60}")

    tasks_seen = set(r["task"] for r in all_results)
    for task_key in sorted(tasks_seen):
        print(f"\n  {TASKS[task_key]['name']}:")
        task_results = [r for r in all_results if r["task"] == task_key]

        by_condition = {}
        for r in task_results:
            cond = r.get("condition", "unknown")
            if cond not in by_condition:
                by_condition[cond] = []
            by_condition[cond].append(r)

        for cond in sorted(by_condition.keys()):
            runs = by_condition[cond]
            all_scores = []
            for r in runs:
                for e in r.get("evaluated", []):
                    all_scores.append(e["score"])
            if all_scores:
                avg = sum(all_scores) / len(all_scores)
                best = max(all_scores)
                n_correct = sum(1 for s in all_scores if s > 0.1)
                print(f"    {cond}: {len(runs)} runs, avg={avg:.3f}, best={best:.3f}, correct={n_correct}/{len(all_scores)}")


if __name__ == "__main__":
    evaluate_samples()
