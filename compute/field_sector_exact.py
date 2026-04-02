r"""Exact integer analysis of all field sectors.

Key discovery from initial computation:
  [d^w T coeff at symmetric point] / [(-1)^{r+1} * C_{r-1}] is ALWAYS an integer.

For w=0: this integer is (2r+1) * (2r)!.
Question: what is it for general w?

Define: a_w(r) = [d^w T coeff] / [(-1)^{r+1} * C_{r-1}]  (an integer)

We know: a_0(r) = (2r+1) * (2r)! = (2r+1)!

Then: f_w(r) = a_w(r) / (2r)!

The goal: find closed forms for a_w(r) and the two-variable generating function.
"""

from __future__ import annotations
import sys, os, math
from fractions import Fraction
from typing import Dict, Tuple

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib'))

from m7_m10_depth_frontier import StasheffEngine


def catalan(n: int) -> int:
    if n < 0: return 0
    return math.comb(2 * n, n) // (n + 1)


def compute_integer_table(max_r: int = 8) -> Dict[Tuple[int,int], int]:
    """Compute a_w(r) = [d^w T coeff] / [(-1)^{r+1} * C_{r-1}] for all sectors."""
    engine = StasheffEngine(0.0)  # c=0 for pure field sector
    table = {}  # (r, w) -> integer

    for r in range(1, max_r + 1):
        k = 2 * r + 1
        engine._cache.clear()
        lams = tuple(1.0 for _ in range(k - 1))
        result = engine.mk(lams)

        sign = (-1) ** (r + 1)
        cat = catalan(r - 1)

        for w in range(0, 2*r + 1):
            val = result.get(w, 0.0)
            if abs(val) < 0.5:
                table[(r, w)] = 0
                continue
            a_wr = val / (sign * cat)
            a_int = round(a_wr)
            if abs(a_wr - a_int) > max(1.0, abs(a_int) * 1e-6):
                print(f"  WARNING: a_{w}({r}) = {a_wr} is NOT integer!")
                table[(r, w)] = 0
            else:
                table[(r, w)] = a_int

    return table


