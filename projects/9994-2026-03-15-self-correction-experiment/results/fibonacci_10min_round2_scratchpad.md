# Fibonacci Optimization Round 2 - Deep Analysis

## Starting Code Analysis

The starting code is the Fibonacci-Lucas fast doubling with:
- f*l: 1 general multiplication per step
- l*l: 1 squaring per step
- Total: ~1.5 equivalent muls per bit (squaring is ~0.6-0.8x general mul cost)
- Odd step (bit=1): only O(digits) additions/shifts

## Pass 1: Can we beat 1 mul + 1 sq per step?

### Sub-question: Is 1 mul + 1 sq a theoretical lower bound?

We maintain 2 state values. Each doubling step produces 2 new values.
Each new value is a degree-2 polynomial in the old values.
To evaluate two independent degree-2 polynomials, we need at minimum...

Actually the question is whether the two polynomials share structure we can exploit.

F(2k) = F(k) * L(k)                    -- product of the two states
L(2k) = L(k)^2 - 2*(-1)^k             -- square of one state + constant

These are "independent" in the sense that F(2k) uses both variables while
L(2k) uses only one. The L(2k) computation doesn't help compute F(2k) or vice versa.

Could we reformulate so both formulas share a common sub-expression?

### Alternative state: (F(k), F(k)+L(k)) or (F(k), F(k)*L(k))

If s = F(k) + L(k) = F(k) + F(k-1) + F(k+1) = F(k-1) + 2F(k) + F(k-1)...
Actually L(k) = F(k-1) + F(k+1), so s = F(k) + F(k-1) + F(k+1) = F(k+1) + L(k-1)... messy.

### Product state: (P, L) where P = F(k)*L(k) = F(2k)

If we track F(2k) directly... then to double again we need F(4k) = F(2k)*L(2k).
We'd need L(2k). From P = F(2k) and L(2k), we'd compute:
F(4k) = P' where P' = F(2k)*L(2k) = P*L(2k) -- 1 mul
L(4k) = L(2k)^2 - 2 -- 1 sq

But we need to UPDATE from step k to step 2k, meaning we need to go from
(F(k), L(k)) to (F(2k), L(2k)). That's what we already have.

## Pass 2: Deep dive into Karatsuba sharing

When we compute f*l and l*l in the same step, can Python's Karatsuba implementation
share any intermediate results?

f*l via Karatsuba (splitting at midpoint m):
  f = f1*B + f0, l = l1*B + l0
  f*l = f1*l1*B^2 + ((f1+f0)*(l1+l0) - f1*l1 - f0*l0)*B + f0*l0
  Needs: f1*l1, f0*l0, (f1+f0)*(l1+l0) = 3 sub-multiplications

l*l via Karatsuba:
  l^2 = l1^2*B^2 + ((l1+l0)^2 - l1^2 - l0^2)*B + l0^2
  Needs: l1^2, l0^2, (l1+l0)^2 = 3 sub-squarings

Shared sub-expressions: NONE between f*l and l*l decompositions.
Even at the recursive level, there's no sharing.

Can we restructure to CREATE sharing?

What if instead of computing f*l and l*l separately, we compute:
- l^2 (squaring)
- f*l = ? Can we derive f*l from l^2 and something cheaper?

f*l = l * f. If f = α*l + β for some known α, β, then f*l = α*l^2 + β*l.
But α = F(k)/L(k) which is irrational and changes each step. Not useful.

What about: compute l^2 first, then f*l = f * l.
No sharing possible since they're independent.

Alternative: compute (f+l)*l = f*l + l^2. This is 1 general mul.
Then f*l = (f+l)*l - l^2. But we still need l^2, so: 1 sq + 1 mul = same.
AND we'd compute (f+l)*l instead of f*l as the general mul. The operand (f+l) is
slightly larger than f (about the same size as l), so the mul might be slightly
more expensive. Net: slightly worse.

Alternative: compute f*(f+l) = f^2 + f*l. Then f*l = f*(f+l) - f^2.
1 general mul + 1 squaring. The general mul has operands f and f+l ≈ l.
Sizes: f has d bits, f+l ≈ l has d+1 bits. Similar to f*l.
But now we square f instead of l! f is smaller by ~1 bit.
And we still get f*l from the subtraction.

Wait, this is interesting! Let me formalize:

