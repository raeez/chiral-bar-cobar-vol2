r"""Deep dive into the palindrome pattern: resolving numerical artifacts and
identifying the true structural patterns.

Key questions from Round 1:
- k=6 scalar at symmetric point: 1.93e-12 (numerical zero or genuine?)
- k=8 scalar at symmetric point: 5.46e-09 (numerical zero or genuine?)
- The reversal symmetry: m_k(reversed) at SHALLOWEST depth is always +1,
  at the DEEPEST populated field for even k is always -1. What's the pattern?
- Odd-arity symmetric-point values: {12, 360, 40320, 9072000}. These look like factorials!
- Scalar polynomial P_k(1,...,1) at c=0: all zero. At c=1: what's the exact sequence?
"""

import sys
import os
import random
import math
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from compute.m7_m10_depth_frontier import StasheffEngine


def high_precision_symmetric_point(max_arity=10):
    """Compute symmetric-point values at c=0 (pure T-sector, no scalar contamination)."""
    engine = StasheffEngine(0.0)  # c=0: no scalar terms at all
    results = {}
    for k in range(2, max_arity + 1):
        engine._cache.clear()
        lams = tuple(1.0 for _ in range(k - 1))
        result = engine.mk(lams)
        T_fields = {f: v for f, v in result.items() if f >= 0}
        T_total = sum(v for f, v in T_fields.items())  # signed sum
        T_abs = sum(abs(v) for f, v in T_fields.items())
        results[k] = {
            'fields': T_fields,
            'signed_sum': T_total,
            'abs_sum': T_abs,
            'scalar': result.get(-1, 0.0),
        }
    return results


def identify_odd_arity_sequence():
    """The T-sector sum at symmetric point for odd arities.

    From Round 1 data at c=1:
    k=3: T=6, dT=5, d2T=1 => sum of fields = 12
    k=5: T=-120, dT=-154, d2T=-71, d3T=-14 => sum = -359
    k=7: T=10080, dT=16056, d2T=10208, d3T=3330 => sum = 39674

    But we need the SIGNED SUM, not the abs sum. Let me compute carefully.
    Also: the |T-sector|(1,...,1) from Round 1 was {3, 12, 0, 360, 0, 40320, 0, 9072000, 0}
    at c=1. The nonzero values are {3, 12, 360, 40320, 9072000}.

    Wait: 3 = 3!/2, 12 = 4!/2, 360 = 6!/2, 40320 = 8!/2, 9072000 = 10!/2.
    Pattern: |T-sector|(1,...,1) for odd k: (k+1)!/2 ??
    Let me check: k=3: (3+1)!/2 = 24/2 = 12. But we got |T-sector| = 12. YES!
    k=5: (5+1)!/2 = 720/2 = 360. YES!
    k=7: (7+1)!/2 = 40320/2 = 20160. But we got 40320. That's 8! = 40320, not 8!/2.

    Hmm, let me reconsider. The values were:
    k=2: 3.0, k=3: 12.0, k=5: 360.0, k=7: 40320.0, k=9: 9072000.0

    k=2: 3
    k=3: 12
    k=5: 360
    k=7: 40320
    k=9: 9072000

    3 = 3
    12 = 12
    360 = 360
    40320 = 8! = 40320
    9072000 = ?

    Let me try: 3 = 3!/1, 12 = 4!/2, 360 = 6!/2, 40320 = 8!/1, 9072000 = 10!/0.4?
    Or: 3 = (2+1)C(1)*something, etc.

    Actually from the signed T-values:
    k=2: T=2
    k=3: T+dT+d2T = 6+5+1 = 12
    Hmm wait, |T-sector| is the sum of ABSOLUTE values.
    k=2: |T|=|2|+|1| = 3. But the sum of values is 2+1 = 3.
    k=3: |T|+|dT|+|d2T| = 6+5+1 = 12. Sum = 6+5+1 = 12.
    k=5: 120+154+71+14 = 359. But |T-sector| = 360. Hmm, close.

    Actually looking at the raw data from Round 1 more carefully:
    k=5: T=-120, dT=-154, d2T=-71, d3T=-14
    |T-sector| = 120+154+71+14 = 359. But Round 1 showed 3.600000e+02 = 360.
    There might be a d4T term? Let me check.

    This needs careful recomputation.
    """
    engine = StasheffEngine(1.0)
    results = {}
    for k in range(2, 11):
        engine._cache.clear()
        lams = tuple(1.0 for _ in range(k - 1))
        result = engine.mk(lams)

        # Detailed breakdown
        fields_pos = {f: v for f, v in result.items() if f >= 0}
        abs_sum = sum(abs(v) for v in fields_pos.values())
        signed_sum = sum(v for v in fields_pos.values())

        results[k] = {
            'fields': fields_pos,
            'abs_sum': abs_sum,
            'signed_sum': signed_sum,
            'scalar': result.get(-1, 0.0),
        }
    return results


