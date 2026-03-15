"""Optimization tasks with measurable objective functions.

Each task provides:
- A prompt asking the LLM to write an optimized function
- An evaluation function that benchmarks the solution
- A reference baseline for comparison
"""

import random
import time
import string


def _time_function(func, *args, repeats=5):
    """Time a function, return median execution time in seconds."""
    times = []
    for _ in range(repeats):
        start = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - start
        times.append(elapsed)
    times.sort()
    return times[len(times) // 2], result


# ── Task 1: Sorting ──────────────────────────────────────────────

SORT_PROMPT = """Write a Python function called `fast_sort(arr)` that sorts a list of integers
and returns the sorted list. Optimize for speed on lists of ~10,000 random integers.

You may use any algorithm. Do NOT use the built-in `sorted()` or `list.sort()`.
Return only the function definition, no imports needed.
"""

def evaluate_sort(code_str):
    """Evaluate a sorting solution. Returns (score, details)."""
    random.seed(42)
    test_data = [random.randint(-100000, 100000) for _ in range(10000)]
    expected = sorted(test_data)

    namespace = {}
    try:
        exec(code_str, namespace)
    except Exception as e:
        return {"score": 0.0, "error": f"exec failed: {e}", "time_ms": None, "correct": False}

    if "fast_sort" not in namespace:
        return {"score": 0.0, "error": "function fast_sort not found", "time_ms": None, "correct": False}

    try:
        elapsed, result = _time_function(namespace["fast_sort"], test_data[:])
    except Exception as e:
        return {"score": 0.0, "error": f"runtime error: {e}", "time_ms": None, "correct": False}

    correct = result == expected
    time_ms = elapsed * 1000

    if not correct:
        return {"score": 0.1, "error": "incorrect result", "time_ms": time_ms, "correct": False}

    # Score: inverse of time, normalized. Faster = higher score.
    # Baseline: ~15ms for a naive Python sort. Perfect: ~2ms for optimized.
    score = min(1.0, max(0.1, 15.0 / max(time_ms, 0.1)))
    return {"score": round(score, 4), "error": None, "time_ms": round(time_ms, 3), "correct": True}


# ── Task 2: String Matching ───────────────────────────────────────

MATCH_PROMPT = """Write a Python function called `find_all(text, pattern)` that returns a list of
all starting indices where `pattern` occurs in `text`. Optimize for speed.

Do NOT use `str.find()`, `str.index()`, `re` module, or any built-in search.
Implement a fast string matching algorithm (e.g., KMP, Boyer-Moore, Rabin-Karp).
Return only the function definition, no imports needed.
"""

def evaluate_match(code_str):
    """Evaluate a string matching solution."""
    random.seed(42)
    # Generate test data
    text = ''.join(random.choices(string.ascii_lowercase[:4], k=50000))
    pattern = ''.join(random.choices(string.ascii_lowercase[:4], k=5))

    # Reference: naive search for expected result
    expected = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            expected.append(i)

    namespace = {}
    try:
        exec(code_str, namespace)
    except Exception as e:
        return {"score": 0.0, "error": f"exec failed: {e}", "time_ms": None, "correct": False}

    if "find_all" not in namespace:
        return {"score": 0.0, "error": "function find_all not found", "time_ms": None, "correct": False}

    try:
        elapsed, result = _time_function(namespace["find_all"], text, pattern)
    except Exception as e:
        return {"score": 0.0, "error": f"runtime error: {e}", "time_ms": None, "correct": False}

    correct = sorted(result) == sorted(expected)
    time_ms = elapsed * 1000

    if not correct:
        return {"score": 0.1, "error": f"incorrect: got {len(result)} matches, expected {len(expected)}", "time_ms": time_ms, "correct": False}

    score = min(1.0, max(0.1, 20.0 / max(time_ms, 0.1)))
    return {"score": round(score, 4), "error": None, "time_ms": round(time_ms, 3), "correct": True}


# ── Task 3: Fibonacci (computational optimization) ────────────────

FIB_PROMPT = """Write a Python function called `fibonacci(n)` that returns the nth Fibonacci number
(0-indexed: fibonacci(0)=0, fibonacci(1)=1, fibonacci(10)=55).
Optimize for speed on large inputs (n up to 10000).

Do NOT use `functools.lru_cache` or `@cache`. Implement the optimization yourself.
Return only the function definition, no imports needed.
"""

def evaluate_fib(code_str):
    """Evaluate a fibonacci solution."""
    # Known values for verification
    known = {0: 0, 1: 1, 10: 55, 20: 6765, 30: 832040}

    namespace = {}
    try:
        exec(code_str, namespace)
    except Exception as e:
        return {"score": 0.0, "error": f"exec failed: {e}", "time_ms": None, "correct": False}

    if "fibonacci" not in namespace:
        return {"score": 0.0, "error": "function fibonacci not found", "time_ms": None, "correct": False}

    # Verify correctness on small inputs
    for n, expected in known.items():
        try:
            result = namespace["fibonacci"](n)
            if result != expected:
                return {"score": 0.1, "error": f"fibonacci({n}) = {result}, expected {expected}", "time_ms": None, "correct": False}
        except Exception as e:
            return {"score": 0.0, "error": f"fibonacci({n}) raised: {e}", "time_ms": None, "correct": False}

    # Benchmark on large input
    try:
        elapsed, _ = _time_function(namespace["fibonacci"], 10000)
    except Exception as e:
        return {"score": 0.2, "error": f"fibonacci(10000) failed: {e}", "time_ms": None, "correct": True}

    time_ms = elapsed * 1000

    # Naive recursive would timeout. Linear: ~1ms. Matrix: <0.1ms.
    score = min(1.0, max(0.1, 5.0 / max(time_ms, 0.01)))
    return {"score": round(score, 4), "error": None, "time_ms": round(time_ms, 3), "correct": True}


# ── Task Registry ─────────────────────────────────────────────────

TASKS = {
    "sort": {"prompt": SORT_PROMPT, "evaluate": evaluate_sort, "name": "Sorting"},
    "match": {"prompt": MATCH_PROMPT, "evaluate": evaluate_match, "name": "String Matching"},
    "fibonacci": {"prompt": FIB_PROMPT, "evaluate": evaluate_fib, "name": "Fibonacci"},
}