Compute:
1. q = f * f  (squaring of smaller number)
2. p = f * (f + l)  (general mul, operands: f and f+l)
3. f_new = p - q  (= f*l, subtraction is O(d))
4. l_new = 5*q + 2*(-1)^k  (using L(2k) = 5*F(k)^2 + 2*(-1)^k)

Total: 1 squaring + 1 general mul + O(d) work. SAME COUNT.

But the general mul is now f*(f+l) instead of f*l.
f has ~d bits, f+l has ~d+1 bits (since l ≈ 2.236*f, f+l ≈ 3.236*f ≈ 1.67 bits more).
versus f*l: f has d bits, l has d+1 bits.

So f*(f+l) has operands of size d and d+1.7, while f*l has operands d and d+1.2.
The f*(f+l) version is SLIGHTLY more expensive for the general mul. Bad.

OK, so this particular restructuring doesn't help.

## Pass 3: Alternative - compute f*l and l^2 via a single "combined" operation

Is there a way to compute BOTH f*l and l^2 with fewer than 1 mul + 1 sq total sub-operations?

This is related to the problem: given two polynomials to evaluate, can we use fewer multiplications?

For f*l and l^2:
These share the operand l. In a Karatsuba-like decomposition at the top level:

Split l = l1*B + l0, f = f1*B + f0.

For l^2:
  l1^2, l0^2, (l1+l0)^2 → 3 squarings

For f*l:
  f1*l1, f0*l0, (f1+f0)*(l1+l0) → 3 muls

Total naive: 3 sq + 3 mul at top level.

Can we share?
- (l1+l0)^2 and (f1+f0)*(l1+l0) share the factor (l1+l0).
- If we compute (l1+l0)^2 = s^2 where s=l1+l0, and (f1+f0)*s,
  these are a squaring and a mul with shared operand s.

Can we combine them? (f1+f0)*s and s^2.
These two give us: s * (f1+f0) and s * s.
We could compute s * ((f1+f0) + s) = s * (f1+f0+l1+l0) -- 1 mul
Then s^2 = squaring -- 1 sq
And s*(f1+f0) = s*(f1+f0+s) - s^2 -- subtraction

So: 1 mul + 1 sq instead of 1 mul + 1 sq. Same! No savings.

What about l1^2 and f1*l1? These share l1.
l1^2 is squaring. f1*l1 is general mul.
Can we get both from fewer operations?
Compute (f1+l1)*l1 = f1*l1 + l1^2. Then: 1 general mul.
l1^2 = l1*l1: 1 squaring.
f1*l1 = (f1+l1)*l1 - l1^2: subtraction.
Total: 1 mul + 1 sq → gives both f1*l1 and l1^2. Same count.

OR: compute l1^2 and (f1+l1)*l1, get f1*l1 by subtraction. 1 sq + 1 mul = same.

Similarly for l0^2 and f0*l0: 1 sq + 1 mul.

And for s^2 and (f1+f0)*s: 1 sq + 1 mul.

Grand total at top level: 3 sq + 3 mul reduced to... well, for each pair we have 1 sq + 1 mul = still 3 sq + 3 mul at top Karatsuba level. BUT we can use a different decomposition.

Actually, what if we DON'T use Karatsuba separately for each, but instead design a custom
combined algorithm?

We want: f*l and l^2.
We have 6 "sub-products" at Karatsuba level: l1^2, l0^2, (l1+l0)^2, f1*l1, f0*l0, (f1+f0)(l1+l0).

Relationships:
- l1^2 and f1*l1 share l1
- l0^2 and f0*l0 share l0
- (l1+l0)^2 and (f1+f0)(l1+l0) share (l1+l0)

For each pair, we need: 1 squaring of the shared operand + 1 general mul involving the shared operand.

Is there a way to get BOTH products from a single multiplication?
Given a, b: can we compute a*b and a^2 from ONE multiplication?

a*(a+b) = a^2 + a*b. So from a*(a+b): 1 mul, then:
a^2 = ? We still need it separately.

(a+b)^2 = a^2 + 2ab + b^2. Hmm, introduces b^2.

2ab = (a+b)^2 - a^2 - b^2. Classical Karatsuba identity.

None of these give us both a^2 and ab from 1 operation.

THEOREM (informal): Computing both a*b and a^2 requires at least 2 multiplications.
(Unless one of them is known/trivial.) This is because they represent 2 independent
bilinear/quadratic forms in the inputs.

So at each level of recursion, we need 3 pairs × 2 ops = 6 sub-operations.
Regular Karatsuba for both separately: 3 + 3 = 6 sub-operations. Same!

