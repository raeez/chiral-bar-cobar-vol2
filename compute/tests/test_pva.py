"""
Tests for PVA axiom verification.

These test that the descent from A-infinity to PVA is correct:
- Regular part of m_2 gives commutative product
- Singular part of m_2 gives lambda-bracket
- Jacobi follows from AOS cancellations
- Leibniz from outer-reg/inner-sing projection

Goal: find cases where the axioms might FAIL, not just confirm easy cases.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from sympy import Symbol, Rational, simplify, expand, S, symbols


class TestRegSingProjection:
    """Test that the regular/singular projection is well-defined."""

    def test_projection_is_idempotent(self):
        """reg(reg(f)) = reg(f), sing(sing(f)) = sing(f)."""
        from lib.spectral import LaurentSeries, reg_sing_decompose
        lam = Symbol('lambda')
        a, b = symbols('a b')
        f = LaurentSeries({-2: a, -1: b, 0: 1, 1: 2}, lam)

        reg, sing = reg_sing_decompose(f)
        reg2, _ = reg_sing_decompose(reg)
        _, sing2 = reg_sing_decompose(sing)

        assert reg == reg2
        assert sing == sing2

    def test_projection_complete(self):
        """reg(f) + sing(f) = f."""
        from lib.spectral import LaurentSeries, reg_sing_decompose
        lam = Symbol('lambda')
        a, b = symbols('a b')
        f = LaurentSeries({-2: a, -1: b, 0: 1, 1: 2}, lam)

        reg, sing = reg_sing_decompose(f)
        reconstructed = reg + sing

        for k in [-2, -1, 0, 1]:
            assert simplify(f.coeff(k) - reconstructed.coeff(k)) == 0


class TestPVAFromM2:
    """Test PVA structure arising from m_2 decomposition.

    For the free theory: m_2(a,b;lambda) = a*b (no lambda dependence).
    Regular part = a*b, singular part = 0.
    Product = a*b (commutative), lambda-bracket = 0.
    """

    def test_free_theory_product_commutative(self):
        """Product on H* from free m_2 is commutative."""
        from lib.examples.free_multiplet import product_on_cohomology
        a, b = symbols('a b')
        diff = simplify(product_on_cohomology(a, b) - product_on_cohomology(b, a))
        assert diff == 0

    def test_free_theory_product_associative(self):
        """Product from free m_2 is associative."""
        from lib.examples.free_multiplet import product_on_cohomology
        a, b, c = symbols('a b c')
        lhs = product_on_cohomology(product_on_cohomology(a, b), c)
        rhs = product_on_cohomology(a, product_on_cohomology(b, c))
        assert simplify(lhs - rhs) == 0


class TestPVASkewSymmetry:
    """Test the skew-symmetry claim for the lambda-bracket.

    Paper claim: {a_lambda b} = Asym(m_2^{sing}(a,b;lambda))
    Skew-symmetry: {a_lambda b} = -{b_{-lambda-partial} a}

    This follows from m_2 satisfying the A-infinity identity and
    the antisymmetrization procedure.
    """

    def test_virasoro_skew(self):
        """Already tested in test_examples.py but repeated here for PVA focus."""
        from lib.examples.virasoro import check_virasoro_skew_symmetry
        lam = Symbol('lambda')
        partial = Symbol('partial')
        c = Symbol('c')
        assert check_virasoro_skew_symmetry(lam, partial, c) == 0


class TestHigherMkVanishOnCohomology:
    """Test the claim that m_{k>=3} vanish on cohomology.

    Paper claim: For a, b, c in H*(A,Q), the operations m_{k>=3}
    are exact (null-homotopic), hence vanish in cohomology.

    This is one of the HARDEST claims in the paper. The proof relies
    on explicit homotopies, which are claimed but may not be fully verified.
    """

    def test_free_theory_trivial(self):
        """For free theory, m_{k>=3} = 0 at chain level, so trivially vanish."""
        from lib.examples.free_multiplet import m_k
        a, b, c = symbols('a b c')
        assert m_k(3, a, b, c) == 0

    # For LG and other interacting theories, this needs explicit homotopy
    # construction — which is a major open verification task.
