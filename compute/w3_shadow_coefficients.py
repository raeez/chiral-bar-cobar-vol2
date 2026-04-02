r"""W₃ shadow coefficient formula: the multivariable Catalan analogue.

For Virasoro (1 generator T, weight 2):
  - Shadow metric: Q_Vir(t) = c² + 12ct + [(180c+872)/(5c+22)]t²
  - Generating function: H(t) = t² √Q_Vir(t)
  - Shadow coefficients: S_r = [t^r]H(t)/r for r ≥ 4

For W₃ (2 generators T weight 2, W weight 3):
  - Shadow is a function of two variables (x_T, x_W)
  - Hessian: κ = diag(c/2, c/3)
  - Quartic shadow (rosetta_stone.tex eq w3-quartic):
      Sh_4 = [10/(c(5c+22))] x_T^4
           + [6·320/(c(5c+22)²)] x_T² x_W²
           + [10240/(c(5c+22)³)] x_W⁴

Strategy:
  The shadow generating function for a multi-generator algebra
  takes values in the ring of formal power series in (x_T, x_W).
  On the T-line (x_W = 0), it reduces to the Virasoro shadow.
  On the W-line (x_T = 0), only even arities survive (Z₂ symmetry W → -W).

  For the W-line shadow: define
    H_W(t) = sum_{r≥0} S^W_{2r}(c) · t^{2r}  (with x_W = t, x_T = 0)
  where S^W_{2r} is the W-line shadow coefficient at arity 2r.

  The T-line shadow metric Q^T(t) = Q_Vir(t) is known.
  The W-line shadow metric Q^W(t) encodes the pure-W shadow tower.
  The cross shadow metric Q^{TW}(t,s) encodes the mixed tower.

COMPUTATION PLAN:
  (1) Extract Q_{TTTT}, Q_{TTWW}, Q_{WWWW} from the quartic Stasheff.
  (2) Compute the full W₃ shadow metric Q(x_T, x_W) as a 2×2 matrix.
  (3) Compute shadow coefficients S_r on various lines.
  (4) Verify complementarity under c → 100-c.
  (5) Find closed-form formulas where possible.

Cross-references:
  - compute/w3_quartic_contact.py (quartic contact form)
  - chapters/examples/rosetta_stone.tex, eq:w3-quartic
  - chapters/connections/3d_gravity.tex (Virasoro shadow tower)
"""
from __future__ import annotations

from sympy import (
    Symbol, Rational, symbols, expand, simplify, factor, cancel,
    sqrt, series, S, binomial, collect, Poly, together, apart,
    oo, solve, Matrix,
)

c = Symbol('c')
t = Symbol('t')
x_T = Symbol('x_T')
x_W = Symbol('x_W')


# ===================================================================
# Section 0: Virasoro shadow metric (review)
# ===================================================================

def virasoro_shadow_metric():
    """Q_Vir(t) = c² + 12ct + [(180c+872)/(5c+22)]t².

    The three coefficients encode:
      q_0 = κ² = (c/2)² * 4 = c²
      q_1 = 2κ · S_3 = 2 · (c/2) · 12 = ... wait, let me be careful.

    Actually from the bar-cobar theory:
      Q_Vir(t) = (2κ)² + 2·(2κ)·(2·S_3)·t + [(2·S_3)² + 8κ·S_4]·t²
    where κ = c/2, S_3 = 2 (from the Virasoro data), S_4 = 10/(c(5c+22)).

    Let's verify: (2κ)² = c², 2·c·4·t = 8ct... no, the convention
    from the manuscript is direct:
      Q_Vir(t) = c² + 12ct + [(180c+872)/(5c+22)]t²
    (from 3d_gravity.tex line 5084).
    """
    q0 = c**2
    q1 = 12*c
    q2 = (180*c + 872) / (5*c + 22)
    return q0 + q1*t + q2*t**2


def virasoro_shadow_coefficients(n_max=10):
    """Compute S_r for Virasoro by expanding H(t) = t²√Q(t)."""
    Q = virasoro_shadow_metric()
    # Expand sqrt(Q) as power series in t
    # Q = c² + 12ct + q2·t² = c²(1 + (12/c)t + (q2/c²)t²)
    # sqrt(Q) = c·sqrt(1 + (12/c)t + (q2/c²)t²)

    # Use series expansion
    q2 = (180*c + 872) / (5*c + 22)
    u = (12/c)*t + (q2/c**2)*t**2
    # sqrt(1+u) = 1 + u/2 - u²/8 + u³/16 - 5u⁴/128 + ...

    # More directly: expand H(t) = t²·sqrt(Q(t)) as Taylor series
    # H(t) = sum_{r>=2} h_r t^r, and S_r = h_r / r

    coeffs = {}
    # Build Q and expand sqrt
    Q_expr = c**2 + 12*c*t + q2*t**2
    sqrt_Q_series = series(sqrt(Q_expr), t, 0, n=n_max+1)

    print("=" * 72)
    print("VIRASORO SHADOW METRIC AND COEFFICIENTS")
    print("=" * 72)
    print(f"\nQ_Vir(t) = {Q_expr}")
    print(f"\nsqrt(Q) expansion:")

    for r in range(n_max+1):
        coeff_r = sqrt_Q_series.coeff(t, r)
        coeff_r = cancel(coeff_r)
        print(f"  [t^{r}] sqrt(Q) = {coeff_r}")

    print(f"\nH(t) = t² sqrt(Q(t)) expansion:")
    print(f"Shadow coefficients S_r = [t^r]H / r:")
    for r in range(2, n_max+1):
        # [t^r]H = [t^{r-2}]sqrt(Q)
        h_r = sqrt_Q_series.coeff(t, r-2)
        h_r = cancel(h_r)
        S_r = cancel(h_r / r)
        coeffs[r] = S_r
        print(f"  r={r}: [t^r]H = {h_r}, S_{r} = {S_r}")

    return coeffs


# ===================================================================
# Section 1: W₃ quartic shadow (from Stasheff / rosetta_stone)
# ===================================================================

def w3_quartic_shadow():
    """The quartic shadow Sh_4(x_T, x_W) for W₃.

    From rosetta_stone.tex eq:w3-quartic:
      Sh_4 = [10/(c(5c+22))] x_T^4
           + [6·320/(c(5c+22)²)] x_T² x_W²
           + [10240/(c(5c+22)³)] x_W^4

    These are the quartic contact invariants:
      Q_{TTTT} = 10 / (c(5c+22))          [= Virasoro S_4]
      Q_{TTWW} = 6·320 / (c(5c+22)²) = 1920 / (c(5c+22)²)
      Q_{WWWW} = 10240 / (c(5c+22)³)
    """
    Q_TTTT = Rational(10, 1) / (c * (5*c + 22))
    Q_TTWW = Rational(1920, 1) / (c * (5*c + 22)**2)
    Q_WWWW = Rational(10240, 1) / (c * (5*c + 22)**3)

    Sh4 = Q_TTTT * x_T**4 + Q_TTWW * x_T**2 * x_W**2 + Q_WWWW * x_W**4

    print("\n" + "=" * 72)
    print("W₃ QUARTIC SHADOW")
    print("=" * 72)
    print(f"\nQ_TTTT = {Q_TTTT} = 10/(c(5c+22))")
    print(f"Q_TTWW = {Q_TTWW} = 1920/(c(5c+22)²)")
    print(f"Q_WWWW = {Q_WWWW} = 10240/(c(5c+22)³)")
    print(f"\nSh_4(x_T, x_W) = {Sh4}")

    # Ratios
    print(f"\nQ_TTWW / Q_TTTT = {cancel(Q_TTWW / Q_TTTT)} = 192/(5c+22)")
    print(f"Q_WWWW / Q_TTWW = {cancel(Q_WWWW / Q_TTWW)} = 16/(3(5c+22))")
    print(f"Q_WWWW / Q_TTTT = {cancel(Q_WWWW / Q_TTTT)} = 1024/(5c+22)²")

    # Pattern: each pair of W-legs contributes factor 32/(5c+22) = β
    beta = 32 / (5*c + 22)
    print(f"\nβ = 32/(5c+22)")
    print(f"Q_TTTT = 10/(c(5c+22))")
    print(f"Q_TTWW / Q_TTTT = {cancel(Q_TTWW / Q_TTTT)}")
    print(f"  = 192/(5c+22) = 6·β")
    print(f"Q_WWWW / Q_TTTT = {cancel(Q_WWWW / Q_TTTT)}")
    print(f"  = 1024/(5c+22)² = β² · 1024/1024 = β²")

    # Actually let me check: 10240/10 = 1024, and (5c+22)³/(5c+22) = (5c+22)²
    # So Q_WWWW = Q_TTTT · 1024/(5c+22)²
    # And 1024 = 32², so Q_WWWW = Q_TTTT · β²
    # Q_TTWW: 1920/10 = 192, and (5c+22)²/(5c+22) = (5c+22)
    # So Q_TTWW = Q_TTTT · 192/(5c+22) = Q_TTTT · 6β
    print(f"\n  Q_TTWW = 6β · Q_TTTT")
    print(f"  Q_WWWW = β² · Q_TTTT")
    print(f"\n  Sh_4 = Q_TTTT · [x_T^4 + 6β x_T² x_W² + β² x_W^4]")
    print(f"       = Q_TTTT · [x_T^4 + 6β x_T² x_W² + β² x_W^4]")
    print(f"\n  NOTE: (x_T² + β x_W²)² = x_T^4 + 2β x_T² x_W² + β² x_W^4")
    print(f"  So Sh_4 = Q_TTTT · [(x_T² + β x_W²)² + 4β x_T² x_W²]")

    return Q_TTTT, Q_TTWW, Q_WWWW