So there's NO asymptotic sharing benefit from computing f*l and l^2 together.

## Pass 4: Completely different approach — can we use only squarings (no general muls)?

Squarings are cheaper than general muls. Can we reformulate to use ONLY squarings?

Key identities:
- 2*F(k)*L(k) = 2*F(2k) — but we need F(k)*L(k), not 2× it.
- (F+L)^2 = F^2 + 2FL + L^2 → FL = ((F+L)^2 - F^2 - L^2) / 2

So F(2k) = F(k)*L(k) = ((F(k)+L(k))^2 - F(k)^2 - L(k)^2) / 2

This uses 3 squarings + O(d) additions/shifts. Compared to 1 mul + 1 sq.

Is 3 squarings cheaper than 1 mul + 1 sq?
Squaring is about 0.6-0.8x cost of general mul.
3 sq ≈ 1.8-2.4 equivalent muls vs 1 + 0.6-0.8 = 1.6-1.8 equivalent muls.
So 3 squarings is WORSE. Not helpful.

What about 2 squarings?
(F+L)^2 - (F-L)^2 = 4FL → FL = ((F+L)^2 - (F-L)^2) / 4

So: F(2k) = ((F+L)^2 - (F-L)^2) / 4
And: L(2k) = L^2 - 2*(-1)^k → still need L^2.

Total: (F+L)^2 + (F-L)^2 + L^2 = 3 squarings. Wait, we used (F+L)^2 and (F-L)^2 for FL, plus L^2 for L(2k). That's 3 squarings still.

But can we derive L^2 from (F+L)^2 and (F-L)^2?
(F+L)^2 + (F-L)^2 = 2(F^2 + L^2)
(F+L)^2 - (F-L)^2 = 4FL

L^2 = ((F+L)^2 + (F-L)^2)/2 - F^2. Now we need F^2 too. 4 squarings = worse.

Alternatively, use identity L^2 = 5F^2 + 4*(-1)^k:
L(2k) = 5*F(k)^2 + 2*(-1)^k (derived earlier)

So: F(2k) = ((F+L)^2 - (F-L)^2) / 4 [2 squarings]
    L(2k) = 5*F^2 + 2*(-1)^k [1 squaring]
Total: 3 squarings. Still worse than 1 mul + 1 sq ≈ 1.7 equivalent muls.

Minimum 2 squarings for FL + 1 for L update = 3. Can't do it in 2 squarings total.

## Pass 5: Accept the 1 mul + 1 sq bound, optimize everything else

### 5a: Minimize Python overhead

The hot loop has these Python-level operations per iteration:
1. f * l (bigint mul — dominates)
2. l * l (bigint sq — dominates)
3. sign << 1 (tiny int shift)
4. subtraction from l*l result
5. sign = 1 (assignment)
6. (n >> bit) & 1 (bit test)
7. if branch
8. Conditional: additions, shifts, assignments

For the bit test, since n fits in a machine word for our cases (n ≤ 100000),
`(n >> bit) & 1` is O(1). Using `bin()` string would add overhead from string creation.

### 5b: Alternative to `l * l - (sign << 1)`

Replace sign tracking with direct computation:

```python
# sign is (-1)^k where k is the current index
# After doubling, k is even → sign = 1 → 2*sign = 2
# After increment (bit=1), k is odd → sign = -1 → 2*sign = -2
# So adj = 2 after even step, adj = -2 after odd step
```

Using a precomputed adj value eliminates the `2*sign` computation:

```python
adj = -2  # initial: k=1 is odd
for bit in ...:
    f = f * l
    l = l * l - adj
    adj = 2
    if (n >> bit) & 1:
        ...
        adj = -2
```

This saves: one `sign << 1` per iteration (multiplication of small ints).
Tiny but real.

### 5c: Optimize the increment step

Original: `f, l = (f + l) >> 1, (5 * f + l) >> 1`

Using the identity l_new = f_new + 2*f_old:
```python
if (n >> bit) & 1:
    t = f
    f = (f + l) >> 1
    l = f + (t << 1)
    adj = -2
```

This replaces `5*f + l` with `f_new + 2*f_old`. Both are O(d).
`5*f` in CPython: single-digit multiply, processes all digits.
`t << 1`: shift left by 1, processes all digits.
`f + (t << 1)`: addition, processes all digits.

