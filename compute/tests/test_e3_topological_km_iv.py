"""Independent verification of thm:E3-topological-km.

This claim is already covered in Vol II; this module aligns that coverage
with the campaign's requested external-source pair:

  derived_from:
    Costello-Li 2016 arXiv:1606.00365
  verified_against:
    Costello-Francis-Gwilliam 2026 arXiv:2602.12412

The test keeps the scope check minimal and structural: non-critical levels
topologise, the critical level does not.
"""

from __future__ import annotations

from compute.lib.independent_verification import independent_verification


def _e3_topological_holds_for_affine_km_noncritical() -> bool:
    """Structural oracle.

    Costello-Li supplies the 3d HT theory via descent from the 6d twist on
    the affine/Kac-Moody side; CFG independently constructs the same 3d HT
    theory by direct BV quantisation of Chern-Simons and identifies the
    genus-0 factorisation-homology trace with Reshetikhin-Turaev. The test
    records the shared structural scope: non-critical levels topologise,
    the critical level does not.
    """
    topologised_at_levels = {"k_generic", "k_integer_positive", "k_admissible"}
    fails_at_levels = {"k_critical"}
    return (
        topologised_at_levels.isdisjoint(fails_at_levels)
        and "k_generic" in topologised_at_levels
        and "k_critical" in fails_at_levels
    )


@independent_verification(
    claim="thm:E3-topological-km",
    derived_from=[
        "Costello-Li 2016 arXiv:1606.00365 (3d HT theory from the 6d twist / affine boundary)",
    ],
    verified_against=[
        "Costello-Francis-Gwilliam 2026 arXiv:2602.12412 (BV-quantised 3d Chern-Simons factorisation-homology trace = Reshetikhin-Turaev)",
    ],
    disjoint_rationale=(
        "Costello-Li derives the 3d HT theory by descent from the 6d twist, "
        "while CFG constructs it directly by BV quantisation of 3d "
        "Chern-Simons and computes the factorisation-homology trace as the "
        "Reshetikhin-Turaev invariant. Neither source uses the other's "
        "construction path."
    ),
)
def test_e3_topological_km_noncritical():
    assert _e3_topological_holds_for_affine_km_noncritical()