# ===================================================================
# Section 2: W₃ shadow metric Q(x_T, x_W)
# ===================================================================

def w3_shadow_metric():
    r"""Construct the W₃ shadow metric.

    For a single-generator algebra with generator of weight h:
      Q(t) = κ² + 2κ·α·t + (α² + Δ)·t²
    where κ = Hessian, α = "cubic strength" S₃, Δ = 8κ·S₄.

    For the Virasoro algebra:
      κ = c/2, α = 6 (from S₃ = 2, with 2κ·α = 12c → α = 12),
      wait... let me re-derive.

    From Q_Vir(t) = c² + 12ct + [(180c+872)/(5c+22)]t²:
      q₀ = c² = (2κ)² with κ = c/2. So (2κ)² = c². ✓
      q₁ = 12c.
      q₂ = (180c+872)/(5c+22).

    For the 2-generator case, the "shadow metric" is a polynomial in
    the TWO deformation variables (x_T, x_W).

    The generating function for the scalar shadow tower is
      H(x_T, x_W) = sum_{r≥2} Sh_r(x_T, x_W) · t^r  (?)

    No — the multi-generator shadow metric Q_{W₃}(x_T, x_W) is
    the polynomial whose square root generates the shadow tower.
    It is determined by the data:
      - Binary: κ = (c/2, c/3)
      - Ternary: m₃ coefficients
      - Quartic: the Sh₄ coefficients above

    More precisely, on any LINE through the origin in (x_T, x_W) space,
    the restriction is a single-variable shadow metric.

    On the T-line (x_W = 0, x_T = t):
      Q^T(t) = Q_Vir(t)  [by T-sector decoupling]

    On the W-line (x_T = 0, x_W = t):
      Q^W(t) is determined by S₂^W = c/3, S₃^W = 0 (by Z₂),
      S₄^W = Q_WWWW = 10240/(c(5c+22)³), ...

    On a general ray x_T = α·t, x_W = β·t:
      Q(α,β; t) is a DEGREE-4 polynomial in t (!)
      because the quartic involves x_T⁴ + x_T²x_W² + x_W⁴.

    THIS IS THE KEY DIFFERENCE FROM VIRASORO:
      For Virasoro, Q(t) is degree 2 → √Q is algebraic of degree 2.
      For W₃, on a general ray, Q(t) is degree 4 → √Q involves
      an ELLIPTIC integral (hyperelliptic curve of genus 1).

    The shadow metric on a ray (cos θ, sin θ) is:
      Q(θ; t) = q₀(θ) + q₁(θ)·t + q₂(θ)·t² + q₃(θ)·t³ + q₄(θ)·t⁴
    """
    # Binary data: κ_T = c/2, κ_W = c/3
    kT = c / 2
    kW = c / 3

    # Ternary data: S₃
    # On T-line: S₃^T = 2 (Virasoro)
    # On W-line: S₃^W = 0 (Z₂ symmetry W → -W forces odd arities to vanish)
    # Cross: S₃^{TTW} = ? and S₃^{TWW} = ?
    # From the W₃ λ-bracket {T_λ W} = ∂W + 3λW:
    #   m₃(T,T,W) involves the Virasoro-W mixing.
    # The key question: what is the full structure?

    print("\n" + "=" * 72)
    print("W₃ SHADOW METRIC STRUCTURE")
    print("=" * 72)

    # The full shadow polynomial Q_{W₃}(x_T, x_W; t)
    # is determined by all Sh_r for r = 2, 3, 4.

    # Sh_2 = κ_T x_T² + κ_W x_W² = (c/2)x_T² + (c/3)x_W²
    Sh2 = kT * x_T**2 + kW * x_W**2

    # Sh_3 = S₃^{TTT} x_T³ + S₃^{TTW} x_T²x_W + S₃^{TWW} x_Tx_W² + S₃^{WWW} x_W³
    # By the Z₂ symmetry W → -W:
    #   S₃^{TTW} = 0 (odd in W), S₃^{WWW} = 0 (odd in W)
    # Wait — S₃^{TTW} has ONE W-leg, which is odd under W → -W.
    # So S₃^{TTW} = 0. Similarly S₃^{TWW} has TWO W-legs, which is
    # EVEN under W → -W, so S₃^{TWW} need not vanish.
    # And S₃^{WWW} has THREE W-legs, odd, so S₃^{WWW} = 0.
    # Actually wait: S₃^{TTT} = 2 (Virasoro).
    # S₃^{TWW}: this comes from m₃(T,W,W) on the scalar part.
    # From the rosetta computation, the cubic shadow from m₃(T,T,T) gives 2,
    # but we need to think about what the cubic shadow IS for mixed inputs.

    # The shadow coefficients as written in the rosetta stone:
    #   S_2 = κ = c/2 (Virasoro, on T-line)
    #   S_3 = 2 (Virasoro, on T-line)
    # For the full 2-variable theory, the shadow polynomial on a line
    # x_T = α, x_W = β has
    #   Sh_2(α,β) = (c/2)α² + (c/3)β²
    #   Sh_3(α,β) = S₃^{TTT}·α³ + S₃^{TWW}·αβ²  (only even-W terms)

    # From {T_λ W} = ∂W + 3λW, the cubic operation m₃(T,W,W):
    # The scalar part of m₃(T,W,W) is zero because conformal weight
    # conservation requires h_out + deg = h₁+h₂+h₃ - 1 = 2+3+3-1 = 7,
    # and the scalar (h_out = 0) would need deg = 7, but m₃ produces
    # spectral polynomials of degree ≤ 2 (it has 2 spectral params).
    # Wait, the total degree in spectral params for m₃ at the SCALAR level:
    # h + a + b = h₁+h₂+h₃ - |m₃| = 8 - 1 = 7? Let me reconsider.

    # Actually, for the shadow tower framework, the "shadow" at arity r
    # is defined as S_r = Sh_r / (monomial), where Sh_r is the
    # homogeneous-degree-r piece of the full shadow function.
    # The Virasoro shadow metric Q_L(t) with t the single deformation
    # parameter satisfies H(t) = t²·√Q_L(t) = sum S_r t^r.

    # For the multi-generator case, the shadow metric is a polynomial
    # Q_{W₃}(x_T, x_W) (homogeneous of some degree in the x variables),
    # and the generating function is related to √Q_{W₃}.

    # THE KEY INSIGHT from the Virasoro case:
    # Q_Vir(t) is degree 2 in t, with coefficients:
    #   [t⁰] = κ² = c²  (from Sh₂² = (c/2 · t²)² at t² level... )
    # Actually Q_Vir = (2Sh₂)² + 2·(2Sh₂)·(2Sh₃)·t + [(2Sh₃)² + 8Sh₂·Sh₄]·t²
    # where I'm being sloppy. Let me just use the known formula directly.

    # For the multi-generator case, we need to determine Q as a function
    # of (x_T, x_W) that generates the shadow tower when we take its
    # square root.

    # The correct framework: the shadow generating function on a line
    # x_T = αs, x_W = βs in the deformation space satisfies
    #   H(α,β; s) = s^(h_min) · √Q(α,β; s)
    # where h_min is the minimum generator weight = 2.
    # Actually for Virasoro, H(t) = t² √Q(t), and the t² is from
    # the weight of T: the leading term is κ·t² = (c/2)·t².
    # For W₃ on the W-line, the leading term is κ_W · t³ = (c/3)·t³.
    # On a mixed line, the leading power depends on the direction.

    # Let me think about this differently. The shadow generating function
    # is really
    #   H(x_T, x_W) = sum_{r≥2} sum_{a+b=r} S_{a,b} x_T^a x_W^b
    # and the "shadow metric" Q satisfies H² = (something involving Q).
    # For the SINGLE VARIABLE case: H(t)² = t⁴ · Q(t).

    # For the MULTI-VARIABLE case, we need to think about what Q is.
    # The shadow generating function on the T-line:
    #   H_T(t) = H(t, 0) = sum_{r≥2} S_{r,0} t^r
    # and H_T² = t⁴ · Q_Vir(t).
    # On the W-line:
    #   H_W(s) = H(0, s) = sum_{r≥2} S_{0,r} s^r
    #   (only even r survive by Z₂)
    # and H_W² = s⁶ · Q_W(s)  [s⁶ because weight 3 gives leading s³]
    # Actually H_W(s) starts at s⁰ = κ_W · s² ... no.

    # Wait. I need to reconsider. The "shadow" at arity r in the
    # Virasoro case means the trace Sh_r = <η, m_r(η,...,η)>
    # where η is a test vector. With η = x_T · T + x_W · W for W₃,
    # the arity-r shadow is:
    #   Sh_r(x_T, x_W) = <η, m_r(η,...,η)>
    # which is a homogeneous polynomial of degree r+1 in (x_T, x_W)
    # (r inputs plus one output contracted with η).
    # No — it's degree r from the r inputs, with the output contracted.
    # Let me be precise.

    # m_r takes r inputs and produces an output. The contraction with
    # the Shapovalov form gives Sh_r(x_T, x_W) = <η|m_r(η,...,η)>
    # where each η = x_T T + x_W W. With r copies of η as input,
    # Sh_r is homogeneous of degree r in (x_T, x_W).
    # (The output is contracted with η via the form, adding 1 more power,
    # so actually degree r+1? Let me check against Virasoro.)

    # For Virasoro: Sh_2 = <η|m_2(η,η)> with η = x_T T. But m_2(T,T) = {T_λT}
    # and the Shapovalov pairing <T|scalar> = c/2. So Sh_2 involves
    # <T|{T_λT}> which gives the Hessian κ = c/2 · x_T². Wait, we need
    # to be more careful about what "scalar" means.

    # Actually from the rosetta_stone.tex data:
    # Sh_2 = κ · x² = (c/2) · x_T², so Sh_2 ~ x_T² (degree 2).
    # Sh_3 = ... degree 3 in x_T.
    # Sh_4 = ... degree 4 in x_T.

    # For W₃: Sh_4 = Q_TTTT x_T⁴ + Q_TTWW x_T²x_W² + Q_WWWW x_W⁴
    # This is degree 4 in (x_T, x_W). ✓

    # So the shadow is:
    # Sh(x_T, x_W; t) = sum_{r≥2} Sh_r(x_T, x_W) · t^r
    #                  = Sh_2·t² + Sh_3·t³ + Sh_4·t⁴ + ...
    # The "shadow metric" Q(x_T, x_W; t) satisfies
    # Sh² = t⁴ · Q  (for Virasoro, on T-line)
    # but for multi-variable, the relationship is different.

    # Actually, the shadow generating function for Virasoro is:
    #   H(t) = sum_{r≥2} r·S_r·t^r = κ·t² + S₃·t³ + S₄·t⁴ + ...
    # wait, the manuscript says S_r = [t^r]H/r. So H(t) = sum h_r t^r
    # with h_r = r·S_r, and H = t²√Q.

    # For the single-variable case, the relationship H² = t⁴Q encodes
    # the recursion between shadow coefficients. For the multi-variable
    # case, we need to restrict to lines.

    # ON A LINE x_T = αs, x_W = βs:
    #   Sh_r(α·s, β·s) = s^r · Sh_r(α, β)
    # So the shadow on this line is
    #   H_line(t) = sum_{r≥2} Sh_r(α,β) · t^r
    # and we can define Q_line(t) by H_line² = t⁴ · Q_line.
    # Then Q_line(t) = [sum Sh_r(α,β)·t^{r-2}]².
    # That's just (H_line/t²)² = Q_line.
    # So Q_line = (Sh_2(α,β) + Sh_3(α,β)·t + Sh_4(α,β)·t² + ...)²?
    # No, H = t²√Q implies H² = t⁴·Q, so Q = (H/t²)²... that means
    # Q = (sum Sh_r·t^{r-2})² which is always a perfect square!
    # That can't be right.

    # Let me re-derive from the Virasoro case.
    # H(t) = t²√Q(t). So H² = t⁴·Q(t).
    # H = sum_{r≥2} h_r t^r with h_2 = c (= 2κ), h_3 = 6 (= 2S₃·κ?).
    # From 3d_gravity.tex: H = ct² + 6t³ + [40/(c(5c+22))]t⁴ + ...
    # So h_2 = c, h_3 = 6, h_4 = 40/(c(5c+22)), ...
    # And S_r = h_r/r: S_2 = c/2, S_3 = 2, S_4 = 10/(c(5c+22)). ✓

    # H² = c²t⁴ + 12ct⁵ + [36 + 80/(c(5c+22))]t⁶ + ...
    # t⁴·Q = t⁴·(c² + 12ct + q₂t²) = c²t⁴ + 12ct⁵ + q₂t⁶.
    # So q₂ = 36 + 80/(c(5c+22)) = (36c(5c+22) + 80)/(c(5c+22))
    #        = (180c² + 792c + 80)/(c(5c+22))
    # Hmm, but the manuscript says q₂ = (180c+872)/(5c+22). Let me check:
    # (180c+872)/(5c+22) vs (180c²+792c+80)/(c(5c+22)).
    # These are DIFFERENT. Let me recompute.
    # H² = (ct² + 6t³ + at⁴ + ...)² = c²t⁴ + 2c·6t⁵ + (36 + 2ca)t⁶ + ...
    # where a = h_4 = 40/(c(5c+22)).
    # So [t⁶]H² = 36 + 2c · 40/(c(5c+22)) = 36 + 80/(5c+22)
    #            = (36(5c+22) + 80)/(5c+22) = (180c + 792 + 80)/(5c+22)
    #            = (180c + 872)/(5c+22). ✓!

    # Good. So Q is NOT (H/t²)², but rather Q is defined so that
    # H = t²√Q, i.e., H²/t⁴ = Q. This means:
    # Q(t) = H(t)²/t⁴ = (h_2 + h_3 t + h_4 t² + ...)²
    # Q(t) = h_2² + 2h_2 h_3 t + (h_3² + 2h_2 h_4)t² + ...
    # = c² + 12c·t + (36 + 80/(5c+22))t² + ...
    # = c² + 12ct + (180c+872)/(5c+22) · t² + higher

    # But Q is EXACTLY degree 2 for Virasoro (the higher terms vanish).
    # This is because H = t²√Q with Q degree 2 means H has a specific
    # algebraic structure. The shadow coefficients S_r for r≥5 are
    # DETERMINED by (c, S₃, S₄) = (c/2, 2, 10/(c(5c+22))).

    # KEY: Q(t) is the EXACT shadow metric, not a truncation.
    # For Virasoro, Q is degree 2 (only 3 independent data: κ, S₃, S₄).
    # For W₃ on a general line, Q can have degree > 2.

    print(f"\n  Sh_2(x_T, x_W) = (c/2)x_T² + (c/3)x_W²")
    print(f"  Sh_3(x_T, x_W) = 2·x_T³ + S₃^TWW · x_T·x_W²")
    print(f"       (S₃^TTW = S₃^WWW = 0 by Z₂)")

    # Now: on the T-line, Q_T(t) = c² + 12ct + [(180c+872)/(5c+22)]t²
    # (degree 2, Virasoro).
    # On the W-line, S₃ = 0, so Q_W(s) starts differently.

    # On the W-line: x_T = 0, x_W = s.
    # Sh_2 = (c/3)s², Sh_3 = 0, Sh_4 = Q_WWWW · s⁴, Sh_5 = 0, ...
    # H_W(s) = (c/3)s² + 0 + Q_WWWW s⁴ + 0 + Sh_6 s⁶ + ...
    # But wait: H_W(s) = s²√Q_W(s) means
    # (c/3)s² + Q_WWWW s⁴ + ... = s²(c/3 + Q_WWWW s² + ...)
    # So √Q_W = c/3 + Q_WWWW s² + ...
    # Q_W = (c/3)² + 2(c/3)Q_WWWW s² + ...
    # Wait, that doesn't work — √Q_W(0) = c/3, so Q_W(0) = (c/3)² = c²/9.

    # Hmm, but for Virasoro: H_T(t) = ct² + 6t³ + ...
    # So √Q_T(t) = c + 6t + ... and Q_T(0) = c² (not (c/2)²).
    # So H = t²√Q means the leading coefficient of H is h_2 = √Q(0).
    # But h_2 = Sh_2 = κ on the T-line: κ_T = c/2, and h_2 = c.
    # That means Sh_2 = c/2 but h_2 = c? Let me re-read...

    # From the 3d_gravity.tex: S_2 = c/12, and [t²]H = c.
    # Wait, I read S_2 = c/12 from the table but earlier I saw S_2 = c/2
    # from the rosetta stone. Let me check.

    # 3d_gravity.tex table says: r=2, S_2 = c/12. But the rosetta stone
    # table says r=2, S_2 = c/2. These are DIFFERENT tables with
    # different conventions!

    # Ah I see — the rosetta stone has the Virasoro column with S_2 = c/2.
    # The 3d_gravity.tex has S_2 = c/12. These must use different
    # normalization conventions for the shadow. Let me check:
    # If S_r = [t^r]H/r, then S_2 = h_2/2 = c/2. That matches rosetta.
    # The 3d_gravity.tex says S_2 = c/12 — maybe different convention there.

    # Actually the 3d_gravity.tex table at line 5141 says:
    # r=2: S_2 = c/12, r=3: S_3 = -c.
    # That's the "physical" shadow coefficient (different from the
    # algebraic shadow tower coefficient). The rosetta stone has S_2 = c/2
    # (algebraic). Let me use the algebraic convention.

    # ALGEBRAIC CONVENTION (rosetta stone):
    # Sh_r is the full trace, and H(t)² = t⁴·Q(t).
    # H(t) = ct² + 6t³ + [40/(c(5c+22))]t⁴ + ...
    # So h_r = r · S_r^{rosetta}: h_2 = 2·(c/2) = c, h_3 = 3·2 = 6,
    # h_4 = 4·10/(c(5c+22)) = 40/(c(5c+22)). ✓

    # For W₃ on the W-line, by Z₂ only even arities contribute:
    # H_W(s) = (c/3)·s² + 0·s³ + Q_WWWW·s⁴ + 0·s⁵ + ...
    # Wait — s is the W-line parameter, and Sh_2 = (c/3)s²
    # means h_2^W = 2·(c/3)/2... no.

    # Let me be very careful. On the W-line (x_T=0, x_W=s):
    # Sh_2(0,s) = (c/3)·s² — this is the arity-2 shadow, quadratic in s.
    # Sh_3(0,s) = 0 — by Z₂.
    # Sh_4(0,s) = Q_WWWW · s⁴ = [10240/(c(5c+22)³)] · s⁴.
    # Now H_W(s) = sum_{r≥2} Sh_r(0,s) = (c/3)s² + 0 + Q_WWWW s⁴ + ...
    # And H_W(s) = s^? · √Q_W(s).
    # The leading power: H_W starts at s², so H_W = s² · (c/3 + 0·s + Q_WWWW s² + ...)
    # If Q_W(s) is defined by H_W = s²·√Q_W, then
    # √Q_W(s) = c/3 + Q_WWWW s² + ...
    # Q_W(s) = (c/3)² + 2(c/3)Q_WWWW s² + Q_WWWW² s⁴ + 2(c/3)Sh_6 s⁴ + ...
    # But Q_W may have higher degree terms!

    # The question: is Q_W EXACTLY a polynomial? For Virasoro, Q is degree 2
    # (exactly). For W₃ on the W-line, Q_W could be degree 4 (from the
    # quartic input). But it could also be infinite.

    # The algebraic structure tells us: Q is determined by finitely many
    # data (κ, S₃, S₄, ...) up to the pole order. For Virasoro (pole order 4),
    # Q is degree 2. For W₃ (pole order 6 from {W_λ W}), Q could have
    # higher degree.

    print(f"\n  On the W-line (x_T=0, x_W=s):")
    print(f"    H_W(s) = (c/3)s² + Q_WWWW·s⁴ + Sh_6^W·s⁶ + ...")
    print(f"    = s²·[(c/3) + Q_WWWW·s² + Sh_6^W·s⁴ + ...]")
    print(f"    = s²·√Q_W(s)")
    print(f"    Q_W(s) = [(c/3) + Q_WWWW·s² + ...]²")
    print(f"\n  If Q_W is degree 4 in s, then √Q_W truncates after s⁴,")
    print(f"  and the W-line shadow tower is algebraic of degree 2.")

    return Sh2


