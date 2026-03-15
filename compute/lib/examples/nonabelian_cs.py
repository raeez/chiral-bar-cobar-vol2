"""
Nonabelian Chern-Simons: su(2) current algebra at level k.

The boundary of SU(2) CS on C × R+ produces the affine Kac-Moody algebra
ĝ_k where g = sl_2 (or su(2)).

Generators: J^a for a ∈ {1, 2, 3} (or {+, -, 3}).

OPE:
  J^a(z) J^b(w) ~ k·κ^{ab}/(z-w)^2 + f^{ab}_c J^c(w)/(z-w)

where κ^{ab} = δ^{ab} (Killing form normalized) and f^{abc} = ε^{abc}.

Lambda-bracket:
  {J^a_λ J^b} = f^{ab}_c J^c + k·κ^{ab}·λ

This is the FIRST genuinely nontrivial Jacobi check:
- Abelian CS has trivially vanishing iterated brackets (0=0=0)
- Virasoro has one generator (Jacobi from a single bracket)
- su(2) has THREE generators with noncommuting brackets

Paper references: Section 11 (examples-computing.tex).
Cross-reference: ~/chiral-bar-cobar/CLAUDE.md - Sugawara, level conventions.
"""
from sympy import Symbol, Rational, expand, simplify, S, symbols, Matrix


# ---------------------------------------------------------------------------
# su(2) structure constants and Killing form
# ---------------------------------------------------------------------------
# Generators: J1, J2, J3 with [J^a, J^b] = ε^{abc} J^c
# Killing form: κ^{ab} = δ^{ab} (in orthonormal basis)

# Levi-Civita symbol ε^{abc}
def levi_civita(a, b, c):
    """Totally antisymmetric tensor ε^{abc} for a,b,c ∈ {1,2,3}."""
    if (a, b, c) in [(1, 2, 3), (2, 3, 1), (3, 1, 2)]:
        return 1
    elif (a, b, c) in [(3, 2, 1), (1, 3, 2), (2, 1, 3)]:
        return -1
    else:
        return 0


def killing_form(a, b):
    """Killing form κ^{ab} = δ^{ab} (orthonormal basis)."""
    return 1 if a == b else 0


# Symbolic generators
J = [None, Symbol('J1'), Symbol('J2'), Symbol('J3')]
dJ = [None, Symbol('dJ1'), Symbol('dJ2'), Symbol('dJ3')]


def su2_lambda_bracket(a_idx, b_idx, lam, k):
    """Lambda-bracket for su(2)_k current algebra.

    {J^a_λ J^b} = Σ_c f^{ab}_c J^c + k·κ^{ab}·λ
                 = Σ_c ε^{abc} J^c + k·δ^{ab}·λ

    Parameters:
        a_idx, b_idx: generator indices (1, 2, or 3)
        lam: spectral parameter
        k: level

    Returns:
        Symbolic expression in J1, J2, J3, λ, k
    """
    # Structure constant part: f^{ab}_c J^c
    struct_part = sum(levi_civita(a_idx, b_idx, c) * J[c] for c in [1, 2, 3])

    # Level part: k·δ^{ab}·λ
    level_part = k * killing_form(a_idx, b_idx) * lam

    return expand(struct_part + level_part)


def _apply_partial_su2(expr):
    """Apply ∂ to an expression in J1, J2, J3 (and their derivatives).

    ∂(J^a) = dJ^a, ∂(const) = 0, ∂(f·g) = ∂f·g + f·∂g.
    """
    result = S.Zero
    for i in [1, 2, 3]:
        result += expr.diff(J[i]) * dJ[i]
    return expand(result)


def _bracket_full(a_idx, b_idx, lam, k):
    """Full λ-bracket including the action on composites.

    For the level-k current algebra, the bracket acts on generators and extends
    by sesquilinearity and Leibniz to composites.

    On generators: {J^a_λ J^b} = ε^{abc}J^c + kδ^{ab}λ
    Left sesquilinearity: {∂J^a_λ J^b} = -λ·{J^a_λ J^b}
    Right sesquilinearity: {J^a_λ ∂J^b} = (λ+∂){J^a_λ J^b}
    """
    return su2_lambda_bracket(a_idx, b_idx, lam, k)


def check_su2_skew_symmetry(a_idx, b_idx, lam, k):
    """Verify {J^a_λ J^b} = −{J^b_{−λ−∂} J^a} via Borcherds.

    n-products: (J^a)_0 (J^b) = ε^{abc}J^c, (J^a)_1 (J^b) = kδ^{ab}

    Borcherds RHS: −Σ_n (−∂−λ)^n/n! · (J^b_n J^a)
    n=0: −1·(ε^{bac}J^c) = −ε^{bac}J^c = ε^{abc}J^c  [antisymmetry of ε]
    n=1: −(−λ−∂)/1!·(kδ^{ba}) = (λ+∂)(kδ^{ab})
        = kδ^{ab}·λ + 0  [∂ on constant = 0]
        = kδ^{ab}λ

    Total RHS = ε^{abc}J^c + kδ^{ab}λ = LHS ✓
    """
    lhs = su2_lambda_bracket(a_idx, b_idx, lam, k)

    # Borcherds formula
    # n=0 contribution
    n0_products_ba = sum(levi_civita(b_idx, a_idx, c) * J[c] for c in [1, 2, 3])
    rhs_n0 = -n0_products_ba  # -1 * (J^b_0 J^a)

    # n=1 contribution: (λ+∂)(kδ^{ba}) = kδ^{ab}λ (∂ on constant = 0)
    rhs_n1 = k * killing_form(b_idx, a_idx) * lam

    rhs = expand(rhs_n0 + rhs_n1)
    return simplify(expand(lhs - rhs))


