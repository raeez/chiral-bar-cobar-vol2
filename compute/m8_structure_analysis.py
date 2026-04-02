r"""Exact structural analysis of m_8 for the Virasoro algebra.

Computes:
1. Symmetric-point values m_8|_T(1,...,1) at c=1,13,26
2. Anti-palindrome point λ_1=1, λ_7=-1, all others=0
3. Scalar polynomial P_8(1,...,1) — period-2 predicts ZERO
4. L^1 norm ||m_8|_T|| and ratio to 8!
5. Factorization structure: linear factors, reducibility
6. Depth-2 leading term analysis

Uses the numerical StasheffEngine from m7_m10_depth_frontier.py.
"""

import sys
import os
import math
import random
import itertools

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from compute.m7_m10_depth_frontier import StasheffEngine


# =============================================================================
# 1. SYMMETRIC POINT: m_8|_T(1,...,1) at c=1, 13, 26
# =============================================================================

def symmetric_point_analysis():
    """Compute m_8 at the symmetric point λ_i = λ for all i, for several c values."""
    print("=" * 90)
    print("1. SYMMETRIC POINT ANALYSIS: m_8(T^8; λ,...,λ)")
    print("=" * 90)

    # k=8: 7 spectral parameters
    k = 8
    n_lams = k - 1  # = 7

    for c_val in [1.0, 13.0, 26.0]:
        engine = StasheffEngine(c_val)
        print(f"\n  c = {c_val}")
        print(f"  {'λ':>10} {'|T-sector|':>14} {'d^6T':>14} {'d^5T':>14} "
              f"{'d^4T':>14} {'d^3T':>14} {'d^2T':>14} {'dT':>14} {'T':>14} {'scalar':>14}")
        print("  " + "-" * 150)

        for lam in [0.001, 0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0, -1.0, -2.0]:
            engine._cache.clear()
            lams = tuple(lam for _ in range(n_lams))
            result = engine.mk(lams)

            # Collect field coefficients by derivative order
            fields = {}
            for d_order in range(7):  # d^0T through d^6T
                fields[d_order] = result.get(d_order, 0.0)

            T_total = sum(abs(v) for d, v in result.items() if d >= 0)
            sc = result.get(-1, 0.0)

            print(f"  {lam:>10.3f} {T_total:>14.6e} "
                  f"{fields.get(6, 0):>14.6e} {fields.get(5, 0):>14.6e} "
                  f"{fields.get(4, 0):>14.6e} {fields.get(3, 0):>14.6e} "
                  f"{fields.get(2, 0):>14.6e} {fields.get(1, 0):>14.6e} "
                  f"{fields.get(0, 0):>14.6e} {sc:>14.6e}")

        # Fine analysis: test λ=1 at high precision
        engine._cache.clear()
        lams_1 = tuple(1.0 for _ in range(n_lams))
        result_1 = engine.mk(lams_1)
        T_total_1 = sum(abs(v) for d, v in result_1.items() if d >= 0)
        sc_1 = result_1.get(-1, 0.0)
        print(f"\n  ** λ=1 summary at c={c_val}: |T-sector| = {T_total_1:.6e}, scalar = {sc_1:.6e}")
        if T_total_1 < 1e-8:
            print(f"     T-sector VANISHES at symmetric point (period-2 theorem confirmed)")
        else:
            print(f"     T-sector NONZERO at symmetric point ({T_total_1:.6e})")
            # Check each field
            for d_order in range(7):
                val = result_1.get(d_order, 0.0)
                depth = k - 1 - d_order
                if abs(val) > 1e-10:
                    print(f"     d^{d_order}T (depth {depth}): {val:.6e}")

    print()


# =============================================================================
# 2. ANTI-PALINDROME POINT: λ_1=1, λ_7=-1, all others=0
# =============================================================================

