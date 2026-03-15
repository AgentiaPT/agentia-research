# Fibonacci Optimization Scratchpad

## Pass 1: Analyze the Starting Code

The starting code uses **fast doubling**:
- Given F(k) = a, F(k+1) = b:
  - F(2k) = a * (2b - a)
  - F(2k+1) = a² + b²
- Then if the current bit is 1, shift to (F(2k+1), F(2k+2)) = (d, c+d)
- ~3 multiplications per bit: a*(2b-a) needs 1 mul, a² needs 1 mul, b² needs 1 mul

Total: 3 multiplications per bit of n. For n=100000, that's about 17 bits, so ~51 big-int multiplications.

## Key Question: Can we reduce multiplications per step?

### Idea 1: Rewrite to use fewer multiplications
The formulas are:
- c = a * (2b - a) = 2ab - a²
- d = a² + b²

If we compute a² first, then:
- a_sq = a * a          (1 mul)
- b_sq = b * b          (1 mul)
- d = a_sq + b_sq
- c = 2ab - a_sq

But 2ab = (a+b)² - a² - b². So c = (a+b)² - a² - b² - a² = (a+b)² - 2*a² - b²
That's still 3 multiplications (a², b², (a+b)²) but we can compute:
- a_sq = a*a
- b_sq = b*b
- ab_sum_sq = (a+b)*(a+b)  -- but this is also a multiplication

Wait, there's a classic trick: Karatsuba-style.
Given a*a, b*b, and (a+b)*(a+b), we get:
- a², b², and a² + 2ab + b²
- So 2ab = (a+b)² - a² - b²

This means:
- c = 2ab - a² = (a+b)² - a² - b² - a² = (a+b)² - 2*a² - b²
- d = a² + b²

Still 3 squarings. But **squarings can be faster than general multiplications** in Python's big integer implementation!

In CPython, `x*x` (squaring) is detected and optimized vs `x*y` (general multiplication). The Karatsuba algorithm for squaring has fewer recursive calls. Squaring is roughly 1.5-2x faster than general multiplication for large numbers.

### Idea 2: Replace a*(2b-a) with squarings only

Using the Karatsuba trick:
- Compute a² = a*a
- Compute b² = b*b
- Compute s² = (a+b)*(a+b)  -- this is (a+b)²
- Then 2ab = s² - a² - b²
- c = F(2k) = 2ab - a² = s² - 2*a² - b²
- d = F(2k+1) = a² + b²

So: 3 squarings instead of 2 multiplications + 1 squaring (the original has 1 general mul a*(2b-a) and the a*a, b*b which could be either).

Wait, let me re-examine the original:
- `c = a * ((b << 1) - a)` -- this is a general multiplication (a != 2b-a in general)
- `d = a * a + b * b` -- these are two squarings

So the original has: 1 general mul + 2 squarings = 3 operations.

My proposal: 3 squarings = 3 operations. Since squarings are faster than general muls, this should be faster!

### Idea 3: Can we get to 2 multiplications?

The matrix [[1,1],[1,0]]^n approach uses matrix squaring. Each matrix square needs:
- For [[a,b],[b,c]] (symmetric!), squaring gives:
  - a² + b², ab + bc = b(a+c), b² + c²
- That's 3 multiplications for the symmetric matrix... same count.

What about using different recurrence relations?

Lucas numbers: L(n) = F(n-1) + F(n+1) = 2*F(n-1) + F(n)
There are identities involving F and L:
- F(2n) = F(n) * L(n)
- L(2n) = L(n)² - 2*(-1)^n
- L(n) = 2*F(n+1) - F(n)

If we track (F(k), L(k)):
- F(2k) = F(k) * L(k)                    -- 1 multiplication
- L(2k) = L(k)² - 2*(-1)^k              -- 1 squaring
- F(2k+1) = (F(2k) + L(2k)) / 2         -- wait, need to handle odd step