# ===================================================================
# Section 3: W-line shadow metric (pure W sector)
# ===================================================================

def w_line_shadow_metric():
    """Compute Q_W(s) for the W-line (x_T = 0).

    On the W-line, only even-arity shadows survive (Z₂ symmetry).
    The generating function is
      H_W(s) = sum_{r≥1} Sh_{2r}^W · s^{2r}
    where Sh_{2r}^W = Sh_{2r}(0, s) evaluated at x_W = s.

    We have:
      Sh_2^W = κ_W = c/3
      Sh_4^W = Q_{WWWW} = 10240/(c(5c+22)³)

    The W-line shadow metric Q_W(s) satisfies H_W(s) = s² √Q_W(s),
    equivalently H_W² = s⁴ Q_W(s).

    Since H_W has only even powers: H_W(s) = (c/3)s² + Q_4 s⁴ + Q_6 s⁶ + ...
    H_W²/s⁴ = (c/3 + Q_4 s² + Q_6 s⁴ + ...)²

    THIS IS IMPORTANT: if the shadow data consists of EXACTLY (κ_W, S_4^W),
    then Q_W is degree 2 (in s²) and
      Q_W(u) = (c/3)² + 2(c/3)Q_4 u + [Q_4² + 2(c/3)Q_6] u²
    where u = s².

    But we need more shadow data (Sh_6^W, etc.) to determine Q_W fully.
    The question is: what DETERMINES Q_W? Is it degree 2 in u = s²?

    For Virasoro, Q is degree 2, determined by 3 data (κ, S₃, S₄).
    The key insight from Vol I: the shadow metric is determined by the
    POLE STRUCTURE of the OPE. For {W_λ W} with pole order 5, the
    shadow metric on the W-line should be degree 2 in u = s²
    (since the "effective" data are κ_W and Q_WWWW, with S₃^W = 0).

    If Q_W(u) = A + Bu + Cu², with A = (c/3)², then
      √Q_W = (c/3)·(1 + Bu/(c/3)² + Cu²/(c/3)²)^{1/2}
    and the shadow coefficients are determined by the binomial expansion.
    The data Sh_4 = Q_WWWW determines B:
      [u] in √Q_W = B/(2·c/3) = 3B/(2c)
    and H_W = s² √Q_W(s²), so [s⁴] H_W = [u]√Q_W = 3B/(2c)
    But [s⁴] H_W = Sh_4^W = Q_WWWW = 10240/(c(5c+22)³).
    So B = 2c·Q_WWWW/3 = 2c/(3) · 10240/(c(5c+22)³) = 20480/(3(5c+22)³).

    Then C (the degree-2 coefficient) would be determined by Sh_6^W.
    If C = 0 (simplest case), Q_W is degree 1 in u (degree 2 in s),
    and all higher Sh_{2r}^W are determined by (κ_W, Q_WWWW).
    """
    kW = c / 3
    Q_WWWW = Rational(10240, 1) / (c * (5*c + 22)**3)

    # Shadow metric on W-line: Q_W(u) with u = s²
    # Q_W = A + Bu (LINEAR in u, assuming degree 1)
    A = kW**2  # = c²/9
    # From [u]√(A+Bu) = B/(2√A) = B/(2c/3) = 3B/(2c)
    # and this equals Sh_4^W = Q_WWWW:
    B = 2*c*Q_WWWW/3

    Q_W_linear = A + B * t  # t stands for u = s²

    print("\n" + "=" * 72)
    print("W-LINE SHADOW METRIC (pure W sector)")
    print("=" * 72)

    print(f"\n  κ_W = c/3")
    print(f"  Q_WWWW = 10240/(c(5c+22)³)")
    print(f"\n  A = κ_W² = c²/9")
    B_simplified = cancel(B)
    print(f"  B = 2c·Q_WWWW/3 = {B_simplified}")
    print(f"    = {factor(B_simplified)}")

    # Check: 2c/(3) · 10240/(c(5c+22)³) = 20480/(3(5c+22)³)
    B_expected = Rational(20480, 3) / (5*c + 22)**3
    print(f"  B expected = 20480/(3(5c+22)³) = {B_expected}")
    print(f"  Match: {simplify(B_simplified - B_expected) == 0}")

    print(f"\n  Q_W(u) = c²/9 + [20480/(3(5c+22)³)]·u  (u = s²)")

    # Now compute W-line shadow coefficients from this Q_W:
    # H_W(s) = s²√Q_W(s²) = s²√(c²/9 + B·s²)
    #        = (c/3)s² √(1 + 9B/c² · s²)
    # [s^{2r}]H_W = (c/3) · binom(1/2, r-1) · (9B/c²)^{r-1}
    # Sh_{2r}^W = [s^{2r}]H_W

    print(f"\n  W-line shadow coefficients (assuming Q_W linear in u):")
    print(f"  H_W(s) = (c/3)s² · √(1 + γ·s²)")
    gamma = 9*B/c**2
    gamma_simplified = cancel(gamma)
    print(f"  γ = 9B/c² = {gamma_simplified}")
    # 9 · 20480/(3(5c+22)³) / c² = 9·20480 / (3c²(5c+22)³)
    # = 184320 / (3c²(5c+22)³) = 61440 / (c²(5c+22)³)
    gamma_check = Rational(61440, 1) / (c**2 * (5*c+22)**3)
    print(f"  γ check = 61440/(c²(5c+22)³): {simplify(gamma_simplified - gamma_check) == 0}")

    for r in range(1, 8):
        # binom(1/2, r-1) = (1/2)(1/2-1)...(1/2-r+2)/(r-1)!
        bcoeff = Rational(1, 1)
        for j in range(r-1):
            bcoeff *= (Rational(1, 2) - j)
        bcoeff /= Rational(1, 1) if r == 1 else 1
        from math import factorial
        bcoeff = bcoeff / factorial(r-1) if r > 1 else bcoeff
        # [s^{2r}]H_W = (c/3) · binom(1/2, r-1) · γ^{r-1}
        coeff = (c/3) * bcoeff * gamma_check**(r-1)
        coeff_simplified = cancel(coeff)
        sr = cancel(coeff / (2*r))  # S_{2r} = Sh_{2r} / (2r)
        print(f"  Sh_{2*r}^W = {coeff_simplified}")
        print(f"  S_{2*r}^W  = Sh_{2*r}/(2r) = {sr}")

    return Q_W_linear, gamma_check


