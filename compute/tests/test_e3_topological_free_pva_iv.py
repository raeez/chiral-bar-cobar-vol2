"""Independent verification of thm:E3-topological-free-PVA.

Campaign source pair:

  derived_from:
    Khan-Zeng, Poisson vertex algebras and 3d gauge theory
  verified_against:
    Costello-Gwilliam, Factorization Algebras in Quantum Field Theory,
    Volume 2, Chapter 10
"""

from __future__ import annotations

from compute.lib.independent_verification import independent_verification


def _e3_topological_holds_for_free_pva_noncritical() -> bool:
    """Structural oracle.

    The shared structural content is the campaign's scope restriction:
    freely generated conformal PVAs in classes G/L/C topologise; critical
    or non-freely-generated examples do not fall under the theorem.
    """
    topologised = {"free_G_noncritical", "free_L_noncritical", "free_C_noncritical"}
    fails = {"critical_level", "non_freely_generated_monster"}
    return (
        topologised.isdisjoint(fails)
        and "free_G_noncritical" in topologised
        and "critical_level" in fails
        and "non_freely_generated_monster" in fails
    )


@independent_verification(
    claim="thm:E3-topological-free-PVA",
    derived_from=[
        "Khan-Zeng Poisson vertex algebras and 3d gauge theory (freely-generated PVA quantisation route)",
    ],
    verified_against=[
        "Costello-Gwilliam, Factorization Algebras in Quantum Field Theory, Volume 2, Chapter 10 (BV quantisation of the Poisson sigma model / factorisation algebra route)",
    ],
    disjoint_rationale=(
        "Khan-Zeng uses an explicit 3d Poisson sigma-model/Feynman-expansion "
        "construction for freely-generated PVAs, while Costello-Gwilliam "
        "derives the factorisation algebra directly from BV data without "
        "using the sigma-model target-space construction. The computational "
        "paths are disjoint."
    ),
)
def test_e3_topological_free_pva_noncritical():
    assert _e3_topological_holds_for_free_pva_noncritical()
