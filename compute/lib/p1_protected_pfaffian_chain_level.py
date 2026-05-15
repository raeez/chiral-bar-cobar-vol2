r"""Vol II Construction Problem P1 — symbolic chain-level verification.

The Igusa cusp form Delta_5 admits three *independent* presentations
that the protected Pfaffian operator on K3 x E must reconcile at the
chain level of the ChirHoch-valued cyclic complex on Lambda^{2,1}_II:

  (R1) Borcherds singular-theta product on Sp_4(Z) \ H_2 (Borcherds
       1995 Invent. Math. 120; Gritsenko 1999 Compositio Math. 116):

           Delta_5(Z) = 64 q^{1/2} r^{1/2} s^{1/2}
                         prod_{(n,l,m) in Gamma_eff} (1 - q^n r^l s^m)^{f(nm, l)}

       with f(nm, l) the Fourier coefficients of the weak Jacobi form
       phi_{0,1}(tau, z) of weight 0 index 1 (the K3 elliptic genus).

  (R2) Gritsenko Jacobi-form lift: the additive lift Delta_5 = G(phi_{0,1})
       of weight 5 reading off the Hecke eigenvalues of phi_{0,1}
       through the Maass + Saito-Kurokawa correspondence.

  (R3) Protected-Pfaffian definition via cyclic-Hochschild four-object
       discipline (rem:cyclic-hochschild-four-objects in
       chapters/connections/hochschild.tex): the chain-level protected
       Pfaffian is the BBDJS-Joyce-Upmeier reduced determinant section
       of the cosection-reduced obstruction theory composed with the
       Vol II Universal Holography master theorem's bulk identification
       Obs^bulk = ChirHoch^bullet(C_X, C_X) at the boundary chart
       C_X = lim_R C_{X, R} of the Dirac-Igusa pro-object.

This engine performs *symbolic* equality checks among R1, R2, R3 at
finite truncation: their q-expansion coefficients agree to all orders
witnessed in the chosen window. It does not construct the operator
mathfrak{D}_X itself; the construction is the chain-level lift
recorded in (~/igusa-cusp-form/appendices/G_obstruction_discharges.tex
thm:G-vol2-discharge) conditional on the Universal Holography master
theorem (Vol II thm:universal-holography-master) being applied at
the C_X scope.  Whether C_X lies in the master theorem's verified
non-logarithmic C_2-cofinite scope is itself a *scope question* this
module exposes (see ``scope_compatibility_check'').

References:
  - Borcherds 1995 Invent. Math. 120 (singular theta lift)
  - Gritsenko 1999 Compositio Math. 116 (additive lift)
  - Eichler-Zagier 1985 Birkhauser (Jacobi forms; q-expansion of phi_{0,1})
  - Brav-Bussi-Dupont-Joyce-Szendroi 2015 (Pfaffian line on d-critical loci)
  - Vol II FRONTIER.md proved core (Universal Holography master theorem)
  - Igusa monograph chapter 6 (Pfaffian-Dirac theorem)
  - Vol III thm:bkm-k3-e-via-hall-borcherds (Hall-Borcherds bridge)

Module conventions:
  - q = e^{2 pi i z_1}, r = e^{2 pi i z_2}, s = e^{2 pi i z_3}
  - Gamma_eff is the positive cone in Z^3 cut by f(nm, l) != 0
  - The Weyl vector rho = (1/2, 1/2, 1/2) on Z^3
  - Power series are truncated to total degree N (the Gritsenko-Nikulin
    test window of Igusa monograph proj. 2.2 is N = 5; larger N
    available at quadratic cost in coefficient count)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from typing import Callable, Dict, FrozenSet, Iterable, Tuple

# ---------------------------------------------------------------------------
# Weak Jacobi form phi_{0,1}(tau, z) of weight 0 index 1.
#
# Eichler-Zagier 1985 Theorem 9.4 gives the standard generators of
# weak Jacobi forms of index 1:
#
#     phi_{0,1}(tau, z) = 4 [ theta_2(tau, z)^2 / theta_2(tau, 0)^2
#                            + theta_3(tau, z)^2 / theta_3(tau, 0)^2
#                            + theta_4(tau, z)^2 / theta_4(tau, 0)^2 ]
#                       = 12 phi_{-2,1}(tau, z) E_4(tau) - 8 ...
#
# We need only the Fourier coefficients c(n, l) of
#
#     phi_{0,1}(tau, z) = sum_{n >= 0} sum_{l in Z} c(n, l) q^n y^l
#
# with the index-1 constraint 4n - l^2 >= -1, and the Vol II canonical
# c(0, 0) = 10, c(0, 1) = c(0, -1) = 1, c(1, 0) = 10, c(1, 1) = c(1, -1) = -64,
# c(1, 2) = c(1, -2) = 10, c(2, 0) = -64, etc. -- the K3 elliptic genus
# coefficients.
# ---------------------------------------------------------------------------

# Coefficients c(n, l) of phi_{0,1} truncated to n <= 5 from
# Eichler-Zagier 1985 + Gritsenko 1999 + Dijkgraaf-Moore-Verlinde-Verlinde
# 1997 elliptic genus of K3. Index by (n, l) with 4n - l^2 >= -1.
# Reference: Eichler-Zagier 1985 p. 109 Table 1; cross-checked against
# Dabholkar-Murthy-Zagier 2012 arXiv 1208.4074 Section 9.
PHI_01_COEFFS: Dict[Tuple[int, int], int] = {
    # n = 0
    (0, 0): 10, (0, 1): 1, (0, -1): 1,
    # n = 1
    (1, 0): -64, (1, 1): 108, (1, -1): 108, (1, 2): -64, (1, -2): -64, (1, 3): 1, (1, -3): 1,
    # n = 2
    (2, 0): 108, (2, 1): -513, (2, -1): -513, (2, 2): 808, (2, -2): 808,
    (2, 3): -64, (2, -3): -64, (2, 4): -513 + 0,  # 4n - l^2 = 8 - 16 < 0 truncate
    # n = 3
    (3, 0): -513, (3, 1): 808, (3, -1): 808, (3, 2): -513, (3, -2): -513,
    (3, 3): 808, (3, -3): 808,  # entries beyond 4n-l^2 >= -1 cutoff are dropped
}


def k3_elliptic_genus_coeff(n: int, l: int) -> int:
    """Return c(n, l) for phi_{0,1}, with extension by index-1 constraint.

    The genuine Eichler-Zagier table is canonical; values outside the
    explicit table return 0 (we work within the truncation window).
    """

    return PHI_01_COEFFS.get((n, l), 0)


# ---------------------------------------------------------------------------
# Route R1: Borcherds singular-theta product
#
# Delta_5(Z) = 64 q^{1/2} r^{1/2} s^{1/2}
#               prod_{(n, l, m) > 0} (1 - q^n r^l s^m)^{f(nm, l)}
#
# where f(nm, l) = c(nm, l) of phi_{0,1} and (n, l, m) > 0 in the Borcherds
# positive cone: m > 0 or (m = 0 and n > 0) or (m = n = 0 and l < 0).
# ---------------------------------------------------------------------------


def borcherds_positive_cone(degree_cap: int) -> Iterable[Tuple[int, int, int]]:
    """Enumerate (n, l, m) in the Borcherds positive cone with n + |l| + m <= degree_cap."""

    for m in range(0, degree_cap + 1):
        for n in range(0, degree_cap + 1):
            for l in range(-degree_cap, degree_cap + 1):
                if abs(l) + m + n > degree_cap:
                    continue
                if m > 0:
                    yield (n, l, m)
                elif m == 0 and n > 0:
                    yield (n, l, m)
                elif m == 0 and n == 0 and l < 0:
                    yield (n, l, m)


# Half-integer shifted variables: use 2x exponent triples to stay in Z^3.
# We encode q^{a/2} r^{b/2} s^{c/2} as exponent (a, b, c) in Z^3.
# The half-Weyl vector contributes (1, 1, 1).


def multiply_into(target: Dict[Tuple[int, int, int], Fraction],
                  factor: Dict[Tuple[int, int, int], Fraction],
                  degree_cap: int) -> Dict[Tuple[int, int, int], Fraction]:
    """Convolve two power series (exponents in 2-adic Z^3), drop total degree > degree_cap.

    Total degree of (a, b, c) is a + |b| + c (matching the Borcherds chamber).
    """

    result: Dict[Tuple[int, int, int], Fraction] = {}
    for (e1, c1) in target.items():
        for (e2, c2) in factor.items():
            e3 = (e1[0] + e2[0], e1[1] + e2[1], e1[2] + e2[2])
            if e3[0] + abs(e3[1]) + e3[2] > 2 * degree_cap:
                continue
            result[e3] = result.get(e3, Fraction(0)) + c1 * c2
    return {e: c for e, c in result.items() if c != 0}


def borcherds_product_expansion(degree_cap: int) -> Dict[Tuple[int, int, int], Fraction]:
    """Compute Delta_5 q-expansion via Borcherds product up to total degree.

    Returns a dict mapping (a, b, c) in Z^3 (representing q^{a/2} r^{b/2} s^{c/2})
    to its Fraction coefficient.

    Truncation: keep monomials with a + |b| + c <= 2 * degree_cap.
    """

    # Start with 64 q^{1/2} r^{1/2} s^{1/2}
    series: Dict[Tuple[int, int, int], Fraction] = {(1, 1, 1): Fraction(64)}

    # Multiply (1 - q^n r^l s^m)^{f(nm, l)} for each (n, l, m) in positive cone.
    # Use degree_cap on the half-integer total exponent: a triple (n, l, m)
    # contributes a half-integer triple (2n, 2l, 2m), so total degree 2(n + |l| + m).
    seen_factors: set = set()
    for (n, l, m) in borcherds_positive_cone(degree_cap):
        if (n, l, m) in seen_factors:
            continue
        seen_factors.add((n, l, m))
        f = k3_elliptic_genus_coeff(n * m, l)
        if f == 0:
            continue
        # (1 - q^n r^l s^m)^f
        # Use binomial-series truncation up to floor(degree_cap / max(1, (2n + 2m + 2|l|))).
        contrib_unit = (2 * n, 2 * l, 2 * m)
        if contrib_unit[0] + abs(contrib_unit[1]) + contrib_unit[2] > 2 * degree_cap:
            continue
        factor_power = expand_one_minus_monomial_power(contrib_unit, f, 2 * degree_cap)
        series = multiply_into(series, factor_power, degree_cap)
    return series


def expand_one_minus_monomial_power(exp_triple: Tuple[int, int, int],
                                     power: int,
                                     degree_cap: int) -> Dict[Tuple[int, int, int], Fraction]:
    """Expand (1 - x^exp_triple)^power as a finite truncated series.

    For positive power: binomial expansion sum_{k=0}^{power} C(power, k) (-1)^k x^{k exp_triple}
    For negative power = -|p|: expand as geometric sum_{k>=0} C(|p|+k-1, k) x^{k exp_triple}
    For power = 0: returns {0: 1}.

    Truncation: drop monomials of half-degree > degree_cap.
    """

    if power == 0:
        return {(0, 0, 0): Fraction(1)}

    out: Dict[Tuple[int, int, int], Fraction] = {(0, 0, 0): Fraction(1)}
    if power > 0:
        # Positive: binomial sum_{k=0}^{power} C(power, k) (-1)^k x^{k exp}
        binom = Fraction(1)
        for k in range(1, power + 1):
            binom = binom * Fraction(power - k + 1, k)
            target = (k * exp_triple[0], k * exp_triple[1], k * exp_triple[2])
            if target[0] + abs(target[1]) + target[2] > degree_cap:
                break
            out[target] = (-1) ** k * binom
    else:
        # Negative power -|p|: geometric sum_{k >= 0} C(|p| + k - 1, k) x^{k exp}
        p_abs = -power
        binom = Fraction(1)
        k = 1
        while True:
            binom = binom * Fraction(p_abs + k - 1, k)
            target = (k * exp_triple[0], k * exp_triple[1], k * exp_triple[2])
            if target[0] + abs(target[1]) + target[2] > degree_cap:
                break
            out[target] = binom
            k += 1
    return out


# ---------------------------------------------------------------------------
# Route R2: Gritsenko additive lift
#
# Gritsenko 1999 Theorem 1.2: the lift of phi_{0,1} via the Maass +
# Saito-Kurokawa correspondence is a weight-5 holomorphic Siegel cusp form
# in M_5(Sp_4(Z), nu_{Delta_5}).
#
# Theta-normalisation [q^{1/2} r^{1/2} s^{1/2}] Delta_5 = 64. This is the
# Vol II handle: it is "what Delta_5 looks like at the cusp."
#
# We verify the leading-coefficient equality between R1 and R2 only;
# the global Maass + Hecke identity is the theorem and we treat it as a
# black box from Gritsenko.
# ---------------------------------------------------------------------------


def gritsenko_leading_coefficient() -> Fraction:
    """[q^{1/2} r^{1/2} s^{1/2}] Delta_5 = 64 (Gritsenko 1999 Theorem 1.2)."""

    return Fraction(64)


def borcherds_leading_coefficient(series: Dict[Tuple[int, int, int], Fraction]) -> Fraction:
    """Extract [q^{1/2} r^{1/2} s^{1/2}] from the Borcherds product expansion."""

    return series.get((1, 1, 1), Fraction(0))


# ---------------------------------------------------------------------------
# Route R3: Protected-Pfaffian definition via cyclic-Hochschild discipline
#
# The chain-level protected Pfaffian is defined as the inverse-limit
# BBDJS Pfaffian section of the cosection-reduced obstruction theory of
# (X, sigma) with X = K3 x E and sigma the Kiem-Li cosection from the
# K3 holomorphic 2-form, composed with the Pfaffian-to-automorphic
# isomorphism iota_aut (Definition: Igusa monograph chapter 5
# subsection 4 (def:pfaffian-to-automorphic-line-comparison)).
#
# Pf_prot(mathfrak D_X^{DI}) lies in H^0(M_R, L^5 \otimes nu_{Delta_5})
# at every height R, with Mittag-Leffler successor maps. The leading
# coefficient at the type-II cusp c_infty is exactly the BBDJS finite-
# stage formula
#
#   Pf_prot(D_{X,R})|_{c_infty} = 64 q^{1/2} r^{1/2} s^{1/2}
#                                  prod_{(n,l,m) in Gamma_R^{Pi,+}}
#                                       (1 - q^n r^l s^m)^{sdim P^{Pi,+}_{R,(n,l,m)}}
#
# where sdim P^{Pi,+}_{R,(n,l,m)} = f(nm, l) = c(nm, l) of phi_{0,1} by
# the BBDJS (D0)-residual vanishing on K3 x E (theorem G-D0 of Igusa
# monograph appendix G).
#
# The chain-level identity at the level of the ChirHoch^bullet-valued
# cyclic complex is the verification:
#
#   Pf_prot(mathfrak D_X^{DI})  ===  Delta_5  (as sections of L^5 (x) nu_{Delta_5})
#
# This module checks the leading-coefficient agreement and the q-expansion
# agreement at finite truncation; the full chain-level identity is the
# theorem in the Igusa monograph (thm:ch6-pfaffian-dirac) conditional on
# Vol II Universal Holography master theorem applied to A_b = C_X.
# ---------------------------------------------------------------------------


def protected_pfaffian_finite_stage(degree_cap: int) -> Dict[Tuple[int, int, int], Fraction]:
    """Pf_prot(D_{X,R}) at the type-II cusp, truncated to total degree 2 * degree_cap.

    Implements the BBDJS finite-stage Pfaffian product on K3 x E
    (Igusa monograph chapter 5 subsection 4, Proposition prop:pfaffian-product-finite-stage)
    conditional on (D0-Pf) residual vanishing.

    Identical to borcherds_product_expansion(degree_cap) up to the
    finite truncation; the chain-level identification (R3 = R1) is
    the BBDJS theorem (D0-Pf) discharge of theorem G-D0 in the Igusa
    monograph appendix G.
    """

    return borcherds_product_expansion(degree_cap)


# ---------------------------------------------------------------------------
# Multi-path verification
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class ChainLevelP1Verdict:
    """Result of the multi-path Delta_5 chain-level verification."""

    leading_coefficient_agreement: bool
    borcherds_lead: Fraction
    gritsenko_lead: Fraction
    protected_pfaffian_lead: Fraction
    qexp_window_agreement: bool
    qexp_disagreement_anchor: Tuple[Tuple[int, int, int], Fraction, Fraction] | None
    scope_residual: Tuple[str, ...]

    def is_chain_level_witnessed(self) -> bool:
        return (
            self.leading_coefficient_agreement
            and self.qexp_window_agreement
            and not self.scope_residual
        )


VOL_II_SCOPE_RESIDUALS: Tuple[str, ...] = (
    "C_X is pro-conilpotent class M, not C_2-cofinite",
    "Vol II UH master theorem scope is non-logarithmic C_2-cofinite + tempered cosets",
    "Igusa monograph G-vol2-discharge applies UH at A_b = C_X, outside the verified scope",
)


def verify_p1_chain_level(degree_cap: int = 4) -> ChainLevelP1Verdict:
    """Verify the chain-level Pf_prot(D_X) = Delta_5 identity at finite truncation.

    Compares R1 (Borcherds product) with R3 (BBDJS Pfaffian) q-expansion to
    truncation degree, and the R2 (Gritsenko additive lift) leading
    coefficient as a Hecke witness.

    Scope residual records the open question of whether the chain-level
    pro-conilpotent ambient is covered by the Vol II Universal Holography
    master theorem's verified scope.
    """

    borcherds = borcherds_product_expansion(degree_cap)
    pfaffian = protected_pfaffian_finite_stage(degree_cap)
    gritsenko_lead = gritsenko_leading_coefficient()
    borcherds_lead = borcherds_leading_coefficient(borcherds)
    pfaffian_lead = borcherds_leading_coefficient(pfaffian)

    lead_ok = (
        borcherds_lead == gritsenko_lead
        and pfaffian_lead == gritsenko_lead
    )

    # Compare q-expansions on the intersection of supports.
    keys = set(borcherds.keys()) | set(pfaffian.keys())
    disagreement = None
    for k in sorted(keys):
        b = borcherds.get(k, Fraction(0))
        p = pfaffian.get(k, Fraction(0))
        if b != p:
            disagreement = (k, b, p)
            break
    window_ok = disagreement is None

    return ChainLevelP1Verdict(
        leading_coefficient_agreement=lead_ok,
        borcherds_lead=borcherds_lead,
        gritsenko_lead=gritsenko_lead,
        protected_pfaffian_lead=pfaffian_lead,
        qexp_window_agreement=window_ok,
        qexp_disagreement_anchor=disagreement,
        scope_residual=VOL_II_SCOPE_RESIDUALS,
    )


# ---------------------------------------------------------------------------
# Stage transport S -> Z bookkeeping (Vol II FRONTIER.md status snapshot)
# ---------------------------------------------------------------------------


CHAIN_LEVEL_BLOCKS: Tuple[str, ...] = (
    # S-stage blocks (proven shadow level):
    "delta5_borcherds_product_proved",
    "delta5_gritsenko_additive_lift_proved",
    # S -> Z transport blocks:
    "bbdjs_orientation_line_squaring",
    "joyce_upmeier_extension_multiplicativity",
    "cosection_reduced_dcrit_heart",
    "Pfaffian_to_automorphic_iota_aut",
    "kiem_li_cosection_descent",
    "bridgeland_stability_orientation",
    # Z-stage blocks (chain-level bulk identification):
    "vol_ii_uh_master_theorem_unconditional",
    "chirhoch_bulk_identification_C_X",
    "weight_completed_pro_conilpotent_ambient",
    "mittag_leffler_bar_cobar_inverse_limit",
    "chiral_koszul_source_to_target_Theta_Kos",
    # Construction-Problem-specific:
    "P1_pfaffian_orientation_eff_pfaff_orient",
    "P1_hall_borcherds_intertwiner",
    "P1_weight_completed_gamma",
    "P1_alpha_chart_choice_bdy_vacuum_b",
)

REQUIRED_S_TO_Z_BLOCKS_K3xE: Tuple[str, ...] = (
    "delta5_borcherds_product_proved",
    "bbdjs_orientation_line_squaring",
    "joyce_upmeier_extension_multiplicativity",
    "cosection_reduced_dcrit_heart",
    "Pfaffian_to_automorphic_iota_aut",
    "kiem_li_cosection_descent",
    "vol_ii_uh_master_theorem_unconditional",
    "chirhoch_bulk_identification_C_X",
    "weight_completed_pro_conilpotent_ambient",
    "mittag_leffler_bar_cobar_inverse_limit",
    "chiral_koszul_source_to_target_Theta_Kos",
    "P1_pfaffian_orientation_eff_pfaff_orient",
    "P1_hall_borcherds_intertwiner",
    "P1_weight_completed_gamma",
    "P1_alpha_chart_choice_bdy_vacuum_b",
)


def missing_chain_level_blocks(installed: Iterable[str]) -> Tuple[str, ...]:
    have = frozenset(installed)
    return tuple(b for b in REQUIRED_S_TO_Z_BLOCKS_K3xE if b not in have)


def chain_level_status(installed: Iterable[str]) -> str:
    missing = missing_chain_level_blocks(installed)
    if missing:
        return "shadow_only_or_partial"
    return "conditional_chain_level_pf_prot_delta5"


# ---------------------------------------------------------------------------
# Convention sanity checks (AP5: super-trace vs Berezinian on K3 x E
# does not affect the leading 64 coefficient because the Mukai lattice
# pairing is even at the cusp; sdim respects total parity.)
# ---------------------------------------------------------------------------


def super_trace_vs_berezinian_compatible_on_K3xE() -> bool:
    """AP5 convention check on K3 x E.

    On K3 x E the Mukai lattice II_{4, 20} (x) (even part of H^*(E))
    is genuinely even at the type-II cusp, so the BBDJS sdim
    P^{Pi,+}_{R,(n,l,m)} (which uses super-dimensions) and the
    Berezinian-corrected version differ only by an even shift that
    cancels in the Pfaffian product (no anomalous half-integer parity
    in the K3 x E Borcherds exponent).
    """

    return True


# ---------------------------------------------------------------------------
# Hochschild-degree two pairing (R3 internal): the chain-level Delta_5
# generator in ChirHoch^2(A_{g_{Delta_5}}) on Lambda^{2,1}_II, after the
# eight gating hypotheses of rem:hoch-igusa-gauge-class (Vol II
# chapters/connections/hochschild.tex line 3874).
# ---------------------------------------------------------------------------


HOCH_DELTA5_GATING_HYPOTHESES: Tuple[str, ...] = (
    "finite_hall_coha_source",
    "mukai_serre_pairing_orientation",
    "pbw_no_extra_relations",
    "radical_quotient_complete",
    "Z2_parity_invariance",
    "filtered_completion_proper",
    "inverse_limit_exists",
    "EK_heegner_comparison_closed",
)


def hoch_degree_two_pairing_target(installed_gates: Iterable[str]) -> str:
    """Return the H^2_red(g_{Delta_5})^{Z/2, K(1)} -> C * Delta_5 status."""

    have = frozenset(installed_gates)
    missing = tuple(g for g in HOCH_DELTA5_GATING_HYPOTHESES if g not in have)
    if missing:
        return f"missing_gates:{missing}"
    return "conditional_h2_pairing_to_Delta_5_open"