# ===================================================================
# Section 4: Full shadow metric Q_{W₃}
# ===================================================================

def full_shadow_metric():
    """Construct the full 2-variable shadow metric for W₃.

    The shadow metric Q_{W₃}(x_T, x_W) is a polynomial in (x_T, x_W)
    such that the generating function on any line through the origin
    satisfies H_line(t) = t² √Q_line(t).

    For the T-line: Q_T(t) = c² + 12ct + [(180c+872)/(5c+22)]t²  (Virasoro)
    For the W-line: Q_W(u) = c²/9 + [20480/(3(5c+22)³)]u  (u=s²)

    The full metric has the form:
      Q(x_T, x_W) = [κ_T x_T + κ_W x_W²/(x_T)]²  ... no, this isn't right.

    On a line x_T = αt, x_W = βt:
      Sh_2(α,β) = (c/2)α² + (c/3)β²
      Sh_3(α,β) = 2α³ + S₃^TWW αβ²  (need S₃^TWW)
      Sh_4(α,β) = Q_TTTT α⁴ + Q_TTWW α²β² + Q_WWWW β⁴
      Sh_5(α,β) = ... (higher)

      H_line(t) = Sh_2(α,β)t² + Sh_3(α,β)t³ + Sh_4(α,β)t⁴ + ...
      H_line² = t⁴ · Q_line(t)
      Q_line(t) = Sh_2² + 2·Sh_2·Sh_3·t + (Sh_3² + 2·Sh_2·Sh_4)t² + ...

    If Q_line is degree 2 in t for ALL directions (α,β), then all
    shadow coefficients Sh_r for r ≥ 5 are determined by Sh_2, Sh_3, Sh_4.
    This requires (Sh_3² + 2 Sh_2 Sh_4) to be the COMPLETE t² coefficient,
    i.e., no cubic or higher terms in Q.

    Q_line has a t³ coefficient: 2Sh_2·Sh_5 + 2Sh_3·Sh_4.
    For this to vanish for all (α,β), we need Sh_5 = -Sh_3·Sh_4/Sh_2.
    On the T-line: Sh_5^T = h_5 = -h_3·h_4/h_2 = -6·40/(c(5c+22))/c
    = -240/(c²(5c+22)). And S_5 = h_5/5 = -48/(c²(5c+22)). ✓!

    So the Q-degree-2 condition holds for Virasoro. For W₃ on the W-line:
    Sh_3 = 0 so we need Sh_5 = 0 (which it is, by Z₂), and
    the t³ coeff = 2·Sh_2·Sh_5 + 2·0·Sh_4 = 0. ✓
    The t⁴ coeff = 2Sh_2·Sh_6 + 2Sh_3·Sh_5 + Sh_4² = 2Sh_2·Sh_6 + Sh_4².
    For Q to be degree 2 (in u=t²), we need [u²]Q_W = Sh_4² + 2Sh_2·Sh_6 = C.
    But we also need this to be EXACTLY the t⁴ coefficient. If Q_W has
    no u² term, then C = 0, giving Sh_6 = -Sh_4²/(2Sh_2).

    This is the recursion that generates the tower!

    Let me compute numerically to determine whether Q_{W₃} is degree 2
    on all rays.
    """
    print("\n" + "=" * 72)
    print("FULL W₃ SHADOW METRIC: DEGREE ANALYSIS")
    print("=" * 72)

    # Data
    Q_TTTT = Rational(10, 1) / (c * (5*c + 22))
    Q_TTWW = Rational(1920, 1) / (c * (5*c + 22)**2)
    Q_WWWW = Rational(10240, 1) / (c * (5*c + 22)**3)

    a, b = symbols('a b')

    Sh2 = (c/2)*a**2 + (c/3)*b**2

    # For Sh_3: we need S₃^TWW. From the W₃ m₃ computation.
    # m₃(T,W,W) scalar part: from conformal weight conservation,
    # outputs have weight h with h + deg = 8 - 1 = 7.
    # The scalar (h=0) would need deg = 7, but m₃ has 2 spectral params.
    # The maximum total spectral degree for m₃ is bounded by the OPE poles.
    # For {T_λ W} = ∂W + 3λW (pole order 2), the m₃ from composing
    # these should have total degree ≤ 4 (from the Virasoro {T_λT} pole 3
    # composed with {T_λ W} pole 2).
    # But the SCALAR of m₃(T,W,W) requires h_out = 0 and deg = 7.
    # That's impossible if total degree ≤ 4. So S₃^TWW(scalar) = 0.
    # The non-scalar parts give S₃^TWW for field-valued shadows.

    # Wait: I need to be more precise about what "shadow coefficient" means.
    # Sh_r = <η, m_r(η,...,η)> where <·,·> is the Shapovalov form.
    # For the scalar part, we'd need m_r to produce a scalar output,
    # and then contract with the Shapovalov form applied to η.
    # Actually, the shadow coefficient is more nuanced: it contracts
    # the OUTPUT of m_r with the Shapovalov dual of the input.

    # For the Virasoro case: <T|m₃(T,T,T)> at the scalar level is
    # the contraction <T|scalar_part · T + ...>. The Shapovalov form
    # <T|T> = c/2, so if m₃(T,T,T) = P(λ₁,λ₂)T + ..., then
    # <T|m₃(T,T,T)> = (c/2)·P.

    # For W₃: <η|m₃(η,η,η)> with η = aT + bW.
    # = a³<T|m₃(T,T,T)> + a²b<T|m₃(T,T,W)> + a²b<W|m₃(T,T,T)>
    #   + ... [all cross-terms]
    # = a³·Virasoro_S3 + cross terms.

    # The cross term <T|m₃(T,T,W)>: m₃(T,T,W) produces fields.
    # Its T-projection paired with <T|·> = (c/2)·(T coefficient).
    # By weight conservation: m₃(T,T,W) has input weight 2+2+3=7,
    # and |m₃|=1, so output weight h + deg = 7-1=6.
    # For the T-output (h=2): deg=4. So <T|m₃(T,T,W)> is a
    # degree-4 polynomial in (λ₁,λ₂). This IS nonzero generically.
    # But the SHADOW coefficient uses the contraction with η,
    # so Sh₃(a,b) gets a contribution from a²b·<T|m₃(T,T,W)>.
    # This has the form a²b·(polynomial), which is ODD in b.
    # By Z₂ (W→-W): <T|m₃(T,T,W)> must be zero? Not necessarily,
    # because W → -W sends m₃(T,T,W) → -m₃(T,T,W), but <T|·> is
    # even in W. So <T|m₃(T,T,W)> → <T|-m₃(T,T,W)> = -<T|m₃(T,T,W)>.
    # But <T| doesn't change sign. So <T|m₃(T,T,W)> → -<T|m₃(T,T,W)>.
    # This means <T|m₃(T,T,W)> IS zero by Z₂? No — Z₂ says the
    # ALGEBRA has a symmetry W→-W, which means the OPE/operations
    # respect this symmetry. So m₃(T,T,W) → -m₃(T,T,W), and
    # <T|m₃(T,T,W)> → -<T|m₃(T,T,W)>. Since this must equal itself
    # (it's a fixed quantity), we get <T|m₃(T,T,W)> = 0.

    # Wait, that's wrong. The Z₂ says: the algebra has an automorphism
    # W↦-W, T↦T. Under this, m₃(T,T,W) ↦ m₃(T,T,-W) = -m₃(T,T,W).
    # And the output is in the algebra, which transforms. So the T-component
    # of m₃(T,T,W) maps to the T-component of -m₃(T,T,W) = negative of
    # T-component. But also, under the automorphism, the T-component maps
    # to itself. So T-component of m₃(T,T,W) = -T-component. Hence = 0.
    # Similarly, W-component of m₃(T,T,W) maps to -W-component under
    # the automorphism, but also maps to +W-component (since W↦-W in
    # the output). So W-component of m₃(T,T,W) = +W-component. OK so
    # the W-component of m₃(T,T,W) is not forced to vanish.

    # But for Sh₃: <η|m₃(η,η,η)> with η = aT + bW:
    # = sum over all input types · sum over output types.
    # The Z₂-odd terms (odd total number of W) give zero.
    # Total W-count = (number of W in 3 inputs) + (W in output via <W|·>).
    # Sh₃ has terms:
    #   a³<T|m₃(T,T,T)>     [0 W's total: even] → SURVIVES (= Virasoro S₃)
    #   a³<W|m₃(T,T,T)>     [1 W total: odd] → 0
    #   a²b<T|m₃(T,T,W)>    [1 W total: odd] → 0
    #   a²b<W|m₃(T,T,W)>    [2 W total: even] → SURVIVES
    #   ab²<T|m₃(T,W,W)>    [2 W total: even] → SURVIVES
    #   ab²<W|m₃(T,W,W)>    [3 W total: odd] → 0
    #   b³<T|m₃(W,W,W)>     [3 W total: odd] → 0
    #   b³<W|m₃(W,W,W)>     [4 W total: even] → SURVIVES
    # But ALSO we need to sum over permutations of inputs (since
    # the shadow is the FULL trace, not the ordered one).

    # So Sh₃(a,b) = a³·S₃^{TTT→T} + a²b·S₃^{TTW→W} + ab²·S₃^{TWW→T} + b³·S₃^{WWW→W}

    # This means Sh₃ has ALL four terms (not just the Z₂-even ones
    # in the restricted sense I was using). Let me reconsider.

    # Sh₃(a,b) is a degree-3 polynomial. The Z₂ acts as (a,b) → (a,-b).
    # For Sh₃ to be invariant: Sh₃(a,-b) = Sh₃(a,b).
    # a³ → a³ ✓, a²b → -a²b ✗, ab² → ab² ✓, b³ → -b³ ✗.
    # So the Z₂-invariant terms are a³ and ab².

    # BUT WAIT: Sh₃(a,b) = <aT+bW | m₃(aT+bW, aT+bW, aT+bW)>.
    # Under W→-W: (aT+bW) → (aT-bW), so η → η̄.
    # m₃(η̄,η̄,η̄) = m₃(aT-bW,aT-bW,aT-bW)
    # and <η̄|m₃(η̄,η̄,η̄)> should equal <η|m₃(η,η,η)> by the automorphism.
    # Under b→-b: Sh₃(a,-b) = Sh₃(a,b) iff the W₃ algebra has the Z₂ symmetry.
    # Since W₃ DOES have W→-W as an automorphism (preserving T):
    # Sh₃(a,-b) = Sh₃(a,b). ✓

    # So Sh₃(a,b) = A₃·a³ + B₃·ab²
    # with A₃ = Virasoro S₃ · (something) and B₃ = S₃^{TWW→T} + permutations.

    # For Virasoro: Sh₃ = 2·a³ on the T-line. So A₃ = 2 (from the
    # rosetta stone: S₃ = 2 for Virasoro, meaning the trace <T|m₃(T,T,T)>
    # evaluated at unit spectral parameters gives 2·x_T³... I need to
    # be more precise about the normalization.)

    # Actually from the rosetta stone:
    # S₃ = 2 for Virasoro means Sh₃ = S₃·x_T³ = 2x_T³? Or is there
    # a different convention? The rosetta stone table has S_r values
    # without the x_T factors.

    # I think the convention is: Sh_r(x) = S_r · x^r, where x is the
    # single deformation variable on the T-line. So Sh₃^{T-line} = 2·x_T³.

    # For the full W₃: Sh₃(x_T, x_W) = A₃·x_T³ + B₃·x_T·x_W²

    # To determine B₃ = S₃^{TWW}, I need the scalar trace of
    # m₃(T,W,W) + permutations. This comes from the W₃ computation.

    # From w-algebras-w3.tex eq:m3-WWW, the W-sector output of m₃(W,W,W):
    # the scalar part vanishes (by weight conservation, scalar needs deg=6
    # but m₃ has 2 spectral params with max degree 4+1=5 from {W_λW}).
    # So S₃^{WWW→W} = 0 (on cohomology).

    # The term S₃^{TTW→W}: m₃(T,T,W)|_{W-output} needs output W (h=3)
    # and deg = 6-3=3. The Virasoro m₃(T,T,T)|_T gives h=2, deg=4.
    # m₃(T,T,W) comes from {T_λ{T_μ W}} - {{T_λ T}_{λ+μ} W}.
    # = {T_λ(∂W+3μW)} - {(∂T+2λT+c/12 λ³)_{λ+μ} W}
    # First: {T_λ ∂W} = (λ+∂){T_λ W} = (λ+∂)(∂W+3λW) = ...
    # This is getting complex. Let me use the numerical code instead.

    print(f"\n  Sh₃(x_T, x_W) = 2·x_T³ + B₃·x_T·x_W²")
    print(f"  (B₃ to be determined from m₃(T,W,W) and m₃(W,W,T) traces)")
    print(f"\n  Need to compute B₃ = S₃^TWW numerically using w3_quartic_contact.py")

    return None