So we trade 1 multiply-by-5 + 1 addition + 1 shift for: 1 shift + 1 addition.
Save: 1 multiply-by-5 operation → save 1 O(d) pass over the data.

For n=100000, d ≈ 70000 bits ≈ 1094 64-bit words. Each pass over the data is ~1000 word operations. The big multiplications are O(d^1.585) ≈ 1,000,000+ word operations. So saving one O(d) pass saves ~0.1% per iteration. Negligible.

But it's free in terms of code complexity, so keep it.

### 5d: Can we reformulate the doubling to do fewer O(d) operations?

Current doubling:
```
f = f * l          # O(d^1.585) mul
l = l * l - adj    # O(d^1.585) sq + O(d) sub
```

The subtraction is O(d). Can't avoid it (it's part of the formula).
The only way to avoid it would be if we could fold it into the next step.

L(2k) = L(k)^2 - 2*(-1)^k

In the next iteration, we compute:
F(4k) = F(2k) * L(2k) = F(2k) * (L(k)^2 - 2*(-1)^k)

If we delay the subtraction:
l_raw = l * l  # L(k)^2, without the -2*sign adjustment
# Then in next iteration:
f_next = f * (l_raw - adj)  # fold the adjustment into the mul

But f*(l_raw - adj) = f*l_raw - f*adj. We can't avoid computing f*l_raw (the expensive part)
and then subtracting f*adj (O(d)). The total work is the same; we just moved the subtraction.

Actually wait — this is WORSE because f*adj is O(d) (multiply f by 2 or -2) vs the original
adj subtraction from l which is O(1) (subtract 2 from a big number = adjust last few digits).

Subtracting 2 from a big integer is O(1) on average (only a few carries), not O(d)!
So `l*l - 2` is cheaper than `l*l` followed by delay-folded `f*(l-2) = f*l - 2f`.

Keep the subtraction where it is.

### 5e: Use a while loop with mask instead of range()

```python
mask = 1 << (n.bit_length() - 2)
while mask:
    f = f * l
    l = l * l - adj
    adj = 2
    if n & mask:
        t = f
        f = (f + l) >> 1
        l = f + (t << 1)
        adj = -2
    mask >>= 1
```

`while mask` + `mask >>= 1` vs `for bit in range(...)` + `(n >> bit) & 1`.
The while loop avoids creating a range object and the bit-shift of n on each iteration.
Instead it shifts the (small) mask. Both are O(1) for small n.

### 5f: Consider whether `f * l` can be reordered with `l * l`

If we compute l*l FIRST (while the previous f*l result is being garbage collected?),
does that affect cache behavior? In Python, this is all managed by the interpreter
and we can't control cache behavior. Irrelevant.

But wait — if we compute l*l first, we get l_new. Then we need old l for f*l... but we
already overwrote it! So we'd need to save old l.

Original order: f = f*l (uses old f, old l), l = l*l - adj (uses old l).
Both use old l. In the original code, after `f = f*l`, f is updated but l still has old value.
Then l*l uses the old l. Correct.

Alternative: l_sq = l*l; f = f*l; l = l_sq - adj. Same thing, just saves l*l in a temp.

Or: l_sq = l*l - adj; f = f*l; l = l_sq. Wait, now f = f * old_l, but old_l is still available because we saved l_sq separately! No... we need old l for both f*l and l*l. Both are computed before either is assigned. The Python semantics handle this correctly in the original code.

## Pass 6: The BIG idea — can we change the REPRESENTATION?

What if we don't use standard Python integers?

"Pure Python, no external libraries" — but we could store numbers as lists of digits
and implement our own multiplication that's faster for this specific use case?

Python's built-in int multiplication is implemented in C (longobject.c). Any pure-Python
reimplementation would be orders of magnitude slower due to interpreter overhead.
Even if we used a theoretically better algorithm (e.g., FFT-based), the constant factor
from Python interpretation would kill us.

So: we MUST use Python's native int multiplication. No way around it.

## Pass 7: The ONLY remaining avenue — reduce the number of bits processed

Can we skip any iterations?

The number of iterations = n.bit_length() - 1.
For n=100000: 17 bits → 16 iterations.
For n=10000: 14 bits → 13 iterations.

Can we reduce from 16 to 15 by processing 2 bits in the first step?

Start with precomputed (F(k), L(k)) for k ∈ {2, 3} instead of k=1.
Then skip the first iteration.

k=1: F=1, L=1
After 1st iteration with bit=0: F(2)=1, L(2)=3
After 1st iteration with bit=1: F(3)=2, L(3)=4

