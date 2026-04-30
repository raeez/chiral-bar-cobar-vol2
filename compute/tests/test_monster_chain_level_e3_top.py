"""Finite-orbifold checks for the Monster ``Z/2`` descent criterion.

These tests verify the exact group-cohomology normalization used in the
manuscript.  They do not compute the local BV anomaly of the FLM lift.
The Leech orbifold theorem remains conditional on supplying the local
finite-orbifold BV trivialization
``alpha_orb(sigma, sigma, sigma) = +1``.
"""

from __future__ import annotations

import pytest

from compute.lib.z2_group_cohomology import (
    IDENTITY,
    SIGMA,
    NormalizedSignCochain,
    coboundary,
    h3_bz2_u1_class_from_triple_sign,
    is_cocycle,
    normalized_h3_bz2_u1_classes,
    normalized_z2_3_cocycle,
)


def test_h3_bz2_u1_normalized_sign_representatives() -> None:
    """Normalized ``3``-cocycles are classified by the triple sign."""
    classes = normalized_h3_bz2_u1_classes()
    assert classes == {1: 0, -1: 1}

    for triple_sign, additive_class in classes.items():
        alpha = normalized_z2_3_cocycle(triple_sign)
        assert is_cocycle(alpha)
        assert alpha(SIGMA, SIGMA, SIGMA) == triple_sign
        assert alpha(IDENTITY, SIGMA, SIGMA) == 1
        assert alpha(SIGMA, IDENTITY, SIGMA) == 1
        assert alpha(SIGMA, SIGMA, IDENTITY) == 1
        assert h3_bz2_u1_class_from_triple_sign(triple_sign) == additive_class


@pytest.mark.parametrize("beta_sign", [1, -1])
def test_normalized_two_coboundaries_do_not_change_triple_sign(beta_sign: int) -> None:
    """A normalized ``2``-cochain has trivial ``3``-coboundary on
    ``(sigma, sigma, sigma)``.
    """
    beta = NormalizedSignCochain(2, {(SIGMA, SIGMA): beta_sign})
    delta_beta = coboundary(beta)
    assert delta_beta(SIGMA, SIGMA, SIGMA) == 1
    assert h3_bz2_u1_class_from_triple_sign(delta_beta(SIGMA, SIGMA, SIGMA)) == 0


def test_positive_determinant_sign_does_not_select_the_bv_class() -> None:
    """The Leech determinant sign is compatible with triviality but does
    not decide the group-cohomology class.
    """
    determinant_sign = +1
    alpha_plus = normalized_z2_3_cocycle(+1)
    alpha_minus = normalized_z2_3_cocycle(-1)

    assert determinant_sign == +1
    assert alpha_plus(SIGMA, SIGMA, SIGMA) == +1
    assert alpha_minus(SIGMA, SIGMA, SIGMA) == -1
    assert h3_bz2_u1_class_from_triple_sign(alpha_plus(SIGMA, SIGMA, SIGMA)) == 0
    assert h3_bz2_u1_class_from_triple_sign(alpha_minus(SIGMA, SIGMA, SIGMA)) == 1


def test_monster_descent_requires_local_bv_trivialization_input() -> None:
    """The descent criterion closes only after the local BV sign is
    supplied as ``+1``.
    """
    leech_parent_has_e3 = True
    finite_orbifold_bv_descent_applies = True
    flm_boundary_identification = True

    local_bv_triple_sign = +1
    local_bv_class = h3_bz2_u1_class_from_triple_sign(local_bv_triple_sign)

    criterion_hypotheses = (
        leech_parent_has_e3
        and finite_orbifold_bv_descent_applies
        and flm_boundary_identification
        and local_bv_class == 0
    )
    assert criterion_hypotheses


def test_nontrivial_local_bv_sign_blocks_the_descent_criterion() -> None:
    """The non-trivial normalized sign is exactly the obstruction class."""
    local_bv_triple_sign = -1
    local_bv_class = h3_bz2_u1_class_from_triple_sign(local_bv_triple_sign)
    assert local_bv_class == 1
    assert local_bv_class != 0


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