Actually the Fibonacci-Lucas doubling:
Given F(k) and L(k):
- F(2k) = F(k) * L(k)
- L(2k) = L(k)² - 2*(-1)^k

For the odd bit (shifting from 2k to 2k+1):
- F(2k+1) = (2*F(2k) + L(2k)) / 2... hmm, or use:
  - F(k+1) = (F(k) + L(k)) / 2
  - L(k+1) = (L(k) + 5*F(k)) / 2... this involves division by 2 and multiplication by 5

Wait, let me be more careful.

Key identities:
- L(n) = F(n-1) + F(n+1) = 2*F(n+1) - F(n)
- 5*F(n)² = L(n)² - 4*(-1)^n  (relates F and L)
- F(2n) = F(n)*L(n)
- L(2n) = L(n)² - 2*(-1)^n

For the "+1" step when bit is 1:
- F(n+1) = (F(n) + L(n)) / 2
- L(n+1) = (5*F(n) + L(n)) / 2

The division by 2... if F(n) and L(n) have the same parity (which they do: F and L always have the same parity), this is exact integer division.

So the doubling step is:
- F(2k) = F(k) * L(k)       -- 1 general multiplication
- L(2k) = L(k)² - 2*(-1)^k  -- 1 squaring
- sign = (-1)^(2k) = ((-1)^k)² = 1 always... wait no.
  (-1)^k alternates. After doubling, (-1)^(2k) = ((-1)^k)^2 = 1 always? No: (-1)^(2k) = 1 for all k. So L(2k) = L(k)² - 2.

And for odd step:
- F(2k+1) = (F(2k) + L(2k)) / 2  -- just addition and shift
- L(2k+1) = (5*F(2k) + L(2k)) / 2  -- mul by 5 (cheap: 4*F + F, shift+add) and shift
- And (-1)^(2k+1) = -1

So total per bit: **1 general multiplication + 1 squaring** (+ cheap add/shift ops)!

That's only 2 big-int multiplications per step instead of 3!

This is a significant improvement! Let me think about whether this is correct...

## Verification of Fibonacci-Lucas doubling

Start: F(0) = 0, L(0) = 2, (-1)^0 = 1

Let me trace for n = 7 (binary 111):

Bit processing MSB first: bits are 1, 1, 1

Start: k=0, F=0, L=2

Bit 2 (MSB, value 1):
- Double: F(0)=0, L(0)=2
  - F(0) = 0*2 = 0 (F(0)=0 ✓)
  - L(0) = 2²-2 = 2 (L(0)=2 ✓)
- Bit is 1, so increment:
  - F(1) = (0+2)/2 = 1 ✓
  - L(1) = (5*0+2)/2 = 1 ✓
  - k=1, (-1)^k = -1

Bit 1 (value 1):
- Double: F(1)=1, L(1)=1, (-1)^1=-1
  - F(2) = 1*1 = 1 (F(2)=1 ✓)
  - L(2) = 1²-2*(-1) = 1+2 = 3 (L(2)=3 ✓)
  - k=2, (-1)^2 = 1
- Bit is 1, so increment:
  - F(3) = (1+3)/2 = 2 ✓
  - L(3) = (5*1+3)/2 = 4 ✓
  - k=3, (-1)^3 = -1

Bit 0 (LSB, value 1):
- Double: F(3)=2, L(3)=4, (-1)^3=-1
  - F(6) = 2*4 = 8 (F(6)=8 ✓)
  - L(6) = 4²-2*(-1) = 16+2 = 18 (L(6)=18 ✓)
  - k=6, (-1)^6 = 1
- Bit is 1, so increment:
  - F(7) = (8+18)/2 = 13 ✓ (F(7)=13!)
  - L(7) = (5*8+18)/2 = 58/2 = 29 ✓ (L(7)=29!)
  - k=7

Result: F(7) = 13 ✓

This works and uses only 2 big-int multiplications per bit!

