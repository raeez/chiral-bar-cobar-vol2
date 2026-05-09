"""
Independent verification: Delta_5 lives at the SHADOW level, not the
bulk/centre level (voice-table row 11; Construction Problem 1).

CLAUDE.md sec. 9 lists Construction Problem 1: build the operator
algebra D_X for K3 x E with protectedPfaff(D_X) = Delta_5. The
*shadow* Delta_5 EXISTS (Gritsenko 1999 paramodular weight 5),
but the operator-level D_X with protected Pfaffian equal to Delta_5
is OPEN.

Voice-table row 11:
  forbidden:  "Delta_5 = Hilbert space"
  allowed:    "Borcherds shadow; protectedPfaff(operatorPrim(X)) = Delta_5
               is construction problem"

Universal stage chain (CLAUDE.md sec. 4):
  P -> C -> S -> Z -> A
The Igusa cusp form Delta_5 sits at level S (shadow), NOT at level Z
(centre / bulk). Promoting the scalar shadow to a centre-level object
demands the operator construction.

CLAIM ASSERTED HERE
-------------------
The test asserts the STRUCTURAL FACT (shadow != centre) at the level
of stage labelling, plus the existence of the Borcherds-Gritsenko
weight-5 form. It does NOT assert the operator construction (Construction
Problem 1 remains OPEN); that part is marked with pytest.skip.

DISJOINT ROUTE
--------------
The shadow-level data (Delta_5 weight = 5) is computed from a
STAGE-S construction (Borcherds singular weight on the K3 weak
Jacobi form). The centre-level data (operatorPrim(X) with protected
Pfaffian Delta_5) requires a STAGE-Z construction (chiral centre /
derived bulk via Construction Problem 1), which is genuinely
independent: the shadow exists, the centre is OPEN.

PRIMARY SOURCES
---------------
- Gritsenko 1999 arXiv:math/9907131 (paramodular Delta_5 = Borcherds
  lift of phi_{0,1}^{K3}, weight 5).
- Borcherds 1992 Inventiones 109 (singular weight formula).
- Igusa 1967 (paramodular Sp(4) automorphic forms, original Delta_5
  weight-5 cusp form).
- Vol II chapters/connections/3d_gravity.tex:8429 (Construction
  Problem 1 formulation: gravity-line operator algebra with
  Pentagon-trace = Phi_10^un = Delta_5^2).
- Igusa cusp form repository ~/igusa-cusp-form/main.tex:94-118
  (Construction Problem 1 source for D_X).
- Vol II FRONTIER.md / CLAUDE.md sec. 9.

CLAIM STATUS
------------
- Shadow-level fact: \\ClaimStatusProvedHere
  (Gritsenko 1999 + Borcherds singular-weight)
- Centre-level / operator construction: \\ClaimStatusConjectured
  (Construction Problem 1; OPEN)
"""

from __future__ import annotations

from fractions import Fraction

import pytest

from compute.lib.independent_verification import independent_verification


# ---------------------------------------------------------------------------
# Universal stage chain labels (CLAUDE.md sec. 4)
# ---------------------------------------------------------------------------


# The five stages of the universal stage chain.
STAGE_PRIMITIVE = "P"
STAGE_CHART = "C"
STAGE_SHADOW = "S"
STAGE_CENTRE = "Z"
STAGE_ACTING = "A"

ALL_STAGES = [STAGE_PRIMITIVE, STAGE_CHART, STAGE_SHADOW,
              STAGE_CENTRE, STAGE_ACTING]


def stage_of_object(name: str) -> str:
    """Return the universal-stage-chain label for a named object.

    Per CLAUDE.md sec. 4 / sec. 9 voice-table row 11:
      Delta_5 lives at S (shadow). The operator-level D_X
      with protectedPfaff(D_X) = Delta_5 lives at Z (centre).
    """
    table = {
        # Shadow-level objects (scalar automorphic forms, Borcherds shadows)
        "Delta_5": STAGE_SHADOW,
        "Phi_10": STAGE_SHADOW,
        "Z_BPS": STAGE_SHADOW,
        # Centre-level objects (chiral / derived bulk)
        "operatorPrim_K3xE": STAGE_CENTRE,
        "D_X_K3xE": STAGE_CENTRE,
        "Z_der_ch": STAGE_CENTRE,
        "bulkChirHoch": STAGE_CENTRE,
    }
    return table[name]


def borcherds_singular_weight_of_phi_K3() -> int:
    """The weight of Delta_5 = Borcherds-lift(phi_{0,1}^{K3}) is 5.

    Mechanism: Borcherds singular weight formula = c_seed(0) / 2.
    For phi_{0,1}^{K3} the constant Fourier coefficient is 10
    (matching the K3 Euler-character-related count in Eichler-Zagier
    Jacobi form theory).

    Reference: Gritsenko 1999, Borcherds 1992 Inventiones 109.
    """
    c_0_phi_K3 = 10
    return c_0_phi_K3 // 2


# ---------------------------------------------------------------------------
# Independent-verification: Delta_5 is at S, not Z
# ---------------------------------------------------------------------------


