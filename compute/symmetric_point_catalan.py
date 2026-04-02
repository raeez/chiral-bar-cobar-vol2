r"""Compute Virasoro symmetric-point T-coefficient T_k(1,...,1) to order k=25.

Verifies the Catalan theorem:
  T_{2r+1}(1,...,1) = (-1)^{r+1} * (2r+1) * C_{r-1} * (2r)!   for odd k = 2r+1
  T_k(1,...,1) = 0                                               for even k >= 4

Also computes:
  - P_k(1,...,1) the scalar at symmetric point
  - L^1 norms ||m_k|_T|| for k=2,...,15
  - Gevrey-1 ratio ||m_k|_T|| / k!
"""

import sys
import os
import math
import time
import random

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from compute.m7_m10_depth_frontier import StasheffEngine


def catalan(n):
    """Catalan number C_n = (2n)! / ((n+1)! * n!)"""
    if n < 0:
        return 0
    return math.comb(2 * n, n) // (n + 1)


def catalan_formula(k):
    """The conjectured T_k(1,...,1) for odd k = 2r+1.

    T_{2r+1}(1,...,1) = (-1)^{r+1} * (2r+1) * C_{r-1} * (2r)!
    Returns None for even k >= 4.
    """
    if k % 2 == 0 and k >= 4:
        return 0.0
    if k == 2:
        # m_2(T,T; 1) = dT + 2T*1 + (c/12)*1 => T-coeff = 2
        return 2.0
    if k % 2 == 1:
        r = (k - 1) // 2
        sign = (-1) ** (r + 1)
        return sign * k * catalan(r - 1) * math.factorial(2 * r)
    return None


def scalar_formula(k):
    """The conjectured P_k(1,...,1) for odd k = 2r+1.

    P_k(1,...,1) = (-1)^{r-1} * C_{r-1} * (2r+1)! / 2  for odd k = 2r+1
    P_k(1,...,1) = 0 for even k >= 4
    """
    if k % 2 == 0 and k >= 4:
        return 0.0
    if k == 2:
        # m_2(T,T;1) has scalar = c/12 * 1^3 = c/12. P_2 = scalar/(c/12) = 1
        return 1.0
    if k % 2 == 1:
        r = (k - 1) // 2
        sign = (-1) ** (r - 1)
        return sign * catalan(r - 1) * math.factorial(2 * r + 1) / 2.0
    return None