def factorial_pattern_test():
    """Test whether the T-sector abs sum at symmetric point matches factorial patterns."""
    engine = StasheffEngine(1.0)

    print("  Testing factorial patterns for |T-sector|(1,...,1):")
    print(f"  {'k':>3} {'|T-sector|':>15} {'k!':>12} {'(k+1)!':>12} {'(k-1)!':>12} "
          f"{'2k!/(k+1)':>12} {'ratio/k!':>12}")
    print("  " + "-" * 85)

    for k in range(2, 11):
        engine._cache.clear()
        lams = tuple(1.0 for _ in range(k - 1))
        result = engine.mk(lams)
        abs_sum = sum(abs(v) for f, v in result.items() if f >= 0)

        if abs_sum < 1e-10:
            print(f"  {k:>3} {'ZERO':>15}")
            continue

        kf = math.factorial(k)
        kp1f = math.factorial(k+1)
        km1f = math.factorial(k-1)
        ratio_kf = abs_sum / kf

        print(f"  {k:>3} {abs_sum:>15.1f} {kf:>12} {kp1f:>12} {km1f:>12} "
              f"{'-':>12} {ratio_kf:>12.6f}")


def scalar_even_arity_investigation():
    """Determine if the scalar at the symmetric point for even k >= 6 is exactly zero.

    Strategy: compute at c=0 (should be exactly 0), c=1, and high c.
    If the scalar is c-proportional and the c=0 value is exactly 0,
    then the scalar = c * P_k(1,...,1) / 12. Check if P_k(1,...,1) = 0.
    """
    print("\n  Scalar at symmetric point for even arities:")
    print(f"  {'k':>3} {'c=0':>15} {'c=1':>15} {'c=100':>15} {'c=10000':>15} {'exact zero?':>12}")
    print("  " + "-" * 75)

    for k in [4, 6, 8, 10]:
        results = {}
        for c_val in [0.0, 1.0, 100.0, 10000.0]:
            engine = StasheffEngine(c_val)
            engine._cache.clear()
            lams = tuple(1.0 for _ in range(k - 1))
            result = engine.mk(lams)
            results[c_val] = result.get(-1, 0.0)

        # If all are essentially zero, it's exact
        max_abs = max(abs(v) for v in results.values())
        # For c=10000, if the scalar were really c-proportional and nonzero,
        # it would be 10000x the c=1 value
        exact_zero = max_abs < 1e-6

        print(f"  {k:>3} {results[0.0]:>15.6e} {results[1.0]:>15.6e} "
              f"{results[100.0]:>15.6e} {results[10000.0]:>15.6e} "
              f"{'YES' if exact_zero else 'no':>12}")


