"""Direct module-level coverage scaffolds for campaign-priority engines.

These tests are intentionally small. They ensure each named engine/module is
imported directly and checked against one published or structural invariant,
instead of relying on incidental coverage through broader integration suites.
"""

from __future__ import annotations

from sympy import Symbol, simplify

from compute.lib.ainfty import verify_sesquilinearity_left
from compute.lib.arnold import arnold_relation_exterior, arnold_relation_partial_fractions
from compute.lib.convention_check import verify_conventions_equivalent
from compute.lib.fm_boundary import check_stokes_term_count, count_boundary_strata
from compute.lib.genus2_ordered_bar import genus2_intersection_heisenberg
from compute.lib.laplace_bridge import verify_br3_virasoro
from compute.lib.spectral import LaurentSeries, reg_sing_decompose
from compute.lib.symbolic_stasheff import m4_T_coefficient_c_independence


def test_ainfty_left_sesquilinearity_scaffold():
    """A_infinity lambda-sesquilinearity matches the defining sign rule."""
    lam = Symbol("lam")
    bracket_base = lam + 2
    bracket_with_deriv = -lam * bracket_base
    assert simplify(
        verify_sesquilinearity_left(bracket_with_deriv, bracket_base, lam)
    ) == 0


def test_arnold_partial_fraction_scaffold():
    """Arnold vanishes on configuration space, but not in the free exterior algebra."""
    assert arnold_relation_partial_fractions(1, 2, 3) == 0
    assert not arnold_relation_exterior(1, 2, 3).is_zero()


def test_convention_check_scaffold():
    """The LV and Koszul conventions agree up to the known outer-arity sign."""
    result = verify_conventions_equivalent(4, [0, 1, 0, 1])
    assert result["relationship_holds"] is True


def test_fm_boundary_scaffold():
    """FM boundary counts match the subset formula and consecutive-block count."""
    assert count_boundary_strata(4) == 11
    term_count = check_stokes_term_count(4)
    assert term_count["match"] is True
    assert term_count["expected"] == 10


def test_genus2_ordered_bar_scaffold():
    """Heisenberg genus-2 data stays in the modular even-power regime."""
    data = genus2_intersection_heisenberg(k_val=1, max_order=3)
    props = data["structural_properties"]
    assert props["only_even_powers"] is True
    assert props["all_modular"] is True
    assert props["no_quasi_modular"] is True
    assert data["leading_term"]["coefficient"] == 3


def test_laplace_bridge_scaffold():
    """The Virasoro lambda-bracket and OPE agree under the BR3 Laplace bridge."""
    c = Symbol("c")
    z = Symbol("z")
    _, _, difference = verify_br3_virasoro(c, z)
    assert simplify(difference) == 0


def test_spectral_scaffold():
    """Regular/singular decomposition splits a Laurent series by sign of the power."""
    lam = Symbol("lam")
    series = LaurentSeries({-2: 5, -1: 3, 0: 7, 2: 11}, lam)
    regular, singular = reg_sing_decompose(series)
    assert singular.coeffs == {-2: 5, -1: 3}
    assert regular.coeffs == {0: 7, 2: 11}


def test_symbolic_stasheff_scaffold():
    """The symbolic Stasheff recursion keeps the m4 T-coefficient c-independent."""
    result = m4_T_coefficient_c_independence()
    assert result["c_independent"] is True