## Parity concern for the division by 2

F(n) and L(n): Are F(n)+L(n) and 5*F(n)+L(n) always even?

F(n) mod 2: 0,1,1,0,1,1,0,1,1,... (period 3: 0,1,1)
L(n) mod 2: 2,1,3,4,7,11,... mod 2: 0,1,1,0,1,1,... (period 3: 0,1,1)

So F(n) and L(n) have the same parity! Therefore F(n)+L(n) is always even. ✓
And 5*F(n)+L(n) ≡ F(n)+L(n) ≡ 0 (mod 2). ✓

## Sign tracking

Need to track (-1)^k. After doubling, k becomes 2k, so (-1)^(2k) = 1 always.
After incrementing, k becomes 2k+1, so (-1)^(2k+1) = -1 always.

So the sign after each step depends only on whether the bit was 1 (sign becomes -1) or 0 (sign stays +1 from doubling).

Actually wait - the sign before the doubling matters for the L(2k) formula:
L(2k) = L(k)² - 2*(-1)^k

So I need to track the sign of (-1)^k entering each step. Let me re-think...

After processing bit i:
- If bit was 0: k = 2*k_prev, sign = +1 (since (-1)^(2k) = 1)
- If bit was 1: k = 2*k_prev + 1, sign = -1

So entering the NEXT step, sign is determined by the PREVIOUS bit.

Let me re-trace more carefully, tracking sign:

Initial: k=0, F(0)=0, L(0)=2, sign=(-1)^0=+1

For each bit (MSB to LSB):
  1. Double step:
     F(2k) = F(k) * L(k)
     L(2k) = L(k)² - 2*sign   (where sign = (-1)^k entering this step)
     new_sign = +1  (since (-1)^(2k) = 1)

  2. If bit is 1:
     F(2k+1) = (F(2k) + L(2k)) / 2
     L(2k+1) = (5*F(2k) + L(2k)) / 2
     new_sign = -1  (since (-1)^(2k+1) = -1)

Actually, I realize we can simplify: after doubling, sign is always +1, and after increment, sign is always -1. So:
- sign entering doubling = whatever sign was after previous step
- If previous bit was 0: sign = +1
- If previous bit was 1: sign = -1

For the very first iteration, sign = +1 (k=0 initially).

But wait, the first bit is always 1 for positive n (MSB). And we start at k=0.
In the first doubling: F(0)*L(0) = 0, L(0)²-2*(+1) = 2. So F(0)=0, L(0)=2. Good.
Then bit=1: F(1)=(0+2)/2=1, L(1)=(0+2)/2=1. sign=-1.

Second bit: doubling with sign=-1:
F(2k) = F*L, L(2k) = L² - 2*(-1) = L² + 2.

Yes this matches my trace above!

## Code for Fibonacci-Lucas version

```python
def fibonacci(n):
    if n < 0:
        return 0
    if n <= 1:
        return n

    f, l = 0, 2  # F(0), L(0)
    sign = 1     # (-1)^0

    for bit in range(n.bit_length() - 1, -1, -1):
        # Double
        f_new = f * l
        l_new = l * l - 2 * sign
        sign = 1  # (-1)^(2k) = 1

        if (n >> bit) & 1:
            # Increment
            f_new, l_new = (f_new + l_new) >> 1, (5 * f_new + l_new) >> 1
            sign = -1  # (-1)^(2k+1) = -1

        f, l = f_new, l_new

    return f
```

This uses **2 big-int multiplications per bit** (f*l and l*l) vs the original's 3.

The `5*f_new` is cheap: it's (f_new << 2) + f_new, which is just shifts and adds.

## Can we do even better? 1 multiplication per step?

Probably not without a fundamentally different approach. The algebraic structure requires at least knowing products of the growing numbers.

## Pass 2: Further micro-optimizations