def reversal_depth_pattern():
    """Investigate the reversal symmetry pattern more carefully.

    From Round 1: at each arity k, the SHALLOWEST T-dependent field (depth 0 for odd,
    depth 2 for even) has reversal ratio = +1 (constant). The DEEPEST such field
    has ratio varying. But for even k, the deepest populated field has ratio = -1.

    The pattern for even k seems to be: reversal = (-1)^{depth}.
    Let's check this carefully.
    """
    print("\n  Reversal symmetry: m_k(λ_rev) / m_k(λ) at each field")

    for k in [3, 4, 5, 6, 7, 8]:
        engine = StasheffEngine(1.0)
        rng = random.Random(98765 + k)
        n_lams = k - 1

        # Collect ratios per field
        field_ratios = {}

        for trial in range(500):
            lams = tuple(rng.uniform(-3.0, 3.0) for _ in range(n_lams))
            lams_rev = tuple(reversed(lams))

            engine._cache.clear()
            result_fwd = engine.mk(lams)
            engine._cache.clear()
            result_rev = engine.mk(lams_rev)

            for f in set(list(result_fwd.keys()) + list(result_rev.keys())):
                if f < 0:
                    continue
                v_fwd = result_fwd.get(f, 0.0)
                v_rev = result_rev.get(f, 0.0)
                if abs(v_fwd) > 1e-8:
                    r = v_rev / v_fwd
                    if f not in field_ratios:
                        field_ratios[f] = []
                    field_ratios[f].append(r)

        print(f"\n  k={k} ({'even' if k % 2 == 0 else 'odd'}):")
        print(f"  {'field':>8} {'depth':>6} {'ratio':>12} {'stable?':>8} {'(-1)^d':>8}")
        print("  " + "-" * 50)
        for f in sorted(field_ratios.keys()):
            rats = field_ratios[f]
            if len(rats) < 10:
                continue
            mean_r = sum(rats) / len(rats)
            var_r = sum((r - mean_r)**2 for r in rats) / len(rats)
            depth = k - 1 - f
            stable = var_r < 1e-4
            sign_pred = (-1)**depth
            match = abs(mean_r - sign_pred) < 0.1 if stable else False

            print(f"  {'d^'+str(f)+'T' if f > 0 else 'T':>8} {depth:>6} "
                  f"{mean_r:>12.6f} {'YES' if stable else 'no':>8} "
                  f"{sign_pred:>8}{'  MATCH' if match else ''}")


def compute_signed_symmetric_sums():
    """Compute SIGNED sums at symmetric point to look for clean patterns."""
    engine_c0 = StasheffEngine(0.0)
    engine_c1 = StasheffEngine(1.0)

    print("\n  Signed sums at symmetric point:")
    print(f"  {'k':>3} {'parity':>7} {'signed_sum(c=0)':>20} {'signed_sum(c=1)':>20} "
          f"{'abs_sum(c=0)':>18} {'abs_sum(c=1)':>18}")
    print("  " + "-" * 90)

    for k in range(2, 11):
        for eng, c_label in [(engine_c0, 'c0'), (engine_c1, 'c1')]:
            eng._cache.clear()

        lams = tuple(1.0 for _ in range(k - 1))

        r0 = engine_c0.mk(lams)
        r1 = engine_c1.mk(lams)

        ss0 = sum(v for f, v in r0.items() if f >= 0)
        ss1 = sum(v for f, v in r1.items() if f >= 0)
        as0 = sum(abs(v) for f, v in r0.items() if f >= 0)
        as1 = sum(abs(v) for f, v in r1.items() if f >= 0)
        parity = "even" if k % 2 == 0 else "odd"

        print(f"  {k:>3} {parity:>7} {ss0:>20.6f} {ss1:>20.6f} "
              f"{as0:>18.6f} {as1:>18.6f}")


def odd_arity_T_value_sequence():
    """Extract the T-coefficient (depth k-1, weight 0) at symmetric point.

    This is the simplest invariant: m_k|_T(1,...,1) = coefficient of T field.
    """
    engine = StasheffEngine(1.0)

    print("\n  T-coefficient (weight 0, depth k-1) at symmetric point:")
    print(f"  {'k':>3} {'m_k|_T(1,...,1)':>20} {'k!':>12} {'ratio':>14} "
          f"{'(k-1)!':>12} {'ratio2':>14}")
    print("  " + "-" * 80)

    T_vals = {}
    for k in range(2, 11):
        engine._cache.clear()
        lams = tuple(1.0 for _ in range(k - 1))
        result = engine.mk(lams)
        T = result.get(0, 0.0)
        T_vals[k] = T

        kf = math.factorial(k)
        km1f = math.factorial(k - 1)
        r1 = T / kf if abs(T) > 1e-10 else 0
        r2 = T / km1f if abs(T) > 1e-10 else 0

        print(f"  {k:>3} {T:>20.6f} {kf:>12} {r1:>14.6f} "
              f"{km1f:>12} {r2:>14.6f}")

    # Check: m_k|_T(1,...,1) / (k-1)! for odd k
    print("\n  For odd k, m_k|_T(1,...,1) sequence:")
    for k in [3, 5, 7, 9]:
        v = T_vals[k]
        print(f"    k={k}: T = {v:.1f}")
        if k > 3:
            prev = T_vals[k - 2]
            print(f"           T_k / T_{k-2} = {v / prev:.6f}")

    print("\n  Ratios: T_5/T_3 = {:.1f}, T_7/T_5 = {:.1f}, T_9/T_7 = {:.1f}".format(
        T_vals[5] / T_vals[3], T_vals[7] / T_vals[5], T_vals[9] / T_vals[7]))