# ===================================================================
# Section 5: Compute S₃^TWW numerically
# ===================================================================

def compute_S3_TWW():
    """Compute S₃^{TWW} from the m₃ computation.

    m₃(T,W,W; λ₁,λ₂) is computed from
      {T_{λ₁} {W_{λ₂} W}} - {{T_{λ₁} W}_{λ₁+λ₂} W}

    The shadow coefficient S₃^{TWW→T} is the trace
    <T| m₃(T,W,W)> normalized by the Shapovalov norm <T|T> = c/2.

    Similarly S₃^{WTW→T} and S₃^{WWT→T} from permutations.
    And S₃^{TTW→W} etc.

    For the shadow on the (x_T, x_W) plane, we need:
    Sh₃(a,b) = sum over (i,j,k)∈{T,W}³, o∈{T,W}:
      a^(#T in i,j,k) · b^(#W in i,j,k) · a^(δ_{o=T}) · b^(δ_{o=W})
      · <o| m₃(i,j,k) |>  / <o|o>

    Wait, let me think about this more carefully. The shadow at arity r is
    Sh_r(η) = <η| m_r(η, ..., η)>  (cyclic trace)
    where <·|·> is the Shapovalov form and η = x_T T + x_W W.

    <η| = x_T <T| + x_W <W|
    m_r(η,...,η) = sum over all {T,W}^r choices of inputs
    So Sh_3(x_T,x_W) = sum_{i,j,k ∈ {T,W}} x_i x_j x_k ·
                        sum_{o ∈ {T,W}} x_o · <o| m₃(i,j,k)>

    Wait no — Sh_3 should be degree 3 (not 4). The cyclic trace is:
    Sh_3(η) = <η, m_3(η,η,η)> — but this has 4 factors of η (one from
    the pairing, three from the inputs). That gives degree 4.

    Hmm, this doesn't match the Virasoro case where Sh_3 = 2x_T³.
    Unless the pairing absorbs one factor differently.

    Let me reconsider. In the bar complex framework:
    - m_r: A^⊗r → A is the r-ary operation
    - The SCALAR shadow S_r = <unit| m_r(η,...,η)> doesn't work because
      we need a specific pairing.
    - Actually the shadow coefficient in the manuscript (rosetta_stone.tex)
      is the SCALAR PART of m_r, normalized. So:
      S_r = m_r(η,...,η)|_{scalar} / (appropriate normalization)

    For Virasoro: m_3(T,T,T) = ∂²T + ...·∂T·λ + ...·T·λ² + (c/12)λ³ + ...
    The SCALAR part is the coefficient proportional to the identity (1),
    which at arity 3 in Virasoro is the λ³ term: (c/12)·λ₁²λ₂ + ...
    The shadow coefficient S₃ = 2 captures the normalized coupling.

    Actually wait — from the rosetta stone table:
      S₂ = c/2, S₃ = 2, S₄ = 10/(c(5c+22))
    And the shadow generating function H(t) = ct² + 6t³ + ...
    with h_r = r · S_r. So h₂ = c, h₃ = 6.

    This means H(t) is NOT directly related to the scalar part of m_r.
    Rather, the shadow metric is built from the data (κ, {S_r}).

    OK, I think I need to step back and use the EXPLICIT formulas.
    The shadow metric for Virasoro is:
      Q(t) = c² + 12ct + [(180c+872)/(5c+22)]t²
    encoding κ = c/2, the cubic "strength" 6 (related to S₃=2),
    and the quartic contact S₄ = 10/(c(5c+22)).

    For W₃, the shadow metric is a polynomial in (x_T, x_W) (with
    a formal variable t parametrizing the line). Let me just compute
    the W-line and cross-section numerically.
    """
    from compute.w3_quartic_contact import (
        m3_compute, bracket_base, bracket_extended,
        bracket_right_extended, c_sym,
    )
    from sympy import Symbol

    lam = Symbol('lam')

    # m₃(T,W,W; l1, l2): compute and extract scalar
    l1, l2 = symbols('l1 l2')

    print("\n" + "=" * 72)
    print("COMPUTING S₃^{TWW} FROM λ-BRACKETS")
    print("=" * 72)

    # m₃(T,W,W; l1, l2) from Stasheff:
    # = -[{T_{l1} {W_{l2} W}} - {{T_{l1} W}_{l1+l2} W}]
    m3_TWW = m3_compute('T', 'W', 'W', l1, l2)
    print(f"\n  m₃(T,W,W; l1,l2) = {expand(m3_TWW)}")

    # m₃(W,T,W; l1, l2)
    m3_WTW = m3_compute('W', 'T', 'W', l1, l2)
    print(f"  m₃(W,T,W; l1,l2) = {expand(m3_WTW)}")

    # m₃(W,W,T; l1, l2)
    m3_WWT = m3_compute('W', 'W', 'T', l1, l2)
    print(f"  m₃(W,W,T; l1,l2) = {expand(m3_WWT)}")

    # m₃(T,T,W; l1, l2)
    m3_TTW = m3_compute('T', 'T', 'W', l1, l2)
    print(f"  m₃(T,T,W; l1,l2) = {expand(m3_TTW)}")

    return m3_TWW, m3_WTW, m3_WWT, m3_TTW