### Optimization: Avoid the first iteration
Since we start at F(0)=0, L(0)=2, the first doubling always gives F(0)=0, L(0)=2. And the MSB is always 1, so we always increment to F(1)=1, L(1)=1. We can skip the first iteration entirely.

```python
def fibonacci(n):
    if n < 0:
        return 0
    if n <= 1:
        return n

    f, l = 1, 1  # F(1), L(1)
    sign = -1    # (-1)^1 = -1

    for bit in range(n.bit_length() - 2, -1, -1):  # skip MSB
        # Double
        f_new = f * l
        l_new = l * l - 2 * sign
        sign = 1

        if (n >> bit) & 1:
            f_new, l_new = (f_new + l_new) >> 1, (5 * f_new + l_new) >> 1
            sign = -1

        f, l = f_new, l_new

    return f
```

### Optimization: Use bit manipulation for 5*f
`5 * f_new` = `(f_new << 2) + f_new`. For big integers, this avoids the multiplication overhead. Python's `*` with small int 5 should already be fast though... but let me think.

Actually for big integers, multiplying by a small constant like 5 is O(n) where n is the number of digits - it's a single-word multiply. Python handles this efficiently. The `<< 2` + add approach is also O(n). Probably similar speed, but the multiply-by-small-int might have less overhead since it's a single C function call vs two.

### Optimization: Reduce object creation
In the bit=0 case, we can skip the increment step's tuple creation:

```python
if (n >> bit) & 1:
    f = (f_new + l_new) >> 1
    l = (5 * f_new + l_new) >> 1
    sign = -1
else:
    f = f_new
    l = l_new
```

Wait, I was already essentially doing this. Let me just be clean:

```python
def fibonacci(n):
    if n < 0:
        return 0
    if n <= 1:
        return n

    f, l = 1, 1  # F(1), L(1)
    sign = -1    # (-1)^1

    for bit in range(n.bit_length() - 2, -1, -1):
        # Double: F(2k) = F(k)*L(k), L(2k) = L(k)²-2(-1)^k
        fl = f * l
        ll = l * l
        l = ll + 2 if sign < 0 else ll - 2
        f = fl
        sign = 1

        # Increment if bit is 1
        if (n >> bit) & 1:
            f, l = (f + l) >> 1, (5 * f + l) >> 1
            sign = -1

    return f
```

Hmm wait, I can avoid creating `ll` and `fl` as separate names:

Actually, let me think about whether sign tracking can be simplified. sign after doubling is always +1. After increment it's always -1. So entering the doubling step, sign = -1 if previous bit was 1, sign = +1 if previous bit was 0 (or first iter).

Since the first bit we process (after skipping MSB) can be 0 or 1, and we start with sign=-1 (from setting up F(1), L(1)):

The adjustment term is `-2*sign`. When sign=-1, it's +2. When sign=+1, it's -2.

Actually, I can avoid the sign variable entirely by just checking the previous bit... but that's messier. Let's keep sign.

### Optimization: Precompute bit list to avoid repeated bit extraction

```python
bits = []
k = n
while k:
    bits.append(k & 1)
    k >>= 1
# bits is LSB first, reverse it
# Then skip first (MSB) bit
```

Actually for n up to 100000, bit_length is about 17. The loop overhead is tiny. This won't matter.

### What about the 5*f multiplication?

For very large Fibonacci numbers (F(100000) has ~20,000 digits), 5*f is an O(digits) operation. Each doubling step does:
- f*l: O(digits^~1.585) via Karatsuba (or better for very large)
- l*l: O(digits^~1.585) (squaring, slightly faster)
- 5*f: O(digits) - negligible
- f+l: O(digits) - negligible
- >> 1: O(digits) - negligible

So the dominant cost is the two big multiplications. We've reduced from 3 to 2. That should give roughly a 33% speedup.

### Idea: Can we make one of the two multiplications a squaring?

Currently we have f*l (general) and l*l (squaring).