def diagonal_slice_analysis():
    """Analyze m_k on the DIAGONAL λ_i = λ for all i, as a function of λ.

    At the diagonal, m_k should be a polynomial in λ times each field.
    For even k >= 4, we expect vanishing at all λ (not just λ=1).
    """
    engine = StasheffEngine(0.0)  # c=0 for clean T-sector

    print("\n  Diagonal slice: m_k(λ,...,λ) at c=0 as polynomial in λ")

    for k in [4, 6, 8]:
        print(f"\n  k={k}:")
        # Sample at enough λ-values to determine the polynomial
        lambdas = [0.1 * i for i in range(-20, 21) if i != 0]

        field_vals = {}
        for lam in lambdas:
            engine._cache.clear()
            result = engine.mk(tuple(lam for _ in range(k - 1)))
            for f, v in result.items():
                if f >= 0:
                    if f not in field_vals:
                        field_vals[f] = []
                    field_vals[f].append((lam, v))

        for f in sorted(field_vals.keys()):
            vals = field_vals[f]
            max_v = max(abs(v) for _, v in vals)
            field_name = f"d^{f}T" if f > 0 else "T"
            depth = k - 1 - f

            if max_v < 1e-10:
                print(f"    {field_name:>8} (depth {depth:>2}): IDENTICALLY ZERO on diagonal")
            else:
                # Find degree: the polynomial m_k|_{d^fT}(λ,...,λ) in λ
                # Its degree is at most k-1+f or so. Sample at enough points.
                print(f"    {field_name:>8} (depth {depth:>2}): max |coeff| = {max_v:.6e}")
                # Show a few values
                sample_lams = [0.5, 1.0, 2.0, -1.0]
                for sl in sample_lams:
                    engine._cache.clear()
                    result = engine.mk(tuple(sl for _ in range(k - 1)))
                    v = result.get(f, 0.0)
                    print(f"      λ={sl:>5.1f}: {v:>15.6e}")