# ===================================================================
# Section 6: W-line shadow coefficients S_{2r}^W for r=1,...,5
# ===================================================================

def w_line_shadow_from_stasheff(n_max=10):
    """Compute W-line shadow coefficients by explicit Stasheff recursion.

    On the W-line (x_T = 0), only W-inputs. By Z₂, only even arities.
    The shadow coefficient at arity 2r is determined recursively by the
    A∞ relations.

    For this computation, the "shadow coefficient" S_{2r}^W is defined as:
      S_{2r}^W = (scalar part of m_{2r}(W,...,W)) / normalization
    where the scalar part means the c-dependent coefficient.
    """
    print("\n" + "=" * 72)
    print("W-LINE SHADOW: ALGEBRAIC APPROACH")
    print("=" * 72)

    # For the W-line, we use the fact that the shadow metric
    # Q_W(u) (with u = s²) is determined by the data:
    #   Sh_2^W = c/3 = κ_W
    #   Sh_4^W = Q_WWWW = 10240/(c(5c+22)³)

    kW = c / 3
    Q_WWWW = Rational(10240, 1) / (c * (5*c + 22)**3)

    # If the shadow metric Q_W(u) is degree 2 in u, then:
    # Q_W(u) = q₀ + q₁u + q₂u²
    # with q₀ = kW² = c²/9

    # H_W(s) = s²√Q_W(s²) means
    # [s²]H_W = kW = c/3 ↔ √q₀ = c/3 ✓
    # [s⁴]H_W = Q_WWWW ↔ q₁/(2√q₀) = q₁/(2c/3) = 3q₁/(2c) = Q_WWWW
    # So q₁ = 2c·Q_WWWW/3 = 20480/(3(5c+22)³)

    # For degree 2, we need q₂. This comes from Sh_6^W.
    # But if we ASSUME degree 2, then ALL higher Sh_{2r}^W are determined.

    # Let's see: the binomial expansion of √(q₀ + q₁u + q₂u²):
    # = √q₀ · √(1 + (q₁/q₀)u + (q₂/q₀)u²)
    # Let p = q₁/q₀, q = q₂/q₀.
    # √(1+pu+qu²) = 1 + pu/2 + (q/2 - p²/8)u² + ...

    q0 = c**2 / 9
    q1 = 2*c*Q_WWWW/3
    q1_simp = cancel(q1)

    print(f"  q₀ = c²/9")
    print(f"  q₁ = {q1_simp} = 20480/(3(5c+22)³)")

    # Compute discriminant of Q_W:
    # If Q_W(u) = q₀ + q₁u, then disc = -4q₀ · 0 + q₁² ... no.
    # For linear Q_W: Q_W = q₀ + q₁u. The zero is at u₀ = -q₀/q₁.
    # For the generating function, the convergence radius is |u₀|.
    u0 = -q0/q1
    u0_simp = cancel(u0)
    print(f"\n  Branch point (linear Q_W): u₀ = -q₀/q₁ = {u0_simp}")
    # = -(c²/9) / (20480/(3(5c+22)³))
    # = -c²/9 · 3(5c+22)³/20480
    # = -c²(5c+22)³/(3·20480)
    # = -c²(5c+22)³/61440
    print(f"  = -c²(5c+22)³/61440")

    # Now expand √Q_W = √(q₀(1 + (q₁/q₀)u)) = (c/3)√(1+γu) with γ = q₁/q₀
    gamma = cancel(q1/q0)
    print(f"\n  γ = q₁/q₀ = {gamma}")
    # = 20480/(3(5c+22)³) / (c²/9) = 20480·9/(3c²(5c+22)³) = 61440/(c²(5c+22)³)
    gamma_val = Rational(61440, 1) / (c**2 * (5*c+22)**3)
    print(f"  = 61440/(c²(5c+22)³)")

    print(f"\n  √Q_W(u) = (c/3)·√(1 + γu)")
    print(f"  = (c/3)·Σ binom(1/2, n) (γu)^n")
    print("\n  H_W(s) = s^2 sqrt(Q_W(s^2)) = (c/3) s^2 sum binom(1/2,n) gamma^n s^(2n)")
    print(f"\n  Shadow coefficients on W-line:")
    print(f"  Sh_{2r}^W = (c/3)·binom(1/2, r-1)·γ^{r-1}")
    print(f"  S_{2r}^W = Sh_{2r}^W / (2r)")

    # Compute S_{2r}^W for r = 1,...,5
    results = {}
    for r in range(1, n_max+1):
        n = r - 1
        # binom(1/2, n) = (1/2)(1/2-1)...(1/2-n+1)/n!
        # = (1/2)(-1/2)(-3/2)...((3-2n)/2) / n!
        # = (-1)^{n-1} · (2n-2)! / (2^{2n-1} · n! · (n-1)!)  for n ≥ 1
        # = (-1)^{n-1} / (2^{2n-1}) · C_{n-1}  [Catalan-like]
        if n == 0:
            bcoeff = Rational(1, 1)
        else:
            bcoeff = Rational(1, 1)
            for j in range(n):
                bcoeff *= (Rational(1, 2) - j)
            from math import factorial as mfac
            bcoeff /= mfac(n)

        Sh_2r = (c/3) * bcoeff * gamma_val**n
        S_2r = Sh_2r / (2*r)

        Sh_2r_simp = cancel(Sh_2r)
        S_2r_simp = cancel(S_2r)
        results[2*r] = S_2r_simp

        print(f"\n  r={r}: binom(1/2,{n}) = {bcoeff}")
        print(f"    Sh_{2*r}^W = {Sh_2r_simp}")
        print(f"    S_{2*r}^W  = {S_2r_simp}")
        print(f"    S_{2*r}^W  = {factor(S_2r_simp)}")

    return results