What if we tracked different quantities? If we tracked (L(k), something) where both doublings are squarings...

Alternatively, what if we use (a+b) and (a-b) style? Let:
- s = f + l
- d = l - f  (or f - l)

Then s*d = l² - f² and s² = f² + l² + 2fl, d² = f² + l² - 2fl

Hmm, this doesn't obviously help.

What about tracking L(k) and L(k+1)?  Or F(k) and F(k-1)?

Actually, let me reconsider. For the standard fast doubling with F(k) and F(k+1):
- We need F(k)*F(k), F(k+1)*F(k+1), and F(k)*(2*F(k+1)-F(k))
- That's 2 squarings + 1 general mul

For the FL approach:
- We need F(k)*L(k) (general) and L(k)*L(k) (squaring)
- That's 1 squaring + 1 general mul

**The FL approach saves one squaring per step!** The original has 2 squarings + 1 general mul = 3 ops. FL has 1 squaring + 1 general mul = 2 ops. That's a reduction from 3 to 2.

Wait, but in the original code: `c = a * ((b << 1) - a)` is a general mul, `a * a` is a squaring, `b * b` is a squaring. So original = 1 general + 2 squarings = 3 ops.

FL = 1 general (f*l) + 1 squaring (l*l) = 2 ops. Saves 1 squaring.

If squaring is ~0.7x the cost of a general mul, then:
- Original: 1.0 + 2*0.7 = 2.4 "mul-equivalents"
- FL: 1.0 + 0.7 = 1.7 "mul-equivalents"
- Speedup: ~29%

### Can we convert f*l to a squaring using the identity trick?

f*l = ((f+l)² - f² - l²) / 2

That replaces 1 general mul with 3 squarings... worse.

Or: f*l = ((f+l)² - (f-l)²) / 4

That's 2 squarings for 1 mul... still worse in total count.

So 1 general mul + 1 squaring seems optimal for the FL approach.

### Idea: Can we express F(2k) using only L values?

F(2k) = F(k) * L(k)

But F(k) = (L(k+1) - L(k-1)) / ... this gets complicated.

Or: L(n) = F(n-1) + F(n+1), and F(n) = (2*L(n) - L(n-1) - L(n+1))/... no, wrong.

Actually: 5*F(n) = L(n+1) + L(n-1)... I'd need to verify.

This doesn't look like it leads to fewer multiplications.

## Pass 2 Summary

The FL (Fibonacci-Lucas) approach with 2 multiplications per bit (1 general + 1 squaring) vs the original's 3 (1 general + 2 squarings) is the main win. This should give ~25-33% speedup.

## Pass 3: Micro-optimizations within the FL approach

1. **Local variable lookup**: In CPython, local variable access is LOAD_FAST which is faster than global or attribute lookup. Already using locals.

2. **Avoid repeated `n >> bit` computation**: We could pre-extract the bits. For small n (17 bits), this is negligible.

3. **Avoid the conditional branch**: We could try branchless, but with big integers the cost of the multiplications dominates.

4. **Can we reduce the "+1" step cost?**
   The increment step does:
   - f, l = (f + l) >> 1, (5 * f + l) >> 1
   This involves: 1 addition, 1 shift, 1 mul-by-5, 1 addition, 1 shift. All O(digits), negligible vs the multiplications.

5. **Right-to-left binary method?** Going LSB to MSB... I don't think this helps for fast doubling.

6. **2-bit windowing**: Process 2 bits at a time to reduce the number of iterations.
   For 2 bits, we'd need formulas for F(4k), F(4k+1), F(4k+2), F(4k+3).
   This halves the number of iterations but each iteration would need more multiplications.

   F(4k) from F(k), L(k):
   - First double: F(2k) = F(k)*L(k), L(2k) = L(k)²-2*(-1)^k
   - Second double: F(4k) = F(2k)*L(2k), L(4k) = L(2k)²-2
   - That's 2 general muls + 2 squarings = 4 ops for 2 bits
   - vs 2 ops/bit * 2 bits = 4 ops. Same!

   But with some cleverness, maybe we can share intermediate results?

   For the 00 case (no increments):
   - F(4k) = F(2k)*L(2k) = F(k)*L(k) * (L(k)²-2s)
   - This doesn't factor nicely.

   Probably not worth the complexity. Moving on.