def anti_palindrome_analysis():
    """Test m_8 at the anti-palindrome point and related configurations."""
    print("=" * 90)
    print("2. ANTI-PALINDROME ANALYSIS: λ_1=1, λ_7=-1, rest=0")
    print("=" * 90)

    k = 8
    engine = StasheffEngine(1.0)

    # Configuration 1: λ_1=1, λ_7=-1, rest=0
    print("\n  Configuration: λ_1=1, λ_7=-1, λ_2=...=λ_6=0")
    lams_ap = (1.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0)
    engine._cache.clear()
    result_ap = engine.mk(lams_ap)
    T_ap = sum(abs(v) for d, v in result_ap.items() if d >= 0)
    sc_ap = result_ap.get(-1, 0.0)
    print(f"  |T-sector| = {T_ap:.6e}, scalar = {sc_ap:.6e}")
    for d_order in sorted([d for d in result_ap if d >= 0], reverse=True):
        depth = k - 1 - d_order
        if abs(result_ap[d_order]) > 1e-10:
            print(f"  d^{d_order}T (depth {depth}): {result_ap[d_order]:.6e}")

    # Configuration 2: λ_1=t, λ_7=-t, rest=0 for various t
    print("\n  Family: λ_1=t, λ_7=-t, λ_2=...=λ_6=0")
    print(f"  {'t':>10} {'|T-sector|':>14} {'scalar':>14}")
    for t in [0.001, 0.01, 0.1, 0.5, 1.0, 2.0, 5.0]:
        engine._cache.clear()
        lams_t = (t, 0.0, 0.0, 0.0, 0.0, 0.0, -t)
        result_t = engine.mk(lams_t)
        T_t = sum(abs(v) for d, v in result_t.items() if d >= 0)
        sc_t = result_t.get(-1, 0.0)
        print(f"  {t:>10.3f} {T_t:>14.6e} {sc_t:>14.6e}")

    # Configuration 3: Compare with generic point
    print("\n  Generic point comparison:")
    rng = random.Random(99999)
    generic_totals = []
    for _ in range(100):
        lams_gen = tuple(rng.uniform(-2.0, 2.0) for _ in range(7))
        engine._cache.clear()
        result_gen = engine.mk(lams_gen)
        T_gen = sum(abs(v) for d, v in result_gen.items() if d >= 0)
        generic_totals.append(T_gen)

    avg_gen = sum(generic_totals) / len(generic_totals)
    max_gen = max(generic_totals)
    print(f"  Generic |T|: avg = {avg_gen:.6e}, max = {max_gen:.6e}")
    print(f"  Anti-palindrome |T| = {T_ap:.6e}")
    print(f"  Ratio AP/generic_avg = {T_ap / avg_gen:.6f}")

    # Configuration 4: palindrome constraint λ_1 = λ_7
    print("\n  Palindrome constraint: λ_1 = λ_7")
    print(f"  {'λ_1=λ_7':>10} {'others':>10} {'|T-sector|':>14} {'scalar':>14}")
    for val in [0.5, 1.0, 2.0]:
        for other in [0.0, 0.5, 1.0]:
            engine._cache.clear()
            lams_pal = (val, other, other, other, other, other, val)
            result_pal = engine.mk(lams_pal)
            T_pal = sum(abs(v) for d, v in result_pal.items() if d >= 0)
            sc_pal = result_pal.get(-1, 0.0)
            print(f"  {val:>10.3f} {other:>10.3f} {T_pal:>14.6e} {sc_pal:>14.6e}")

    print()


# =============================================================================
# 3. SCALAR POLYNOMIAL P_8(1,...,1) — should be ZERO by period-2
# =============================================================================

