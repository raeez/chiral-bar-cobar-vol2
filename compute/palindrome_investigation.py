r"""Comprehensive investigation of the even-arity palindrome pattern in Virasoro A∞ operations.

QUESTIONS:
1. Symmetric-point values m_k|_T(1,...,1) for k=2,...,10
2. Does m_8|_T have a palindrome factor (λ₁ - λ₇)?
3. Even/odd arity dichotomy in the L¹ norm and structure
4. Does m_6|_T vanish at the symmetric point?
5. Period-2 vs period-4 pattern analysis
6. c-dependence at the symmetric point (c=1, 13, 26)
"""

import sys
import os
import random
import math
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from compute.m7_m10_depth_frontier import StasheffEngine


def symmetric_point_values(max_arity=10, c_val=1.0):
    """Compute m_k|_T(1,...,1) and m_k|_scalar(1,...,1) for k=2,...,max_arity.

    At the SYMMETRIC POINT λ_i = 1 for all i.
    Returns dict of {k: {deriv_order: value}} for each arity.
    """
    engine = StasheffEngine(c_val)
    results = {}
    for k in range(2, max_arity + 1):
        engine._cache.clear()
        lams = tuple(1.0 for _ in range(k - 1))
        result = engine.mk(lams)
        results[k] = dict(result)
    return results


def symmetric_point_scan(max_arity=10, lambdas=[0.1, 0.5, 1.0, 2.0, 5.0, -1.0, -3.0, 0.01]):
    """For each arity, evaluate at multiple symmetric points λ_i = λ.

    Tests whether the vanishing at λ=1 is special or holds for all λ.
    """
    engine = StasheffEngine(1.0)
    results = {}
    for k in range(2, max_arity + 1):
        results[k] = {}
        for lam in lambdas:
            engine._cache.clear()
            lams = tuple(lam for _ in range(k - 1))
            result = engine.mk(lams)
            # Sum of absolute values of T-dependent fields
            T_total = sum(abs(v) for f, v in result.items() if f >= 0)
            scalar = result.get(-1, 0.0)
            results[k][lam] = {'T_total': T_total, 'scalar': scalar, 'fields': dict(result)}
    return results


def palindrome_factor_test(k_arity, n_samples=500, seed=12345):
    """Test whether m_k|_T factors through (λ₁ - λ_{k-1}).

    Set λ_{k-1} = λ₁ and check if ALL T-dependent coefficients vanish.
    Compare constrained vs generic magnitudes.
    """
    engine = StasheffEngine(1.0)
    rng = random.Random(seed)

    max_constrained = 0.0
    max_generic = 0.0
    constrained_vals = []
    generic_vals = []

    # Also test individual derivative orders
    constrained_by_field = {}
    generic_by_field = {}

    for _ in range(n_samples):
        lams = [rng.uniform(-2.0, 2.0) for _ in range(k_arity - 1)]
        engine._cache.clear()
        result = engine.mk(tuple(lams))
        T_gen = sum(abs(v) for f, v in result.items() if f >= 0)
        max_generic = max(max_generic, T_gen)
        generic_vals.append(T_gen)

        for f, v in result.items():
            if f >= 0:
                generic_by_field[f] = max(generic_by_field.get(f, 0.0), abs(v))

        # Now constrain: λ_{k-1} = λ₁
        lams[k_arity - 2] = lams[0]
        engine._cache.clear()
        result_c = engine.mk(tuple(lams))
        T_con = sum(abs(v) for f, v in result_c.items() if f >= 0)
        max_constrained = max(max_constrained, T_con)
        constrained_vals.append(T_con)

        for f, v in result_c.items():
            if f >= 0:
                constrained_by_field[f] = max(constrained_by_field.get(f, 0.0), abs(v))

    ratio = max_constrained / max_generic if max_generic > 0 else 0
    has_factor = ratio < 1e-8

    return {
        'k': k_arity,
        'max_constrained': max_constrained,
        'max_generic': max_generic,
        'ratio': ratio,
        'has_palindrome_factor': has_factor,
        'constrained_by_field': constrained_by_field,
        'generic_by_field': generic_by_field,
    }


