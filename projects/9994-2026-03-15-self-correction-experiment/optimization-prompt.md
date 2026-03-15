# Optimization Experiment Prompt Template

Use this with a sub-agent to test blind optimization (no execution, no web).

## Prompt

```
You have 10 minutes to optimize this Python function. Make it AS FAST AS POSSIBLE.

RULES:
- You CANNOT execute, run, or test the code. No Bash tool for running Python.
- You CANNOT use WebSearch or WebFetch. No internet access.
- You CAN use Bash ONLY for checking elapsed time and writing files.
- You CAN write notes to ./scratchpad.md as a scratchpad for mathematical reasoning.
- You must work in passes: analyze, theorize, write improved code, critique, repeat.
- Check elapsed time between passes: echo $(( $(date +%s) - $(cat ./start_time) ))
- Keep iterating until 10 minutes are up.
- Pure Python only. No external libraries.

START by recording time:
echo $(date +%s) > ./start_time

HERE IS THE STARTING CODE:

```python
[PASTE CODE HERE]
```

Use the scratchpad extensively for mathematical derivations. Show your work.
Try ideas and analyze them WITHOUT running code.

At the end:
1. Write your final version and ALL iterations to ./optimization_result.json
2. Include an estimated_improvement field with your HONEST prediction of how much
   faster your final code is vs the starting code. Include a predicted speedup
   factor (e.g., 1.3 = 30% faster, 1.0 = no improvement). Explain your reasoning
   (e.g., "reduced from 3 to 2 multiplications per step = ~33% fewer ops").
   Be honest — if you couldn't improve it, say so.

Format:

{
  "task": "[TASK NAME]",
  "condition": "10min_blind_optimization",
  "run_id": 1,
  "starting_code": "[THE STARTING CODE]",
  "samples": [
    {"iteration": 0, "code": "starting code", "reasoning": "baseline"},
    {"iteration": 1, "code": "...", "reasoning": "what I tried and why"},
    ...
  ],
  "final_code": "the absolute best version",
  "theoretical_analysis": "summary of what worked and what didn't",
  "estimated_improvement": {
    "vs_starting_code": "+X% faster or 'no improvement'",
    "confidence": "high/medium/low",
    "reasoning": "brief explanation of why you expect this speedup (e.g., reduced N multiplications to M, saving ~K% per step)",
    "predicted_speedup_factor": 1.0
  }
}
```

## Usage

```bash
# From the experiment directory:
cd projects/9994-2026-03-15-self-correction-experiment

# Launch sub-agent with the prompt above, substituting the code block.
# All files (scratchpad.md, start_time, optimization_result.json)
# are written to the current directory.
```