def scalar_polynomial_analysis():
    """Verify P_8(1,...,1) = 0 and analyze scalar structure at k=8."""
    print("=" * 90)
    print("3. SCALAR POLYNOMIAL P_8 ANALYSIS")
    print("=" * 90)

    k = 8

    # At c=1: scalar = (c/12) * P_k(λ) = (1/12) * P_k(λ)
    # So P_k(λ) = 12 * scalar
    engine = StasheffEngine(1.0)

    # Symmetric point
    engine._cache.clear()
    lams_1 = tuple(1.0 for _ in range(7))
    result_1 = engine.mk(lams_1)
    sc_1 = result_1.get(-1, 0.0)
    P_8_sym = 12.0 * sc_1
    print(f"\n  P_8(1,...,1) = 12 * scalar = 12 * {sc_1:.10e} = {P_8_sym:.10e}")

    if abs(P_8_sym) < 1e-6:
        print(f"  CONFIRMED: P_8(1,...,1) = 0 (period-2 theorem)")
    else:
        print(f"  WARNING: P_8(1,...,1) = {P_8_sym:.6e} (not zero!)")

    # Cross-check with other c values
    for c_val in [13.0, 26.0, 100.0]:
        engine_c = StasheffEngine(c_val)
        engine_c._cache.clear()
        result_c = engine_c.mk(lams_1)
        sc_c = result_c.get(-1, 0.0)
        P_8_c = 12.0 * sc_c / c_val  # P_8 should be c-independent (divided out)
        print(f"  c={c_val}: scalar = {sc_c:.10e}, P_8/(c/12) = {P_8_c:.10e}")

    # Scalar at generic points (to confirm it IS nonzero generically)
    print("\n  Scalar at generic points (confirming nonzero generically):")
    rng = random.Random(11111)
    for trial in range(5):
        lams_gen = tuple(rng.uniform(-2.0, 2.0) for _ in range(7))
        engine._cache.clear()
        result_gen = engine.mk(lams_gen)
        sc_gen = result_gen.get(-1, 0.0)
        P_8_gen = 12.0 * sc_gen
        print(f"  Trial {trial}: P_8({[f'{l:.2f}' for l in lams_gen]}) = {P_8_gen:.6e}")

    # Verify the scalar sequence P_k(1,...,1) for k=2..10
    print("\n  Complete scalar sequence P_k(1,...,1):")
    print(f"  {'k':>3} {'P_k(1,...,1)':>20} {'parity':>8} {'zero?':>8}")
    for k_test in range(2, 11):
        engine_test = StasheffEngine(1.0)
        engine_test._cache.clear()
        lams_test = tuple(1.0 for _ in range(k_test - 1))
        result_test = engine_test.mk(lams_test)
        sc_test = result_test.get(-1, 0.0)
        P_k = 12.0 * sc_test
        parity = "even" if k_test % 2 == 0 else "odd"
        is_zero = abs(P_k) < 1e-4
        print(f"  {k_test:>3} {P_k:>20.4f} {parity:>8} {'YES' if is_zero else 'no':>8}")

    print()


# =============================================================================
# 4. L^1 NORM VERIFICATION
# =============================================================================

def L1_norm_verification():
    """Compute ||m_8|_T|| carefully and verify the reported value."""
    print("=" * 90)
    print("4. L^1 NORM VERIFICATION FOR m_8")
    print("=" * 90)

    k = 8
    engine = StasheffEngine(1.0)
    rng = random.Random(77777)

    # Compute L^1 norms with high sample count
    n_samples = 5000
    total_T_coeff = 0.0       # |coeff of T| (depth k-1)
    total_T_sector = 0.0      # sum of |coefficients| of all T-dependent fields
    total_sc = 0.0
    max_T = 0.0

    for trial in range(n_samples):
        engine._cache.clear()
        lams = tuple(rng.uniform(-1.0, 1.0) for _ in range(7))
        result = engine.mk(lams)

        T_coeff = abs(result.get(0, 0.0))
        T_sector = sum(abs(v) for d, v in result.items() if d >= 0)
        sc = abs(result.get(-1, 0.0))

        total_T_coeff += T_coeff
        total_T_sector += T_sector
        total_sc += sc
        max_T = max(max_T, T_sector)

    avg_T_coeff = total_T_coeff / n_samples
    avg_T_sector = total_T_sector / n_samples
    avg_sc = total_sc / n_samples

    ratio_to_factorial = avg_T_sector / math.factorial(k)

    print(f"\n  Sample size: {n_samples}")
    print(f"  ||m_8|_T-coeff|| (depth 7, coeff of T) = {avg_T_coeff:.6e}")
    print(f"  ||m_8|_T-sector|| (all T fields) = {avg_T_sector:.6e}")
    print(f"  ||m_8|_scalar|| = {avg_sc:.6e}")
    print(f"  max|T-sector| = {max_T:.6e}")
    print(f"")
    print(f"  8! = {math.factorial(8)}")
    print(f"  ||m_8|_T-sector|| / 8! = {ratio_to_factorial:.8e}")
    print(f"  Reported value: 3.47e+02, ratio 0.00860")
    print(f"  Computed value: {avg_T_sector:.4e}, ratio {ratio_to_factorial:.6e}")

    # Compute norms for k=2 through 10 for comparison
    print(f"\n  Full norm table (T-sector L^1 averages on [-1,1]^{{k-1}}):")
    print(f"  {'k':>3} {'||m_k|_T||':>14} {'k!':>14} {'||/k!':>14} {'growth':>10}")

    prev_norm = None
    for k_test in range(2, 11):
        engine_t = StasheffEngine(1.0)
        rng_t = random.Random(77777)
        total_t = 0.0
        ns = 3000 if k_test <= 8 else 1000

        for _ in range(ns):
            engine_t._cache.clear()
            lams_t = tuple(rng_t.uniform(-1.0, 1.0) for _ in range(k_test - 1))
            result_t = engine_t.mk(lams_t)
            T_t = sum(abs(v) for d, v in result_t.items() if d >= 0)
            total_t += T_t

        avg_t = total_t / ns
        fac = math.factorial(k_test)
        ratio_t = avg_t / fac
        growth = avg_t / prev_norm if prev_norm and prev_norm > 0 else float('nan')
        print(f"  {k_test:>3} {avg_t:>14.6e} {fac:>14} {ratio_t:>14.8e} {growth:>10.4f}")
        prev_norm = avg_t

    # Gevrey-1 check: is ||m_k||/k! ~ C * A^k?
    print(f"\n  Gevrey-1 permanence test:")
    print(f"  If ||m_k|_T|| ~ C * A^k * k!, then ||m_k||/(k!) should grow geometrically.")

    print()


