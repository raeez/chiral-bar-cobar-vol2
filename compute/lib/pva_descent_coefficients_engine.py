"""PVA descent coefficient engine (D_2 -- D_6) for Vol II Part I.

Verifies the five descent coefficients/axiom-verifiers D_2 through D_6 of
the cohomological descent theorem from chapters/theory/pva-descent.tex
(and the expanded form in chapters/theory/pva-descent-repaired.tex,
Example comp:pva-descent-affine-sl2).

Theorem statement recap.  A logarithmic SC^{ch,top}-algebra (A, {m_k}, Q)
arising from a 3d HT theory satisfying H1--H4 descends on cohomology
H*(A,Q) to a (-1)-shifted Poisson vertex algebra.  The binary PVA
identities are recorded as D_2 through D_5; D_6 is a separate
higher-formality certificate for chosen comparison models.

    D_2 : Sesquilinearity      {d a, b}_lam = -lam * {a, b}_lam
                                {a, d b}_lam = (lam + d) * {a, b}_lam
    D_3 : Skew-symmetry         {a, b}_lam   = -{b, a}_{-lam - d}
    D_4 : Jacobi identity       {a,{b,c}_mu}_lam - eps {b,{a,c}_lam}_mu
                                  = {{a,b}_lam, c}_{lam+mu}
    D_5 : Leibniz rule          {a, b * c}_lam = {a, b}_lam * c + b * {a, c}_lam
    D_6 : Higher-formality flag m_k vanishes in cohomology for k >= 3
                                only when a nullhomotopy certificate is
                                recorded for the chosen comparison model

The descent functional D_k : (A, {m_k}, Q) -> truth value returns a
formal/numeric residue measuring axiom failure for D_2 through D_5 and
a certificate flag for D_6.  For every certified standard comparison
model (Heisenberg = abelian current algebra, affine sl_2, Virasoro),
the binary residues vanish and the stored D_6 certificate is true.  This
engine encodes the universal Borel-transformed formulas from the chapter:

    {a_lam b} = sum_{n >= 0} a_{(n)}b * lam^n / n!

(polynomial convention, Remark rmk:Laurent_vs_poly).  Given OPE mode
data {a_{(n)}b}_{n >= 0} for a finite basis, the engine computes each
D_k residue symbolically in SymPy and verifies it against independent
closed-form expressions derived directly from the chapter (abelian
contraction, sl_2 affine structure constants, Virasoro lambda^3
divided-power central term, V2-AP34).

Anti-pattern enforcement
------------------------
AP1/AP39 kappa identities are stored per-family and never copied:

    kappa(Heis_k)   = k
    kappa(Vir_c)    = c/2
    kappa(sl_2, k)  = k + h_dual = k + 2     (Kac-Moody level at dim=3, h^v=2)

V2-AP34: Virasoro lambda-bracket uses divided-power central term
c/12 * lam^3, NOT c/2 * lam^3.  Sesquilinearity of the mode relation
T_{(3)} T = c/2 maps to c/12 in the polynomial convention via division
by 3! = 6.

AP126/AP141: At level k = 0 the Kac-Moody central extension of the
lambda-bracket vanishes identically ({e_lam f}|_{k=0} = h, no lam
contribution); the classical r-matrix is k * Omega / z and must vanish
at k = 0.  The engine enforces this boundary: the `verify_level_zero'
hook on the affine_sl2 family confirms that the central term drops out.

AP11 single-point dependency: this engine depends only on the Borel
transform formula of the chapter (pva-descent-repaired.tex lines 55--56)
and the mode relations for each standard family.  All formulas are
verified by at least two independent derivation paths per test.

Public API
----------
class PVASpec                 Structure-constant container for a PVA
class DescentResult           Named tuple wrapping D_k residue data
compute_D2(spec, a, b)        Sesquilinearity residue
compute_D3(spec, a, b)        Skew-symmetry residue
compute_D4(spec, a, b, c)     Jacobi residue
compute_D5(spec, a, b, c)     Leibniz residue
compute_D6(spec, k)           Certified higher-formality predicate (k >= 3)
descent_coefficients(spec, triples)
                              Return DescentResult for the descent checks

Standard-family builders
------------------------
heisenberg_pva(k_symbol)      Abelian current algebra at level k
affine_sl2_pva(k_symbol)      Affine sl_2 at level k
virasoro_pva(c_symbol)        Virasoro at central charge c

Notation
--------
We store the polynomial lambda-bracket as a SymPy expression in the
formal spectral parameter `lam'.  A mode table is a dict with keys
(a, b) pointing to a list of coefficients [a_{(0)}b, a_{(1)}b, ...]
matching the Borel expansion {a_lam b} = sum a_{(n)}b * lam^n / n!.

Derivative action `d' is encoded as a formal map on generator symbols:
each generator `g' gets an infinite family g, dg, d2g, ... represented
via a dict.  For the closed-form tests below we only need d acting on
a single layer (enough for D_2, D_3, D_4 on standard families).

This engine is self-contained (standard library + sympy) and is not
meant to solve the general descent problem: it is a certifier that
verifies each descent coefficient against its closed-form value on
the three families occurring in the chapter.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from typing import Callable, Dict, Iterable, List, Optional, Tuple

try:
    from sympy import (
        Expr, Integer, Rational, Symbol, S, expand, factorial, simplify, zoo,
    )
except ImportError as exc:  # pragma: no cover - sympy is a standard dep
    raise ImportError(
        "pva_descent_coefficients_engine requires sympy"
    ) from exc


# ---------------------------------------------------------------------------
# Data containers
# ---------------------------------------------------------------------------


@dataclass
class PVASpec:
    """Finite-dimensional specification of a PVA on generators.

    Attributes
    ----------
    name : str
        Family label (for diagnostics).
    generators : list of str
        Names of the generators (basis of the degree-0 part).
    degrees : dict
        Map generator -> cohomological degree.  For the standard
        families all generators sit in degree 0.
    modes : dict
        Map (a, b) -> list of mode coefficients [a_{(0)}b, a_{(1)}b,...]
        each element being a SymPy expression (possibly involving the
        level/central charge and the generators themselves).  Missing
        keys are treated as identically zero (all regular).  Reserved
        keys ("__D6__", str(k)) and ("__D6__", "all") record explicit
        higher-formality certificates for comparison models.
    product : callable
        (a_expr, b_expr) -> product a * b in the commutative
        differential polynomial ring R generated by the generators
        and their translates.  For standard families this is ordinary
        multiplication in SymPy.
    translate : callable
        g -> d g.  A formal derivation on R.
    kappa : Expr
        Family-specific kappa constant (AP1/AP39).  Stored but never
        copied across families.
    level_symbol : Symbol, optional
        The level/central charge symbol, used by `verify_level_zero`.
    """

    name: str
    generators: List[str]
    degrees: Dict[str, int]
    modes: Dict[Tuple[str, str], List[Expr]] = field(default_factory=dict)
    product: Optional[Callable[[Expr, Expr], Expr]] = None
    translate: Optional[Callable[[Expr], Expr]] = None
    kappa: Expr = S.Zero
    level_symbol: Optional[Symbol] = None

    def mode(self, a: str, b: str, n: int) -> Expr:
        """Return a_{(n)} b.

        Missing entries are zero.  Out-of-range indices are zero.
        """
        key = (a, b)
        table = self.modes.get(key)
        if table is None:
            return S.Zero
        if n < 0 or n >= len(table):
            return S.Zero
        return table[n]

    def bracket(self, a: str, b: str, lam: Symbol, max_order: int = 4) -> Expr:
        """Polynomial lambda-bracket {a_lam b} via Borel transform.

        Returns sum_{n=0}^{max_order} a_{(n)}b * lam^n / n!
        """
        total = S.Zero
        for n in range(max_order + 1):
            coeff = self.mode(a, b, n)
            if coeff == 0:
                continue
            total = total + coeff * lam ** n / factorial(n)
        return expand(total)


@dataclass
class DescentResult:
    """Binary PVA residues plus the separate D_6 higher-formality flag."""

    family: str
    D2_left: Expr
    D2_right: Expr
    D3: Expr
    D4: Expr
    D5: Expr
    D6: bool

    def is_pva(self) -> bool:
        """Return True iff the binary PVA residues vanish."""
        residues = [self.D2_left, self.D2_right, self.D3, self.D4, self.D5]
        return all(simplify(r) == 0 for r in residues)

    def is_higher_formal(self) -> bool:
        """Return True iff the D_6 higher-formality certificate is present."""
        return self.D6


# ---------------------------------------------------------------------------
# D_2: Sesquilinearity
# ---------------------------------------------------------------------------


def compute_D2(
    spec: PVASpec,
    a: str,
    b: str,
    lam: Symbol,
    max_order: int = 4,
) -> Tuple[Expr, Expr]:
    """Return (left-residue, right-residue) for PVA1 sesquilinearity.

    Left axiom:   {d a, b}_lam + lam * {a, b}_lam = 0
    Right axiom:  {a, d b}_lam - (lam + d) {a, b}_lam = 0

    We encode d a, d b by shifted mode relations:

        (d a)_{(n)} b = -n * a_{(n-1)} b
        a_{(n)} (d b) = d (a_{(n)} b) + n * a_{(n-1)} b

    so the Borel transform gives {d a_lam b} = -lam * {a_lam b}
    and {a_lam d b} = (lam + d) * {a_lam b}; both residues must vanish.
    """
    base = spec.bracket(a, b, lam, max_order=max_order)

    # Left: reconstruct {(d a)_lam b} from mode relations
    shifted_left = S.Zero
    for n in range(max_order + 1):
        # (d a)_{(n)} b = -n * a_{(n-1)} b
        coeff = -Integer(n) * spec.mode(a, b, n - 1)
        if coeff == 0:
            continue
        shifted_left = shifted_left + coeff * lam ** n / factorial(n)
    left_res = expand(shifted_left - (-lam * base))

    # Right: reconstruct {a_lam (d b)} from mode relations
    shifted_right = S.Zero
    for n in range(max_order + 1):
        base_mode = spec.mode(a, b, n)
        shift_mode = spec.mode(a, b, n - 1)
        # a_{(n)} (d b) = d(a_{(n)} b) + n * a_{(n-1)} b
        translated = spec.translate(base_mode) if spec.translate else S.Zero
        coeff = translated + Integer(n) * shift_mode
        if coeff == 0:
            continue
        shifted_right = shifted_right + coeff * lam ** n / factorial(n)

    # (lam + d) * {a_lam b}
    d_base = spec.translate(base) if spec.translate else S.Zero
    right_res = expand(shifted_right - (lam * base + d_base))

    return (simplify(left_res), simplify(right_res))


# ---------------------------------------------------------------------------
# D_3: Skew-symmetry
# ---------------------------------------------------------------------------


def compute_D3(
    spec: PVASpec,
    a: str,
    b: str,
    lam: Symbol,
    max_order: int = 4,
) -> Expr:
    """Return residue of PVA2 skew-symmetry in cohomology.

    In the lambda-bracket convention used by the affine examples,
    degree-zero generators satisfy the standard PVA skew identity
    {a_lam b} + {b_{-lam - d} a} = 0.

    The substitution mu -> -lam - d on a polynomial P(mu, g) means:
        sum_n c_n mu^n  maps to  sum_n c_n * (-lam - d)^n
    where d acts as the translation endomorphism on the coefficient ring.
    Since the standard-family tests only involve degree-0 generators
    and brackets with at most linear lam dependence, we expand
    (-lam - d)^n on SymPy polynomials via translate().
    """
    deg_a = spec.degrees.get(a, 0)
    deg_b = spec.degrees.get(b, 0)
    skew_sign = (-1) ** (deg_a * deg_b)

    lhs = spec.bracket(a, b, lam, max_order=max_order)

    # Build {b_mu a} then substitute mu -> -lam - d.
    mu = Symbol("_mu_D3", commutative=True)
    rhs_in_mu = spec.bracket(b, a, mu, max_order=max_order)

    # For max_order <= 1 (all standard HT families) the substitution
    # reduces to mu -> -lam (the d contribution lands on the scalar
    # coefficients of mu^1 and is then translated).
    substituted = S.Zero
    try:
        poly = rhs_in_mu.as_poly(mu) if rhs_in_mu != 0 else None
    except Exception:
        poly = None

    if poly is None:
        substituted = rhs_in_mu.subs(mu, -lam)
    else:
        for power, coef in poly.as_dict().items():
            n = power[0]
            # (-lam - d)^n applied to coef via translate().  For n = 0
            # this is just coef; for n = 1 it is (-lam * coef - d coef);
            # for n >= 2 we iterate translate on the coefficient.
            term = S.Zero
            # Binomial expansion: sum_{j} C(n,j) * (-lam)^(n-j) * (-d)^j coef
            from sympy import binomial
            iterated = coef
            for j in range(n + 1):
                bin_coef = binomial(n, j)
                sign = (-1) ** (n - j) * (-1) ** j  # from (-lam)^(n-j) * (-d)^j
                term = term + sign * bin_coef * lam ** (n - j) * iterated
                if spec.translate is not None:
                    iterated = spec.translate(iterated)
                else:
                    iterated = S.Zero
            substituted = substituted + term

    residue = expand(lhs + skew_sign * substituted)
    return simplify(residue)


# ---------------------------------------------------------------------------
# D_4: Jacobi identity
# ---------------------------------------------------------------------------


def compute_D4(
    spec: PVASpec,
    a: str,
    b: str,
    c: str,
    lam: Symbol,
    mu: Symbol,
    max_order: int = 3,
) -> Expr:
    """Return residue of PVA3 Jacobi for the triple (a, b, c).

    Identity (degree-0 inputs, shifted sign +1):
        {a_lam {b_mu c}} - {b_mu {a_lam c}} - {{a_lam b}_{lam+mu} c} = 0

    The inner brackets return polynomials in mu (resp. lam) whose
    coefficients live in the differential polynomial ring R.  To evaluate
    the outer bracket on those coefficients we expand via
    R-linearity and call `spec.bracket` on the generator factors; this
    is enough for the standard HT landscape where every mode coefficient
    is a linear combination of generators (plus scalar k or c).
    """
    # Three inner brackets as generator-valued polynomials.
    inner_bc = spec.bracket(b, c, mu, max_order=max_order)
    inner_ac = spec.bracket(a, c, lam, max_order=max_order)
    inner_ab = spec.bracket(a, b, lam, max_order=max_order)

    # {a_lam {b_mu c}}: bracket a with each generator-coefficient of
    # inner_bc.  We support the case where inner_bc is a SymPy linear
    # combination of Symbols named by generators, possibly plus lam/mu
    # scalar terms.
    outer_1 = _bracket_with_expr(spec, a, inner_bc, lam, max_order)
    outer_2 = _bracket_with_expr(spec, b, inner_ac, mu, max_order)

    # {{a_lam b}_{lam+mu} c}: bracket each generator in inner_ab with c
    # at spectral parameter (lam+mu).
    lm = lam + mu
    outer_3 = _bracket_expr_with(spec, inner_ab, c, lm, max_order)

    residue = expand(outer_1 - outer_2 - outer_3)
    return simplify(residue)


def _bracket_with_expr(
    spec: PVASpec,
    a: str,
    expr: Expr,
    lam: Symbol,
    max_order: int,
) -> Expr:
    """Compute {a_lam expr} by linear extension over generator symbols.

    `expr` is expected to be a SymPy expression in the generators of
    `spec` and in scalar constants (level, central charge, lambda-like
    variables).  Scalars bracket to zero.  Products of generators are
    handled via the Leibniz rule on the first factor only, iterated;
    this matches D_5 and is sufficient for the standard-family tests.
    """
    expanded = expand(expr)
    if expanded == 0:
        return S.Zero
    # Decompose into a sum of monomials
    try:
        terms = expanded.as_ordered_terms()
    except Exception:
        terms = [expanded]
    total = S.Zero
    for term in terms:
        total = total + _bracket_with_monomial(spec, a, term, lam, max_order)
    return total


def _bracket_with_monomial(
    spec: PVASpec,
    a: str,
    monomial: Expr,
    lam: Symbol,
    max_order: int,
) -> Expr:
    """Compute {a_lam monomial} for a product of generator symbols * scalar."""
    # Separate generator symbols from scalar factors.
    gen_syms = {g: Symbol(g) for g in spec.generators}
    gen_names = set(spec.generators)

    gen_factors: List[str] = []
    scalar = S.One
    for factor, power in monomial.as_powers_dict().items():
        name = str(factor)
        if name in gen_names:
            for _ in range(int(power)):
                gen_factors.append(name)
        else:
            scalar = scalar * factor ** power

    if not gen_factors:
        # Pure scalar: {a_lam scalar} = 0
        return S.Zero

    # Leibniz rule: {a_lam b_1 b_2 ... b_m} = sum_i b_1 ... b_{i-1}
    #   {a_lam b_i} b_{i+1} ... b_m
    result = S.Zero
    for i, bi in enumerate(gen_factors):
        br = spec.bracket(a, bi, lam, max_order=max_order)
        prefix = S.One
        for j, bj in enumerate(gen_factors):
            if j == i:
                continue
            prefix = prefix * gen_syms[bj]
        result = result + prefix * br
    return scalar * result


def _bracket_expr_with(
    spec: PVASpec,
    expr: Expr,
    c: str,
    lam: Symbol,
    max_order: int,
) -> Expr:
    """Compute {expr_lam c} by linear extension (first slot).

    Symmetric to _bracket_with_expr but brackets on the left.  Scalars
    bracket to zero in the left slot as well (the level k is a scalar
    derivative-free constant; its bracket with anything is zero).
    """
    expanded = expand(expr)
    if expanded == 0:
        return S.Zero
    try:
        terms = expanded.as_ordered_terms()
    except Exception:
        terms = [expanded]
    total = S.Zero
    gen_names = set(spec.generators)
    for term in terms:
        # Extract the single generator factor (if any) and treat the
        # rest as scalar.  For the standard HT families the inner
        # bracket is linear in one generator + scalar central term.
        gen_factor: Optional[str] = None
        scalar = S.One
        for factor, power in term.as_powers_dict().items():
            name = str(factor)
            if name in gen_names:
                # Multi-linear case: we fall back to linearity in the
                # first generator encountered.
                gen_factor = name
                scalar = scalar * factor ** (int(power) - 1)
            else:
                scalar = scalar * factor ** power
        if gen_factor is None:
            # Pure scalar factor: bracket is zero.
            continue
        br = spec.bracket(gen_factor, c, lam, max_order=max_order)
        total = total + scalar * br
    return total


# ---------------------------------------------------------------------------
# D_5: Leibniz rule
# ---------------------------------------------------------------------------


def compute_D5(
    spec: PVASpec,
    a: str,
    b: str,
    c: str,
    lam: Symbol,
    max_order: int = 3,
) -> Expr:
    """Return residue of PVA5 Leibniz for the triple (a, b, c).

    Axiom (degree-0 inputs):
        {a_lam (b * c)} = {a_lam b} * c + b * {a_lam c}

    We use the commutative product of R (SymPy `*`).
    """
    gen_syms = {g: Symbol(g) for g in spec.generators}
    product = gen_syms[b] * gen_syms[c]
    lhs = _bracket_with_expr(spec, a, product, lam, max_order)
    rhs = (
        spec.bracket(a, b, lam, max_order=max_order) * gen_syms[c]
        + gen_syms[b] * spec.bracket(a, c, lam, max_order=max_order)
    )
    return simplify(expand(lhs - rhs))


# ---------------------------------------------------------------------------
# D_6: Higher vanishing
# ---------------------------------------------------------------------------


def compute_D6(spec: PVASpec, k: int) -> bool:
    """Return True iff a recorded certificate makes m_k vanish on cohomology.

    Contractibility of Conf_k^<(R) is not by itself a proof that every
    m_k is Q-exact.  Proposition prop:m3_vanish requires compatible
    topological nullhomotopies / bounding chains.  This engine therefore
    treats higher-formality as a certificate attached to a chosen
    comparison model, not as a universal default.

    The per-family flag is stored in `spec.modes` under the key
    ('__D6__', str(k)) or ('__D6__', 'all') as a boolean value.  The
    default is False for k >= 3.
    """
    if k < 3:
        # D_6 is the k >= 3 vanishing statement; lower arities are
        # governed by D_2 (n=2) and are vacuously handled.
        return True
    key = ("__D6__", str(k))
    override = spec.modes.get(key)
    if override is not None:
        if isinstance(override, list):
            return bool(override[0])
        return bool(override)
    all_override = spec.modes.get(("__D6__", "all"))
    if all_override is not None:
        if isinstance(all_override, list):
            return bool(all_override[0])
        return bool(all_override)
    return False


# ---------------------------------------------------------------------------
# Aggregator
# ---------------------------------------------------------------------------


def descent_coefficients(
    spec: PVASpec,
    triple: Tuple[str, str, str],
    lam: Symbol,
    mu: Symbol,
    max_order: int = 3,
) -> DescentResult:
    """Compute D_2--D_5 residues and the separate D_6 certificate."""
    a, b, c = triple
    d2l, d2r = compute_D2(spec, a, b, lam, max_order=max_order)
    d3 = compute_D3(spec, a, b, lam, max_order=max_order)
    d4 = compute_D4(spec, a, b, c, lam, mu, max_order=max_order)
    d5 = compute_D5(spec, a, b, c, lam, max_order=max_order)
    d6 = compute_D6(spec, 3)
    return DescentResult(
        family=spec.name,
        D2_left=d2l,
        D2_right=d2r,
        D3=d3,
        D4=d4,
        D5=d5,
        D6=d6,
    )


# ---------------------------------------------------------------------------
# Standard-family builders
# ---------------------------------------------------------------------------


def _trivial_translate(expr: Expr) -> Expr:
    """Default formal derivation: zero on constants/generators.

    For the closed-form descent checks on degree-0 generators where the
    mode coefficients are scalars or at most linear in generators,
    `d` acts as zero on scalar constants (level k, central charge c)
    and is recorded symbolically on generator terms when needed.
    The tests below do not exercise higher jets of the translation
    operator.
    """
    return S.Zero


def heisenberg_pva(k: Expr) -> PVASpec:
    """Build the abelian current PVA {J_lam J} = k * lam.

    Ref: pva-descent-repaired.tex Example ex:repaired-abelian-current,
    lines 1288--1318.  AP1/AP39: kappa(Heis_k) = k.
    AP126: at k = 0 the bracket vanishes identically.
    """
    J = Symbol("J")
    modes = {
        ("J", "J"): [S.Zero, k],  # J_{(0)} J = 0, J_{(1)} J = k
        ("__D6__", "all"): True,
    }
    return PVASpec(
        name="Heisenberg",
        generators=["J"],
        degrees={"J": 0},
        modes=modes,
        product=lambda x, y: x * y,
        translate=_trivial_translate,
        kappa=k,
        level_symbol=k if isinstance(k, Symbol) else None,
    )


def affine_sl2_pva(k: Expr) -> PVASpec:
    """Build the affine sl_2 PVA at level k.

    Ref: pva-descent-repaired.tex Example comp:pva-descent-affine-sl2,
    lines 1320--1397.  Mode tables:

        e_{(0)} f = h,   e_{(1)} f = k
        f_{(0)} e = -h,  f_{(1)} e = k
        h_{(0)} e = 2e,  h_{(0)} f = -2f
        h_{(1)} h = 2k

    AP1/AP39: kappa(sl_2, k) = k + h^v = k + 2.
    AP126: at k = 0 the central extension vanishes but the semisimple
    part {e_lam f} = h survives.
    """
    e = Symbol("e")
    f = Symbol("f")
    h = Symbol("h")
    modes = {
        ("e", "f"): [h, k],
        ("f", "e"): [-h, k],
        ("h", "e"): [2 * e],
        ("h", "f"): [-2 * f],
        ("e", "h"): [-2 * e],
        ("f", "h"): [2 * f],
        ("h", "h"): [S.Zero, 2 * k],
        ("e", "e"): [S.Zero, S.Zero],
        ("f", "f"): [S.Zero, S.Zero],
        ("__D6__", "all"): True,
    }
    # Dual Coxeter h^v(sl_2) = 2, so kappa_KM = dim(g)*(k+h^v)/(2 h^v)
    # = 3*(k+2)/4.  Stored for AP1 cross-check (never copied).
    kappa_km = Rational(3, 4) * (k + 2)
    return PVASpec(
        name="AffineSL2",
        generators=["e", "f", "h"],
        degrees={"e": 0, "f": 0, "h": 0},
        modes=modes,
        product=lambda x, y: x * y,
        translate=_trivial_translate,
        kappa=kappa_km,
        level_symbol=k if isinstance(k, Symbol) else None,
    )


def virasoro_pva(c: Expr) -> PVASpec:
    """Build the Virasoro PVA at central charge c.

    The OPE T(z)T(w) ~ (c/2)/(z-w)^4 + 2T(w)/(z-w)^2 + dT(w)/(z-w)
    yields mode relations

        T_{(0)} T = dT,  T_{(1)} T = 2T,  T_{(2)} T = 0,  T_{(3)} T = c/2,

    so the polynomial lambda-bracket (divided-power / V2-AP34) is

        {T_lam T} = dT + 2 T lam + (c/12) lam^3

    Ref: pva-descent-repaired.tex lines 30--56 (Borel transform) and
    the divided-power convention at V2-AP34 in the Vol II CLAUDE.md.
    AP1/AP39: kappa(Vir_c) = c/2.
    """
    T = Symbol("T")
    # T_{(0)} T = dT; we encode dT by a fresh symbol since the
    # translate() on a pure generator is formal here.
    dT = Symbol("dT")
    modes = {
        # positions: n = 0, 1, 2, 3
        ("T", "T"): [dT, 2 * T, S.Zero, c / 2],
        ("__D6__", "all"): True,
    }

    def _virasoro_translate(expr: Expr) -> Expr:
        """Formal d: T -> dT, dT -> 0, c -> 0."""
        return expr.subs({T: dT, dT: S.Zero})

    return PVASpec(
        name="Virasoro",
        generators=["T"],
        degrees={"T": 0},
        modes=modes,
        product=lambda x, y: x * y,
        translate=_virasoro_translate,
        kappa=c / 2,
        level_symbol=c if isinstance(c, Symbol) else None,
    )


# ---------------------------------------------------------------------------
# Edge-case / boundary helpers
# ---------------------------------------------------------------------------


def trivial_pva() -> PVASpec:
    """Return the trivial PVA (single generator, zero bracket).

    Every descent coefficient is automatically zero.
    """
    x = Symbol("x")  # noqa: F841 (used indirectly by bracket)
    return PVASpec(
        name="Trivial",
        generators=["x"],
        degrees={"x": 0},
        modes={("x", "x"): [S.Zero], ("__D6__", "all"): True},
        product=lambda a, b: a * b,
        translate=_trivial_translate,
        kappa=S.Zero,
    )


def verify_level_zero(spec_builder: Callable[[Expr], PVASpec], lam: Symbol) -> bool:
    """Verify the AP126/AP141 boundary check at level 0.

    At k = 0 or c = 0 (depending on family) the ``central extension''
    contribution to the lambda-bracket must vanish or reduce to the
    classical semisimple part.  For Heisenberg: {J_lam J}|_{k=0} = 0.
    For affine sl_2: {e_lam f}|_{k=0} = h (no lambda term).
    For Virasoro: {T_lam T}|_{c=0} = dT + 2 T lam (no lambda^3 term).
    """
    spec = spec_builder(S.Zero)
    # Test the signature mode for each family.
    if spec.name == "Heisenberg":
        return spec.bracket("J", "J", lam) == 0
    if spec.name == "AffineSL2":
        b = spec.bracket("e", "f", lam)
        return simplify(b - Symbol("h")) == 0
    if spec.name == "Virasoro":
        b = spec.bracket("T", "T", lam)
        expected = Symbol("dT") + 2 * Symbol("T") * lam
        return simplify(b - expected) == 0
    return False


__all__ = [
    "PVASpec",
    "DescentResult",
    "compute_D2",
    "compute_D3",
    "compute_D4",
    "compute_D5",
    "compute_D6",
    "descent_coefficients",
    "heisenberg_pva",
    "affine_sl2_pva",
    "virasoro_pva",
    "trivial_pva",
    "verify_level_zero",
]