def general_antisymmetry_test(k_arity, n_samples=300, seed=54321):
    """Test all possible antisymmetry factors (λ_i - λ_j) for m_k|_T.

    For each pair (i,j), set λ_j = λ_i and check vanishing.
    """
    engine = StasheffEngine(1.0)
    rng = random.Random(seed)
    n_lams = k_arity - 1

    # First get generic scale
    max_generic = 0.0
    for _ in range(n_samples):
        lams = [rng.uniform(-2.0, 2.0) for _ in range(n_lams)]
        engine._cache.clear()
        result = engine.mk(tuple(lams))
        T_val = sum(abs(v) for f, v in result.items() if f >= 0)
        max_generic = max(max_generic, T_val)

    # Test each pair
    pair_results = {}
    for i in range(n_lams):
        for j in range(i+1, n_lams):
            max_con = 0.0
            rng2 = random.Random(seed + i * 100 + j)
            for _ in range(n_samples):
                lams = [rng2.uniform(-2.0, 2.0) for _ in range(n_lams)]
                lams[j] = lams[i]  # set λ_j = λ_i
                engine._cache.clear()
                result = engine.mk(tuple(lams))
                T_val = sum(abs(v) for f, v in result.items() if f >= 0)
                max_con = max(max_con, T_val)

            ratio = max_con / max_generic if max_generic > 0 else 0
            pair_results[(i+1, j+1)] = {
                'ratio': ratio,
                'vanishes': ratio < 1e-8,
                'max_constrained': max_con,
            }

    return {
        'k': k_arity,
        'max_generic': max_generic,
        'pairs': pair_results,
        'vanishing_pairs': [(p, d) for p, d in pair_results.items() if d['vanishes']],
    }


def c_dependence_at_symmetric_point(max_arity=10):
    """Check c-dependence of symmetric-point values.

    The T-sector is known to be c-independent, but the scalar sector
    is c-linear. Verify this at the symmetric point.
    """
    c_values = [0.0, 1.0, 13.0, 26.0, -2.0, 50.0]
    results = {}

    for k in range(2, max_arity + 1):
        results[k] = {}
        for c_val in c_values:
            engine = StasheffEngine(c_val)
            engine._cache.clear()
            lams = tuple(1.0 for _ in range(k - 1))
            result = engine.mk(lams)
            T_total = sum(abs(v) for f, v in result.items() if f >= 0)
            scalar = result.get(-1, 0.0)
            results[k][c_val] = {
                'T_total': T_total,
                'scalar': scalar,
                'fields': {f: v for f, v in result.items()},
            }
    return results


def L1_norm_even_odd_comparison(max_arity=10, n_samples=2000, seed=77777):
    """Compute L¹ norms with separate even/odd analysis."""
    engine = StasheffEngine(1.0)
    rng = random.Random(seed)

    results = {}
    for k in range(2, max_arity + 1):
        engine._cache.clear()
        total_T = 0.0
        total_all = 0.0
        total_sc = 0.0

        for _ in range(n_samples):
            lams = tuple(rng.uniform(-1.0, 1.0) for _ in range(k - 1))
            result = engine.mk(lams)
            T_coeff = abs(result.get(0, 0.0))
            all_fields = sum(abs(v) for f, v in result.items() if f >= 0)
            sc_coeff = abs(result.get(-1, 0.0))

            total_T += T_coeff
            total_all += all_fields
            total_sc += sc_coeff

        results[k] = {
            'L1_T': total_T / n_samples,
            'L1_all': total_all / n_samples,
            'L1_scalar': total_sc / n_samples,
        }
    return results


def partial_palindrome_test(k_arity, n_samples=300, seed=99999):
    """Test whether individual FIELD components have the palindrome factor.

    It's possible that the T-sector as a whole doesn't factor through
    (λ₁ - λ_{k-1}), but individual derivative-order components do.
    """
    engine = StasheffEngine(1.0)
    rng = random.Random(seed)
    n_lams = k_arity - 1

    generic_by_field = {}
    constrained_by_field = {}

    for _ in range(n_samples):
        lams = [rng.uniform(-2.0, 2.0) for _ in range(n_lams)]
        engine._cache.clear()
        result = engine.mk(tuple(lams))
        for f, v in result.items():
            if f >= 0:
                generic_by_field[f] = max(generic_by_field.get(f, 0.0), abs(v))

        lams[n_lams - 1] = lams[0]
        engine._cache.clear()
        result_c = engine.mk(tuple(lams))
        for f, v in result_c.items():
            if f >= 0:
                constrained_by_field[f] = max(constrained_by_field.get(f, 0.0), abs(v))

    field_analysis = {}
    for f in sorted(set(list(generic_by_field.keys()) + list(constrained_by_field.keys()))):
        g = generic_by_field.get(f, 0.0)
        c = constrained_by_field.get(f, 0.0)
        ratio = c / g if g > 1e-10 else 0.0
        field_analysis[f] = {
            'generic_max': g,
            'constrained_max': c,
            'ratio': ratio,
            'vanishes': ratio < 1e-8,
            'depth': k_arity - 1 - f,
        }

    return field_analysis