def main():
    c_val = 1.0
    engine = StasheffEngine(c_val)

    max_k = 25

    print("=" * 100)
    print("VIRASORO SYMMETRIC-POINT T-COEFFICIENT T_k(1,...,1)")
    print(f"Computed at c = {c_val} using numerical Stasheff recursion")
    print("=" * 100)

    # ========== PART 1: T_k(1,...,1) for k=2,...,25 ==========
    print("\n" + "=" * 100)
    print("PART 1: T_k(1,...,1) numerically at c=1 for k=2,...,25")
    print("=" * 100)

    T_values = {}
    P_values = {}
    timings = {}

    print(f"\n{'k':>3} {'T_k(1,...,1)':>25} {'time(s)':>10}")
    print("-" * 45)

    for k in range(2, max_k + 1):
        engine._cache.clear()
        lams = tuple(1.0 for _ in range(k - 1))

        t0 = time.time()
        result = engine.mk(lams)
        dt = time.time() - t0
        timings[k] = dt

        T_coeff = result.get(0, 0.0)
        scalar_coeff = result.get(-1, 0.0)

        T_values[k] = T_coeff
        P_values[k] = scalar_coeff / (c_val / 12.0) if abs(scalar_coeff) > 1e-300 else 0.0

        if abs(T_coeff) < 1e-10:
            T_str = "0"
        elif abs(T_coeff) < 1e6:
            T_str = f"{T_coeff:.6f}"
        else:
            T_str = f"{T_coeff:.6e}"

        print(f"{k:>3} {T_str:>25} {dt:>10.3f}")

    # ========== PART 2: Verify Catalan formula ==========
    print("\n" + "=" * 100)
    print("PART 2: Catalan formula verification through r=12 (k=25)")
    print("=" * 100)
    print()
    print("THEOREM: T_{2r+1}(1,...,1) = (-1)^{r+1} * (2r+1) * C_{r-1} * (2r)!")
    print("         T_k(1,...,1) = 0  for even k >= 4")
    print()

    print(f"{'k':>3} {'r':>3} {'T_k numerical':>25} {'Catalan formula':>25} {'match':>8} {'rel err':>14}")
    print("-" * 85)

    all_match = True
    for k in range(2, max_k + 1):
        T_num = T_values[k]
        T_cat = catalan_formula(k)

        if k % 2 == 0 and k >= 4:
            r_str = "-"
            match = abs(T_num) < 1e-6
            rel_err_str = f"{abs(T_num):.2e}" if not match else "0"
        elif k == 2:
            r_str = "1"
            match = abs(T_num - T_cat) < 1e-6 * max(1, abs(T_cat))
            rel_err = abs(T_num - T_cat) / max(1e-300, abs(T_cat))
            rel_err_str = f"{rel_err:.2e}"
        else:
            r = (k - 1) // 2
            r_str = str(r)
            if abs(T_cat) > 1e-300:
                rel_err = abs(T_num - T_cat) / abs(T_cat)
                match = rel_err < 1e-6
                rel_err_str = f"{rel_err:.2e}"
            else:
                match = abs(T_num) < 1e-6
                rel_err_str = "N/A"

        if not match:
            all_match = False

        T_num_str = f"{T_num:.6e}" if abs(T_num) > 1e6 or (abs(T_num) > 0 and abs(T_num) < 1e-3) else (
            "0" if abs(T_num) < 1e-10 else f"{T_num:.6f}")
        T_cat_str = f"{T_cat:.6e}" if T_cat is not None and (abs(T_cat) > 1e6 or (abs(T_cat) > 0 and abs(T_cat) < 1e-3)) else (
            "0" if T_cat is not None and abs(T_cat) < 1e-10 else f"{T_cat}")

        print(f"{k:>3} {r_str:>3} {T_num_str:>25} {T_cat_str:>25} {'OK' if match else 'FAIL':>8} {rel_err_str:>14}")

    print(f"\n  ALL MATCH: {'YES' if all_match else 'NO'}")

    # ========== PART 2b: Display the Catalan pattern ==========
    print("\n  --- Catalan number pattern ---")
    print(f"  {'k':>3} {'r':>3} {'C_{r-1}':>10} {'(-1)^{r+1}':>12} {'(2r+1)*C_{r-1}*(2r)!':>25}")
    print("  " + "-" * 60)
    for k in range(3, max_k + 1, 2):
        r = (k - 1) // 2
        C = catalan(r - 1)
        sgn = (-1) ** (r + 1)
        val = sgn * k * C * math.factorial(2 * r)
        print(f"  {k:>3} {r:>3} {C:>10} {sgn:>12} {val:>25.0f}")

    # ========== PART 3: P_k(1,...,1) scalar polynomial ==========
    print("\n" + "=" * 100)
    print("PART 3: Scalar at symmetric point P_k(1,...,1) for k=2,...,25")
    print("=" * 100)
    print()
    print("CONJECTURE: P_k(1,...,1) = 0 for even k >= 4")
    print("            P_{2r+1}(1,...,1) = (-1)^{r-1} * C_{r-1} * (2r+1)! / 2  for odd k")
    print()

    print(f"{'k':>3} {'P_k(1,...,1) numerical':>25} {'formula':>25} {'match':>8}")
    print("-" * 70)

    all_P_match = True
    for k in range(2, max_k + 1):
        P_num = P_values[k]
        P_form = scalar_formula(k)

        if P_form is not None and abs(P_form) > 1e-300:
            if abs(P_num) > 1e-300:
                rel_err = abs(P_num - P_form) / abs(P_form)
                match = rel_err < 1e-4
            else:
                match = abs(P_form) < 1e-6
        else:
            match = abs(P_num) < 1e-6

        if not match:
            all_P_match = False

        def fmt(x):
            if x is None:
                return "N/A"
            if abs(x) < 1e-10:
                return "0"
            if abs(x) > 1e6:
                return f"{x:.6e}"
            return f"{x:.2f}"

        print(f"{k:>3} {fmt(P_num):>25} {fmt(P_form):>25} {'OK' if match else 'FAIL':>8}")

    print(f"\n  ALL SCALAR MATCH: {'YES' if all_P_match else 'NO -- investigate formula'}")

    # ========== PART 4: L^1 norms ||m_k|_T|| for k=2,...,15 ==========
    print("\n" + "=" * 100)
    print("PART 4: L^1 norms ||m_k|_T|| for k=2,...,15")
    print("=" * 100)

    n_samples = 2000
    rng = random.Random(77777)

    norms = {}
    print(f"\n{'k':>3} {'||m_k|_T||':>16} {'k!':>16} {'||m_k|_T||/k!':>16} {'ratio to prev':>16}")
    print("-" * 75)

    for k in range(2, 16):
        engine._cache.clear()
        total_T = 0.0

        rng_local = random.Random(77777 + k)
        for _ in range(n_samples):
            lams = tuple(rng_local.uniform(-1.0, 1.0) for _ in range(k - 1))
            result = engine.mk(lams)
            T_coeff = abs(result.get(0, 0.0))
            total_T += T_coeff

        L1_T = total_T / n_samples
        norms[k] = L1_T
        kfact = math.factorial(k)
        ratio = L1_T / kfact

        if k > 2 and norms.get(k - 1, 0) > 1e-300:
            prev_ratio = norms[k - 1] / math.factorial(k - 1)
            if prev_ratio > 1e-300:
                growth = ratio / prev_ratio
            else:
                growth = float('nan')
        else:
            growth = float('nan')

        growth_str = f"{growth:.6f}" if not math.isnan(growth) else "-"

        print(f"{k:>3} {L1_T:>16.6e} {kfact:>16d} {ratio:>16.8e} {growth_str:>16}")

    # ========== PART 5: Gevrey-1 analysis ==========
    print("\n" + "=" * 100)
    print("PART 5: Gevrey-1 verification: ||m_k|_T||/k! should stabilize ~ 10^{-2}")
    print("=" * 100)
    print()

    print("  If ||m_k|_T|| ~ C * A^k * k!  (Gevrey-1), then ||m_k|_T||/k! ~ C * A^k.")
    print("  Successive ratios (||m_k||/k!) / (||m_{k-1}||/(k-1)!) should approach A.")
    print()

    print(f"  {'k':>3} {'||m_k|_T||/k!':>16} {'ratio':>12} {'log10(ratio)':>14}")
    print("  " + "-" * 50)

    ratios = []
    for k in range(2, 16):
        if k not in norms:
            continue
        gev = norms[k] / math.factorial(k)

        if k > 2 and (k - 1) in norms:
            prev_gev = norms[k - 1] / math.factorial(k - 1)
            if prev_gev > 1e-300:
                r = gev / prev_gev
                ratios.append(r)
                log_r = math.log10(abs(r)) if r > 0 else float('nan')
                print(f"  {k:>3} {gev:>16.8e} {r:>12.6f} {log_r:>14.4f}")
            else:
                print(f"  {k:>3} {gev:>16.8e} {'N/A':>12} {'N/A':>14}")
        else:
            print(f"  {k:>3} {gev:>16.8e} {'-':>12} {'-':>14}")

    if ratios:
        avg_ratio = sum(ratios) / len(ratios)
        late_ratios = ratios[-5:] if len(ratios) >= 5 else ratios
        avg_late = sum(late_ratios) / len(late_ratios)
        print(f"\n  Average ratio (all): {avg_ratio:.6f}")
        print(f"  Average ratio (last 5): {avg_late:.6f}")
        print(f"  => Estimated Gevrey constant A ~ {avg_late:.4f}")
        print(f"  => log10(||m_k|_T||/k!) at k=15: {math.log10(norms.get(15, 1e-300) / math.factorial(15)):.2f}")

    # ========== SUMMARY ==========
    print("\n" + "=" * 100)
    print("EXECUTIVE SUMMARY")
    print("=" * 100)

    print(f"""
CATALAN THEOREM VERIFICATION (k=2,...,{max_k}):
  For odd k = 2r+1:
    T_{{2r+1}}(1,...,1) = (-1)^{{r+1}} * (2r+1) * C_{{r-1}} * (2r)!
  For even k >= 4:
    T_k(1,...,1) = 0

  Verified through r={max_k // 2} (k={max_k}): {'ALL MATCH' if all_match else 'FAILURES DETECTED'}

CATALAN NUMBERS APPEARING:
  r=1 (k=3):  C_0 = 1
  r=2 (k=5):  C_1 = 1
  r=3 (k=7):  C_2 = 2
  r=4 (k=9):  C_3 = 5
  r=5 (k=11): C_4 = 14
  r=6 (k=13): C_5 = 42
  ...

SCALAR POLYNOMIAL:
  Verified: {'ALL MATCH' if all_P_match else 'NEEDS INVESTIGATION'}

L^1 NORMS AND GEVREY-1:
  The ratio ||m_k|_T|| / k! is examined for k=2,...,15.
""")

    # Print the Catalan numbers and factorials for reference
    print("REFERENCE TABLE: Catalan formula values")
    print(f"{'k':>3} {'r':>3} {'C_{r-1}':>10} {'(2r)!':>20} {'T_k formula':>25}")
    print("-" * 70)
    for k in range(3, max_k + 1, 2):
        r = (k - 1) // 2
        C = catalan(r - 1)
        fac = math.factorial(2 * r)
        val = catalan_formula(k)
        print(f"{k:>3} {r:>3} {C:>10} {fac:>20} {val:>25.0f}")


if __name__ == '__main__':
    main()