7. **Is GMP-style sub-quadratic multiplication being used?**
   CPython uses Karatsuba for large integers (threshold ~70 digits in the C code). For F(100000) which has ~20,000 digits, we're well into Karatsuba territory. CPython doesn't use Toom-Cook or FFT though (unlike GMP).

8. **Can we help Python's memory allocation?**
   Not really in pure Python. Each big integer operation creates a new object.

## Pass 3: Alternative idea - use the (F(k), F(k-1)) pair

The standard doubling uses (a, b) = (F(k), F(k+1)).
What about (F(k), F(k-1))?

F(2k) = F(k) * (2*F(k-1) + F(k))
F(2k-1) = F(k)² + F(k-1)²

Hmm, this is isomorphic to the original. Same number of multiplications.

## Pass 4: Let me think about what makes the FL approach genuinely better

Original: per step = 1 general mul + 2 squarings
FL: per step = 1 general mul + 1 squaring

The saving is 1 squaring per step. With ~17 steps for n=100000, that's saving 17 squarings of very large numbers. This is significant.

## Pass 4: Code polish

Let me write the cleanest, fastest version:

```python
def fibonacci(n):
    if n < 0:
        return 0
    if n <= 1:
        return n

    # Use Fibonacci-Lucas doubling: 2 big-int muls per bit vs 3
    # F(2k) = F(k)*L(k),  L(2k) = L(k)² - 2*(-1)^k
    # F(k+1) = (F(k)+L(k))/2,  L(k+1) = (5*F(k)+L(k))/2

    f, l = 1, 1  # F(1), L(1)
    sign = -1

    for bit in range(n.bit_length() - 2, -1, -1):
        # Doubling step: 1 general mul + 1 squaring
        f = f * l          # F(2k) = F(k) * L(k)
        l = l * l - (sign << 1)  # L(2k) = L(k)² - 2*(-1)^k; sign<<1 = 2*sign
        sign = 1

        if (n >> bit) & 1:
            # Increment step: all O(digits) ops
            f, l = (f + l) >> 1, (5 * f + l) >> 1
            sign = -1

    return f
```

Wait, there's a subtle issue. In the doubling step, I compute `f = f * l` which overwrites f, but then I use the OLD f value is already gone when I compute l. Wait no - I compute `l = l * l - ...` which only uses l, not f. So the order is fine! f is updated first (uses old f and l), then l is updated (uses old l only).

Actually wait: `l = l * l - (sign << 1)`. This uses `l` which is the OLD l. Good.
And `f = f * l` uses old f and old l. Good.