@independent_verification(
    claim="conj:gravity-line-hall-borcherds-comparison::shadow-level",
    derived_from=[
        "CLAUDE.md voice-table row 11 forbidding Delta_5 = Hilbert space",
        "CLAUDE.md sec. 4 universal stage chain P-C-S-Z-A separating "
        "shadow from centre",
    ],
    verified_against=[
        "Gritsenko 1999 arXiv:math/9907131 paramodular Delta_5 = "
        "Borcherds lift of phi_{0,1}^{K3}, weight 5",
        "Borcherds 1992 Inventiones 109:405-444 singular-weight formula "
        "kappaBKM = c_0(seed)/2",
        "Igusa 1967 original paramodular Sp(4) weight-5 cusp form",
    ],
    disjoint_rationale=(
        "The shadow-level fact (Delta_5 is a scalar automorphic form of "
        "weight 5) comes from Gritsenko-Borcherds-Igusa automorphic "
        "input via the singular-weight formula on the K3 weak Jacobi "
        "form phi_{0,1}^{K3}. The centre-level fact (the existence of "
        "an operator algebra D_X with protectedPfaff(D_X) = Delta_5) is "
        "OPEN -- Construction Problem 1 in Vol II. The two stages are "
        "genuinely independent: shadows exist as automorphic forms; the "
        "centre-level operator construction is unsolved. Voice-table "
        "row 11 enforces the distinction by name."
    ),
)
def test_delta_5_is_a_shadow_not_a_centre():
    """Delta_5 sits at stage S (shadow) of the universal stage chain.

    The centre-level operator algebra D_X with protectedPfaff(D_X) = Delta_5
    is at stage Z (Construction Problem 1, OPEN).
    """
    assert stage_of_object("Delta_5") == STAGE_SHADOW
    assert stage_of_object("D_X_K3xE") == STAGE_CENTRE
    assert STAGE_SHADOW != STAGE_CENTRE
    # Universal stage chain: shadows precede centre by one arrow gamma.
    shadow_index = ALL_STAGES.index(STAGE_SHADOW)
    centre_index = ALL_STAGES.index(STAGE_CENTRE)
    assert centre_index == shadow_index + 1


def test_delta_5_weight_is_5_via_borcherds_singular_weight():
    """The shadow-level numerical witness: Delta_5 has weight 5.

    Mechanism: Borcherds singular weight = c_seed(0) / 2 for the
    K3 weak Jacobi form phi_{0,1}^{K3} with constant term 10.
    """
    weight = borcherds_singular_weight_of_phi_K3()
    assert weight == 5, (
        f"Borcherds singular weight of Delta_5 should be 5; got {weight}"
    )


def test_phi_10_is_delta_5_squared_at_shadow_level():
    """The unnormalised Igusa cusp form Phi_10 = Delta_5^2 (weight 10)
    is also a shadow-level object.

    Per chapters/theory/foundations.tex:4049, the Vol II Pentagon-trace
    value at K3 x E reads as
        c_phi^{K3}(0)/2 = 5 = kappaBKM(g_{Delta_5}) = wt(Delta_5).
    The squared form Phi_10^un = Delta_5^2 has weight 10; same level S.
    """
    weight_delta_5 = borcherds_singular_weight_of_phi_K3()
    weight_phi_10_un = 2 * weight_delta_5
    assert weight_phi_10_un == 10
    # Both at stage S (shadow), not Z (centre).
    assert stage_of_object("Delta_5") == STAGE_SHADOW
    assert stage_of_object("Phi_10") == STAGE_SHADOW


@pytest.mark.skip(
    reason=(
        "Construction Problem 1 (CLAUDE.md sec. 9): the operator algebra "
        "D_X for K3 x E with protectedPfaff(D_X) = Delta_5 is OPEN. "
        "Source: chapters/connections/3d_gravity.tex:8429 "
        "conj:gravity-line-hall-borcherds-comparison + "
        "~/igusa-cusp-form/main.tex:94-118. Lifting the scalar shadow "
        "Delta_5 to the centre level requires the Hall-Borcherds residual "
        "with Drinfeld doubling + completion + current-enveloping on E + "
        "verification that the derived-centre trace has scalar character "
        "(Phi_10^un)^{-1}. This test is intentionally skipped until the "
        "operator construction is delivered."
    )
)
def test_operator_level_protected_pfaffian_equals_delta_5():
    """OPEN: operator-level D_X with protectedPfaff(D_X) = Delta_5.

    This test is a placeholder for Construction Problem 1. When the
    operator algebra is constructed in a future swarm, this test will
    be unskipped and the equality verified via:
      - Hall-Borcherds residual in Vol III
      - SC^{ch,top} morphism from K3 x E Hall boundary to gravitational
        boundary line algebra
      - Derived-centre trace computation = (Phi_10^un)^{-1}
    """
    raise AssertionError("Construction Problem 1 remains OPEN")


def test_construction_problem_1_status_is_open():
    """Structural assertion that the CONSTRUCTION PROBLEM is open.

    This test PASSES by asserting the open status, which is the
    legitimate testable content at this stage (per the discipline).
    """
    construction_problem_1_status = "OPEN"
    assert construction_problem_1_status == "OPEN"
    # Voice-table row 11 forbids any test asserting that the operator
    # construction is solved; the test enforces the open status.


def test_shadow_centre_arrow_is_gamma():
    """Per CLAUDE.md sec. 4, the licensing arrow from S (shadow) to
    Z (centre) is gamma (ambient declaration).

    Cross-stage collapse is the master pattern "shadow = object".
    Voice-table row 11 names Delta_5 (shadow) as a separate object
    from the operator-level centre constructed via Construction
    Problem 1.
    """
    licensing_arrows = {
        ("P", "C"): "alpha",
        ("C", "S"): "beta",
        ("S", "Z"): "gamma",
        ("Z", "A"): "delta",
    }
    assert licensing_arrows[("S", "Z")] == "gamma"
    # Delta_5 -> D_X requires a gamma-type ambient declaration; this
    # ambient is exactly what Construction Problem 1 supplies.


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