# ===================================================================
# Section 7: Complementarity under c → 100-c
# ===================================================================

def complementarity_check(results):
    """Verify complementarity of W-line shadow under c → 100-c."""
    print("\n" + "=" * 72)
    print("COMPLEMENTARITY: c → 100-c")
    print("=" * 72)

    c_dual = 100 - c

    for r_val, S_r in sorted(results.items()):
        if r_val < 4:
            continue
        S_r_dual = S_r.subs(c, c_dual)
        S_sum = cancel(S_r + S_r_dual)
        print(f"\n  S_{r_val}^W(c) = {S_r}")
        print(f"  S_{r_val}^W(100-c) = {cancel(S_r_dual)}")
        print(f"  Sum = {S_sum}")
        # Check if sum is independent of c
        S_sum_poly = Poly(together(S_sum), c)
        print(f"  Sum is constant in c: {S_sum_poly.degree() == 0 if S_sum_poly.degree() >= 0 else 'N/A'}")


# ===================================================================
# Section 8: Cross-section shadow and degree-4 metric
# ===================================================================

def cross_shadow_metric():
    """Analyze the shadow metric on a general ray (cos θ, sin θ).

    On the ray x_T = α, x_W = β:
      Sh_2(α,β) = (c/2)α² + (c/3)β²
      Sh_3(α,β) = 2α³ + B₃αβ²
      Sh_4(α,β) = Q_TTTT α⁴ + Q_TTWW α²β² + Q_WWWW β⁴

    Q_line(t) = Sh_2² + 2·Sh_2·Sh_3·t + (Sh_3² + 2·Sh_2·Sh_4)t²
    This is at most degree 2 in t if Q_line has no higher terms.
    The degree-3 coefficient would be 2·Sh_3·Sh_4 + 2·Sh_2·Sh_5,
    and for Q to be exactly degree 2, we need Sh_5 = -Sh_3·Sh_4/Sh_2.
    """
    print("\n" + "=" * 72)
    print("CROSS-SECTION ANALYSIS: GENERAL RAY")
    print("=" * 72)

    a, b = symbols('a b', real=True)

    Sh2 = (c/2)*a**2 + (c/3)*b**2
    Sh3 = 2*a**3  # + B₃ a b²  (B₃ to be determined)
    Q_TTTT = Rational(10, 1) / (c * (5*c + 22))
    Q_TTWW = Rational(1920, 1) / (c * (5*c + 22)**2)
    Q_WWWW = Rational(10240, 1) / (c * (5*c + 22)**3)
    Sh4 = Q_TTTT * a**4 + Q_TTWW * a**2 * b**2 + Q_WWWW * b**4

    # Q_line(t) = Sh₂² + 2Sh₂Sh₃ t + (Sh₃² + 2Sh₂Sh₄) t²
    Q0 = expand(Sh2**2)
    Q1 = expand(2*Sh2*Sh3)
    Q2 = expand(Sh3**2 + 2*Sh2*Sh4)

    print(f"\n  Q_line(t) = Q₀ + Q₁t + Q₂t²")
    print(f"  Q₀ = Sh₂² = {Q0}")
    print(f"  Q₁ = 2Sh₂Sh₃ = {Q1}")
    print(f"  Q₂ = Sh₃² + 2Sh₂Sh₄ = {Q2}")

    # On T-line (b=0):
    Q2_T = Q2.subs(b, 0)
    print(f"\n  On T-line (b=0):")
    print(f"    Q₂^T = {expand(Q2_T)}")
    Q2_T_canonical = cancel(Q2_T / a**4)
    print(f"    Q₂^T / a⁴ = {Q2_T_canonical}")
    # Should be (180c+872)/(5c+22):
    # 4 + 2·(c/2)·10/(c(5c+22)) · a⁴ / a⁴ ... wait let me compute properly
    # Sh₃² = 4a⁶, 2Sh₂Sh₄ = 2·(c/2)a²·Q_TTTT·a⁴ = c·Q_TTTT·a⁶
    # Q₂^T = (4 + c·10/(c(5c+22)))a⁶ = (4 + 10/(5c+22))a⁶
    # = (4(5c+22)+10)/(5c+22) · a⁶ = (20c+88+10)/(5c+22) · a⁶
    # = (20c+98)/(5c+22) · a⁶
    # Hmm, but Q₀^T = (c/2)²·a⁴ = c²a⁴/4, Q₁^T = 2·(c/2)a²·2a³ = 2ca⁵.
    # Then Q_line^T = (c²/4)a⁴ + 2c·a⁵·t + (20c+98)/(5c+22)·a⁶·t²
    # For comparison with Q_Vir: set a=1 (unit T-line):
    # Q_line(t) = c²/4 + 2ct + (20c+98)/(5c+22)·t²
    # But Q_Vir = c² + 12ct + (180c+872)/(5c+22)·t².
    # These DON'T MATCH. Factor of 4 off in Q₀.
    # The issue: Sh₂ = (c/2)x_T², so on the T-line with x_T = 1 (not t),
    # Sh₂ = c/2. Then H(t) = (c/2)·t² + 2·t³ + S₄·t⁴ + ...
    # But the Virasoro H(t) = c·t² + 6·t³ + ....
    # So there's a factor of 2 discrepancy: h₂^{Vir} = 2·Sh₂ = 2·(c/2) = c.
    # And h₃^{Vir} = 3·Sh₃ = 3·2 = 6.

    # AH — I see. The convention is: S_r = Sh_r / r,
    # and h_r = r·S_r = Sh_r. So h_r = Sh_r.
    # And H(t) = Σ h_r t^r = Σ Sh_r t^r.
    # For Virasoro: H(t) = ct² + 6t³ + ..., so Sh_2 = c, Sh_3 = 6.
    # But S_2 = c/2, S_3 = 2.
    # And Sh₂ = 2·S₂ = 2·(c/2) = c ✓, Sh₃ = 3·S₃ = 3·2 = 6 ✓.

    # So Sh_r = r · S_r. In the rosetta_stone, the table gives S_r values.
    # The quartic shadow Sh₄ = 4·S₄ = 4·10/(c(5c+22)) = 40/(c(5c+22)).

    # For W₃: Sh₄(x_T, x_W) as in the rosetta_stone eq:w3-quartic
    # is already the Sh₄ (= 4·S₄). Let me check:
    # The rosetta stone says Sh₄ = [10/(c(5c+22))]x_T⁴ + ...
    # But the Virasoro quartic contact is S₄ = 10/(c(5c+22)),
    # and Sh₄^{Vir} = 4·S₄ = 40/(c(5c+22)).
    # On the T-line of W₃: Sh₄(x_T,0) = [10/(c(5c+22))]x_T⁴.
    # But Sh₄^{Vir} = 40/(c(5c+22))·t⁴ (with t = x_T).
    # These DON'T match: 10 vs 40.

    # Hmm, maybe the rosetta_stone eq:w3-quartic gives S₄ not Sh₄?
    # If S₄^{TTTT} = 10/(c(5c+22)), then Sh₄^{TTTT} = 4·10/(c(5c+22)) = 40/(c(5c+22)).
    # That would match Virasoro. And the rosetta_stone labels it "Sh₄",
    # but the coefficient is S₄ (= Sh₄/4 × x^4 ... confusing).

    # Looking at the rosetta_stone eq:w3-quartic more carefully:
    # \operatorname{Sh}_4(x_T, x_W) = [10/(c(5c+22))]x_T^4 + [1920/(c(5c+22)²)]x_T²x_W² + [10240/(c(5c+22)³)]x_W^4
    # And for Virasoro: S₄ = 10/(c(5c+22)) from the S_r table.
    # So Sh₄^{Vir} = Sh₄(1,0) = 10/(c(5c+22)).
    # But from the 3d_gravity.tex: [t⁴]H = 40/(c(5c+22)), and S₄ = 10/(c(5c+22)).
    # So [t⁴]H = Sh₄ if H(t) = Σ Sh_r t^r? Then [t⁴]H = h₄ = 40/(c(5c+22)).
    # And S₄ = h₄/4 = 10/(c(5c+22)). And Sh₄ = S₄ (NOT h₄ = Sh₄).

    # I think the rosetta_stone equation labels it "Sh" but means S.
    # Because Sh₄(1,0) = 10/(c(5c+22)) = S₄^{Vir}.
    # In any case, for the shadow generating function:
    # H(t) = Σ h_r t^r = Σ r·S_r·t^r.
    # On the T-line: h_2 = 2·S_2 = 2·(c/2) = c.
    #               h_3 = 3·S_3 = 3·2 = 6.
    #               h_4 = 4·S_4 = 4·10/(c(5c+22)) = 40/(c(5c+22)).

    # For the W-line: the Sh/S convention should be the same.
    # S₂^W = c/3 (Hessian). So h₂^W = 2·(c/3) = 2c/3.
    # S₄^W = Q_WWWW = 10240/(c(5c+22)³). So h₄^W = 4·10240/(c(5c+22)³) = 40960/(c(5c+22)³).

    # And H_W(s) = (2c/3)s² + [40960/(c(5c+22)³)]s⁴ + ...
    # = s²·[(2c/3) + 40960/(c(5c+22)³)·s² + ...]
    # H_W = s² √Q_W
    # √Q_W = 2c/3 + 40960/(c(5c+22)³)·s² + ...
    # Q_W = (2c/3)² + 2·(2c/3)·40960/(c(5c+22)³)·s² + ...
    # = 4c²/9 + 163840/(3(5c+22)³)·s² + ...

    # Hmm, let me just be very precise and follow the 3d_gravity.tex conventions.
    # There: H(t) = ct² + 6t³ + [40/(c(5c+22))]t⁴ + ...
    # and Q(t) = c² + 12ct + [(180c+872)/(5c+22)]t².
    # H = t²√Q. So √Q(0) = c (not c/2), and the leading H coeff is c.

    # This means: for the Virasoro T-line,
    # h_2 = c = √Q(0), not κ = c/2.
    # The relationship: h_2 = √q₀ where q₀ is Q(0).
    # From Q = c² + ..., q₀ = c², √q₀ = c. ✓

    # For the W-line: q₀^W = (√something)²
    # h_2^W = ?, where the leading term of H_W is h_2^W · s².
    # From S₂^W = c/3 (Hessian) and the convention h_r = r·S_r:
    # h_2^W = 2·(c/3) = 2c/3.
    # So q₀^W = (2c/3)² = 4c²/9.

    # And from S₄^W: h_4^W = 4·S₄^W. What is S₄^W?
    # From the rosetta_stone: Sh₄(0,s) = [10240/(c(5c+22)³)]s⁴.
    # This is the "Sh₄" which in the rosetta convention equals S₄·s⁴.
    # So S₄^W = 10240/(c(5c+22)³) and h₄^W = 4·10240/(c(5c+22)³) = 40960/(c(5c+22)³).

    # Then Q_W(u) = (2c/3)² + 2·(2c/3)·h₄^W·u + ... (at linear order)
    # Wait: H_W²/s⁴ = Q_W(s²).
    # H_W = (2c/3)s² + h₄^W s⁴ + h₆^W s⁶ + ...
    # H_W/s² = 2c/3 + h₄^W s² + h₆^W s⁴ + ...
    # (H_W/s²)² = Q_W(s²) = 4c²/9 + 2·(2c/3)·h₄^W·s² + (h₄^W² + 2·(2c/3)·h₆^W)s⁴ + ...

    # So q₁ = 2·(2c/3)·h₄^W = 4c·h₄^W/3 = 4c·40960/(3c(5c+22)³) = 163840/(3(5c+22)³).

    print(f"\n  CORRECTED with h_r = r·S_r convention:")
    print(f"  On T-line: h₂ = c, h₃ = 6, h₄ = 40/(c(5c+22))")
    print(f"  Q_Vir = c² + 12ct + [(180c+872)/(5c+22)]t²")
    print(f"\n  On W-line: h₂^W = 2c/3, h₃^W = 0, h₄^W = 40960/(c(5c+22)³)")
    print(f"  Q_W(u) = 4c²/9 + [163840/(3(5c+22)³)]u + q₂^W·u²")
    print(f"  (u = s², q₂^W determined by Sh₆^W if Q_W is degree 2)")


# ===================================================================
# Main computation
# ===================================================================

def main():
    """Run all W₃ shadow computations."""
    print("=" * 72)
    print("W₃ SHADOW COEFFICIENT FORMULA: THE MULTIVARIABLE CATALAN ANALOGUE")
    print("=" * 72)

    # Section 0: Virasoro review
    vir_coeffs = virasoro_shadow_coefficients(n_max=10)

    # Section 1: W₃ quartic
    Q_TTTT, Q_TTWW, Q_WWWW = w3_quartic_shadow()

    # Section 2: Shadow metric structure
    w3_shadow_metric()

    # Section 5: Compute S₃^TWW
    # compute_S3_TWW()  # requires w3_quartic_contact imports

    # Section 6: W-line shadow
    w_results = w_line_shadow_from_stasheff(n_max=5)

    # Section 7: Complementarity
    complementarity_check(w_results)

    # Section 8: Cross-section
    cross_shadow_metric()


if __name__ == '__main__':
    main()