def main():
    print("=" * 80)
    print("EXACT INTEGER FIELD-SECTOR ANALYSIS")
    print("=" * 80)

    max_r = 7  # enough data, avoid floating-point issues at r=8
    table = compute_integer_table(max_r=max_r)

    # ===================================================================
    # Display the integer table a_w(r)
    # ===================================================================
    print("\n" + "=" * 80)
    print("TABLE 1: a_w(r) = [d^w T coeff] / [(-1)^{r+1} * C_{r-1}]")
    print("=" * 80)

    max_w = max(w for (r, w) in table if table[(r, w)] != 0)

    for r in range(1, max_r + 1):
        k = 2 * r + 1
        print(f"\n  r={r} (k={k}):")
        for w in range(0, 2*r + 1):
            a = table.get((r, w), 0)
            if a != 0:
                print(f"    w={w:2d}: a = {a}")

    # ===================================================================
    # Check: is a_0(r) = (2r+1)! ?
    # ===================================================================
    print("\n" + "=" * 80)
    print("CHECK 1: a_0(r) = (2r+1)! = (2r+1) * (2r)!")
    print("=" * 80)

    for r in range(1, max_r + 1):
        a = table[(r, 0)]
        expected = math.factorial(2 * r + 1)
        print(f"  r={r}: a_0 = {a}, (2r+1)! = {expected}, match = {a == expected}")

    # ===================================================================
    # Factor out (2r)! : define b_w(r) = a_w(r) / (2r)!
    # ===================================================================
    print("\n" + "=" * 80)
    print("TABLE 2: b_w(r) = a_w(r) / (2r)! = f_w(r)")
    print("  (this is NOT integer in general, but is rational)")
    print("=" * 80)

    for w in range(0, 10):
        print(f"\n  w={w}:")
        for r in range(1, max_r + 1):
            a = table.get((r, w), 0)
            if a == 0 and w > 0:
                continue
            fact = math.factorial(2 * r)
            b = Fraction(a, fact)
            print(f"    r={r}: a_w={a}, b_w = a_w/(2r)! = {b} = {float(b):.10f}")

    # ===================================================================
    # Alternative normalization: divide by (2r-2w)! instead
    # For w=0: a_0/(2r)! = 2r+1. What about a_w / (2r-2w+1)! ?
    # Or try a_w / (2r+1-w)! etc.
    # ===================================================================
    print("\n" + "=" * 80)
    print("TABLE 3: Try various normalizations for a_w(r)")
    print("=" * 80)

    # Try: a_w(r) / (2r+1-2w)!
    print("\n  --- Trying a_w(r) / (2r+1-2w)! ---")
    for w in range(0, 6):
        print(f"\n  w={w}:")
        for r in range(max(1, w+1), max_r + 1):
            a = table.get((r, w), 0)
            if a == 0: continue
            n = 2*r + 1 - 2*w
            if n < 0: continue
            fact_n = math.factorial(n)
            ratio = Fraction(a, fact_n)
            print(f"    r={r}: a_w/{n}! = {ratio} = {float(ratio):.10f}")

    # Try: a_w(r) / (2r-w)!
    print("\n  --- Trying a_w(r) / (2r-w)! ---")
    for w in range(0, 6):
        print(f"\n  w={w}:")
        for r in range(max(1, (w+2)//2), max_r + 1):
            a = table.get((r, w), 0)
            if a == 0: continue
            n = 2*r - w
            if n < 0: continue
            fact_n = math.factorial(n)
            ratio = Fraction(a, fact_n)
            print(f"    r={r}: a_w/{n}! = {ratio} = {float(ratio):.10f}")

    # ===================================================================
    # The two-variable EGF: F(x,y) = sum_{r,w} a_w(r) * x^r * y^w / w!
    # ===================================================================
    print("\n" + "=" * 80)
    print("TABLE 4: c_w(r) = a_w(r) / w! (coefficients for EGF in y)")
    print("=" * 80)

    for w in range(0, 8):
        print(f"\n  w={w}:")
        wfact = math.factorial(w)
        for r in range(1, max_r + 1):
            a = table.get((r, w), 0)
            if a == 0: continue
            c = Fraction(a, wfact)
            print(f"    r={r}: a_w/w! = {c} = {float(c):.6f}")

    # ===================================================================
    # Look at the SHIFTED sequence: a_w(r) for fixed w, as function of r
    # ===================================================================
    print("\n" + "=" * 80)
    print("TABLE 5: RATIOS a_w(r+1) / a_w(r)")
    print("=" * 80)

    for w in range(0, 8):
        print(f"\n  w={w}:")
        prev_a = None
        for r in range(1, max_r + 1):
            a = table.get((r, w), 0)
            if a == 0:
                prev_a = None
                continue
            if prev_a is not None and prev_a != 0:
                ratio = Fraction(a, prev_a)
                # Also compare to -(2r)(2r+1) which is the ratio for (2r+1)!/(2r-1)!
                canonical = Fraction(-(2*r)*(2*r+1), 1)
                print(f"    r={r}: a_w(r)/a_w(r-1) = {ratio} = {float(ratio):.6f}  "
                      f"[cf -(2r)(2r+1) = {canonical}]")
            prev_a = a

    # ===================================================================
    # KEY INSIGHT: Look at a_w(r) / a_0(r) = a_w(r) / (2r+1)!
    # This should be a "nice" function.
    # ===================================================================
    print("\n" + "=" * 80)
    print("TABLE 6: a_w(r) / a_0(r) = [d^w T coeff] / [T coeff]")
    print("  = a_w(r) / (2r+1)!")
    print("=" * 80)

    for w in range(0, 10):
        print(f"\n  w={w}:")
        for r in range(1, max_r + 1):
            a_w = table.get((r, w), 0)
            a_0 = table.get((r, 0), 0)
            if a_0 == 0 or a_w == 0: continue
            ratio = Fraction(a_w, a_0)
            print(f"    r={r}: a_w/a_0 = {ratio}")

    # ===================================================================
    # HARMONIC NUMBER DETECTION
    # The ratios from Table 6 might involve harmonic numbers H_n = sum_{k=1}^n 1/k
    # ===================================================================
    print("\n" + "=" * 80)
    print("TABLE 7: HARMONIC NUMBER IDENTIFICATION")
    print("  H_n = 1 + 1/2 + ... + 1/n")
    print("=" * 80)

    def harmonic(n):
        return sum(Fraction(1, k) for k in range(1, n + 1))

    print("\n  Harmonic numbers:")
    for n in range(1, 16):
        print(f"    H_{n} = {harmonic(n)} = {float(harmonic(n)):.10f}")

    # Check: is a_1(r)/a_0(r) related to H_{2r} or H_{2r+1}?
    print("\n  w=1: checking a_1/a_0 vs harmonic numbers:")
    for r in range(1, max_r + 1):
        a_1 = table.get((r, 1), 0)
        a_0 = table.get((r, 0), 0)
        if a_0 == 0 or a_1 == 0: continue
        ratio = Fraction(a_1, a_0)
        H_2r = harmonic(2*r)
        H_2r1 = harmonic(2*r + 1)
        H_r = harmonic(r)
        print(f"    r={r}: ratio = {ratio} = {float(ratio):.10f}")
        print(f"           H_{2*r} = {H_2r} = {float(H_2r):.10f}")
        print(f"           H_{2*r+1} = {H_2r1} = {float(H_2r1):.10f}")
        print(f"           ratio - H_{2*r} = {float(ratio - H_2r):.10f}")
        print(f"           ratio - H_{2*r+1} = {float(ratio - H_2r1):.10f}")
        # Try: ratio = H_{2r} - 1/2 ?
        print(f"           H_{2*r} - 1/2 = {float(H_2r - Fraction(1,2)):.10f}")
        # Try: ratio = H_{2r} - 1/(2(2r+1))
        diff_H2r = ratio - H_2r
        print(f"           ratio - H_{2*r} = {diff_H2r}")

    # ===================================================================
    # DEEPER: check if a_w/a_0 involves products of harmonic numbers
    # ===================================================================
    print("\n" + "=" * 80)
    print("TABLE 8: SECOND DERIVATIVE SECTOR — a_2/a_0")
    print("=" * 80)

    print("\n  w=2: checking a_2/a_0:")
    for r in range(1, max_r + 1):
        a_2 = table.get((r, 2), 0)
        a_0 = table.get((r, 0), 0)
        if a_0 == 0 or a_2 == 0: continue
        ratio = Fraction(a_2, a_0)
        H_2r = harmonic(2*r)
        r1 = Fraction(a_2, a_0)
        # Check (ratio * 2) vs H_{2r}^2, etc.
        print(f"    r={r}: a_2/a_0 = {ratio} = {float(ratio):.10f}")
        print(f"           H_{2*r}^2/2 = {float(H_2r**2/2):.10f}")
        # Try: ratio = (H_{2r}^2 - H_{2r}^{(2)}) / 2 where H^{(2)} = sum 1/k^2
        H2r_sq2 = sum(Fraction(1, k*k) for k in range(1, 2*r+1))
        check = (H_2r**2 - H2r_sq2) / 2
        print(f"           (H_{2*r}^2 - H_{2*r}^(2))/2 = {float(check):.10f}")
        diff = ratio - check
        print(f"           difference = {diff}")

    # ===================================================================
    # The magic formula: a_w/a_0 = e_w(H_1, H_2, ..., H_2r) ??
    # where H_j^{(p)} = sum_{k=1}^j 1/k^p
    # ===================================================================
    # For w=1: try a_1/a_0 = H_{2r} + c for some constant c
    print("\n" + "=" * 80)
    print("TABLE 9: w=1 PRECISE FORMULA")
    print("=" * 80)

    # Compute a_1/a_0 - H_{2r}
    print("\n  Residual after subtracting H_{2r}:")
    for r in range(1, max_r + 1):
        a_1 = table.get((r, 1), 0)
        a_0 = table.get((r, 0), 0)
        if a_0 == 0 or a_1 == 0: continue
        ratio = Fraction(a_1, a_0)
        H_2r = harmonic(2*r)
        residual = ratio - H_2r
        print(f"    r={r}: a_1/a_0 - H_{2*r} = {residual} = {float(residual):.10f}")

    # Try a_1/a_0 - H_{2r+1}
    print("\n  Residual after subtracting H_{2r+1}:")
    for r in range(1, max_r + 1):
        a_1 = table.get((r, 1), 0)
        a_0 = table.get((r, 0), 0)
        if a_0 == 0 or a_1 == 0: continue
        ratio = Fraction(a_1, a_0)
        H_2r1 = harmonic(2*r + 1)
        residual = ratio - H_2r1
        print(f"    r={r}: a_1/a_0 - H_{2*r+1} = {residual} = {float(residual):.10f}")

    # Try a_1/a_0 = H_{2r} - c/(2r+1)
    print("\n  Try: a_1/a_0 - H_{2r} + 1/(2(2r+1)):")
    for r in range(1, max_r + 1):
        a_1 = table.get((r, 1), 0)
        a_0 = table.get((r, 0), 0)
        if a_0 == 0 or a_1 == 0: continue
        ratio = Fraction(a_1, a_0)
        H_2r = harmonic(2*r)
        correction = Fraction(1, 2*(2*r+1))
        residual = ratio - H_2r + correction
        print(f"    r={r}: a_1/a_0 - H_{2*r} + 1/{2*(2*r+1)} = {residual}")

    # ===================================================================
    # Let me try the EXACT sequence a_1: 5, 154, 8028, 663696, ...
    # Divide by (2r)!: 5/2!, 154/4!, 8028/6!, 663696/8!, ...
    # = 5/2, 77/12, 223/20, 4609/280, ...
    # Denominator pattern: 2, 12, 20, 280, ...
    # ===================================================================
    print("\n" + "=" * 80)
    print("TABLE 10: INTEGER SEQUENCES a_w(r) DIRECT")
    print("=" * 80)

    for w in range(0, 8):
        seq = []
        for r in range(1, max_r + 1):
            a = table.get((r, w), 0)
            if a != 0 or w == 0:
                seq.append(a)
        print(f"\n  w={w}: {seq}")
        # Try OEIS-style: divide consecutive terms
        if len(seq) >= 2:
            diffs = [seq[i+1] - seq[i] for i in range(len(seq)-1) if seq[i] != 0]

    # ===================================================================
    # THE KEY APPROACH: exponential generating function in BOTH variables
    # Define: F(x,y) = sum_{r>=1, w>=0} a_w(r)/(2r)! * (-1)^{r+1} * C_{r-1} * x^r * y^w
    #        = sum_{r>=1} (-1)^{r+1} * C_{r-1} * x^r * [sum_w f_w(r) * y^w]
    # And the TOTAL coefficient for arity k=2r+1 at symmetric point is:
    #   m_k(T+dT*y + d^2T*y^2/2 + ...; 1,...,1)
    # i.e., the generating function in y is the FULL output.
    #
    # Alternatively: define P_r(y) = sum_{w=0}^{2r} a_w(r) * y^w
    # This is the "profile polynomial" at half-arity r.
    # ===================================================================
    print("\n" + "=" * 80)
    print("TABLE 11: PROFILE POLYNOMIALS P_r(y) = sum_w a_w(r) * y^w")
    print("  P_r(1) = sum of all coefficients = TOTAL at symmetric point")
    print("=" * 80)

    for r in range(1, max_r + 1):
        k = 2 * r + 1
        total = sum(table.get((r, w), 0) for w in range(0, 2*r + 1))
        a_0 = table[(r, 0)]
        print(f"\n  r={r} (k={k}): P_r(1) = {total}, a_0 = {a_0}, P_r(1)/a_0 = {Fraction(total, a_0)}")

    # ===================================================================
    # Check: is P_r(1) = (2r+2)! / something?
    # ===================================================================
    print("\n  Checking P_r(1) vs factorials:")
    for r in range(1, max_r + 1):
        total = sum(table.get((r, w), 0) for w in range(0, 2*r + 1))
        for n in range(2*r, 4*r+3):
            fact_n = math.factorial(n)
            if total != 0 and fact_n % abs(total) == 0:
                print(f"    r={r}: {n}! / P_r(1) = {fact_n // total}")
            elif total != 0 and abs(total) % fact_n == 0:
                print(f"    r={r}: P_r(1) / {n}! = {total // fact_n}")

    # ===================================================================
    # FINAL: exact evaluation of (1+y)^{2r} style
    # At the symmetric point, the full output is
    # sum_w a_w(r) * d^w T = m_{2r+1}(T,...,T; 1,...,1)
    # Let's check if P_r(1) / (2r+1)! has a pattern
    # ===================================================================
    print("\n" + "=" * 80)
    print("TABLE 12: P_r(1) / (2r+1)!")
    print("=" * 80)

    for r in range(1, max_r + 1):
        total = sum(table.get((r, w), 0) for w in range(0, 2*r + 1))
        fact = math.factorial(2*r + 1)
        ratio = Fraction(total, fact)
        print(f"  r={r}: P_r(1)/(2r+1)! = {ratio} = {float(ratio):.10f}")

    # ===================================================================
    # Check P_r(1) / (2r+1)! against 2^{2r}
    # ===================================================================
    print("\n  P_r(1) / (2r+1)! vs 2^{2r}:")
    for r in range(1, max_r + 1):
        total = sum(table.get((r, w), 0) for w in range(0, 2*r + 1))
        fact = math.factorial(2*r + 1)
        ratio = Fraction(total, fact)
        power2 = 2**(2*r)
        ratio2 = Fraction(total, fact * power2)
        print(f"  r={r}: P_r(1)/((2r+1)! * 4^r) = {ratio2} = {float(ratio2):.10f}")

    # ===================================================================
    # TABLE 13: The BIG insight — check a_w(r) / binom(2r, w) or a_w(r) / binom(2r+1, w)
    # ===================================================================
    print("\n" + "=" * 80)
    print("TABLE 13: a_w(r) / binom(2r, w)")
    print("=" * 80)

    for w in range(0, 8):
        print(f"\n  w={w}:")
        for r in range(max(1, (w+1)//2), max_r + 1):
            a = table.get((r, w), 0)
            if a == 0: continue
            binom_val = math.comb(2*r, w)
            if binom_val > 0:
                ratio = Fraction(a, binom_val)
                print(f"    r={r}: a_w/C(2r,w) = {ratio} = {float(ratio):.6f}")

    print("\n" + "=" * 80)
    print("COMPUTATION COMPLETE")
    print("=" * 80)


if __name__ == '__main__':
    main()