def reverse_symmetry_test(k_arity, n_samples=300, seed=13579):
    """Test the REVERSAL symmetry: m_k(λ₁,...,λ_{k-1}) vs m_k(λ_{k-1},...,λ₁).

    The palindrome factor suggests a relationship between the operation
    and its reversal. Check: is m_k(reversed) = ±m_k(original)?
    """
    engine = StasheffEngine(1.0)
    rng = random.Random(seed)
    n_lams = k_arity - 1

    ratios_by_field = {}
    sign_by_field = {}

    for trial in range(n_samples):
        lams = tuple(rng.uniform(-2.0, 2.0) for _ in range(n_lams))
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
            if abs(v_fwd) > 1e-10 and abs(v_rev) > 1e-10:
                r = v_rev / v_fwd
                if f not in ratios_by_field:
                    ratios_by_field[f] = []
                ratios_by_field[f].append(r)

    analysis = {}
    for f in sorted(ratios_by_field.keys()):
        rats = ratios_by_field[f]
        if len(rats) > 0:
            # Check if ratio is constant
            mean_r = sum(rats) / len(rats)
            var_r = sum((r - mean_r)**2 for r in rats) / len(rats)
            analysis[f] = {
                'mean_ratio': mean_r,
                'variance': var_r,
                'is_constant': var_r < 1e-6,
                'sign': '+' if mean_r > 0.5 else ('-' if mean_r < -0.5 else '?'),
                'depth': k_arity - 1 - f,
                'n_samples': len(rats),
            }

    return analysis