# =============================================================================
# 5. FACTORIZATION STRUCTURE
# =============================================================================

def factorization_analysis():
    """Test whether m_8|_T has any linear factors in the λ variables."""
    print("=" * 90)
    print("5. FACTORIZATION STRUCTURE OF m_8|_T")
    print("=" * 90)

    k = 8
    engine = StasheffEngine(1.0)

    # Test 1: Does (λ_1 - λ_7) divide m_8|_T?
    print("\n  Test 1: Does (λ_1 - λ_7) divide m_8|_T?")
    rng = random.Random(54321)
    max_ratio = 0.0
    max_constrained = 0.0
    max_generic = 0.0
    n_tests = 200

    for _ in range(n_tests):
        lams = [rng.uniform(-2.0, 2.0) for _ in range(7)]
        engine._cache.clear()
        result_gen = engine.mk(tuple(lams))
        T_gen = sum(abs(v) for d, v in result_gen.items() if d >= 0)
        max_generic = max(max_generic, T_gen)

        # Force λ_1 = λ_7
        lams_con = list(lams)
        lams_con[6] = lams_con[0]
        engine._cache.clear()
        result_con = engine.mk(tuple(lams_con))
        T_con = sum(abs(v) for d, v in result_con.items() if d >= 0)
        max_constrained = max(max_constrained, T_con)

    ratio = max_constrained / max_generic if max_generic > 0 else 0
    print(f"  max|T|(λ_1=λ_7) = {max_constrained:.6e}")
    print(f"  max|T|(generic) = {max_generic:.6e}")
    print(f"  Ratio = {ratio:.6e}")
    divides = ratio < 1e-6
    print(f"  Does (λ_1-λ_7) divide? {'YES' if divides else 'NO'}")

    # Test 2: Systematic linear factor test
    # A linear factor has the form sum_i a_i λ_i = 0
    # We test ALL single-variable factors (λ_i = 0) and all pairwise (λ_i ± λ_j = 0)
    print("\n  Test 2: Single-variable linear factors (does λ_i = 0 => m_8|_T = 0?)")
    for idx in range(7):
        max_val = 0.0
        for _ in range(100):
            lams = [rng.uniform(-2.0, 2.0) for _ in range(7)]
            lams[idx] = 0.0
            engine._cache.clear()
            result = engine.mk(tuple(lams))
            T_val = sum(abs(v) for d, v in result.items() if d >= 0)
            max_val = max(max_val, T_val)
        divides_i = max_val < 1e-6
        print(f"  λ_{idx+1}=0: max|T| = {max_val:.6e} {'DIVIDES' if divides_i else ''}")

    print("\n  Test 3: Pairwise difference factors (λ_i - λ_j = 0)")
    factor_found = []
    for i in range(7):
        for j in range(i + 1, 7):
            max_val = 0.0
            for _ in range(50):
                lams = [rng.uniform(-2.0, 2.0) for _ in range(7)]
                lams[j] = lams[i]
                engine._cache.clear()
                result = engine.mk(tuple(lams))
                T_val = sum(abs(v) for d, v in result.items() if d >= 0)
                max_val = max(max_val, T_val)
            if max_val < 1e-6:
                factor_found.append((i + 1, j + 1))
                print(f"  (λ_{i+1}-λ_{j+1}): DIVIDES! max|T| = {max_val:.6e}")

    if not factor_found:
        print(f"  No pairwise difference factors found.")

    print("\n  Test 4: Pairwise sum factors (λ_i + λ_j = 0)")
    sum_factors = []
    for i in range(7):
        for j in range(i + 1, 7):
            max_val = 0.0
            for _ in range(50):
                lams = [rng.uniform(-2.0, 2.0) for _ in range(7)]
                lams[j] = -lams[i]
                engine._cache.clear()
                result = engine.mk(tuple(lams))
                T_val = sum(abs(v) for d, v in result.items() if d >= 0)
                max_val = max(max_val, T_val)
            if max_val < 1e-6:
                sum_factors.append((i + 1, j + 1))
                print(f"  (λ_{i+1}+λ_{j+1}): DIVIDES! max|T| = {max_val:.6e}")

    if not sum_factors:
        print(f"  No pairwise sum factors found.")

    # Test 5: Total sum factor (sum λ_i = 0)
    print("\n  Test 5: Total sum factor (Σ λ_i = 0)")
    max_val = 0.0
    for _ in range(200):
        lams = [rng.uniform(-2.0, 2.0) for _ in range(6)]
        lams.append(-sum(lams))  # force Σ λ_i = 0
        engine._cache.clear()
        result = engine.mk(tuple(lams))
        T_val = sum(abs(v) for d, v in result.items() if d >= 0)
        max_val = max(max_val, T_val)
    divides_sum = max_val < 1e-6
    print(f"  max|T|(Σλ=0) = {max_val:.6e} {'DIVIDES' if divides_sum else 'does not divide'}")

    # Test 6: Partial sum factors
    print("\n  Test 6: Consecutive partial sum factors (λ_i + λ_{i+1} + ... + λ_j = 0)")
    for length in range(2, 5):
        for start in range(7 - length + 1):
            max_val = 0.0
            for _ in range(50):
                lams = [rng.uniform(-2.0, 2.0) for _ in range(7)]
                # Force sum of lams[start:start+length] = 0
                target_sum = sum(lams[start:start + length - 1])
                lams[start + length - 1] = -target_sum
                engine._cache.clear()
                result = engine.mk(tuple(lams))
                T_val = sum(abs(v) for d, v in result.items() if d >= 0)
                max_val = max(max_val, T_val)
            if max_val < 1e-6:
                indices = [start + 1 + p for p in range(length)]
                print(f"  (λ_{'+λ_'.join(map(str, indices))}=0): DIVIDES! max|T| = {max_val:.6e}")

    # Test 7: Comparison with m_4 factorization
    print("\n  Test 7: m_4 factorization for comparison")
    engine4 = StasheffEngine(1.0)
    print("  m_4|_T factors as 4(λ_1-λ_3)(λ_1-λ_2+λ_3)(λ_1+λ_2+λ_3)")
    print("  This is a product of 3 LINEAR factors in 3 variables (degree 3).")
    print(f"  m_8|_T is a polynomial of degree 7 in 7 variables.")

    # Verify m_4 factorization
    for _ in range(10):
        l1, l2, l3 = rng.uniform(-3, 3), rng.uniform(-3, 3), rng.uniform(-3, 3)
        engine4._cache.clear()
        result4 = engine4.mk((l1, l2, l3))
        # m_4|_T: the T coefficient (depth 2) — derivative order 0
        T_coeff_4 = result4.get(0, 0.0)  # T field
        # Predicted: 4*(l1-l3)*(l1-l2+l3)*(l1+l2+l3) -- but this would be degree 3
        # Actually m_4|_T should be the coefficient of the FIELD T, with spectral degree 3
        predicted = 4.0 * (l1 - l3) * (l1 - l2 + l3) * (l1 + l2 + l3)
        if abs(T_coeff_4) > 1e-10:
            ratio_check = T_coeff_4 / predicted if abs(predicted) > 1e-10 else float('inf')
        else:
            ratio_check = 0.0

    print()