So for n with MSB bits "10..." start with (1, 3, adj=2)
For n with MSB bits "11..." start with (2, 4, adj=-2)

This saves 1 iteration. The first iteration involves tiny numbers so the actual
time savings is microseconds. Not meaningful.

But we could extend this: precompute for the first 4 bits → skip 3 iterations.
16 possible starting states. Saves 3 iterations with tiny numbers. Still negligible.

## Pass 8: What about the FINAL multiplication?

The last iteration's multiplication is the most expensive (largest numbers).
Can we optimize specifically for that?

For n even (LSB=0): last step is just doubling. F(n) = F(n/2) * L(n/2).
For n odd (LSB=1): last step is doubling + increment.

For n=100000 (even): the last multiplication is F(50000) * L(50000).
These numbers have ~35000 bits each. The multiplication is O(35000^1.585) ≈ expensive.

Can we avoid this last multiplication? Not without a fundamentally different algorithm.

## Pass 9: What about using the GMP-style binary GCD or Lehmer-type approach?

These are algorithms for GCD computation that work with fractions of the input.
Not applicable to Fibonacci computation.

## Pass 10: Summary and final implementation plan

After exhaustive analysis, the 1 mul + 1 sq per step (FL fast doubling) is optimal
for pure Python. The only improvements are micro-optimizations:

1. Pre-compute adj (2 or -2) instead of sign*2 each iteration
2. Use l_new = f_new + 2*f_old instead of (5*f + l) >> 1 in increment step
3. Use while loop with mask instead of range()
4. Pre-check for n=2 boundary case to skip loop entirely (if n < 4)

ALSO: Let me reconsider one thing I haven't tried:

## Pass 11: WHAT IF we use (F(k), F(k-1)) with a different doubling?

Track a = F(k), b = F(k-1). Then:
F(2k) = F(k) * (2*F(k-1) + F(k))... wait:
F(2k) = F(k) * (2*F(k+1) - F(k)) = F(k) * (2*(F(k)+F(k-1)) - F(k)) = F(k) * (F(k) + 2*F(k-1))
       = a * (a + 2b) = a^2 + 2ab

F(2k-1) = F(k)^2 + F(k-1)^2 = a^2 + b^2 (nope, that's F(2k-1))

Wait, I need F(2k) and F(2k-1) to continue:
For bit=0: go from (F(k), F(k-1)) to (F(2k), F(2k-1))
For bit=1: go from (F(k), F(k-1)) to (F(2k+1), F(2k))

F(2k) = a^2 + 2ab = a(a + 2b)  [1 mul or 1 sq + 1 mul]
F(2k-1) = a^2 + b^2  [2 squarings]

Total ops needed: a^2, b^2, ab → 2 sq + 1 mul. Then:
F(2k) = a^2 + 2*ab
F(2k-1) = a^2 + b^2

This is 1 mul + 2 sq. Worse than FL's 1 mul + 1 sq.

## Pass 12: What about using 3-term recurrence tricks?

Fibonacci satisfies: F(n+1) = F(n) + F(n-1)
And: F(n)^2 = F(n+1)*F(n-1) + (-1)^(n+1) (Cassini's identity)

Could use this to compute squarings from products? Not obviously helpful.

## FINAL IMPLEMENTATION

The best I can do is the FL fast doubling with micro-optimizations. Let me also consider
one more thing: the order of operations might matter for Python's memory allocator.

Actually, let me think about one more approach:

### What about precomputing 5*f in advance?

In the odd step, we need 5*f. But 5*f where f = F(2k) = f_old * l_old.
So 5*f = 5 * f_old * l_old. Could we compute 5*f_old first and then multiply by l_old?
5*f_old is O(d/2) work (f_old has ~d/2 digits at that point in the recursion).
Then (5*f_old) * l_old is a general mul with slightly larger operand.

Actually, this wouldn't help because the general mul dominates and we're making one
operand 2.3x larger (5*f vs f), making the multiplication more expensive.

### Binary representation optimization

For the specific case n=100000:
100000 in binary = 11000011010100000 (17 bits)
Bit pattern from MSB-1: 1000011010100000

Number of 1-bits (excluding MSB): 5 ones out of 16 remaining bits.
So 16 doubling steps + 5 increment steps.

The increment steps are cheap (O(d) additions), so the cost is dominated by 16 muls + 16 sqs.

## DONE — write final version