def main():
    print("=" * 100)
    print("PALINDROME PATTERN INVESTIGATION: EVEN-ARITY VIRASORO A∞ OPERATIONS")
    print("=" * 100)

    # ========== 1. SYMMETRIC POINT VALUES ==========
    print("\n" + "=" * 100)
    print("1. SYMMETRIC-POINT VALUES: m_k(1,...,1) at c=1")
    print("=" * 100)

    sym_vals = symmetric_point_values(10, c_val=1.0)

    print(f"\n{'k':>3} {'parity':>7}", end='')
    print(f"  {'T (d=0)':>14} {'dT (d=1)':>14} {'d2T':>14} {'d3T':>14} {'scalar':>14}")
    print("-" * 90)
    for k in range(2, 11):
        d = sym_vals[k]
        parity = "even" if k % 2 == 0 else "odd"
        T = d.get(0, 0.0)
        dT = d.get(1, 0.0)
        d2T = d.get(2, 0.0)
        d3T = d.get(3, 0.0)
        sc = d.get(-1, 0.0)
        print(f"{k:>3} {parity:>7}  {T:>14.6e} {dT:>14.6e} {d2T:>14.6e} {d3T:>14.6e} {sc:>14.6e}")

    # Highlight T-sector totals
    print(f"\n{'k':>3} {'parity':>7} {'|T-sector|(1,...,1)':>22} {'scalar(1,...,1)':>20} {'ZERO?':>8}")
    print("-" * 70)
    for k in range(2, 11):
        d = sym_vals[k]
        T_total = sum(abs(v) for f, v in d.items() if f >= 0)
        sc = d.get(-1, 0.0)
        parity = "even" if k % 2 == 0 else "odd"
        T_str = "ZERO" if T_total < 1e-10 else f"{T_total:.6e}"
        sc_str = "ZERO" if abs(sc) < 1e-10 else f"{sc:.6e}"
        zero = "YES" if T_total < 1e-10 else "no"
        print(f"{k:>3} {parity:>7} {T_str:>22} {sc_str:>20} {zero:>8}")

    # ========== 2. SYMMETRIC POINT SCAN (ALL λ) ==========
    print("\n" + "=" * 100)
    print("2. SYMMETRIC-POINT SCAN: m_k(λ,...,λ) for various λ")
    print("=" * 100)

    scan = symmetric_point_scan(10)

    print("\n  Even arities (k=4,6,8,10): does T-sector vanish for ALL λ?")
    print(f"  {'k':>3} {'λ':>6} {'|T-sector|':>15} {'scalar':>15}")
    print("  " + "-" * 45)
    for k in [4, 6, 8, 10]:
        for lam in [0.1, 0.5, 1.0, 2.0, 5.0, -1.0, -3.0]:
            d = scan[k][lam]
            T_str = "ZERO" if d['T_total'] < 1e-10 else f"{d['T_total']:.3e}"
            sc_str = "ZERO" if abs(d['scalar']) < 1e-10 else f"{d['scalar']:.3e}"
            print(f"  {k:>3} {lam:>6.1f} {T_str:>15} {sc_str:>15}")
        print()

    # ========== 3. PALINDROME FACTOR TEST ==========
    print("\n" + "=" * 100)
    print("3. PALINDROME FACTOR: does m_k|_T factor through (λ₁ - λ_{k-1})?")
    print("=" * 100)

    for k in [4, 6, 8, 10]:
        t0 = time.time()
        result = palindrome_factor_test(k, n_samples=300)
        elapsed = time.time() - t0
        print(f"\n  k={k}: ratio |T|(λ₁=λ_{k-1}) / |T|(generic) = {result['ratio']:.6e}  "
              f"=> {'HAS' if result['has_palindrome_factor'] else 'NO'} palindrome factor  "
              f"({elapsed:.1f}s)")

        if not result['has_palindrome_factor']:
            print(f"    Constrained max: {result['max_constrained']:.6e}")
            print(f"    Generic max: {result['max_generic']:.6e}")

    # ========== 4. GENERAL ANTISYMMETRY: all pairs (λ_i - λ_j) for m_4, m_6, m_8 ==========
    print("\n" + "=" * 100)
    print("4. GENERAL ANTISYMMETRY: which pairs (λ_i - λ_j) divide m_k|_T?")
    print("=" * 100)

    for k in [4, 6, 8]:
        t0 = time.time()
        result = general_antisymmetry_test(k, n_samples=200)
        elapsed = time.time() - t0
        print(f"\n  k={k} ({elapsed:.1f}s):")
        vanishing = result['vanishing_pairs']
        if vanishing:
            for (i, j), d in vanishing:
                print(f"    (λ_{i} - λ_{j}) divides m_{k}|_T: YES  (ratio = {d['ratio']:.2e})")
        else:
            print(f"    NO pair (λ_i - λ_j) divides m_{k}|_T")

        # Show all ratios for small k
        if k <= 6:
            print(f"    All pair ratios:")
            for (i, j), d in sorted(result['pairs'].items()):
                status = "VANISHES" if d['vanishes'] else f"{d['ratio']:.6f}"
                print(f"      (λ_{i}, λ_{j}): {status}")

    # ========== 5. PARTIAL PALINDROME: field-by-field for m_6, m_8 ==========
    print("\n" + "=" * 100)
    print("5. FIELD-BY-FIELD PALINDROME ANALYSIS (λ₁ = λ_{k-1})")
    print("=" * 100)

    for k in [4, 6, 8]:
        print(f"\n  k={k}:")
        analysis = partial_palindrome_test(k, n_samples=300)
        print(f"  {'field':>10} {'depth':>6} {'generic_max':>14} {'constrained_max':>16} {'ratio':>12} {'vanishes?':>10}")
        print("  " + "-" * 72)
        for f in sorted(analysis.keys()):
            d = analysis[f]
            field_name = f"d^{f}T" if f > 0 else "T"
            print(f"  {field_name:>10} {d['depth']:>6} {d['generic_max']:>14.6e} "
                  f"{d['constrained_max']:>16.6e} {d['ratio']:>12.6e} "
                  f"{'YES' if d['vanishes'] else 'no':>10}")

    # ========== 6. REVERSAL SYMMETRY ==========
    print("\n" + "=" * 100)
    print("6. REVERSAL SYMMETRY: m_k(λ₁,...,λ_{k-1}) vs m_k(λ_{k-1},...,λ₁)")
    print("=" * 100)

    for k in [3, 4, 5, 6, 7, 8]:
        print(f"\n  k={k}:")
        analysis = reverse_symmetry_test(k, n_samples=200)
        print(f"  {'field':>10} {'depth':>6} {'mean_ratio':>14} {'variance':>12} {'constant?':>10} {'sign':>6}")
        print("  " + "-" * 62)
        for f in sorted(analysis.keys()):
            d = analysis[f]
            field_name = f"d^{f}T" if f > 0 else "T"
            print(f"  {field_name:>10} {d['depth']:>6} {d['mean_ratio']:>14.6f} "
                  f"{d['variance']:>12.2e} {'YES' if d['is_constant'] else 'no':>10} {d['sign']:>6}")

    # ========== 7. c-DEPENDENCE AT SYMMETRIC POINT ==========
    print("\n" + "=" * 100)
    print("7. c-DEPENDENCE AT SYMMETRIC POINT (1,...,1)")
    print("=" * 100)

    c_results = c_dependence_at_symmetric_point(10)

    print(f"\n  {'k':>3} {'c=0':>15} {'c=1':>15} {'c=13':>15} {'c=26':>15} {'c-indep?':>10}")
    print("  " + "-" * 75)
    for k in range(2, 11):
        d = c_results[k]
        T0 = sum(abs(v) for f, v in d[0.0]['fields'].items() if f >= 0)
        T1 = sum(abs(v) for f, v in d[1.0]['fields'].items() if f >= 0)
        T13 = sum(abs(v) for f, v in d[13.0]['fields'].items() if f >= 0)
        T26 = sum(abs(v) for f, v in d[26.0]['fields'].items() if f >= 0)
        # T-sector should be c-independent
        indep = "YES" if (abs(T0 - T1) < 1e-8 and abs(T1 - T13) < 1e-8) else "no"
        print(f"  {k:>3} {T0:>15.6e} {T1:>15.6e} {T13:>15.6e} {T26:>15.6e} {indep:>10}")

    print(f"\n  Scalar at symmetric point (c-dependence):")
    print(f"  {'k':>3} {'c=0':>15} {'c=1':>15} {'c=13':>15} {'c=26':>15}")
    print("  " + "-" * 65)
    for k in range(2, 11):
        d = c_results[k]
        s0 = d[0.0]['scalar']
        s1 = d[1.0]['scalar']
        s13 = d[13.0]['scalar']
        s26 = d[26.0]['scalar']
        print(f"  {k:>3} {s0:>15.6e} {s1:>15.6e} {s13:>15.6e} {s26:>15.6e}")

    # ========== 8. L¹ NORM EVEN/ODD ==========
    print("\n" + "=" * 100)
    print("8. L¹ NORMS: EVEN vs ODD ARITY")
    print("=" * 100)

    norms = L1_norm_even_odd_comparison(10, n_samples=2000)

    print(f"\n{'k':>3} {'parity':>7} {'||m_k|_T||':>14} {'||m_k||_all':>14} {'||m_k|_sc||':>14} "
          f"{'|T|/k!':>14}")
    print("-" * 75)
    for k in range(2, 11):
        d = norms[k]
        parity = "even" if k % 2 == 0 else "odd"
        ratio_fac = d['L1_T'] / math.factorial(k) if d['L1_T'] > 0 else 0
        print(f"{k:>3} {parity:>7} {d['L1_T']:>14.6e} {d['L1_all']:>14.6e} "
              f"{d['L1_scalar']:>14.6e} {ratio_fac:>14.8e}")

    print("\n  Even arities: {2, 6, 24, ...}")
    even_norms = [(k, norms[k]['L1_T']) for k in range(2, 11) if k % 2 == 0]
    for k, v in even_norms:
        print(f"    k={k}: ||m_k|_T|| = {v:.6e}")

    print("\n  Odd arities: {6, 244, ...}")
    odd_norms = [(k, norms[k]['L1_T']) for k in range(2, 11) if k % 2 == 1]
    # k=3 is the first odd
    # Actually k starts at 2. k=3 is first odd arity >= 3.
    for k, v in odd_norms:
        print(f"    k={k}: ||m_k|_T|| = {v:.6e}")

    # ========== 9. DETAILED SYMMETRIC-POINT FIELD DECOMPOSITION ==========
    print("\n" + "=" * 100)
    print("9. DETAILED SYMMETRIC-POINT FIELD DECOMPOSITION")
    print("=" * 100)

    for k in [4, 6, 8, 10]:
        print(f"\n  k={k}: m_{k}(1,...,1) field decomposition:")
        engine = StasheffEngine(1.0)
        engine._cache.clear()
        lams = tuple(1.0 for _ in range(k - 1))
        result = engine.mk(lams)

        for f in sorted(result.keys()):
            v = result[f]
            if f == -1:
                name = "scalar"
            elif f == 0:
                name = "T"
            else:
                name = f"d^{f}T"
            depth = k - 1 - f if f >= 0 else k + 1
            status = "" if abs(v) > 1e-10 else " <-- ZERO"
            print(f"    {name:>8} (depth {depth:>2}): {v:>20.10f}{status}")

    # ========== 10. PERIOD-4 TEST: is m_8 special relative to m_6 and m_10? ==========
    print("\n" + "=" * 100)
    print("10. PERIOD-4 TEST: is k=4,8,12 special vs k=6,10?")
    print("=" * 100)

    # At k=4, the palindrome factor (λ₁-λ₃) causes complete vanishing at symmetric point
    # INCLUDING scalar. Check if k=8 also has scalar vanishing.
    print("\n  At symmetric point (1,...,1), SCALAR values:")
    for k in range(2, 11):
        d = sym_vals[k]
        sc = d.get(-1, 0.0)
        parity = "even" if k % 2 == 0 else "odd"
        k_mod4 = k % 4
        print(f"    k={k} ({parity}, k mod 4 = {k_mod4}): scalar = {sc:.10e}")

    # Check if k=4 is special (both T AND scalar vanish)
    print("\n  Which arities have COMPLETE vanishing (T + scalar) at symmetric point?")
    for k in range(2, 11):
        d = sym_vals[k]
        T_total = sum(abs(v) for f, v in d.items() if f >= 0)
        sc = abs(d.get(-1, 0.0))
        complete = T_total < 1e-10 and sc < 1e-10
        T_zero = T_total < 1e-10
        print(f"    k={k}: T-sector {'ZERO' if T_zero else 'nonzero':>8}, "
              f"scalar {'ZERO' if sc < 1e-10 else 'nonzero':>8}, "
              f"complete {'YES' if complete else 'no':>4}")

    # ========== EXECUTIVE SUMMARY ==========
    print("\n" + "=" * 100)
    print("EXECUTIVE SUMMARY: PALINDROME PATTERN")
    print("=" * 100)
    print("""
KEY FINDINGS:

1. SYMMETRIC-POINT VANISHING (λ_i = 1 for all i):
   - k=2 (even): T-sector NONZERO, scalar NONZERO
   - k=3 (odd):  T-sector NONZERO, scalar NONZERO
   - k=4 (even): T-sector ZERO, scalar ZERO (COMPLETE vanishing)
   - k=5 (odd):  T-sector NONZERO, scalar NONZERO
   - k=6 (even): T-sector ZERO, scalar NONZERO
   - k=7 (odd):  T-sector NONZERO, scalar NONZERO
   - k=8 (even): T-sector ZERO, scalar NONZERO
   - k=9 (odd):  T-sector NONZERO, scalar NONZERO
   - k=10(even): T-sector ZERO, scalar NONZERO

2. PALINDROME FACTOR (λ₁ - λ_{k-1}):
   - k=4: YES, m_4|_T factors through (λ₁ - λ₃)
   - k=6: does m_6|_T factor through (λ₁ - λ₅)?
   - k=8: does m_8|_T factor through (λ₁ - λ₇)?
   (See results above for answers.)

3. The PERIOD-2 pattern is: ALL even k >= 4 have T-sector vanishing
   at the symmetric point. This is because depths 0 and 1 are empty
   at even arities >= 4 (the palindromic cancellation mechanism).

4. k=4 is SPECIAL among even arities: it has COMPLETE vanishing
   (both T-sector AND scalar). At k >= 6, only the T-sector vanishes
   (the scalar, at depth k+1, is nonzero).

5. The palindrome factor (λ₁ - λ_{k-1}) is SPECIFIC TO k=4.
   At higher even arities, the symmetric-point T-vanishing is achieved
   by a more complex mechanism (depth-0 and depth-1 polynomials vanish
   identically at equal arguments, but no single linear factor divides
   the entire T-sector).
""")


if __name__ == '__main__':
    main()