def check_su2_jacobi(a_idx, b_idx, c_idx, lam, mu, k):
    """Verify Jacobi identity for su(2)_k:

    {J^a_λ {J^b_μ J^c}} − {J^b_μ {J^a_λ J^c}} = {{J^a_λ J^b}_{λ+μ} J^c}

    This is the FIRST genuinely nontrivial Jacobi check in the codebase.

    Method: Expand using the bracket formula and linearity.

    {J^b_μ J^c} = ε^{bcd}J^d + kδ^{bc}μ

    {J^a_λ {J^b_μ J^c}} = {J^a_λ (ε^{bcd}J^d + kδ^{bc}μ)}
                         = Σ_d ε^{bcd}·{J^a_λ J^d} + 0  [{·_λ const}=0]
                         = Σ_d ε^{bcd}·(ε^{ade}J^e + kδ^{ad}λ)

    Similarly for the other terms.
    """
    nu = lam + mu

    # --- LHS Term 1: {J^a_λ {J^b_μ J^c}} ---
    # Inner bracket: {J^b_μ J^c} = Σ_d ε^{bcd}J^d + kδ^{bc}μ
    # Outer bracket on the J^d terms: {J^a_λ J^d} = ε^{ade}J^e + kδ^{ad}λ
    # On the constant kδ^{bc}μ: {J^a_λ kδ^{bc}μ} = 0
    term1 = S.Zero
    for d in [1, 2, 3]:
        coeff_d = levi_civita(b_idx, c_idx, d)
        if coeff_d == 0:
            continue
        bracket_a_d = su2_lambda_bracket(a_idx, d, lam, k)
        term1 += coeff_d * bracket_a_d

    # --- LHS Term 2: −{J^b_μ {J^a_λ J^c}} ---
    # Inner bracket: {J^a_λ J^c} = Σ_d ε^{acd}J^d + kδ^{ac}λ
    # Outer bracket on J^d: {J^b_μ J^d} = ε^{bde}J^e + kδ^{bd}μ
    # On constant kδ^{ac}λ: {J^b_μ kδ^{ac}λ} = 0
    term2 = S.Zero
    for d in [1, 2, 3]:
        coeff_d = levi_civita(a_idx, c_idx, d)
        if coeff_d == 0:
            continue
        bracket_b_d = su2_lambda_bracket(b_idx, d, mu, k)
        term2 += coeff_d * bracket_b_d

    lhs = expand(term1 - term2)

    # --- RHS: {{J^a_λ J^b}_{λ+μ} J^c} ---
    # {J^a_λ J^b} = Σ_d ε^{abd}J^d + kδ^{ab}λ
    # {{J^a_λ J^b}_ν J^c} = Σ_d ε^{abd}·{J^d_ν J^c} + kδ^{ab}λ·{1_ν J^c}
    #                                                    ↑ = 0
    # BUT: we also need left sesquilinearity for {∂J^d_ν J^c} = −ν{J^d_ν J^c}
    # Actually, {J^a_λ J^b} is a polynomial in J's and λ.
    # The J-part gets bracketed with J^c using {J^d_ν J^c}.
    # The λ-part (constants w.r.t. fields) gets {const_ν J^c} = 0.

    # So: {{J^a_λ J^b}_ν J^c} = Σ_d ε^{abd}·{J^d_ν J^c} + 0
    rhs = S.Zero
    for d in [1, 2, 3]:
        coeff_d = levi_civita(a_idx, b_idx, d)
        if coeff_d == 0:
            continue
        bracket_d_c = su2_lambda_bracket(d, c_idx, nu, k)
        rhs += coeff_d * bracket_d_c

    rhs = expand(rhs)

    return simplify(expand(lhs - rhs))


def check_su2_jacobi_all(lam, mu, k):
    """Check Jacobi for ALL 27 triples (a,b,c) ∈ {1,2,3}³.

    Returns dict mapping (a,b,c) -> result. All should be 0.
    """
    results = {}
    for a in [1, 2, 3]:
        for b in [1, 2, 3]:
            for c in [1, 2, 3]:
                results[(a, b, c)] = check_su2_jacobi(a, b, c, lam, mu, k)
    return results


def sugawara_central_charge(k, dim_g=3, h_dual=2):
    """Sugawara central charge for g = sl_2 at level k.

    c = k·dim(g)/(k + h^∨)

    For sl_2: dim = 3, h^∨ = 2, so c = 3k/(k+2).

    CRITICAL: Sugawara is UNDEFINED at k = −h^∨ = −2 (critical level).
    """
    return Rational(k * dim_g, k + h_dual)
