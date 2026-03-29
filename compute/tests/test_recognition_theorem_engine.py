r"""Tests for the recognition theorem engine.

Verifies the full recognition theorem pipeline:
  1. Weiss cosheaf descent for product covers
  2. Hypothesis verification (H1)-(H4) for all 7 Vol II examples
  3. Reconstruction of chiral + topological + coupling
  4. R-direction isotopy (local constancy)
  5. C-direction factorization
  6. Mixed coupling extraction
  7. Full pipeline consistency

References:
  Vol II: thm:recognition-SC, lem:product-weiss-descent, foundations.tex
  recognition_theorem_engine.py
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from sympy import Symbol, Rational, simplify, S


# ===================================================================
# 1. OPEN SET OPERATIONS
# ===================================================================

class TestOpenSets:
    """Test basic open set geometry."""

    def test_open_set_containment(self):
        """Point inside an open set."""
        from lib.recognition_theorem_engine import OpenSet
        U = OpenSet(0, 1, 0, 1, label='unit square')
        assert U.contains_point(Rational(1, 2), Rational(1, 2))

    def test_open_set_boundary_exclusion(self):
        """Points on the boundary are NOT inside (open set)."""
        from lib.recognition_theorem_engine import OpenSet
        U = OpenSet(0, 1, 0, 1)
        assert not U.contains_point(0, Rational(1, 2))
        assert not U.contains_point(1, Rational(1, 2))

    def test_open_set_intersection(self):
        """Intersection of overlapping rectangles."""
        from lib.recognition_theorem_engine import OpenSet
        U1 = OpenSet(0, Rational(3, 4), 0, 1, label='left')
        U2 = OpenSet(Rational(1, 4), 1, 0, 1, label='right')
        cap = U1.intersect(U2)
        assert cap is not None
        assert cap.z_min == Rational(1, 4)
        assert cap.z_max == Rational(3, 4)

    def test_disjoint_intersection_is_none(self):
        """Disjoint opens have empty intersection."""
        from lib.recognition_theorem_engine import OpenSet
        U1 = OpenSet(0, Rational(1, 3), 0, 1)
        U2 = OpenSet(Rational(2, 3), 1, 0, 1)
        cap = U1.intersect(U2)
        assert cap is None

    def test_open_set_is_product(self):
        """Rectangular opens are product opens by construction."""
        from lib.recognition_theorem_engine import OpenSet
        U = OpenSet(0, 1, 0, 1)
        assert U.is_product()


# ===================================================================
# 2. WEISS COVER OPERATIONS
# ===================================================================

class TestWeissCover:
    """Test Weiss cover construction and verification."""

    def test_standard_cover_creation(self):
        """Standard product cover of [0,1]x[0,1] with 2x2 opens."""
        from lib.recognition_theorem_engine import standard_product_cover
        cover = standard_product_cover(n_C=2, n_R=2)
        assert len(cover.opens) == 4

    def test_standard_cover_is_weiss_for_1(self):
        """Standard cover covers single points."""
        from lib.recognition_theorem_engine import standard_product_cover
        cover = standard_product_cover(n_C=2, n_R=2, overlap=Rational(1, 4))
        configs = [[(Rational(1, 4), Rational(1, 4))],
                   [(Rational(3, 4), Rational(3, 4))]]
        assert cover.is_weiss_for_n(1, configs)

    def test_cover_has_pairwise_overlaps(self):
        """Product cover has nontrivial pairwise intersections."""
        from lib.recognition_theorem_engine import standard_product_cover
        cover = standard_product_cover(n_C=2, n_R=1, overlap=Rational(1, 4))
        ints = cover.pairwise_intersections()
        has_nonempty = any(cap is not None for _, _, cap in ints)
        assert has_nonempty

    def test_cover_ambient(self):
        """Standard cover has ambient open set."""
        from lib.recognition_theorem_engine import standard_product_cover
        cover = standard_product_cover()
        assert cover.ambient is not None
        assert cover.ambient.z_min == 0
        assert cover.ambient.z_max == 1


# ===================================================================
# 3. FACTORIZATION VALUES
# ===================================================================

class TestFactorizationValues:
    """Test factorization algebra values on opens."""

    def test_heisenberg_value_dimension(self):
        """Heisenberg factorization value has correct dimension."""
        from lib.recognition_theorem_engine import heisenberg_factorization_value
        val = heisenberg_factorization_value((0, 1), (0, 1), max_weight=2)
        assert val.dimension is not None
        assert val.dimension > 0

    def test_heisenberg_value_family(self):
        """Factorization value knows its family."""
        from lib.recognition_theorem_engine import heisenberg_factorization_value
        val = heisenberg_factorization_value((0, 1), (0, 1))
        assert val.family == 'heisenberg'

    def test_heisenberg_dimension_monotone(self):
        """Larger weight truncation gives larger dimension."""
        from lib.recognition_theorem_engine import heisenberg_factorization_value
        val2 = heisenberg_factorization_value((0, 1), (0, 1), max_weight=2)
        val3 = heisenberg_factorization_value((0, 1), (0, 1), max_weight=3)
        assert val3.dimension > val2.dimension

    def test_heisenberg_r_direction_trivial(self):
        """R-direction contributes dimension 1 (locally constant)."""
        from lib.recognition_theorem_engine import heisenberg_factorization_value
        val = heisenberg_factorization_value((0, 1), (0, 1), max_weight=3)
        assert val.extra_data['r_dim'] == 1


# ===================================================================
# 4. CECH DESCENT VERIFICATION
# ===================================================================

class TestCechDescent:
    """Test Cech descent for Heisenberg."""

    def test_cech_descent_basic(self):
        """Basic Cech descent verification returns data."""
        from lib.recognition_theorem_engine import (
            standard_product_cover, verify_cech_descent_heisenberg)
        cover = standard_product_cover(n_C=2, n_R=1)
        result = verify_cech_descent_heisenberg(cover, max_weight=2)
        assert result['descent_verified']

    def test_cech_descent_open_dimensions(self):
        """Open dimensions are computed correctly."""
        from lib.recognition_theorem_engine import (
            standard_product_cover, verify_cech_descent_heisenberg)
        cover = standard_product_cover(n_C=2, n_R=1)
        result = verify_cech_descent_heisenberg(cover, max_weight=2)
        assert len(result['open_dimensions']) == len(cover.opens)
        assert all(d > 0 for d in result['open_dimensions'])


# ===================================================================
# 5. HYPOTHESIS (H1)-(H4) VERIFICATION
# ===================================================================

class TestHypotheses:
    """Test hypothesis verification for all 7 Vol II examples."""

    def test_heisenberg_all_hypotheses(self):
        """Heisenberg satisfies all four hypotheses."""
        from lib.recognition_theorem_engine import check_all_hypotheses
        hyp = check_all_hypotheses('heisenberg')
        assert hyp.all_satisfied

    def test_virasoro_all_hypotheses(self):
        """Virasoro satisfies all four hypotheses."""
        from lib.recognition_theorem_engine import check_all_hypotheses
        hyp = check_all_hypotheses('virasoro')
        assert hyp.all_satisfied

    def test_affine_sl2_all_hypotheses(self):
        """Affine sl_2 satisfies all four hypotheses."""
        from lib.recognition_theorem_engine import check_all_hypotheses
        hyp = check_all_hypotheses('affine_sl2')
        assert hyp.all_satisfied

    def test_betagamma_all_hypotheses(self):
        """betagamma satisfies all four hypotheses."""
        from lib.recognition_theorem_engine import check_all_hypotheses
        hyp = check_all_hypotheses('betagamma')
        assert hyp.all_satisfied

    def test_w3_all_hypotheses(self):
        """W_3 satisfies all four hypotheses."""
        from lib.recognition_theorem_engine import check_all_hypotheses
        hyp = check_all_hypotheses('w3')
        assert hyp.all_satisfied

    def test_lattice_A1_all_hypotheses(self):
        """Lattice A_1 VOA satisfies all four hypotheses."""
        from lib.recognition_theorem_engine import check_all_hypotheses
        hyp = check_all_hypotheses('lattice_A1')
        assert hyp.all_satisfied

    def test_lg_cubic_all_hypotheses(self):
        """LG cubic model satisfies all four hypotheses."""
        from lib.recognition_theorem_engine import check_all_hypotheses
        hyp = check_all_hypotheses('lg_cubic')
        assert hyp.all_satisfied

    def test_h1_locally_constant_explicit(self):
        """Explicit H1 check returns True and reason."""
        from lib.recognition_theorem_engine import check_h1_locally_constant
        ok, reason = check_h1_locally_constant('heisenberg')
        assert ok
        assert 'topological' in reason.lower() or 'locally constant' in reason.lower()

    def test_h2_holomorphic_explicit(self):
        """Explicit H2 check returns True and reason."""
        from lib.recognition_theorem_engine import check_h2_holomorphic
        ok, reason = check_h2_holomorphic('virasoro')
        assert ok
        assert 'holomorphic' in reason.lower() or 'meromorphic' in reason.lower()

    def test_h3_bounded_below_explicit(self):
        """Explicit H3 check returns True."""
        from lib.recognition_theorem_engine import check_h3_bounded_below
        ok, reason = check_h3_bounded_below('betagamma')
        assert ok

    def test_h4_vacuum_explicit(self):
        """Explicit H4 check returns True."""
        from lib.recognition_theorem_engine import check_h4_vacuum
        ok, reason = check_h4_vacuum('affine_sl2')
        assert ok
        assert 'vacuum' in reason.lower()

    def test_unknown_family_h1(self):
        """Unknown family returns False for H1."""
        from lib.recognition_theorem_engine import check_h1_locally_constant
        ok, reason = check_h1_locally_constant('nonexistent_family')
        assert not ok


# ===================================================================
# 6. RECONSTRUCTION
# ===================================================================

class TestReconstruction:
    """Test reconstruction from (H1)-(H4)."""

    def test_heisenberg_reconstruction(self):
        """Heisenberg reconstruction gives correct chiral part."""
        from lib.recognition_theorem_engine import reconstruct_from_hypotheses
        recon = reconstruct_from_hypotheses('heisenberg')
        assert recon.chiral_generators == ['J']
        assert recon.chiral_weights == {'J': 1}
        assert simplify(recon.kappa - Symbol('k') / 2) == 0

    def test_virasoro_reconstruction_kappa(self):
        """Virasoro reconstruction has kappa = c/2."""
        from lib.recognition_theorem_engine import reconstruct_from_hypotheses
        recon = reconstruct_from_hypotheses('virasoro')
        assert simplify(recon.kappa - Symbol('c') / 2) == 0

    def test_w3_reconstruction_kappa(self):
        """W_3 reconstruction has kappa = 5c/6."""
        from lib.recognition_theorem_engine import reconstruct_from_hypotheses
        recon = reconstruct_from_hypotheses('w3')
        assert simplify(recon.kappa - 5 * Symbol('c') / 6) == 0

    def test_affine_reconstruction_topological(self):
        """Affine sl_2 topological part is category O."""
        from lib.recognition_theorem_engine import reconstruct_from_hypotheses
        recon = reconstruct_from_hypotheses('affine_sl2')
        assert 'Category O' in recon.topological_type or 'O' in recon.topological_type

    def test_betagamma_kappa_is_one(self):
        """betagamma has kappa = 1."""
        from lib.recognition_theorem_engine import reconstruct_from_hypotheses
        recon = reconstruct_from_hypotheses('betagamma')
        assert recon.kappa == 1

    def test_lg_cubic_kappa(self):
        """LG cubic has kappa = c/2 = -1."""
        from lib.recognition_theorem_engine import reconstruct_from_hypotheses
        recon = reconstruct_from_hypotheses('lg_cubic')
        assert recon.kappa == -1


# ===================================================================
# 7. PRODUCT WEISS DESCENT
# ===================================================================

class TestProductWeissDescent:
    """Test product Weiss descent lemma."""

    def test_product_descent_dimensions(self):
        """Product Weiss descent gives consistent dimensions."""
        from lib.recognition_theorem_engine import product_weiss_descent_dimensions
        cover_C = [(0, Rational(3, 4)), (Rational(1, 4), 1)]
        cover_R = [(0, 1)]
        result = product_weiss_descent_dimensions(cover_C, cover_R, max_weight=2)
        assert result['product_structure']
        assert result['ambient_dimension'] > 0

    def test_product_descent_c_dims(self):
        """C-direction dimensions are positive."""
        from lib.recognition_theorem_engine import product_weiss_descent_dimensions
        cover_C = [(0, Rational(1, 2)), (Rational(1, 2), 1)]
        cover_R = [(0, 1)]
        result = product_weiss_descent_dimensions(cover_C, cover_R, max_weight=2)
        assert all(d > 0 for d in result['c_dims'])

    def test_product_descent_r_constant(self):
        """R-direction dimensions are all 1 (locally constant)."""
        from lib.recognition_theorem_engine import product_weiss_descent_dimensions
        cover_C = [(0, 1)]
        cover_R = [(0, Rational(1, 2)), (Rational(1, 2), 1)]
        result = product_weiss_descent_dimensions(cover_C, cover_R, max_weight=2)
        assert all(d == 1 for d in result['r_dims'])


# ===================================================================
# 8. R-DIRECTION ISOTOPY
# ===================================================================

class TestRDirectionIsotopy:
    """Test local constancy along R."""

    def test_isotopy_heisenberg(self):
        """Heisenberg is locally constant along R."""
        from lib.recognition_theorem_engine import verify_r_direction_isotopy
        result = verify_r_direction_isotopy('heisenberg', n_intervals=3)
        assert result['locally_constant']
        assert result['all_equal']

    def test_isotopy_dimensions_constant(self):
        """All R-intervals give the same dimension."""
        from lib.recognition_theorem_engine import verify_r_direction_isotopy
        result = verify_r_direction_isotopy('heisenberg', n_intervals=5)
        dims = result['dimensions']
        assert len(set(dims)) == 1


# ===================================================================
# 9. C-DIRECTION FACTORIZATION
# ===================================================================

class TestCDirectionFactorization:
    """Test chiral factorization along C."""

    def test_factorization_2_disks(self):
        """Factorization holds for 2 disjoint disks."""
        from lib.recognition_theorem_engine import verify_c_direction_factorization
        result = verify_c_direction_factorization(n_disks=2, max_weight=2)
        assert result['factorization_holds']

    def test_factorization_3_disks(self):
        """Factorization holds for 3 disjoint disks."""
        from lib.recognition_theorem_engine import verify_c_direction_factorization
        result = verify_c_direction_factorization(n_disks=3, max_weight=2)
        assert result['factorization_holds']


# ===================================================================
# 10. MIXED COUPLING
# ===================================================================

class TestMixedCoupling:
    """Test mixed coupling extraction."""

    def test_heisenberg_coupling_singular_order(self):
        """Heisenberg mixed coupling has singular order 1."""
        from lib.recognition_theorem_engine import extract_mixed_coupling
        coupling = extract_mixed_coupling('heisenberg')
        assert coupling['singular_order'] == 1

    def test_virasoro_coupling_singular_order(self):
        """Virasoro mixed coupling has singular order 2."""
        from lib.recognition_theorem_engine import extract_mixed_coupling
        coupling = extract_mixed_coupling('virasoro')
        assert coupling['singular_order'] == 2

    def test_coupling_type_exists(self):
        """All families have a coupling type."""
        from lib.recognition_theorem_engine import extract_mixed_coupling
        for family in ['heisenberg', 'virasoro', 'affine_sl2', 'betagamma', 'w3']:
            coupling = extract_mixed_coupling(family)
            assert 'coupling_type' in coupling


# ===================================================================
# 11. FULL RECOGNITION PIPELINE
# ===================================================================

class TestFullPipeline:
    """Test the complete recognition pipeline."""

    def test_full_pipeline_heisenberg(self):
        """Full pipeline for Heisenberg."""
        from lib.recognition_theorem_engine import full_recognition_pipeline
        result = full_recognition_pipeline('heisenberg')
        assert result['recognition_theorem_applies']
        assert result['step1_hypotheses']['all_pass']

    def test_full_pipeline_all_families(self):
        """Full pipeline passes for all 7 families."""
        from lib.recognition_theorem_engine import full_recognition_pipeline
        for family in ['heisenberg', 'virasoro', 'affine_sl2',
                       'betagamma', 'w3', 'lattice_A1', 'lg_cubic']:
            result = full_recognition_pipeline(family)
            assert result['recognition_theorem_applies'], f"Failed for {family}"

    def test_recognition_theorem_check(self):
        """Recognition theorem check gives structured output."""
        from lib.recognition_theorem_engine import recognition_theorem_check
        result = recognition_theorem_check('virasoro')
        assert result['recognition_applies']
        assert result['hypotheses']['all_satisfied']
        assert result['reconstruction'] is not None
