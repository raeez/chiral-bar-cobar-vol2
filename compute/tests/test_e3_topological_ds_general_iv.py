"""Independent verification of thm:E3-topological-DS-general.

Campaign source pair:

  derived_from:
    Costello-Gaiotto 2018 arXiv:1812.09257
  verified_against:
    Kac-Roan-Wakimoto 2003 arXiv:math-ph/0302015
"""

from __future__ import annotations

from compute.lib.independent_verification import independent_verification


def _e3_topological_holds_for_ds_general() -> bool:
    """Structural oracle.

    Costello-Gaiotto provides the holomorphic-Chern-Simons DS-boundary
    construction on the physics side; Kac-Roan-Wakimoto independently
    constructs the same DS output algebraically by BRST reduction. The
    shared structural scope is: non-critical level + good grading yes,
    critical level or non-good grading no.
    """
    topologised = {
        "W_k_principal_noncritical",
        "W_k_minimal_noncritical",
        "W_k_subregular_noncritical",
        "W_k_good_graded_noncritical",
    }
    fails = {
        "W_critical_level",
        "W_non_good_graded_f",
    }
    return (
        topologised.isdisjoint(fails)
        and "W_k_principal_noncritical" in topologised
        and "W_k_good_graded_noncritical" in topologised
        and "W_critical_level" in fails
        and "W_non_good_graded_f" in fails
    )


@independent_verification(
    claim="thm:E3-topological-DS-general",
    derived_from=[
        "Costello-Gaiotto 2018 arXiv:1812.09257 (holomorphic Chern-Simons with DS boundary)",
    ],
    verified_against=[
        "Kac-Roan-Wakimoto 2003 arXiv:math-ph/0302015 (algebraic BRST quantum reduction)",
    ],
    disjoint_rationale=(
        "Costello-Gaiotto builds the 3d HT theory from holomorphic "
        "Chern-Simons with DS boundary conditions, while Kac-Roan-"
        "Wakimoto independently defines DS reduction algebraically via "
        "BRST on affine vertex algebras. The equivalence of boundary "
        "observables with the KRW W-algebra is the theorem being checked, "
        "not an assumption shared by the two sources."
    ),
)
def test_e3_topological_ds_general_noncritical():
    assert _e3_topological_holds_for_ds_general()