But wait - we need to be careful. In Python, `f = f * l` is executed first, so f gets the new value. Then `l = l * l - ...` uses the OLD l (which wasn't changed). So the computation is:

f_new = f_old * l_old
l_new = l_old * l_old - 2*sign

This is correct! The order works because l is not modified by the first line.

But in the increment step: `f, l = (f + l) >> 1, (5 * f + l) >> 1`
Here, Python evaluates the RHS fully before assigning. So:
- (f + l) >> 1 uses f_new (from doubling) and l_new (from doubling)
- (5 * f + l) >> 1 uses f_new and l_new

We want: F(2k+1) = (F(2k) + L(2k)) / 2, L(2k+1) = (5*F(2k) + L(2k)) / 2
So yes, we should use the already-doubled values. Correct!

Hmm, but let me double-check: when we write `(5 * f + l) >> 1`, the `f` here is the UPDATED f (from the doubling line above). In Python:

```python
f = f * l          # f is now f_new = F(2k)
l = l * l - ...    # l is now l_new = L(2k)
# Now both f and l are the doubled values
f, l = (f + l) >> 1, (5 * f + l) >> 1
```

The tuple assignment evaluates RHS first using current (doubled) f and l. So:
- temp1 = (f + l) >> 1 = (F(2k) + L(2k)) / 2 = F(2k+1)  ✓
- temp2 = (5*f + l) >> 1 = (5*F(2k) + L(2k)) / 2 = L(2k+1)  ✓
Then f, l = temp1, temp2. Correct!

### Another micro-optimization: `sign << 1` vs `2 * sign`

`sign << 1` when sign is a small int (-1 or 1): both are fast. `sign << 1` shifts -1 to -2 and 1 to 2. Let me verify: in Python, -1 << 1 = -2. Yes. So `l * l - (sign << 1)` = `l*l - 2*sign` = `l*l ∓ 2`. Good.

Actually, since sign is always +1 or -1, and we know which one based on the previous bit, we could just use a conditional:

```python
if sign < 0:
    l = l * l + 2
else:
    l = l * l - 2
```

This avoids the multiplication/shift of sign and the subtraction. Might be microscopically faster.

Or even: we know sign is -1 iff the previous bit was 1. Since we're looking at bits from MSB to LSB, sign is -1 at the start (because we initialized to F(1), L(1), meaning the "previous" bit was 1 - the MSB).

Actually, to make this branchless and simple:

```python
# sign is +1 or -1
# l*l - 2*sign = l*l + 2 when sign=-1, l*l - 2 when sign=+1
```

This doesn't really matter for performance since l*l dominates.

## Let me think if there's any other algorithmic improvement...

### Idea: Can we combine the increment with the next doubling to save work?

If the current bit is 1 and the next bit is also being processed, we go:
double → increment → double → ...

The increment step transforms (F(2k), L(2k)) to (F(2k+1), L(2k+1)):
F(2k+1) = (F(2k) + L(2k)) / 2
L(2k+1) = (5*F(2k) + L(2k)) / 2

Then the next doubling does:
F(2*(2k+1)) = F(2k+1) * L(2k+1)
L(2*(2k+1)) = L(2k+1)² - 2

What if we substitute?
F(4k+2) = [(F(2k)+L(2k))/2] * [(5*F(2k)+L(2k))/2]
         = (F(2k)+L(2k)) * (5*F(2k)+L(2k)) / 4

Let u = F(2k), v = L(2k):
F(4k+2) = (u+v)(5u+v)/4

And we already computed u = f*l, v = l*l - 2s. So:
F(4k+2) = (f*l + l²-2s)(5*f*l + l²-2s) / 4

This is getting complicated and doesn't obviously save multiplications. Let's not pursue.

## Pass 5: Think about completely different approaches

### Matrix exponentiation?
Same complexity as fast doubling. The matrix method IS fast doubling in matrix form.

### Binet's formula with exact arithmetic?
F(n) = (φ^n - ψ^n) / √5 where φ = (1+√5)/2
Could use exact arithmetic with Z[√5] representation: a + b*√5
But this requires multiplying (a + b√5)(c + d√5) = (ac + 5bd) + (ad+bc)√5
Each such multiplication needs 3 general muls (Karatsuba: (a+b)(c+d) - ac - bd for the cross term, plus ac and 5*bd).
That's 3 muls per squaring step, worse than FL approach.

### Zeckendorf or other representations?
Not helpful for computing specific F(n).

### Splitting the computation?
Use Chinese Remainder Theorem: compute F(n) mod several primes, then reconstruct. But for pure Python, the CRT reconstruction of a 20,000-digit number from many small modular results is not obviously faster.

### FLINT/sympy-style polynomial multiplication tricks?
Can't use external libraries.

## Conclusion: The FL approach with 2 muls/step is the best I can do.

Let me write the final polished version.
