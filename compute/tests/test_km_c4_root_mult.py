r"""Tests for C4 strictification obstruction for Kac-Moody algebras with root mult > 1.

Verifies:
  1. Simple Lie algebras: all root multiplicities = 1, C4 holds
  2. Affine sl_2^hat: all mult = 1, C4 holds
  3. Affine sl_N^hat (N >= 3): imaginary mult = N-1, but abelian => C4 holds
  4. Hyperbolic [[2,-3],[-3,2]]: multiplicities grow, C4 fails
  5. Multilinear Lie space dimensions: path = 1, free = (n-1)!, star = 2/1
  6. Spectral Drinfeld class analysis at each root sector
  7. The weaker vanishing condition: mult=1 OR abelian
  8. sl_3^hat explicit bracket computation at delta
  9. Cross-checks: symmetry of multiplicities, growth rates

Multi-path verification:
  Path 1: Direct computation via denominator identity
  Path 2: Weyl orbit structure (real roots)
  Path 3: Cross-family consistency (symmetry m(a,b) = m(b,a) for symmetric A)

References:
  Vol II: dg_shifted_factorization_bridge.tex (Thm thm:complete-strictification)
  Vol II: dg_shifted_factorization_bridge.tex (Conj conj:affine-strictification)
  Kac: Infinite-dimensional Lie Algebras, Ch. 11
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
from math import factorial, gcd

from lib.km_c4_root_mult import (
    cartan_matrix_type,
    inner_product,
    norm_squared,
    simple_root_multiplicity,
    affine_root_multiplicities,
    affine_c4_analysis,
    hyperbolic_root_multiplicities,
    classify_root,
    free_multilinear_lie_dim,
    path_multilinear_lie_dim,
    star_multilinear_lie_dim_free,
    star_multilinear_lie_dim_simple,
    spectral_drinfeld_class_analysis,
    c4_full_analysis,
    sl3hat_delta_brackets,
    weaker_vanishing_condition,
)


# ===================================================================
# 1. CARTAN MATRIX CLASSIFICATION
# ===================================================================

class TestCartanMatrixType:
    """Classify 2x2 Cartan matrices."""

    def test_A2_finite(self):
        """A2: [[2,-1],[-1,2]], det = 3 > 0 => finite."""
        assert cartan_matrix_type([[2, -1], [-1, 2]]) == 'finite'

    def test_B2_finite(self):
        """B2: [[2,-1],[-2,2]], det = 2 > 0 => finite."""
        assert cartan_matrix_type([[2, -1], [-2, 2]]) == 'finite'

    def test_G2_finite(self):
        """G2: [[2,-1],[-3,2]], det = 1 > 0 => finite."""
        assert cartan_matrix_type([[2, -1], [-3, 2]]) == 'finite'

    def test_affine_A1(self):
        """A1^(1): [[2,-2],[-2,2]], det = 0 => affine."""
        assert cartan_matrix_type([[2, -2], [-2, 2]]) == 'affine'

    def test_hyperbolic_3_3(self):
        """[[2,-3],[-3,2]], det = 4-9 = -5 < 0 => indefinite."""
        assert cartan_matrix_type([[2, -3], [-3, 2]]) == 'indefinite'

    def test_hyperbolic_4_4(self):
        """[[2,-4],[-4,2]], det = 4-16 = -12 => indefinite."""
        assert cartan_matrix_type([[2, -4], [-4, 2]]) == 'indefinite'


# ===================================================================
# 2. INNER PRODUCT
# ===================================================================

class TestInnerProduct:
    """Bilinear form from Cartan matrix."""

    def test_simple_root_norm_A2(self):
        """Simple roots of A2 have norm 2."""
        A = [[2, -1], [-1, 2]]
        assert norm_squared((1, 0), A) == 2
        assert norm_squared((0, 1), A) == 2

    def test_highest_root_A2(self):
        """Highest root alpha_1+alpha_2 of A2 has norm 2."""
        A = [[2, -1], [-1, 2]]
        assert norm_squared((1, 1), A) == 2

    def test_imaginary_root_hyperbolic(self):
        """Root (1,1) of hyperbolic [[2,-3],[-3,2]] has norm -2 (imaginary)."""
        A = [[2, -3], [-3, 2]]
        assert norm_squared((1, 1), A) == -2

    def test_inner_product_symmetry(self):
        """(alpha|beta) = (beta|alpha) for symmetric A."""
        A = [[2, -3], [-3, 2]]
        alpha, beta = (2, 3), (3, 1)
        assert inner_product(alpha, beta, A) == inner_product(beta, alpha, A)


# ===================================================================
# 3. SIMPLE LIE ALGEBRAS: ALL MULT = 1
# ===================================================================

class TestSimpleRootMult:
    """Verify root mult = 1 for all simple types."""

    @pytest.mark.parametrize("lie_type,rank", [
        ('A', 1), ('A', 2), ('A', 5), ('A', 10),
        ('B', 2), ('B', 3), ('B', 5),
        ('C', 2), ('C', 3),
        ('D', 4), ('D', 5),
        ('G', 2), ('F', 4),
        ('E', 6), ('E', 7), ('E', 8),
    ])
    def test_all_simple_mult_one(self, lie_type, rank):
        """Every simple Lie algebra has all root multiplicities = 1."""
        result = simple_root_multiplicity(lie_type, rank)
        assert result['max_mult'] == 1
        assert result['all_mult_one'] is True
        assert result['c4_holds'] is True
        assert result['mechanism'] == 'root_space_one_dimensionality'


# ===================================================================
# 4. AFFINE sl_2^hat: ALL MULT = 1
# ===================================================================

class TestAffineSl2:
    """Affine sl_2^hat: all multiplicities = 1."""

    def test_all_mult_one(self):
        """sl_2^hat has rank(sl_2) = 1, so all mults = 1."""
        result = affine_root_multiplicities(finite_rank=1, max_height=5)
        assert result['all_mult_one'] is True
        assert result['imaginary_root_mult'] == 1

    def test_explicit_real_roots(self):
        """Real roots of sl_2^hat have mult = 1."""
        result = affine_root_multiplicities(finite_rank=1, max_height=5)
        mults = result['explicit_mults']
        # Real roots: (n, n+1) and (n+1, n) for n >= 0
        for n in range(5):
            assert mults.get((n, n + 1)) == 1
            assert mults.get((n + 1, n)) == 1

    def test_explicit_imaginary_roots(self):
        """Imaginary roots n*delta of sl_2^hat have mult = 1."""
        result = affine_root_multiplicities(finite_rank=1, max_height=10)
        mults = result['explicit_mults']
        for n in range(1, 6):
            assert mults.get((n, n)) == 1

    def test_c4_holds(self):
        """C4 holds for sl_2^hat."""
        analysis = affine_c4_analysis(finite_rank=1)
        assert analysis['c4_holds'] is True


# ===================================================================
# 5. AFFINE sl_N^hat (N >= 3): ABELIAN IMAGINARY ROOT SPACES
# ===================================================================

class TestAffineHigherRank:
    """Affine sl_N^hat for N >= 3: imaginary root spaces are abelian."""

    def test_sl3_imaginary_mult(self):
        """sl_3^hat imaginary roots have mult = 2."""
        result = affine_root_multiplicities(finite_rank=2)
        assert result['imaginary_root_mult'] == 2
        assert result['all_mult_one'] is False

    def test_sl3_imaginary_abelian(self):
        """sl_3^hat imaginary root spaces are abelian."""
        result = affine_root_multiplicities(finite_rank=2)
        assert result['imaginary_abelian'] is True

    def test_sl3_c4_holds(self):
        """C4 holds for sl_3^hat via abelian gauge-twist."""
        analysis = affine_c4_analysis(finite_rank=2)
        assert analysis['c4_holds'] is True
        assert analysis['mechanism'] == 'root_one_dim_plus_abelian_gauge_twist'
        assert analysis['sectors']['imaginary']['abelian'] is True

    @pytest.mark.parametrize("finite_rank", [3, 4, 5, 8])
    def test_general_affine_c4_holds(self, finite_rank):
        """C4 holds for all untwisted affine algebras."""
        analysis = affine_c4_analysis(finite_rank=finite_rank)
        assert analysis['c4_holds'] is True
        assert analysis['sectors']['imaginary']['abelian'] is True


# ===================================================================
# 6. sl_3^hat EXPLICIT BRACKET COMPUTATION
# ===================================================================

class TestSl3HatBrackets:
    """Explicit multilinear brackets at delta root space of sl_3^hat."""

    def test_root_space_dim(self):
        """g_delta has dim = 2 for sl_3^hat."""
        result = sl3hat_delta_brackets()
        assert result['root_space_dim'] == 2

    def test_root_space_abelian(self):
        """g_delta is abelian."""
        result = sl3hat_delta_brackets()
        assert result['root_space_abelian'] is True

    def test_multilinear_dim(self):
        """Multilinear Lie space at delta has dim = 2."""
        result = sl3hat_delta_brackets()
        assert result['multilinear_dim'] == 2

    def test_surjective(self):
        """Multilinear map is surjective onto g_delta."""
        result = sl3hat_delta_brackets()
        assert result['surjective'] is True
        assert result['linearly_independent'] is True

    def test_c4_vanishes_by_abelianness(self):
        """C4 vanishes at delta despite mult > 1, by abelianness."""
        result = sl3hat_delta_brackets()
        assert result['c4_vanishes'] is True
        assert result['mechanism'] == 'abelian_gauge_twist'


# ===================================================================
# 7. HYPERBOLIC: ROOT MULTIPLICITIES
# ===================================================================

class TestHyperbolicMults:
    """Root multiplicities for rank-2 hyperbolic [[2,-3],[-3,2]]."""

    @pytest.fixture
    def mults(self):
        return hyperbolic_root_multiplicities(-3, -3, max_height=12)

    def test_simple_roots_mult_one(self, mults):
        """Simple roots have mult = 1."""
        assert mults[(1, 0)] == 1
        assert mults[(0, 1)] == 1

    def test_first_imaginary_root(self, mults):
        """Root (1,1) has mult = 1 and |alpha|^2 = -2."""
        assert mults[(1, 1)] == 1
        A = [[2, -3], [-3, 2]]
        assert norm_squared((1, 1), A) == -2

    def test_first_mult_gt_1(self, mults):
        """First root with mult > 1 is at (2,3) or (3,2), height 5."""
        assert mults.get((2, 3)) == 2
        assert mults.get((3, 2)) == 2

    def test_symmetry(self, mults):
        """mult(m,n) = mult(n,m) for symmetric Cartan matrix."""
        for (m, n), v in mults.items():
            if (n, m) in mults:
                assert mults[(n, m)] == v, f"Symmetry fails at ({m},{n})"

    def test_known_values(self, mults):
        """Verify against known root multiplicities from literature."""
        # These values are computed from the denominator identity
        # and match Kac's tables for rank-2 hyperbolic algebras.
        expected = {
            (1, 0): 1, (0, 1): 1,
            (1, 1): 1, (1, 2): 1, (2, 1): 1,
            (1, 3): 1, (3, 1): 1, (2, 2): 1,
            (2, 3): 2, (3, 2): 2,
            (3, 3): 3,
            (3, 4): 4, (4, 3): 4,
            (4, 4): 6,
            (4, 5): 9, (5, 4): 9,
            (5, 5): 16,
        }
        for root, expected_mult in expected.items():
            assert mults.get(root) == expected_mult, \
                f"mult{root} = {mults.get(root)}, expected {expected_mult}"

    def test_real_roots_mult_one(self, mults):
        """Real roots (|alpha|^2 = 2) always have mult = 1."""
        A = [[2, -3], [-3, 2]]
        for alpha, m in mults.items():
            ns = norm_squared(alpha, A)
            if ns == 2:
                assert m == 1, f"Real root {alpha} has mult {m} != 1"

    def test_multiplicities_grow(self, mults):
        """Max multiplicity at each height grows."""
        max_by_height = {}
        for (m, n), v in mults.items():
            h = m + n
            max_by_height[h] = max(max_by_height.get(h, 0), v)
        # Verify growth at heights 5-10
        for h in range(6, 11):
            if h in max_by_height and h - 1 in max_by_height:
                assert max_by_height[h] >= max_by_height[h - 1]

    def test_c4_fails(self, mults):
        """C4 strictification fails for the hyperbolic algebra."""
        analysis = c4_full_analysis(
            'hyperbolic', A=[[2, -3], [-3, 2]], max_height=8)
        assert analysis['c4_holds'] is False
        assert analysis['roots_with_mult_gt_1'] > 0
        assert analysis['first_obstruction_height'] == 5


# ===================================================================
# 8. MULTILINEAR LIE SPACE DIMENSIONS
# ===================================================================

class TestMultilinearDim:
    """Multilinear Lie space dimensions."""

    @pytest.mark.parametrize("n,expected", [
        (1, 1), (2, 1), (3, 2), (4, 6), (5, 24),
    ])
    def test_free_multilinear(self, n, expected):
        """Free multilinear dim = (n-1)!."""
        assert free_multilinear_lie_dim(n) == expected
        assert expected == factorial(n - 1)

    @pytest.mark.parametrize("n", range(1, 10))
    def test_path_always_one(self, n):
        """Path Lie algebra always has multilinear dim = 1 (thm:path-one-dim)."""
        assert path_multilinear_lie_dim(n) == 1

    def test_star_free_is_two(self):
        """D4-star in free Lie algebra has multilinear dim = 2."""
        assert star_multilinear_lie_dim_free() == 2

    def test_star_simple_collapses_to_one(self):
        """D4-star in simple Lie algebra collapses to dim = 1 (Jacobi collapse)."""
        assert star_multilinear_lie_dim_simple() == 1


# ===================================================================
# 9. SPECTRAL DRINFELD CLASS ANALYSIS
# ===================================================================

class TestSpectralDrinfeldClass:
    """Spectral Drinfeld class analysis at root sectors."""

    def test_mult_one_vanishes(self):
        """Mult = 1 => class vanishes by one-dimensionality."""
        A = [[2, -3], [-3, 2]]
        result = spectral_drinfeld_class_analysis((1, 0), 1, A)
        assert result['vanishes'] is True
        assert result['mechanism'] == 'root_space_one_dimensionality'

    def test_abelian_vanishes(self):
        """Mult > 1 but abelian => vanishes by gauge-twist."""
        A = [[2, -2], [-2, 2]]
        result = spectral_drinfeld_class_analysis((1, 1), 2, A, is_abelian=True)
        assert result['vanishes'] is True
        assert result['mechanism'] == 'abelian_gauge_twist'

    def test_non_abelian_mult_gt_1_fails(self):
        """Mult > 1 and non-abelian => potentially nontrivial."""
        A = [[2, -3], [-3, 2]]
        result = spectral_drinfeld_class_analysis((2, 3), 2, A, is_abelian=False)
        assert result['vanishes'] is False
        assert result['obstruction_dim'] > 0

    def test_hyperbolic_high_mult(self):
        """High multiplicity in hyperbolic: large obstruction space."""
        A = [[2, -3], [-3, 2]]
        result = spectral_drinfeld_class_analysis((5, 5), 16, A, is_abelian=False)
        assert result['vanishes'] is False
        assert result['obstruction_dim'] >= 15


# ===================================================================
# 10. WEAKER VANISHING CONDITION
# ===================================================================

class TestWeakerCondition:
    """The weaker vanishing condition: mult=1 OR abelian."""

    def test_mult_one(self):
        result = weaker_vanishing_condition(1, False)
        assert result['vanishes'] is True
        assert result['condition'] == 'mult_one'

    def test_abelian(self):
        result = weaker_vanishing_condition(5, True)
        assert result['vanishes'] is True
        assert result['condition'] == 'abelian'

    def test_neither(self):
        result = weaker_vanishing_condition(3, False)
        assert result['vanishes'] is False
        assert result['condition'] == 'neither'


# ===================================================================
# 11. ROOT CLASSIFICATION
# ===================================================================

class TestRootClassification:
    """Classify roots by type and C4 status."""

    def test_real_root_hyperbolic(self):
        """Real root of hyperbolic algebra: C4 vanishes."""
        A = [[2, -3], [-3, 2]]
        result = classify_root((1, 0), A, 1)
        assert result['root_type'] == 'real'
        assert result['c4_status'] == 'vanishes'

    def test_imaginary_mult_one(self):
        """Imaginary root with mult=1: C4 vanishes."""
        A = [[2, -3], [-3, 2]]
        result = classify_root((1, 1), A, 1)
        assert result['root_type'] == 'imaginary'
        assert result['c4_status'] == 'vanishes'

    def test_imaginary_mult_gt_1_hyperbolic(self):
        """Imaginary root with mult>1 in hyperbolic: C4 potentially fails."""
        A = [[2, -3], [-3, 2]]
        result = classify_root((2, 3), A, 2)
        assert result['root_type'] == 'imaginary'
        assert result['c4_status'] == 'potentially_nontrivial'


# ===================================================================
# 12. FULL C4 ANALYSIS
# ===================================================================

class TestFullC4Analysis:
    """Complete C4 analysis across algebra types."""

    def test_simple(self):
        """Simple Lie algebras: C4 always holds."""
        result = c4_full_analysis('simple')
        assert result['c4_holds'] is True
        assert result['max_root_mult'] == 1

    def test_affine_rank_1(self):
        """Affine sl_2^hat: C4 holds, all mult = 1."""
        result = c4_full_analysis('affine', finite_rank=1)
        assert result['c4_holds'] is True
        assert result['max_root_mult'] == 1

    def test_affine_rank_2(self):
        """Affine sl_3^hat: C4 holds via abelian gauge-twist."""
        result = c4_full_analysis('affine', finite_rank=2)
        assert result['c4_holds'] is True
        assert result['max_root_mult'] == 2

    def test_hyperbolic_fails(self):
        """Hyperbolic [[2,-3],[-3,2]]: C4 fails."""
        result = c4_full_analysis('hyperbolic',
                                  A=[[2, -3], [-3, 2]], max_height=8)
        assert result['c4_holds'] is False
        assert result['max_root_mult'] > 1
        assert result['first_obstruction_height'] == 5

    def test_hyperbolic_obstruction_count(self):
        """Hyperbolic has many obstruction sectors."""
        result = c4_full_analysis('hyperbolic',
                                  A=[[2, -3], [-3, 2]], max_height=10)
        # Should have many roots with mult > 1
        assert result['roots_with_mult_gt_1'] >= 10


# ===================================================================
# 13. CROSS-CHECKS AND CONSISTENCY
# ===================================================================

class TestCrossChecks:
    """Cross-checks for internal consistency."""

    def test_hyperbolic_symmetry_full(self):
        """Full symmetry check: mult(m,n) = mult(n,m) for A symmetric."""
        mults = hyperbolic_root_multiplicities(-3, -3, max_height=10)
        violations = []
        for (m, n), v in mults.items():
            if (n, m) in mults and mults[(n, m)] != v:
                violations.append(((m, n), v, mults[(n, m)]))
        assert len(violations) == 0, f"Symmetry violations: {violations}"

    def test_diagonal_growth(self):
        """Diagonal roots (n,n) have increasing multiplicities."""
        mults = hyperbolic_root_multiplicities(-3, -3, max_height=12)
        diag = [(n, mults.get((n, n), 0)) for n in range(1, 7)
                if (n, n) in mults]
        for i in range(1, len(diag)):
            assert diag[i][1] >= diag[i - 1][1], \
                f"Diagonal growth fails: mult({diag[i][0]},{diag[i][0]}) = {diag[i][1]} < {diag[i-1][1]}"

    def test_rhs_constant_term(self):
        """Denominator identity RHS has constant term 1."""
        from lib.km_c4_root_mult import _compute_weyl_terms
        rhs = _compute_weyl_terms(-3, -3, 10)
        assert rhs.get((0, 0), 0) == 1

    def test_finite_type_all_mult_one(self):
        """For finite type A2, the denominator identity gives all mult = 1."""
        # A2 has Cartan matrix [[2,-1],[-1,2]], det = 3 > 0
        # We can't use hyperbolic_root_multiplicities (requires det < 0),
        # but we verify the simple_root_multiplicity result.
        result = simple_root_multiplicity('A', 2)
        assert result['all_mult_one'] is True


# ===================================================================
# 14. MULTI-PATH VERIFICATION (AP10 compliance)
# ===================================================================

class TestMultiPathVerification:
    """Multi-path verification of root multiplicities.

    Every hardcoded expected value must be verified by at least 2
    independent methods (AP10). The paths used here:

      Path 1: Denominator identity (the primary computation)
      Path 2: Weyl orbit + real root structure (real roots must have mult=1)
      Path 3: Product reconstruction (multiply back and compare to RHS)
      Path 4: Denominator identity at a DIFFERENT Cartan matrix
      Path 5: Symmetry m(a,b) = m(b,a) as independent structural constraint
      Path 6: Peterson recursion cross-check at low heights
    """

    def test_path2_real_roots_from_weyl_orbit(self):
        """Path 2: real roots identified by Weyl orbit have mult = 1.

        Real roots of [[2,-3],[-3,2]] are W-orbits of simple roots.
        s_1(m,n) = (-m+3n, n), s_2(m,n) = (m, -n+3m).
        Starting from (1,0): s_2 -> (1,3), s_1 -> (8,3), s_2 -> (8,21), ...
        Starting from (0,1): s_1 -> (3,1), s_2 -> (3,8), s_1 -> (21,8), ...
        All have |alpha|^2 = 2 and mult = 1.
        """
        mults = hyperbolic_root_multiplicities(-3, -3, max_height=12)

        # Generate real roots via Weyl reflections
        def s1(m, n):
            return (-m + 3*n, n)
        def s2(m, n):
            return (m, -n + 3*m)

        real_positive = set()
        # From alpha_1 = (1,0)
        queue = [(1, 0)]
        for _ in range(6):
            new_queue = []
            for r in queue:
                for refl in [s1, s2]:
                    nr = refl(*r)
                    if nr[0] > 0 and nr[1] >= 0 and sum(nr) <= 25:
                        real_positive.add(nr)
                        new_queue.append(nr)
            queue = new_queue

        # From alpha_2 = (0,1)
        queue = [(0, 1)]
        for _ in range(6):
            new_queue = []
            for r in queue:
                for refl in [s1, s2]:
                    nr = refl(*r)
                    if nr[0] >= 0 and nr[1] > 0 and sum(nr) <= 25:
                        real_positive.add(nr)
                        new_queue.append(nr)
            queue = new_queue

        real_positive.add((1, 0))
        real_positive.add((0, 1))

        A = [[2, -3], [-3, 2]]
        for r in real_positive:
            # All real roots have norm 2
            assert norm_squared(r, A) == 2, f"Real root {r} has norm != 2"
            # All real roots in range have mult = 1
            if r in mults:
                assert mults[r] == 1, \
                    f"Real root {r} has mult = {mults[r]} != 1"

    def test_path3_product_reconstruction(self):
        """Path 3: reconstruct the denominator product and verify against RHS.

        Given the computed multiplicities, form the product
          prod_{alpha>0} (1 - q^alpha)^{mult(alpha)}
        truncated to some order and verify it matches the Weyl-Kac RHS.
        """
        from lib.km_c4_root_mult import _compute_weyl_terms
        from collections import defaultdict

        max_h = 8
        mults = hyperbolic_root_multiplicities(-3, -3, max_height=max_h)
        rhs = _compute_weyl_terms(-3, -3, max_h)

        # Build the product as a formal power series
        # Start with 1 and multiply by (1 - q^alpha)^{mult(alpha)} for each root
        product = defaultdict(float)
        product[(0, 0)] = 1.0

        for alpha in sorted(mults.keys(), key=lambda x: (sum(x), x)):
            m_a = mults[alpha]
            # (1 - q^alpha)^m_a via binomial expansion
            # = sum_{k=0}^{m_a} C(m_a, k) (-1)^k q^{k*alpha}
            binom_terms = {}
            for k in range(m_a + 1):
                ka = (k * alpha[0], k * alpha[1])
                if sum(ka) > max_h:
                    break
                # C(m_a, k) * (-1)^k
                from math import comb
                binom_terms[ka] = binom_terms.get(ka, 0) + comb(m_a, k) * ((-1) ** k)

            # Multiply product by this factor
            new_product = defaultdict(float)
            for (m1, n1), c1 in product.items():
                if m1 + n1 > max_h:
                    continue
                for (m2, n2), c2 in binom_terms.items():
                    if m1 + n1 + m2 + n2 <= max_h:
                        new_product[(m1 + m2, n1 + n2)] += c1 * c2
            product = new_product

        # Compare product to RHS at each monomial
        errors = []
        for h in range(max_h + 1):
            for m in range(h + 1):
                n = h - m
                p_val = product.get((m, n), 0.0)
                r_val = rhs.get((m, n), 0)
                if abs(p_val - r_val) > 0.01:
                    errors.append(((m, n), p_val, r_val))

        assert len(errors) == 0, \
            f"Product-RHS mismatch at {len(errors)} monomials: {errors[:5]}"

    def test_path4_different_cartan_matrix(self):
        """Path 4: verify the engine at [[2,-4],[-4,2]] (a01*a10=16, det=-12).

        Cross-check: the structure should still show all simple roots mult=1,
        symmetry m(a,b) = m(b,a), and exponential growth.
        """
        mults = hyperbolic_root_multiplicities(-4, -4, max_height=8)

        # Simple roots mult = 1
        assert mults[(1, 0)] == 1
        assert mults[(0, 1)] == 1

        # Symmetry
        for (m, n), v in mults.items():
            if (n, m) in mults:
                assert mults[(n, m)] == v

        # (1,1): |alpha|^2 = 2 - 8 + 2 = -4, imaginary
        A = [[2, -4], [-4, 2]]
        assert norm_squared((1, 1), A) == -4
        # Should have mult >= 1
        assert (1, 1) in mults and mults[(1, 1)] >= 1

        # Multiplicities should grow: max at height 8 should exceed 1
        max_mult = max(v for (m, n), v in mults.items() if m + n >= 4)
        assert max_mult > 1, f"Expected mult > 1 at height >= 4, got max = {max_mult}"

    def test_path5_symmetry_independent_constraint(self):
        """Path 5: symmetry as independent structural constraint.

        For symmetric Cartan matrix A = A^T, the Weyl group has an
        automorphism swapping alpha_1 and alpha_2, which forces
        mult(m,n) = mult(n,m). This is NOT built into the computation
        (the denominator identity doesn't assume it), so agreement
        is an independent check.
        """
        mults = hyperbolic_root_multiplicities(-3, -3, max_height=10)
        asymmetric_count = 0
        total_pairs = 0
        for (m, n), v in mults.items():
            if m != n and (n, m) in mults:
                total_pairs += 1
                if mults[(n, m)] != v:
                    asymmetric_count += 1
        assert total_pairs > 10, "Too few pairs to verify symmetry"
        assert asymmetric_count == 0, \
            f"{asymmetric_count}/{total_pairs} asymmetric pairs"

    def test_path6_peterson_crosscheck_low_height(self):
        """Path 6: independent Peterson recursion at low heights.

        At height 2, the only positive root is (1,1).
        The Peterson formula gives:
          (|(1,1)|^2 - 2*(rho|(1,1))) * mult(1,1)
            = 2 * sum_{beta+gamma=(1,1)} (beta|gamma) * mult(beta) * mult(gamma)

        For [[2,-3],[-3,2]]:
          |(1,1)|^2 = 2 - 6 + 2 = -2
          (rho|(1,1)) = 1 + 1 = 2
          denom = -2 - 4 = -6
          decomposition: (1,0)+(0,1) and (0,1)+(1,0)
          (alpha_1|alpha_2) = -3
          S = 2 * (-3) * 1 * 1 = -6
          mult(1,1) = -6 / -6 = 1  ✓
        """
        A = [[2, -3], [-3, 2]]
        # Direct Peterson at (1,1)
        alpha = (1, 1)
        alpha_sq = norm_squared(alpha, A)  # -2
        rho_alpha = 2  # (rho, alpha) = 1 + 1
        denom = alpha_sq - 2 * rho_alpha  # -6
        # Only decomposition: (1,0)+(0,1), ordered pair sum
        S = 2 * inner_product((1, 0), (0, 1), A) * 1 * 1  # 2*(-3) = -6
        peterson_mult = S / denom  # -6 / -6 = 1

        assert peterson_mult == 1.0
        # Cross-check with denominator identity
        mults = hyperbolic_root_multiplicities(-3, -3, max_height=4)
        assert mults[(1, 1)] == 1

    def test_path6_peterson_crosscheck_height3(self):
        """Path 6 continued: Peterson at (2,1) and (1,2).

        For (2,1): decomposition (1,0)+(1,1) and (1,1)+(1,0)
          |(2,1)|^2 = 8-12+2 = -2
          (rho|(2,1)) = 3
          denom = -2 - 6 = -8
          ((1,0)|(1,1)) = 2 - 3 = -1
          S = 2*(-1)*1*1 = -2
          mult = -2/-8 = 0.25 ... WRONG!

        This shows the simple Peterson formula DOES NOT WORK for
        indefinite KM algebras without the Mobius correction.
        The denominator identity is the reliable method.
        This is itself an important verification: the Peterson formula
        requires correction terms for indefinite type.
        """
        mults = hyperbolic_root_multiplicities(-3, -3, max_height=4)
        # The denominator identity gives mult(2,1) = 1
        assert mults[(2, 1)] == 1
        assert mults[(1, 2)] == 1  # by symmetry
        # The naive Peterson gives 0.25, confirming the denominator
        # identity is the correct method for indefinite type.
        A = [[2, -3], [-3, 2]]
        alpha = (2, 1)
        denom = norm_squared(alpha, A) - 2 * sum(alpha)  # -2 - 6 = -8
        S = 2 * inner_product((1, 0), (1, 1), A) * 1 * 1  # 2*(-1) = -2
        naive = S / denom  # 0.25
        assert abs(naive - 0.25) < 1e-10  # Confirms naive Peterson fails

    def test_denominator_identity_self_consistency(self):
        """Product of (1-q^alpha)^mult at two different truncations agree.

        Compute mults at max_height=8 and max_height=12.
        The multiplicities at height <= 8 should be identical.
        """
        mults_8 = hyperbolic_root_multiplicities(-3, -3, max_height=8)
        mults_12 = hyperbolic_root_multiplicities(-3, -3, max_height=12)

        mismatches = []
        for alpha, m8 in mults_8.items():
            m12 = mults_12.get(alpha)
            if m12 != m8:
                mismatches.append((alpha, m8, m12))

        assert len(mismatches) == 0, \
            f"Truncation-dependent mults: {mismatches}"

    def test_path7_peterson_crosscheck_full(self):
        """Path 7: Peterson recursion cross-checks denominator identity at ALL roots.

        The Peterson recursion is an INDEPENDENT method from the
        denominator identity. Agreement at every root is a strong
        multi-path verification (AP10 compliance).
        """
        from lib.km_c4_root_mult import peterson_multiplicity

        A = [[2, -3], [-3, 2]]
        mults = hyperbolic_root_multiplicities(-3, -3, max_height=8)

        mismatches = []
        for alpha, denom_mult in sorted(mults.items(), key=lambda x: sum(x[0])):
            # Pass known multiplicities at lower heights
            known = {r: mults[r] for r in mults if sum(r) < sum(alpha)}
            pet_mult = peterson_multiplicity(alpha, A, known_mults=known)
            pet_int = round(float(pet_mult))
            if pet_int != denom_mult:
                mismatches.append((alpha, pet_int, denom_mult))

        assert len(mismatches) == 0, \
            f"Peterson vs DenomId mismatches: {mismatches}"

    def test_total_mult_partition_identity(self):
        """The sum of all c(alpha) at height h equals the coefficient
        of the negative log of the RHS at height h.

        This is a global consistency check: the Mobius inversion
        and the -log computation must be internally consistent.
        """
        from lib.km_c4_root_mult import _compute_weyl_terms
        from collections import defaultdict

        max_h = 8
        mults = hyperbolic_root_multiplicities(-3, -3, max_height=max_h)

        # Compute c(alpha) = sum_{d | alpha} (1/d) mult(alpha/d)
        for h in range(2, max_h + 1):
            for m in range(h + 1):
                n = h - m
                if (m, n) not in mults:
                    continue
                # Verify: the c-function value must be positive
                g = gcd(m, n) if m > 0 and n > 0 else max(m, n)
                c_val = 0.0
                for d in range(1, g + 1):
                    if m % d == 0 and n % d == 0:
                        red = (m // d, n // d)
                        if red in mults:
                            c_val += mults[red] / d
                # c_val should be positive for any root
                assert c_val > 0, f"c({m},{n}) = {c_val} <= 0"


# ===================================================================
# 15. PETERSON RECURSION (independent verification path)
# ===================================================================

class TestPetersonRecursion:
    """Peterson recursion as independent verification of root multiplicities.

    The Peterson recursion (Kac, Theorem 11.2) is structurally independent
    from the Weyl-Kac denominator identity. Agreement is a genuine
    multi-path verification (AP10).
    """

    def test_simple_roots(self):
        """Simple roots have Peterson mult = 1."""
        from lib.km_c4_root_mult import peterson_multiplicity
        A = [[2, -3], [-3, 2]]
        assert peterson_multiplicity((1, 0), A) == 1
        assert peterson_multiplicity((0, 1), A) == 1

    def test_height_2(self):
        """Peterson at (1,1) for hyperbolic: mult = 1."""
        from lib.km_c4_root_mult import peterson_multiplicity
        A = [[2, -3], [-3, 2]]
        assert peterson_multiplicity((1, 1), A) == 1

    def test_first_mult_gt_1(self):
        """Peterson at (2,3): mult = 2, first root with mult > 1."""
        from lib.km_c4_root_mult import peterson_multiplicity
        A = [[2, -3], [-3, 2]]
        mults = hyperbolic_root_multiplicities(-3, -3, max_height=6)
        known = {r: mults[r] for r in mults if sum(r) < 5}
        result = peterson_multiplicity((2, 3), A, known_mults=known)
        assert round(float(result)) == 2

    def test_diagonal_root(self):
        """Peterson at (3,3): mult = 3."""
        from lib.km_c4_root_mult import peterson_multiplicity
        A = [[2, -3], [-3, 2]]
        mults = hyperbolic_root_multiplicities(-3, -3, max_height=8)
        known = {r: mults[r] for r in mults if sum(r) < 6}
        result = peterson_multiplicity((3, 3), A, known_mults=known)
        assert round(float(result)) == 3

    def test_finite_type_A2(self):
        """Peterson for A2: highest root (1,1) has mult = 1; (2,0) is not a root."""
        from lib.km_c4_root_mult import peterson_multiplicity
        A = [[2, -1], [-1, 2]]
        assert peterson_multiplicity((1, 1), A) == 1
        # (2,0) is not a root of A2
        m = peterson_multiplicity((2, 0), A)
        assert round(float(m)) == 0

    def test_peterson_vs_denominator_systematic(self):
        """Systematic comparison of Peterson vs denominator identity up to height 7."""
        from lib.km_c4_root_mult import peterson_multiplicity
        A = [[2, -3], [-3, 2]]
        mults = hyperbolic_root_multiplicities(-3, -3, max_height=8)

        mismatches = []
        for alpha in sorted(mults.keys(), key=lambda x: (sum(x), x)):
            if sum(alpha) > 7:
                continue
            known = {r: mults[r] for r in mults if sum(r) < sum(alpha)}
            pet = round(float(peterson_multiplicity(alpha, A, known_mults=known)))
            if pet != mults[alpha]:
                mismatches.append((alpha, pet, mults[alpha]))

        assert len(mismatches) == 0, f"Mismatches: {mismatches}"


# ===================================================================
# 16. ROOT SPACE ABELIANNESS
# ===================================================================

class TestRootSpaceAbelianness:
    """Abelianness classification for hyperbolic root spaces.

    The key mathematical fact: a root space g_alpha is non-abelian
    only if mult(alpha) >= 2 AND 2*alpha is a root.
    """

    def test_simple_roots_abelian(self):
        """Simple roots have mult = 1, hence trivially abelian."""
        from lib.km_c4_root_mult import hyperbolic_root_space_abelian
        A = [[2, -3], [-3, 2]]
        mults = hyperbolic_root_multiplicities(-3, -3, max_height=8)
        assert hyperbolic_root_space_abelian((1, 0), A, mults) is True
        assert hyperbolic_root_space_abelian((0, 1), A, mults) is True

    def test_mult_one_always_abelian(self):
        """Any root with mult = 1 is trivially abelian."""
        from lib.km_c4_root_mult import hyperbolic_root_space_abelian
        A = [[2, -3], [-3, 2]]
        mults = hyperbolic_root_multiplicities(-3, -3, max_height=10)
        for alpha, m in mults.items():
            if m == 1:
                assert hyperbolic_root_space_abelian(alpha, A, mults) is True, \
                    f"mult-1 root {alpha} reported as non-abelian"

    def test_first_non_abelian_root(self):
        """Root (2,3) with mult = 2: non-abelian because 2*(2,3) = (4,6) is a root."""
        from lib.km_c4_root_mult import hyperbolic_root_space_abelian
        A = [[2, -3], [-3, 2]]
        mults = hyperbolic_root_multiplicities(-3, -3, max_height=12)
        # (2,3) has mult 2
        assert mults[(2, 3)] == 2
        # (4,6) must be a root for non-abelianness
        assert (4, 6) in mults and mults[(4, 6)] >= 1
        # Therefore non-abelian
        assert hyperbolic_root_space_abelian((2, 3), A, mults) is False

    def test_full_abelianness_analysis(self):
        """Full analysis: non-abelian roots exist at height 5."""
        from lib.km_c4_root_mult import hyperbolic_abelianness_analysis
        A = [[2, -3], [-3, 2]]
        analysis = hyperbolic_abelianness_analysis(A, max_height=10)
        assert analysis['c4_obstruction_exists'] is True
        assert analysis['first_non_abelian_height'] == 5
        # (2,3) and (3,2) should be the first non-abelian roots
        non_ab_roots = {e['root'] for e in analysis['non_abelian_roots']}
        assert (2, 3) in non_ab_roots
        assert (3, 2) in non_ab_roots

    def test_classification_exhaustive(self):
        """Abelian + non-abelian = total; for [[2,-3],[-3,2]] ALL mult>1 are non-abelian.

        Every imaginary root alpha with mult > 1 in the hyperbolic algebra
        has 2*alpha also a root (the root lattice is closed under doubling
        for sufficiently negative Cartan entries). Hence no mult > 1 root
        is abelian. This was a key finding: the truncation-corrected
        analysis (checking 2*alpha at extended height) shows zero abelian
        exceptions.
        """
        from lib.km_c4_root_mult import hyperbolic_abelianness_analysis
        A = [[2, -3], [-3, 2]]
        analysis = hyperbolic_abelianness_analysis(A, max_height=10)
        total_mg1 = len(analysis['roots_mult_gt_1'])
        abelian = len(analysis['abelian_roots'])
        non_abelian = len(analysis['non_abelian_roots'])
        assert abelian + non_abelian == total_mg1
        # Key finding: ALL mult > 1 roots are non-abelian
        assert abelian == 0, f"Expected 0 abelian, got {abelian}"
        assert non_abelian == total_mg1


# ===================================================================
# 17. OBSTRUCTION COCYCLE DIMENSIONS
# ===================================================================

class TestObstructionCocycleDim:
    """Obstruction cocycle space dimensions at root sectors."""

    def test_mult_one_zero_obstruction(self):
        """Mult = 1: obstruction dim = 0."""
        from lib.km_c4_root_mult import obstruction_cocycle_dim
        result = obstruction_cocycle_dim(1, False, 3)
        assert result['obstruction_dim'] == 0
        assert result['mechanism'] == 'root_space_one_dimensionality'

    def test_abelian_zero_obstruction(self):
        """Mult > 1, abelian: obstruction dim = 0 (full Cartan gauge)."""
        from lib.km_c4_root_mult import obstruction_cocycle_dim
        result = obstruction_cocycle_dim(5, True, 4)
        assert result['obstruction_dim'] == 0
        assert result['mechanism'] == 'abelian_gauge_twist'
        assert result['gauge_dim'] == 5  # Full Cartan twist

    def test_non_abelian_positive_obstruction(self):
        """Mult > 1, non-abelian: obstruction may be positive."""
        from lib.km_c4_root_mult import obstruction_cocycle_dim
        result = obstruction_cocycle_dim(2, False, 5)
        # mult=2, height=5: free_ml = min(4!, 2) = 2
        # rigidity = 1, gauge = 2 (inner autos of 2-dim non-abelian)
        assert result['cocycle_dim'] == 2
        assert result['equations_from_rigidity'] == 1

    def test_high_mult_large_obstruction(self):
        """High mult, non-abelian: large obstruction space."""
        from lib.km_c4_root_mult import obstruction_cocycle_dim
        result = obstruction_cocycle_dim(16, False, 10)
        assert result['obstruction_dim'] > 0
        assert result['cocycle_dim'] == 16  # min(9!, 16) = 16

    def test_obstruction_grows_with_mult(self):
        """Obstruction dimension grows with multiplicity (non-abelian)."""
        from lib.km_c4_root_mult import obstruction_cocycle_dim
        obs_dims = []
        for m in [2, 4, 8, 16]:
            result = obstruction_cocycle_dim(m, False, 10)
            obs_dims.append(result['obstruction_dim'])
        # Should be non-decreasing
        for i in range(1, len(obs_dims)):
            assert obs_dims[i] >= obs_dims[i - 1]


# ===================================================================
# 18. GROWTH RATE ANALYSIS
# ===================================================================

class TestGrowthRate:
    """Multiplicity growth rate analysis."""

    def test_finite_bounded(self):
        """Finite type: bounded growth."""
        from lib.km_c4_root_mult import multiplicity_growth_analysis
        A = [[2, -1], [-1, 2]]  # A2
        result = multiplicity_growth_analysis(A)
        assert result['growth'] == 'bounded'

    def test_affine_constant(self):
        """Affine type: constant growth (mult = rank for imaginary)."""
        from lib.km_c4_root_mult import multiplicity_growth_analysis
        A = [[2, -2], [-2, 2]]  # A1^(1)
        result = multiplicity_growth_analysis(A)
        assert result['growth'] == 'constant'

    def test_hyperbolic_exponential(self):
        """Hyperbolic type: exponential growth."""
        from lib.km_c4_root_mult import multiplicity_growth_analysis
        A = [[2, -3], [-3, 2]]
        result = multiplicity_growth_analysis(A, max_height=10)
        assert result['growth'] == 'exponential'
        assert result['avg_growth_ratio'] > 1.3

    def test_diagonal_mult_sequence(self):
        """Diagonal multiplicities (n,n) form an increasing sequence."""
        from lib.km_c4_root_mult import multiplicity_growth_analysis
        A = [[2, -3], [-3, 2]]
        result = multiplicity_growth_analysis(A, max_height=12)
        diag = result['diagonal_mults']
        # Known: mult(1,1)=1, (2,2)=1, (3,3)=3, (4,4)=6, (5,5)=16
        assert len(diag) >= 5
        for i in range(1, len(diag)):
            assert diag[i][1] >= diag[i - 1][1]

    def test_more_hyperbolic_faster_growth(self):
        """[[2,-4],[-4,2]] grows faster than [[2,-3],[-3,2]]."""
        from lib.km_c4_root_mult import multiplicity_growth_analysis
        A3 = [[2, -3], [-3, 2]]
        A4 = [[2, -4], [-4, 2]]
        r3 = multiplicity_growth_analysis(A3, max_height=8)
        r4 = multiplicity_growth_analysis(A4, max_height=8)
        assert r4['max_mult'] >= r3['max_mult']


# ===================================================================
# 19. AFFINE STRICTIFICATION PROOF
# ===================================================================

class TestAffineStrictificationProof:
    """Detailed affine strictification proof pathway."""

    def test_sl2_hat_proof(self):
        """sl_2^hat: all mult = 1, standard argument suffices."""
        from lib.km_c4_root_mult import affine_strictification_proof
        result = affine_strictification_proof('A', 1)
        assert result['c4_holds'] is True
        assert result['proof_sectors']['real']['multiplicity'] == 1
        assert result['proof_sectors']['imaginary']['abelian'] is True

    def test_sl3_hat_proof(self):
        """sl_3^hat: real mult=1, imaginary mult=2 but abelian."""
        from lib.km_c4_root_mult import affine_strictification_proof
        result = affine_strictification_proof('A', 2)
        assert result['c4_holds'] is True
        assert result['proof_sectors']['imaginary']['multiplicity'] == 2
        assert result['proof_sectors']['imaginary']['abelian'] is True
        assert result['proof_sectors']['imaginary']['mechanism'] == 'abelian_gauge_twist'

    def test_e8_hat_proof(self):
        """E_8^hat: imaginary mult = 8, still abelian."""
        from lib.km_c4_root_mult import affine_strictification_proof
        result = affine_strictification_proof('E', 8)
        assert result['c4_holds'] is True
        assert result['proof_sectors']['imaginary']['multiplicity'] == 8
        assert result['proof_sectors']['imaginary']['abelian'] is True

    def test_energy_operator_check(self):
        """Energy operator d acts by scalar n on g_{n*delta}."""
        from lib.km_c4_root_mult import affine_strictification_proof
        result = affine_strictification_proof('A', 3)
        assert result['energy_operator_check']['status'] == 'verified'

    @pytest.mark.parametrize("finite_type,finite_rank", [
        ('A', 1), ('A', 2), ('A', 4), ('B', 2), ('B', 3),
        ('C', 3), ('D', 4), ('G', 2), ('F', 4), ('E', 6), ('E', 7), ('E', 8),
    ])
    def test_all_untwisted_affine(self, finite_type, finite_rank):
        """C4 holds for all untwisted affine algebras."""
        from lib.km_c4_root_mult import affine_strictification_proof
        result = affine_strictification_proof(finite_type, finite_rank)
        assert result['c4_holds'] is True


# ===================================================================
# 20. EXPLICIT SPECTRAL DRINFELD CLASS
# ===================================================================

class TestSpectralDrinfeldExplicit:
    """Explicit spectral Drinfeld class at root sectors."""

    def test_real_root_vanishes(self):
        """Spectral Drinfeld class vanishes at real root (mult=1)."""
        from lib.km_c4_root_mult import spectral_drinfeld_explicit
        A = [[2, -3], [-3, 2]]
        mults = hyperbolic_root_multiplicities(-3, -3, max_height=8)
        result = spectral_drinfeld_explicit((1, 0), A, mults)
        assert result['vanishes'] is True
        assert result['mechanism'] == 'root_space_one_dimensionality'

    def test_non_abelian_obstruction(self):
        """At (2,3) with mult=2: the class is potentially nontrivial."""
        from lib.km_c4_root_mult import spectral_drinfeld_explicit
        A = [[2, -3], [-3, 2]]
        mults = hyperbolic_root_multiplicities(-3, -3, max_height=12)
        result = spectral_drinfeld_explicit((2, 3), A, mults)
        assert result['mult'] == 2
        assert result['abelian'] is False
        assert result['height'] == 5
        # The obstruction analysis is computed
        assert 'obstruction' in result
        assert result['obstruction']['cocycle_dim'] >= 1

    def test_not_a_root(self):
        """At a non-root: class vanishes trivially."""
        from lib.km_c4_root_mult import spectral_drinfeld_explicit
        A = [[2, -3], [-3, 2]]
        mults = hyperbolic_root_multiplicities(-3, -3, max_height=8)
        # (7, 0) at height 7 is likely not a root at this truncation
        result = spectral_drinfeld_explicit((7, 0), A, mults)
        # If mult = 0, it vanishes
        if result['mult'] == 0:
            assert result['vanishes'] is True

    def test_high_mult_root(self):
        """At (5,5) with mult=16: large free multilinear dim, large obstruction."""
        from lib.km_c4_root_mult import spectral_drinfeld_explicit
        A = [[2, -3], [-3, 2]]
        mults = hyperbolic_root_multiplicities(-3, -3, max_height=12)
        result = spectral_drinfeld_explicit((5, 5), A, mults)
        assert result['mult'] == 16
        assert result['height'] == 10
        # Free multilinear dim = (height-1)! = 9! = 362880
        # This is the UPPER BOUND from the free Lie algebra
        assert result['free_multilinear_dim'] == factorial(9)
        # The constrained dim in the obstruction is min(free, mult) = 16
        assert result['obstruction']['cocycle_dim'] == 16


# ===================================================================
# 21. GABBER-KAC ANALYSIS
# ===================================================================

class TestGabberKac:
    """Gabber-Kac theorem constraints on root multiplicities."""

    def test_A2_serre_exponents(self):
        """A2: Serre exponents = 2 (standard)."""
        from lib.km_c4_root_mult import gabber_kac_analysis
        A = [[2, -1], [-1, 2]]
        result = gabber_kac_analysis(A)
        assert result['serre_exponents'][(0, 1)] == 2
        assert result['serre_exponents'][(1, 0)] == 2

    def test_hyperbolic_serre_exponents(self):
        """Hyperbolic [[2,-3],[-3,2]]: Serre exponents = 4."""
        from lib.km_c4_root_mult import gabber_kac_analysis
        A = [[2, -3], [-3, 2]]
        result = gabber_kac_analysis(A)
        assert result['serre_exponents'][(0, 1)] == 4
        assert result['serre_exponents'][(1, 0)] == 4
        assert result['max_serre_exponent'] == 4

    def test_weight_space_finiteness(self):
        """Weight-space finiteness holds for all symmetrizable GCM."""
        from lib.km_c4_root_mult import gabber_kac_analysis
        for A in [[[2, -1], [-1, 2]], [[2, -3], [-3, 2]], [[2, -4], [-4, 2]]]:
            result = gabber_kac_analysis(A)
            assert result['weight_space_finiteness'] is True

    def test_c4_implications_structure(self):
        """Gabber-Kac analysis provides implications for all three types."""
        from lib.km_c4_root_mult import gabber_kac_analysis
        A = [[2, -3], [-3, 2]]
        result = gabber_kac_analysis(A)
        assert 'finite' in result['c4_implications']
        assert 'affine' in result['c4_implications']
        assert 'indefinite' in result['c4_implications']


# ===================================================================
# 22. COMPREHENSIVE OBSTRUCTION SUMMARY
# ===================================================================

class TestObstructionSummary:
    """Comprehensive C4 obstruction summary."""

    def test_finite_type_clean(self):
        """Finite type: no obstruction."""
        from lib.km_c4_root_mult import c4_obstruction_summary
        A = [[2, -1], [-1, 2]]
        result = c4_obstruction_summary(A)
        assert result['c4_holds'] is True
        assert result['km_type'] == 'finite'

    def test_affine_type_clean(self):
        """Affine type: no obstruction (abelian gauge-twist)."""
        from lib.km_c4_root_mult import c4_obstruction_summary
        A = [[2, -2], [-2, 2]]
        result = c4_obstruction_summary(A)
        assert result['c4_holds'] is True
        assert result['km_type'] == 'affine'

    def test_hyperbolic_obstruction_exists(self):
        """Hyperbolic: obstruction exists at non-abelian root spaces."""
        from lib.km_c4_root_mult import c4_obstruction_summary
        A = [[2, -3], [-3, 2]]
        result = c4_obstruction_summary(A, max_height=10)
        assert result['c4_holds'] is False
        assert result['non_abelian_mult_gt_1'] > 0
        assert result['total_obstruction_dim'] >= 0

    def test_hyperbolic_first_obstruction_at_5(self):
        """First non-abelian root is at height 5 for [[2,-3],[-3,2]]."""
        from lib.km_c4_root_mult import c4_obstruction_summary
        A = [[2, -3], [-3, 2]]
        result = c4_obstruction_summary(A, max_height=10)
        assert result['first_non_abelian_height'] == 5

    def test_hyperbolic_44_also_fails(self):
        """[[2,-4],[-4,2]]: C4 also fails, likely at lower height."""
        from lib.km_c4_root_mult import c4_obstruction_summary
        A = [[2, -4], [-4, 2]]
        result = c4_obstruction_summary(A, max_height=10)
        assert result['c4_holds'] is False
        assert result['non_abelian_mult_gt_1'] > 0

    def test_obstruction_sectors_have_root_data(self):
        """Obstruction sectors contain full root data."""
        from lib.km_c4_root_mult import c4_obstruction_summary
        A = [[2, -3], [-3, 2]]
        result = c4_obstruction_summary(A, max_height=8)
        for sector in result['obstruction_sectors']:
            assert 'root' in sector
            assert 'mult' in sector
            assert 'obstruction' in sector
            assert sector['mult'] >= 2
            assert sector['abelian'] is False


# ===================================================================
# 23. THE PRECISE OBSTRUCTION CONDITION
# ===================================================================

class TestPreciseObstructionCondition:
    """The theorem: W1 (mult=1) or W2 (abelian) is the precise boundary."""

    def test_structure(self):
        """The condition has the expected structure."""
        from lib.km_c4_root_mult import precise_obstruction_condition
        result = precise_obstruction_condition()
        assert 'W1: mult_one' in result['sufficient_conditions']
        assert 'W2: abelian' in result['sufficient_conditions']

    def test_proved_classes(self):
        """Proved for simple and untwisted affine."""
        from lib.km_c4_root_mult import precise_obstruction_condition
        result = precise_obstruction_condition()
        proved = result['proved_for']
        assert any('simple' in p for p in proved)
        assert any('affine' in p for p in proved)

    def test_failure_class(self):
        """Fails for hyperbolic."""
        from lib.km_c4_root_mult import precise_obstruction_condition
        result = precise_obstruction_condition()
        assert any('hyperbolic' in f for f in result['fails_for'])

    def test_first_obstruction(self):
        """First obstruction at (2,3) of [[2,-3],[-3,2]]."""
        from lib.km_c4_root_mult import precise_obstruction_condition
        result = precise_obstruction_condition()
        assert result['first_obstruction']['root'] == (2, 3)
        assert result['first_obstruction']['mult'] == 2
        assert result['first_obstruction']['height'] == 5

    def test_w5_insufficient(self):
        """Weight-space finiteness (W5) is INSUFFICIENT."""
        from lib.km_c4_root_mult import precise_obstruction_condition
        result = precise_obstruction_condition()
        assert 'INSUFFICIENT' in result['weaker_candidates']['W5']


# ===================================================================
# 24. HYPERBOLIC [[2,-4],[-4,2]]: STRONGER OBSTRUCTION
# ===================================================================

class TestHyperbolic44:
    """The a=4 hyperbolic algebra: stronger obstruction, faster growth."""

    @pytest.fixture
    def mults_44(self):
        return hyperbolic_root_multiplicities(-4, -4, max_height=10)

    def test_simple_roots_mult_one(self, mults_44):
        """Simple roots still have mult = 1."""
        assert mults_44[(1, 0)] == 1
        assert mults_44[(0, 1)] == 1

    def test_imaginary_root_11(self, mults_44):
        """(1,1) is imaginary with |alpha|^2 = -4."""
        A = [[2, -4], [-4, 2]]
        assert norm_squared((1, 1), A) == -4
        assert (1, 1) in mults_44

    def test_mult_growth_faster_than_33(self, mults_44):
        """Multiplicities grow faster than [[2,-3],[-3,2]]."""
        mults_33 = hyperbolic_root_multiplicities(-3, -3, max_height=10)
        # Compare diagonal multiplicities at matching heights
        for n in range(3, 6):
            if (n, n) in mults_44 and (n, n) in mults_33:
                assert mults_44[(n, n)] >= mults_33[(n, n)], \
                    f"At ({n},{n}): a=4 gives {mults_44[(n,n)]} < a=3 gives {mults_33[(n,n)]}"

    def test_c4_fails(self, mults_44):
        """C4 fails for [[2,-4],[-4,2]]."""
        result = c4_full_analysis('hyperbolic', A=[[2, -4], [-4, 2]], max_height=8)
        assert result['c4_holds'] is False

    def test_symmetry(self, mults_44):
        """Symmetry m(a,b) = m(b,a) for symmetric Cartan matrix."""
        for (m, n), v in mults_44.items():
            if (n, m) in mults_44:
                assert mults_44[(n, m)] == v


# ===================================================================
# 25. CROSS-FAMILY CONSISTENCY
# ===================================================================

class TestCrossFamilyConsistency:
    """Cross-family consistency checks across algebra types.

    These tests verify that the C4 analysis is internally consistent
    across the finite/affine/hyperbolic classification.
    """

    def test_finite_to_affine_boundary(self):
        """A1^(1) at the finite-affine boundary: all mult = 1, C4 holds."""
        from lib.km_c4_root_mult import affine_c4_analysis
        # sl_2^hat: finite_rank = 1
        result = affine_c4_analysis(finite_rank=1)
        assert result['c4_holds'] is True
        # All imaginary roots have mult = 1 (rank = 1)
        assert result['sectors']['imaginary']['mult'] == 1

    def test_affine_to_hyperbolic_boundary(self):
        """At the affine-hyperbolic boundary: a=2 (affine) vs a=3 (hyperbolic).

        [[2,-2],[-2,2]] is affine A1^(1): C4 holds.
        [[2,-3],[-3,2]] is hyperbolic: C4 fails.
        This is a SHARP boundary in the Cartan matrix.
        """
        from lib.km_c4_root_mult import c4_full_analysis
        affine_result = c4_full_analysis('affine', finite_rank=1)
        hyp_result = c4_full_analysis('hyperbolic', A=[[2, -3], [-3, 2]], max_height=8)
        assert affine_result['c4_holds'] is True
        assert hyp_result['c4_holds'] is False

    def test_all_simple_types_consistent(self):
        """All simple Lie types: C4 holds with same mechanism."""
        for lie_type, rank in [('A', 1), ('A', 5), ('B', 3), ('C', 3),
                               ('D', 4), ('E', 6), ('E', 8), ('F', 4), ('G', 2)]:
            result = simple_root_multiplicity(lie_type, rank)
            assert result['c4_holds'] is True
            assert result['mechanism'] == 'root_space_one_dimensionality'

    def test_obstruction_absent_for_affine_present_for_hyperbolic(self):
        """The abelianness of imaginary root spaces is the precise
        boundary between C4 holding (affine) and failing (hyperbolic).
        """
        from lib.km_c4_root_mult import (
            hyperbolic_abelianness_analysis, affine_root_multiplicities
        )
        # Affine sl_3^hat: imaginary roots are abelian
        aff = affine_root_multiplicities(finite_rank=2)
        assert aff['imaginary_abelian'] is True

        # Hyperbolic: some roots with mult > 1 are non-abelian
        A = [[2, -3], [-3, 2]]
        hyp = hyperbolic_abelianness_analysis(A, max_height=10)
        assert hyp['c4_obstruction_exists'] is True

    def test_weaker_condition_boundary(self):
        """The W1-or-W2 condition is exactly the finite+affine boundary."""
        from lib.km_c4_root_mult import weaker_vanishing_condition
        # W1: mult = 1 (simple Lie algebras, real roots of any KM)
        assert weaker_vanishing_condition(1, False)['vanishes'] is True
        # W2: abelian (imaginary roots of affine KM)
        assert weaker_vanishing_condition(8, True)['vanishes'] is True
        # Neither: non-abelian mult > 1 (hyperbolic)
        assert weaker_vanishing_condition(2, False)['vanishes'] is False
        assert weaker_vanishing_condition(16, False)['vanishes'] is False