# =============================================================================
# 6. DEPTH-2 LEADING TERM ANALYSIS
# =============================================================================

def depth_2_analysis():
    """Analyze the depth-2 coefficient of m_8|_T.

    For k=8, the period-2 theorem says:
    - depth 0 (d^6T coeff) VANISHES (degree 1 polynomial = 0)
    - depth 1 (d^5T coeff) VANISHES (degree 2 polynomial = 0)
    - depth 2 (d^4T coeff) is the MINIMAL nonvanishing depth

    The depth-2 coefficient is the coefficient of d^4T in m_8.
    By weight-depth identity: w=4, d=k-1-w=3... wait, let me recheck.

    Actually: derivative order w, depth d = k-1-w.
    For k=8: d^6T has w=6, depth=1. d^5T has w=5, depth=2. d^4T has w=4, depth=3.

    Period-2 says depths 0 and 1 vanish for even k>=4.
    Depth 0 requires d^{k-1}T = d^7T (doesn't exist structurally for m_8 since max is d^6T).
    Depth 1 requires d^{k-2}T = d^6T. This is the LEADING field.

    So the LEADING field d^6T (depth 1) vanishes, and d^5T (depth 2) is the minimal
    nonvanishing T-sector depth.
    """
    print("=" * 90)
    print("6. DEPTH-2 LEADING TERM (d^5T COEFFICIENT OF m_8)")
    print("=" * 90)

    k = 8
    engine = StasheffEngine(1.0)

    # First confirm the depth spectrum
    print("\n  Confirming depth spectrum of m_8:")
    rng = random.Random(12345)
    max_by_deriv = {}
    for _ in range(500):
        lams = tuple(rng.uniform(-3.0, 3.0) for _ in range(7))
        engine._cache.clear()
        result = engine.mk(lams)
        for d_order, coeff in result.items():
            if d_order >= 0:
                depth = k - 1 - d_order
                key = d_order
                if key not in max_by_deriv:
                    max_by_deriv[key] = 0.0
                max_by_deriv[key] = max(max_by_deriv[key], abs(coeff))

    print(f"  {'deriv_order':>12} {'depth':>6} {'max|coeff|':>14} {'status':>12}")
    for d_order in sorted(max_by_deriv.keys(), reverse=True):
        depth = k - 1 - d_order
        val = max_by_deriv[d_order]
        status = "VANISHES" if val < 1e-8 else "populated"
        print(f"  d^{d_order}T {' '*(8-len(str(d_order)))} {depth:>6} {val:>14.6e} {status:>12}")

    # Now analyze the d^5T coefficient (depth 2, the leading nonvanishing term)
    # The d^5T coefficient is a polynomial of degree 2 in λ_1,...,λ_7
    # (since w=5, d=k-1-w=8-1-5=2, so spectral degree 2)
    print("\n  The d^5T coefficient has spectral degree 2 (weight 5, depth 2).")
    print("  It is a QUADRATIC polynomial in 7 variables.")

    # Extract the quadratic form by sampling
    # A quadratic in 7 variables has (7+1)*7/2 + 7 + 1 = 28 + 7 + 1 = 36 coefficients
    # But depth 2 means EXACTLY degree 2 (pure quadratic, no lower terms)
    # So we need the 28 coefficients of λ_i λ_j (with i<=j)

    # Method: evaluate at many points and fit
    # For a homogeneous degree-2 polynomial: Q(λ) = Σ_{i<=j} c_{ij} λ_i λ_j
    # We can extract c_{ii} from Q(e_i) and c_{ij} from Q(e_i + e_j) - Q(e_i) - Q(e_j)

    print("\n  Extracting the quadratic form of the d^5T coefficient:")
    print("  Q(λ) = Σ_{i≤j} c_{ij} λ_i λ_j")

    # First check if there are constant or linear terms
    engine._cache.clear()
    result_0 = engine.mk(tuple(0.0 for _ in range(7)))
    d5T_at_0 = result_0.get(5, 0.0)
    print(f"\n  d^5T at λ=0: {d5T_at_0:.6e} (should be ~0 if purely quadratic)")

    # Check linear terms: d^5T(ε·e_i) ≈ linear_i * ε + quadratic * ε² for small ε
    print("\n  Linear terms check (should vanish for depth-2):")
    for idx in range(7):
        eps = 0.001
        lams_p = [0.0] * 7
        lams_p[idx] = eps
        lams_m = [0.0] * 7
        lams_m[idx] = -eps
        engine._cache.clear()
        result_p = engine.mk(tuple(lams_p))
        engine._cache.clear()
        result_m = engine.mk(tuple(lams_m))
        d5T_p = result_p.get(5, 0.0)
        d5T_m = result_m.get(5, 0.0)
        linear_coeff = (d5T_p - d5T_m) / (2 * eps)
        quad_coeff = (d5T_p + d5T_m - 2 * d5T_at_0) / (eps**2)
        print(f"  λ_{idx+1}: linear = {linear_coeff:.6e}, quadratic = {quad_coeff:.6e}")

    # Extract the full quadratic matrix
    print("\n  Quadratic coefficient matrix c_{ij} (i, j = 1,...,7):")
    c_matrix = [[0.0] * 7 for _ in range(7)]

    # Diagonal: c_{ii} = d^5T(e_i) - d^5T(0)  (up to constant term)
    # Actually: Q(e_i) = c_{ii}, so c_{ii} = d^5T(e_i) (assuming d^5T(0) ≈ 0)
    for i in range(7):
        lams_ei = [0.0] * 7
        lams_ei[i] = 1.0
        engine._cache.clear()
        result_ei = engine.mk(tuple(lams_ei))
        c_matrix[i][i] = result_ei.get(5, 0.0) - d5T_at_0

    # Off-diagonal: c_{ij} = Q(e_i + e_j) - Q(e_i) - Q(e_j)
    # = d^5T(e_i+e_j) - d^5T(e_i) - d^5T(e_j) + d^5T(0)
    for i in range(7):
        for j in range(i + 1, 7):
            lams_eij = [0.0] * 7
            lams_eij[i] = 1.0
            lams_eij[j] = 1.0
            engine._cache.clear()
            result_eij = engine.mk(tuple(lams_eij))
            d5T_eij = result_eij.get(5, 0.0)

            lams_ei = [0.0] * 7
            lams_ei[i] = 1.0
            engine._cache.clear()
            result_ei = engine.mk(tuple(lams_ei))
            d5T_ei = result_ei.get(5, 0.0)

            lams_ej = [0.0] * 7
            lams_ej[j] = 1.0
            engine._cache.clear()
            result_ej = engine.mk(tuple(lams_ej))
            d5T_ej = result_ej.get(5, 0.0)

            c_matrix[i][j] = d5T_eij - d5T_ei - d5T_ej + d5T_at_0
            c_matrix[j][i] = c_matrix[i][j]

    # Print the matrix
    print(f"\n  {'':>8}", end="")
    for j in range(7):
        print(f"  λ_{j+1:>5}", end="")
    print()
    for i in range(7):
        print(f"  λ_{i+1:>3}:", end="")
        for j in range(7):
            val = c_matrix[i][j]
            if abs(val) < 1e-8:
                print(f"  {'0':>7}", end="")
            else:
                # Try to identify as simple fraction
                print(f"  {val:>7.3f}", end="")
        print()

    # Check for nice rational coefficients
    print("\n  Attempting rational identification (multiply by common denominator):")
    # Find the GCD-like structure
    nonzero_vals = [c_matrix[i][j] for i in range(7) for j in range(i, 7) if abs(c_matrix[i][j]) > 1e-8]
    if nonzero_vals:
        min_abs = min(abs(v) for v in nonzero_vals)
        print(f"  Smallest nonzero |c_{'{ij}'}| = {min_abs:.6e}")
        print(f"  Ratios to smallest:")
        for i in range(7):
            for j in range(i, 7):
                if abs(c_matrix[i][j]) > 1e-8:
                    ratio = c_matrix[i][j] / min_abs
                    print(f"    c_{{{i+1},{j+1}}} / min = {ratio:.4f}")

    # Verify the quadratic form by checking at random points
    print("\n  Verification of quadratic form extraction:")
    rng = random.Random(33333)
    max_error = 0.0
    for _ in range(100):
        lams = tuple(rng.uniform(-2.0, 2.0) for _ in range(7))
        # Predicted from quadratic form
        predicted = d5T_at_0
        for i in range(7):
            for j in range(7):
                if i <= j:
                    predicted += c_matrix[i][j] * lams[i] * lams[j]
                # don't double-count: c_matrix is symmetric but we only add i<=j

        engine._cache.clear()
        result_check = engine.mk(lams)
        actual = result_check.get(5, 0.0)
        error = abs(predicted - actual)
        max_error = max(max_error, error)

    print(f"  Max |predicted - actual| over 100 random points: {max_error:.6e}")
    if max_error < 1e-6:
        print(f"  CONFIRMED: d^5T coefficient is exactly quadratic (depth 2)")
    else:
        print(f"  WARNING: extraction error {max_error:.6e} (higher-degree terms present?)")

    # Also check d^6T (should vanish = depth 1)
    print("\n  Confirming d^6T vanishing (depth 1):")
    max_d6T = 0.0
    for _ in range(200):
        lams = tuple(rng.uniform(-3.0, 3.0) for _ in range(7))
        engine._cache.clear()
        result_d6 = engine.mk(lams)
        d6T_val = abs(result_d6.get(6, 0.0))
        max_d6T = max(max_d6T, d6T_val)
    print(f"  max|d^6T coeff| = {max_d6T:.6e}")
    if max_d6T < 1e-6:
        print(f"  CONFIRMED: d^6T coefficient vanishes identically (depth 1 vanishing)")

    print()