def main():
    print("=" * 100)
    print("PALINDROME PATTERN: DEEP DIVE")
    print("=" * 100)

    # === 1. Odd-arity T-value sequence ===
    print("\n" + "=" * 100)
    print("1. ODD-ARITY T-VALUE SEQUENCE AND FACTORIAL PATTERN")
    print("=" * 100)
    odd_arity_T_value_sequence()

    # === 2. Factorial pattern test ===
    print("\n" + "=" * 100)
    print("2. FACTORIAL PATTERN IN |T-SECTOR| AT SYMMETRIC POINT")
    print("=" * 100)
    factorial_pattern_test()

    # === 3. Signed sums ===
    print("\n" + "=" * 100)
    print("3. SIGNED SUMS AT SYMMETRIC POINT")
    print("=" * 100)
    compute_signed_symmetric_sums()

    # === 4. Scalar investigation for even arities ===
    print("\n" + "=" * 100)
    print("4. SCALAR AT SYMMETRIC POINT: EXACT ZERO OR NUMERICAL ARTIFACT?")
    print("=" * 100)
    scalar_even_arity_investigation()

    # === 5. Reversal symmetry pattern ===
    print("\n" + "=" * 100)
    print("5. REVERSAL SYMMETRY: DEPTH-DEPENDENT SIGN PATTERN")
    print("=" * 100)
    reversal_depth_pattern()

    # === 6. Diagonal slice ===
    print("\n" + "=" * 100)
    print("6. DIAGONAL SLICE: EVEN-ARITY VANISHING AS POLYNOMIAL IDENTITY")
    print("=" * 100)
    diagonal_slice_analysis()

    # === 7. High-precision at c=0 ===
    print("\n" + "=" * 100)
    print("7. HIGH-PRECISION SYMMETRIC POINT AT c=0 (PURE T-SECTOR)")
    print("=" * 100)

    hp = high_precision_symmetric_point(10)
    print(f"\n  {'k':>3} {'signed_sum':>20} {'abs_sum':>20} {'scalar':>15}")
    print("  " + "-" * 60)
    for k in range(2, 11):
        d = hp[k]
        print(f"  {k:>3} {d['signed_sum']:>20.6f} {d['abs_sum']:>20.6f} {d['scalar']:>15.6e}")

    # === 8. The sequence recognition ===
    print("\n" + "=" * 100)
    print("8. SEQUENCE RECOGNITION")
    print("=" * 100)

    # From the abs_sum values at c=0 or c=1 (should be identical since T-sector is c-independent)
    engine = StasheffEngine(1.0)
    vals = {}
    for k in range(2, 11):
        engine._cache.clear()
        lams = tuple(1.0 for _ in range(k - 1))
        result = engine.mk(lams)
        vals[k] = sum(abs(v) for f, v in result.items() if f >= 0)

    print("\n  |T-sector|(1,...,1) sequence:")
    for k in range(2, 11):
        v = vals[k]
        parity = "even" if k % 2 == 0 else "odd"
        if v < 1e-10:
            print(f"    k={k} ({parity}): 0")
        else:
            print(f"    k={k} ({parity}): {v:.1f}")

    # The nonzero values: k=2: 3, k=3: 12, k=5: 360, k=7: 40320, k=9: 9072000
    nonzero = [(k, vals[k]) for k in range(2, 11) if vals[k] > 1e-10]
    print("\n  Nonzero values:")
    for k, v in nonzero:
        # Try various factorial identifications
        tests = [
            (f"k!", math.factorial(k)),
            (f"(k+1)!", math.factorial(k+1)),
            (f"(k-1)!", math.factorial(k-1)),
            (f"(2k-2)!!", math.prod(range(2*k-2, 0, -2)) if k > 1 else 1),
            (f"(2k)!!", math.prod(range(2*k, 0, -2))),
            (f"C(k+1,2)*k!/2", (k+1)*k//2 * math.factorial(k) // 2),
            (f"3*(k-1)!", 3 * math.factorial(k-1)),
        ]
        matches = [(name, ref) for name, ref in tests if abs(v - ref) < 0.5]
        match_str = ", ".join(f"{name}={ref}" for name, ref in matches) if matches else "no match"
        print(f"    k={k}: {v:.0f}  [{match_str}]")

    # Let me just try ratios between consecutive nonzero values
    print("\n  Ratios between consecutive nonzero |T-sector|(1,...,1):")
    nz_ks = [k for k, v in nonzero]
    for i in range(1, len(nz_ks)):
        k1, k2 = nz_ks[i-1], nz_ks[i]
        r = vals[k2] / vals[k1]
        print(f"    |T|_{k2} / |T|_{k1} = {r:.2f}")

    # Also check individual field values at symmetric point for odd k
    print("\n  Individual field values at symmetric point for odd k (c=1):")
    for k in [3, 5, 7, 9]:
        engine._cache.clear()
        lams = tuple(1.0 for _ in range(k - 1))
        result = engine.mk(lams)
        fields = {f: v for f, v in result.items() if f >= 0}
        print(f"    k={k}:")
        for f in sorted(fields.keys()):
            v = fields[f]
            name = f"d^{f}T" if f > 0 else "T"
            # Try to identify as simple fraction of factorials
            for den in [1, 2, 3, 4, 6, 12, 24]:
                candidate = v * den
                if abs(candidate - round(candidate)) < 0.01:
                    print(f"      {name}: {v:.6f} = {int(round(candidate))}/{den}")
                    break
            else:
                print(f"      {name}: {v:.6f}")


if __name__ == '__main__':
    main()
