#!/usr/bin/env python3
"""Analyze experiment results and produce summary statistics."""

import json
from pathlib import Path

RESULTS_DIR = Path(__file__).parent / "results"


def load_results():
    """Load all evaluated result files."""
    results = []
    for f in sorted(RESULTS_DIR.glob("*.json")):
        with open(f) as fh:
            data = json.load(fh)
        if "evaluated" in data:
            results.append(data)
    return results


def analyze():
    results = load_results()
    if not results:
        print("No evaluated results found. Run run_via_agents.py --evaluate first.")
        return

    # Group by task and condition
    grouped = {}
    for r in results:
        key = (r["task"], r["condition"])
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(r)

    tasks = sorted(set(r["task"] for r in results))

    print("=" * 70)
    print("SELF-CORRECTION vs. RESAMPLING: EXPERIMENT RESULTS")
    print("=" * 70)

    for task in tasks:
        sc_runs = grouped.get((task, "self_correction"), [])
        rs_runs = grouped.get((task, "resampling"), [])

        print(f"\n{'─' * 70}")
        print(f"  TASK: {task.upper()}")
        print(f"{'─' * 70}")

        # Self-correction improvement curves
        if sc_runs:
            print(f"\n  Self-Correction Improvement Curves:")
            print(f"  {'Run':<6} {'Iter 0':<10} {'Iter 1':<10} {'Iter 2':<10} {'Iter 3':<10} {'Iter 4':<10} {'Iter 5':<10} {'Trend'}")
            for r in sc_runs:
                evals = r["evaluated"]
                scores = [e["score"] for e in sorted(evals, key=lambda x: x["iteration"])]
                trend = "↑" if scores[-1] > scores[0] else ("↓" if scores[-1] < scores[0] else "→")
                if scores[-1] < 0.5 and scores[0] >= 0.5:
                    trend = "💥 DEGRADED"
                row = f"  {r['run_id']:<6}"
                for s in scores:
                    row += f" {s:<10.3f}"
                row += f" {trend}"
                print(row)

            # Average curve
            all_curves = []
            for r in sc_runs:
                evals = r["evaluated"]
                scores = [e["score"] for e in sorted(evals, key=lambda x: x["iteration"])]
                all_curves.append(scores)

            if all_curves:
                n_iters = max(len(c) for c in all_curves)
                avg_curve = []
                for i in range(n_iters):
                    vals = [c[i] for c in all_curves if i < len(c)]
                    avg_curve.append(sum(vals) / len(vals))
                print(f"\n  {'AVG':<6}", end="")
                for s in avg_curve:
                    print(f" {s:<10.3f}", end="")
                delta = avg_curve[-1] - avg_curve[0]
                print(f" {'↑' if delta > 0.01 else '↓' if delta < -0.01 else '→'} ({delta:+.3f})")

        # Resampling stats
        if rs_runs:
            print(f"\n  Resampling Scores:")
            all_rs_scores = []
            for r in rs_runs:
                scores = [e["score"] for e in r["evaluated"]]
                all_rs_scores.extend(scores)
                print(f"  Run {r['run_id']}: {[round(s, 3) for s in scores]}  avg={sum(scores)/len(scores):.3f}")

            rs_avg = sum(all_rs_scores) / len(all_rs_scores)
            rs_correct = sum(1 for s in all_rs_scores if s > 0.1)
            print(f"\n  Resampling overall: avg={rs_avg:.3f}, correct={rs_correct}/{len(all_rs_scores)}")

        # Head-to-head comparison
        if sc_runs and rs_runs:
            sc_finals = []
            sc_bests = []
            sc_baselines = []
            for r in sc_runs:
                evals = sorted(r["evaluated"], key=lambda x: x["iteration"])
                sc_finals.append(evals[-1]["score"])
                sc_bests.append(max(e["score"] for e in evals))
                sc_baselines.append(evals[0]["score"])

            rs_all = [e["score"] for r in rs_runs for e in r["evaluated"]]
            rs_bests = [max(e["score"] for e in r["evaluated"]) for r in rs_runs]

            sc_final_avg = sum(sc_finals) / len(sc_finals)
            sc_best_avg = sum(sc_bests) / len(sc_bests)
            sc_baseline_avg = sum(sc_baselines) / len(sc_baselines)
            rs_avg = sum(rs_all) / len(rs_all)
            rs_best_avg = sum(rs_bests) / len(rs_bests)

            print(f"\n  ┌──────────────────────────────────────────────┐")
            print(f"  │ HEAD-TO-HEAD COMPARISON                      │")
            print(f"  ├──────────────────────────────────────────────┤")
            print(f"  │ Baseline (iter 0):        {sc_baseline_avg:>8.3f}            │")
            print(f"  │ Self-correction (final):  {sc_final_avg:>8.3f}  {'↑' if sc_final_avg > sc_baseline_avg else '↓' if sc_final_avg < sc_baseline_avg else '→'} vs baseline │")
            print(f"  │ Self-correction (best):   {sc_best_avg:>8.3f}            │")
            print(f"  │ Resampling (avg):         {rs_avg:>8.3f}            │")
            print(f"  │ Resampling (best of run): {rs_best_avg:>8.3f}            │")
            print(f"  │                                              │")
            delta = sc_final_avg - rs_avg
            winner = "SELF-CORRECTION" if delta > 0.01 else "RESAMPLING" if delta < -0.01 else "TIE"
            print(f"  │ Winner: {winner:<37}│")
            print(f"  │ Delta (A_final - B_avg): {delta:>+8.3f}            │")
            print(f"  └──────────────────────────────────────────────┘")

    # Overall summary
    print(f"\n{'=' * 70}")
    print("OVERALL VERDICT")
    print(f"{'=' * 70}")

    total_sc_improved = 0
    total_sc_degraded = 0
    total_sc_unchanged = 0

    for task in tasks:
        sc_runs = grouped.get((task, "self_correction"), [])
        for r in sc_runs:
            evals = sorted(r["evaluated"], key=lambda x: x["iteration"])
            if evals[-1]["score"] > evals[0]["score"] + 0.01:
                total_sc_improved += 1
            elif evals[-1]["score"] < evals[0]["score"] - 0.01:
                total_sc_degraded += 1
            else:
                total_sc_unchanged += 1

    total = total_sc_improved + total_sc_degraded + total_sc_unchanged
    print(f"\n  Self-correction outcomes across {total} runs:")
    print(f"    Improved:   {total_sc_improved}/{total} ({100*total_sc_improved/total:.0f}%)")
    print(f"    Degraded:   {total_sc_degraded}/{total} ({100*total_sc_degraded/total:.0f}%)")
    print(f"    Unchanged:  {total_sc_unchanged}/{total} ({100*total_sc_unchanged/total:.0f}%)")

    if total_sc_degraded > total_sc_improved:
        print(f"\n  CONCLUSION: Self-correction WITHOUT external feedback is net HARMFUL.")
        print(f"  The model is more likely to degrade its output than improve it.")
    elif total_sc_improved > total_sc_degraded:
        print(f"\n  CONCLUSION: Self-correction shows some benefit, but compare vs resampling cost.")
    else:
        print(f"\n  CONCLUSION: Self-correction is no better than chance — equivalent to resampling.")


if __name__ == "__main__":
    analyze()