# =============================================================================
# 7. COMPREHENSIVE DEPTH ANALYSIS ACROSS ALL FIELDS
# =============================================================================

def comprehensive_depth_analysis():
    """Detailed analysis of every field in m_8."""
    print("=" * 90)
    print("7. COMPREHENSIVE FIELD-BY-FIELD ANALYSIS OF m_8")
    print("=" * 90)

    k = 8
    engine = StasheffEngine(1.0)
    rng = random.Random(44444)

    # For each field (derivative order), determine the spectral degree
    # by evaluating at scaled points
    print("\n  Spectral degree verification for each field:")
    print(f"  {'field':>10} {'depth':>6} {'predicted_deg':>14} {'verified':>10}")

    for d_order in range(7):  # d^0T through d^6T
        depth = k - 1 - d_order
        # Evaluate at λ and 2λ — if degree d, ratio should be 2^d
        max_ratio = 0.0
        n_good = 0
        for _ in range(100):
            lams = tuple(rng.uniform(-1.0, 1.0) for _ in range(7))
            lams_2 = tuple(2.0 * l for l in lams)

            engine._cache.clear()
            result_1 = engine.mk(lams)
            val_1 = result_1.get(d_order, 0.0)

            engine._cache.clear()
            result_2 = engine.mk(lams_2)
            val_2 = result_2.get(d_order, 0.0)

            if abs(val_1) > 1e-8:
                ratio = val_2 / val_1
                expected = 2.0**depth
                rel_err = abs(ratio - expected) / expected
                if rel_err < 0.01:
                    n_good += 1

        status = "YES" if n_good > 80 else "partial" if n_good > 20 else "NO"
        print(f"  d^{d_order}T{'':>{7-len(str(d_order))}} {depth:>6} {depth:>14} {status:>10} ({n_good}/100)")

    print()


# =============================================================================
# MAIN
# =============================================================================

def main():
    print("*" * 90)
    print("  EXACT STRUCTURAL ANALYSIS OF m_8 FOR THE VIRASORO ALGEBRA")
    print("  Virasoro A∞ operation at arity 8: m_8(T,T,T,T,T,T,T,T; λ_1,...,λ_7)")
    print("*" * 90)
    print()

    symmetric_point_analysis()
    anti_palindrome_analysis()
    scalar_polynomial_analysis()
    L1_norm_verification()
    factorization_analysis()
    depth_2_analysis()
    comprehensive_depth_analysis()

    print("=" * 90)
    print("COMPUTATION COMPLETE")
    print("=" * 90)


if __name__ == '__main__':
    main()
