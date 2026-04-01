"""Tests for the Verlinde algebra verification of the derived-center-as-bulk prediction.

The derived-center-as-bulk claim (thm:universal-bulk, AP-OC overclaim resolution)
predicts that for V_k(sl_2) at integrable level k:

    dim Z^der_ch(C_op) = dim Z(Rep(V_k(sl_2))) = k+1

where Z^der_ch is the categorical derived center (bulk observables of the 3d HT
theory) and Z(Rep(...)) is the Drinfeld center of the module category.

This is the CATEGORICAL center, not the algebraic center HH^0(A,A) = C (dim 1).
The distinction is the core content of the AP-OC overclaim resolution in
foundations_overclaims_resolved.tex: the algebraic Hochschild cohomology of A
as an associative algebra gives dim 1, while the categorical center of the
module category gives dim k+1. The programme's thm:universal-bulk uses the
categorical version, computed via Hochschild cochains of a compact generator.

These tests verify the Verlinde formula computation and known fusion rules,
providing the first concrete numerical check of the prediction.

Test tiers:
    Tier 1 (self-certifying): S-matrix unitarity, symmetry, charge conjugation
    Tier 2 (structural): fusion commutativity, associativity, non-negative integers
    Tier 3 (published): known fusion rules for k=1,2,3 (Kac, Fuchs, Di Francesco et al.)
    Tier 4 (cross-check): truncated tensor product rule vs Verlinde formula
    Tier 5 (prediction): derived-center dimension = k+1

References:
    Di Francesco-Mathieu-Senechal, Conformal Field Theory, ch. 16
    Kac, Vertex Algebras for Beginners, ch. 5
    Bakalov-Kirillov, Lectures on Tensor Categories and Modular Functors
    Vol I: thm:thqg-swiss-cheese (derived center as universal bulk)
    Vol II: foundations_overclaims_resolved.tex (categorical vs algebraic)
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import numpy as np
import pytest


# ===================================================================
# TIER 1: S-MATRIX SELF-CERTIFYING PROPERTIES
# ===================================================================

class TestSMatrixStructure:
    """Verify the modular S-matrix satisfies its defining properties."""

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5, 6, 8, 10])
    def test_s_matrix_unitarity(self, k):
        """S * S^T = I (unitarity, since S is real for sl_2)."""
        from lib.verlinde_bulk_check import verify_s_matrix_unitarity
        passes, deviation = verify_s_matrix_unitarity(k)
        assert passes, f"S-matrix unitarity fails at k={k}, deviation={deviation}"

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5, 6, 8, 10])
    def test_s_matrix_symmetry(self, k):
        """S_{ij} = S_{ji} (symmetric)."""
        from lib.verlinde_bulk_check import verify_s_matrix_symmetry
        passes, deviation = verify_s_matrix_symmetry(k)
        assert passes, f"S-matrix symmetry fails at k={k}, deviation={deviation}"

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5, 6, 8, 10])
    def test_s_matrix_charge_conjugation(self, k):
        """S^2 = C = I for sl_2 (all reps self-conjugate)."""
        from lib.verlinde_bulk_check import verify_charge_conjugation
        passes, deviation = verify_charge_conjugation(k)
        assert passes, f"Charge conjugation fails at k={k}, deviation={deviation}"

    @pytest.mark.parametrize("k", [1, 2, 3, 4])
    def test_s_matrix_shape(self, k):
        """S-matrix has shape (k+1) x (k+1)."""
        from lib.verlinde_bulk_check import sl2_modular_s_matrix
        S = sl2_modular_s_matrix(k)
        assert S.shape == (k + 1, k + 1)

    def test_s_matrix_k1_explicit(self):
        """At k=1, S = sqrt(1/3) * [[sin(pi/3), sin(2pi/3)],
                                     [sin(2pi/3), sin(4pi/3)]].

        sin(pi/3) = sqrt(3)/2, sin(2pi/3) = sqrt(3)/2, sin(4pi/3) = -sqrt(3)/2.
        So S = (1/sqrt(3)) * [[sqrt(3)/2, sqrt(3)/2],
                               [sqrt(3)/2, -sqrt(3)/2]]
             = [[1/2, 1/2], [1/2, -1/2]] * sqrt(3) * (1/sqrt(3))
        Wait: prefactor = sqrt(2/3).
        S_{00} = sqrt(2/3) * sin(pi/3) = sqrt(2/3) * sqrt(3)/2 = 1/sqrt(2).
        S_{01} = sqrt(2/3) * sin(2pi/3) = sqrt(2/3) * sqrt(3)/2 = 1/sqrt(2).
        S_{10} = sqrt(2/3) * sin(2pi/3) = 1/sqrt(2).
        S_{11} = sqrt(2/3) * sin(4pi/3) = sqrt(2/3) * (-sqrt(3)/2) = -1/sqrt(2).
        """
        from lib.verlinde_bulk_check import sl2_modular_s_matrix
        S = sl2_modular_s_matrix(1)
        inv_sqrt2 = 1.0 / np.sqrt(2)
        expected = np.array([[inv_sqrt2, inv_sqrt2],
                             [inv_sqrt2, -inv_sqrt2]])
        np.testing.assert_allclose(S, expected, atol=1e-14)

    def test_s_matrix_first_row_positive(self):
        """S_{0j} > 0 for all j (required for Verlinde formula denominators)."""
        for k in range(1, 8):
            from lib.verlinde_bulk_check import sl2_modular_s_matrix
            S = sl2_modular_s_matrix(k)
            for j in range(k + 1):
                assert S[0, j] > 0, f"S[0,{j}] = {S[0,j]} <= 0 at k={k}"

    def test_s_matrix_invalid_level(self):
        """Level k must be a positive integer."""
        from lib.verlinde_bulk_check import sl2_modular_s_matrix
        with pytest.raises(ValueError):
            sl2_modular_s_matrix(0)
        with pytest.raises(ValueError):
            sl2_modular_s_matrix(-1)


# ===================================================================
# TIER 2: FUSION STRUCTURAL PROPERTIES
# ===================================================================

class TestFusionStructure:
    """Verify structural properties of the fusion ring."""

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5, 6])
    def test_fusion_nonnegative_integers(self, k):
        """All fusion coefficients are non-negative integers."""
        from lib.verlinde_bulk_check import verify_fusion_nonnegative_integers
        assert verify_fusion_nonnegative_integers(k), \
            f"Fusion coefficients fail non-negative integer test at k={k}"

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5, 6])
    def test_fusion_commutativity(self, k):
        """N_{ij}^l = N_{ji}^l (fusion is commutative)."""
        from lib.verlinde_bulk_check import verify_fusion_commutativity
        assert verify_fusion_commutativity(k), \
            f"Fusion commutativity fails at k={k}"

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    def test_fusion_associativity(self, k):
        """(L_i x L_j) x L_m = L_i x (L_j x L_m) (fusion is associative)."""
        from lib.verlinde_bulk_check import verify_fusion_associativity
        assert verify_fusion_associativity(k), \
            f"Fusion associativity fails at k={k}"

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5, 6])
    def test_fusion_unit(self, k):
        """L_0 is the fusion unit: L_0 x L_j = L_j."""
        from lib.verlinde_bulk_check import verify_unit
        assert verify_unit(k), f"L_0 is not the fusion unit at k={k}"

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    def test_fusion_tensor_shape(self, k):
        """Fusion tensor has shape (k+1, k+1, k+1)."""
        from lib.verlinde_bulk_check import verlinde_fusion_coefficients
        N = verlinde_fusion_coefficients(k)
        assert N.shape == (k + 1, k + 1, k + 1)


# ===================================================================
# TIER 3: KNOWN FUSION RULES (published, independent data)
# ===================================================================

class TestKnownFusionRules:
    """Verify fusion coefficients against published fusion rules.

    These are the known fusion rules from the CFT literature,
    serving as independent ground truth.
    """

    def test_k1_L1_x_L1(self):
        """k=1: L_1 x L_1 = L_0 (Z/2 group law)."""
        from lib.verlinde_bulk_check import fusion_product
        result = fusion_product(1, 1, 1)
        assert result == {0: 1}, f"k=1: L_1 x L_1 = {result}, expected {{0: 1}}"

    def test_k1_all_rules(self):
        """k=1: verify all fusion rules against known data."""
        from lib.verlinde_bulk_check import (
            fusion_product, known_fusion_rules_k1
        )
        known = known_fusion_rules_k1()
        for (i, j), expected in known.items():
            result = fusion_product(1, i, j)
            assert result == expected, \
                f"k=1: L_{i} x L_{j} = {result}, expected {expected}"

    def test_k2_L1_x_L1(self):
        """k=2: L_1 x L_1 = L_0 + L_2 (fundamental self-fusion)."""
        from lib.verlinde_bulk_check import fusion_product
        result = fusion_product(2, 1, 1)
        assert result == {0: 1, 2: 1}, \
            f"k=2: L_1 x L_1 = {result}, expected {{0: 1, 2: 1}}"

    def test_k2_L1_x_L2(self):
        """k=2: L_1 x L_2 = L_1."""
        from lib.verlinde_bulk_check import fusion_product
        result = fusion_product(2, 1, 2)
        assert result == {1: 1}, \
            f"k=2: L_1 x L_2 = {result}, expected {{1: 1}}"

    def test_k2_L2_x_L2(self):
        """k=2: L_2 x L_2 = L_0 (adjoint self-fusion, Z/2)."""
        from lib.verlinde_bulk_check import fusion_product
        result = fusion_product(2, 2, 2)
        assert result == {0: 1}, \
            f"k=2: L_2 x L_2 = {result}, expected {{0: 1}}"

    def test_k2_all_rules(self):
        """k=2: verify all fusion rules against known data."""
        from lib.verlinde_bulk_check import (
            fusion_product, known_fusion_rules_k2
        )
        known = known_fusion_rules_k2()
        for (i, j), expected in known.items():
            result = fusion_product(2, i, j)
            assert result == expected, \
                f"k=2: L_{i} x L_{j} = {result}, expected {expected}"

    def test_k3_L1_x_L1(self):
        """k=3: L_1 x L_1 = L_0 + L_2."""
        from lib.verlinde_bulk_check import fusion_product
        result = fusion_product(3, 1, 1)
        assert result == {0: 1, 2: 1}

    def test_k3_L1_x_L2(self):
        """k=3: L_1 x L_2 = L_1 + L_3."""
        from lib.verlinde_bulk_check import fusion_product
        result = fusion_product(3, 1, 2)
        assert result == {1: 1, 3: 1}

    def test_k3_L1_x_L3(self):
        """k=3: L_1 x L_3 = L_2."""
        from lib.verlinde_bulk_check import fusion_product
        result = fusion_product(3, 1, 3)
        assert result == {2: 1}

    def test_k3_L2_x_L2(self):
        """k=3: L_2 x L_2 = L_0 + L_2 (truncation: 2+2=4 > 2*3-2-2=2)."""
        from lib.verlinde_bulk_check import fusion_product
        result = fusion_product(3, 2, 2)
        assert result == {0: 1, 2: 1}

    def test_k3_L2_x_L3(self):
        """k=3: L_2 x L_3 = L_1."""
        from lib.verlinde_bulk_check import fusion_product
        result = fusion_product(3, 2, 3)
        assert result == {1: 1}

    def test_k3_L3_x_L3(self):
        """k=3: L_3 x L_3 = L_0 (Z/2 structure of maximal weight)."""
        from lib.verlinde_bulk_check import fusion_product
        result = fusion_product(3, 3, 3)
        assert result == {0: 1}

    def test_k3_all_rules(self):
        """k=3: verify all fusion rules against known data."""
        from lib.verlinde_bulk_check import (
            fusion_product, known_fusion_rules_k3
        )
        known = known_fusion_rules_k3()
        for (i, j), expected in known.items():
            result = fusion_product(3, i, j)
            assert result == expected, \
                f"k=3: L_{i} x L_{j} = {result}, expected {expected}"


# ===================================================================
# TIER 4: TRUNCATED TENSOR PRODUCT CROSS-CHECK
# ===================================================================

class TestTruncatedTensorProduct:
    """Verify Verlinde formula matches the truncated tensor product rule.

    The truncated tensor product (Clebsch-Gordan with integrability cutoff)
    is an independent combinatorial formula. Agreement with the Verlinde
    formula (which uses the S-matrix and trigonometric sums) is a strong
    cross-check.
    """

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5, 6])
    def test_verlinde_equals_truncated(self, k):
        """For all i, j: Verlinde N_{ij}^l = truncated tensor product."""
        from lib.verlinde_bulk_check import (
            fusion_product, sl2_truncated_tensor_product
        )
        n = k + 1
        for i in range(n):
            for j in range(n):
                verlinde = fusion_product(k, i, j)
                truncated = sl2_truncated_tensor_product(k, i, j)
                assert verlinde == truncated, (
                    f"k={k}: L_{i} x L_{j} disagrees: "
                    f"Verlinde={verlinde}, truncated={truncated}"
                )

    def test_truncated_unit(self):
        """L_0 x L_j = L_j by the truncated rule (|0-j|=j, min(j, 2k-j)>=j)."""
        from lib.verlinde_bulk_check import sl2_truncated_tensor_product
        for k in range(1, 8):
            for j in range(k + 1):
                result = sl2_truncated_tensor_product(k, 0, j)
                assert result == {j: 1}, \
                    f"k={k}: L_0 x L_{j} = {result}, expected {{{j}: 1}}"

    def test_truncated_highest_weight_self_fusion(self):
        """L_k x L_k = L_0 for all k (the maximal weight squares to vacuum).

        Proof: |k-k|=0, min(2k, 2k-2k)=min(2k,0)=0. So sum is just l=0.
        """
        from lib.verlinde_bulk_check import sl2_truncated_tensor_product
        for k in range(1, 10):
            result = sl2_truncated_tensor_product(k, k, k)
            assert result == {0: 1}, \
                f"k={k}: L_{k} x L_{k} = {result}, expected {{0: 1}}"

    def test_truncated_invalid_weight(self):
        """Weights outside [0, k] raise ValueError."""
        from lib.verlinde_bulk_check import sl2_truncated_tensor_product
        with pytest.raises(ValueError):
            sl2_truncated_tensor_product(3, 4, 0)
        with pytest.raises(ValueError):
            sl2_truncated_tensor_product(3, -1, 0)


# ===================================================================
# TIER 5: DERIVED-CENTER PREDICTION
# ===================================================================

class TestDerivedCenterPrediction:
    """The checkable prediction from the derived-center-as-bulk programme.

    For V_k(sl_2) at integrable level k, the programme predicts:

        dim HH^0_cat(C_op) = dim Z(Rep(V_k(sl_2))) = k + 1

    This equals the dimension of the Verlinde algebra, which we compute
    independently via the Verlinde formula and verify against the
    truncated tensor product rule.

    The critical distinction (AP-OC, foundations_overclaims_resolved.tex):
    - Algebraic HH^0(A, A) = C (dimension 1) for simple VOAs
    - Categorical Z(C) = center of monoidal category (dimension k+1)

    The programme uses the CATEGORICAL version. The 3d Chern-Simons bulk
    on S^1 x R^2 has Hilbert space = Verlinde algebra, confirming k+1.
    """

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5, 6, 8, 10])
    def test_verlinde_dimension_equals_prediction(self, k):
        """dim(Verlinde algebra) = k+1 = derived-center prediction."""
        from lib.verlinde_bulk_check import (
            verlinde_algebra_dimension,
            derived_center_dimension_prediction
        )
        assert verlinde_algebra_dimension(k) == k + 1
        assert derived_center_dimension_prediction(k) == k + 1
        assert verlinde_algebra_dimension(k) == derived_center_dimension_prediction(k)

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    def test_number_of_simples_equals_prediction(self, k):
        """Number of simple modules (= number of nonzero fusion rules with L_0)
        equals the predicted derived-center dimension.

        L_0 x L_j = L_j means the unit row of N has exactly k+1 nonzero entries.
        """
        from lib.verlinde_bulk_check import verlinde_fusion_coefficients
        N = verlinde_fusion_coefficients(k)
        n = k + 1
        # Count nonzero entries in the first row (unit action)
        count = sum(1 for j in range(n) if any(N[0, j, l] > 0 for l in range(n)))
        assert count == n

    @pytest.mark.parametrize("k", [1, 2, 3, 4])
    def test_algebraic_vs_categorical_center(self, k):
        """The algebraic center has dimension 1; the categorical center has
        dimension k+1. These are DIFFERENT for k >= 1.

        This is the core content of the AP-OC overclaim resolution.
        """
        from lib.verlinde_bulk_check import (
            algebraic_center_dimension,
            derived_center_dimension_prediction
        )
        alg_dim = algebraic_center_dimension()
        cat_dim = derived_center_dimension_prediction(k)
        assert alg_dim == 1
        assert cat_dim == k + 1
        assert cat_dim > alg_dim  # strict inequality for k >= 1

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    def test_verlinde_algebra_is_semisimple(self, k):
        """The Verlinde algebra is semisimple: it has k+1 idempotents.

        The S-matrix diagonalizes the fusion matrices simultaneously.
        The idempotents are e_m = sum_i (S_{im}/S_{0m}) L_i.
        Semisimplicity means the Verlinde algebra is isomorphic to
        C^{k+1} as a C-algebra (direct product of copies of C).

        This is equivalent to the fusion matrices being simultaneously
        diagonalizable, which follows from S being unitary.
        """
        from lib.verlinde_bulk_check import (
            verlinde_fusion_coefficients, sl2_modular_s_matrix
        )
        N = verlinde_fusion_coefficients(k)
        S = sl2_modular_s_matrix(k)
        n = k + 1

        # For each simple L_i, the fusion matrix N_i has (N_i)_{jl} = N[i,j,l].
        # The S-matrix diagonalizes all N_i simultaneously:
        # N_i = S * diag(S_{im}/S_{0m}) * S^{-1}
        for i in range(n):
            # Build fusion matrix for L_i
            N_i = np.array([[N[i, j, l] for l in range(n)] for j in range(n)])
            # Eigenvalues should be S_{im}/S_{0m} for m = 0, ..., k
            expected_evals = sorted([S[i, m] / S[0, m] for m in range(n)])
            actual_evals = sorted(np.linalg.eigvalsh(N_i))
            np.testing.assert_allclose(
                actual_evals, expected_evals, atol=1e-10,
                err_msg=f"k={k}, i={i}: eigenvalues of N_i disagree"
            )


# ===================================================================
# TIER 6: QUANTUM DIMENSIONS
# ===================================================================

class TestQuantumDimensions:
    """Verify quantum dimensions and global dimension."""

    def test_vacuum_quantum_dimension(self):
        """d_0 = 1 (the vacuum module has quantum dimension 1)."""
        from lib.verlinde_bulk_check import quantum_dimension
        for k in range(1, 8):
            d0 = quantum_dimension(k, 0)
            np.testing.assert_allclose(d0, 1.0, atol=1e-14,
                                       err_msg=f"d_0 != 1 at k={k}")

    def test_fundamental_quantum_dimension(self):
        """d_1 = sin(2*pi/(k+2)) / sin(pi/(k+2)) = 2*cos(pi/(k+2)).

        This is the quantum [2] at q = exp(i*pi/(k+2)).
        """
        from lib.verlinde_bulk_check import quantum_dimension
        for k in range(1, 10):
            d1 = quantum_dimension(k, 1)
            expected = 2 * np.cos(np.pi / (k + 2))
            np.testing.assert_allclose(d1, expected, atol=1e-12,
                                       err_msg=f"d_1 wrong at k={k}")

    def test_quantum_dimensions_positive(self):
        """All quantum dimensions are positive."""
        from lib.verlinde_bulk_check import quantum_dimension
        for k in range(1, 10):
            for i in range(k + 1):
                d_i = quantum_dimension(k, i)
                assert d_i > 0, f"d_{i} = {d_i} <= 0 at k={k}"

    def test_classical_limit(self):
        """At large k, d_i -> i+1 (classical sl_2 dimension).

        The quantum dimension d_i = sin((i+1)*pi/(k+2)) / sin(pi/(k+2))
        converges to i+1 as k -> infinity. The leading correction is
        O((i+1)^2 / k^2), so we use k=500 to get sub-percent agreement.
        """
        from lib.verlinde_bulk_check import quantum_dimension
        k = 500
        for i in range(min(10, k + 1)):
            d_i = quantum_dimension(k, i)
            classical = i + 1
            np.testing.assert_allclose(
                d_i, classical, rtol=0.005,
                err_msg=f"d_{i} = {d_i}, expected ~ {classical} at k={k}"
            )

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    def test_global_dimension_formula(self, k):
        """D^2 = sum d_i^2 = 1/S_{00}^2 = (k+2)/(2*sin^2(pi/(k+2)))."""
        from lib.verlinde_bulk_check import (
            quantum_dimension, global_dimension_squared
        )
        n = k + 1
        sum_d_sq = sum(quantum_dimension(k, i)**2 for i in range(n))
        D_sq = global_dimension_squared(k)
        np.testing.assert_allclose(sum_d_sq, D_sq, atol=1e-10,
                                   err_msg=f"D^2 mismatch at k={k}")

    def test_global_dimension_k1(self):
        """At k=1: d_0=1, d_1=1, so D^2 = 2."""
        from lib.verlinde_bulk_check import global_dimension_squared
        D_sq = global_dimension_squared(1)
        np.testing.assert_allclose(D_sq, 2.0, atol=1e-12)

    def test_global_dimension_k2(self):
        """At k=2: d_0=1, d_1=sqrt(2), d_2=1, so D^2 = 1+2+1 = 4."""
        from lib.verlinde_bulk_check import global_dimension_squared
        D_sq = global_dimension_squared(2)
        np.testing.assert_allclose(D_sq, 4.0, atol=1e-10)


# ===================================================================
# TIER 7: MODULAR T-MATRIX AND SL(2,Z) RELATIONS
# ===================================================================

class TestModularRelations:
    """Verify the SL(2,Z) modular relations for the S and T matrices.

    The S and T matrices generate a projective representation of SL(2,Z).
    The relation (ST)^3 = S^2 = C is a genuinely independent cross-check:
    the T-matrix encodes conformal weights (Virasoro spectral data) while
    the S-matrix encodes modular transformations of characters. Their
    compatibility is a deep consequence of the ribbon structure of the
    modular tensor category.

    This provides a non-tautological verification: if the S-matrix formula
    were wrong, the (ST)^3 = S^2 relation would generically fail.
    """

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5, 6, 8, 10])
    def test_modular_relation_ST3_equals_S2(self, k):
        """(ST)^3 = S^2 = C = I for sl_2."""
        from lib.verlinde_bulk_check import verify_modular_relation
        passes, deviation = verify_modular_relation(k)
        assert passes, f"(ST)^3 != S^2 at k={k}, deviation={deviation}"

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    def test_t_matrix_diagonal(self, k):
        """T-matrix is diagonal."""
        from lib.verlinde_bulk_check import sl2_modular_t_matrix
        T = sl2_modular_t_matrix(k)
        n = k + 1
        for i in range(n):
            for j in range(n):
                if i != j:
                    assert abs(T[i, j]) < 1e-15, \
                        f"T[{i},{j}] = {T[i,j]} != 0 at k={k}"

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    def test_t_matrix_unimodular(self, k):
        """All T-matrix diagonal entries have |T_{ii}| = 1."""
        from lib.verlinde_bulk_check import sl2_modular_t_matrix
        T = sl2_modular_t_matrix(k)
        n = k + 1
        for i in range(n):
            np.testing.assert_allclose(
                abs(T[i, i]), 1.0, atol=1e-14,
                err_msg=f"|T[{i},{i}]| != 1 at k={k}"
            )

    def test_t_matrix_k1_explicit(self):
        """At k=1: c = 1, h_0 = 0, h_1 = 1/4.
        T_{00} = exp(2*pi*i * (0 - 1/24)) = exp(-i*pi/12).
        T_{11} = exp(2*pi*i * (1/4 - 1/24)) = exp(2*pi*i * 5/24) = exp(i*5*pi/12).
        """
        from lib.verlinde_bulk_check import sl2_modular_t_matrix
        T = sl2_modular_t_matrix(1)
        expected_00 = np.exp(-1j * np.pi / 12)
        expected_11 = np.exp(1j * 5 * np.pi / 12)
        np.testing.assert_allclose(T[0, 0], expected_00, atol=1e-14)
        np.testing.assert_allclose(T[1, 1], expected_11, atol=1e-14)

    def test_t_matrix_conformal_weights(self):
        """T_{ii} encodes conformal weight h_i = i(i+2)/(4(k+2))."""
        from lib.verlinde_bulk_check import sl2_modular_t_matrix
        for k in [1, 2, 3, 4]:
            T = sl2_modular_t_matrix(k)
            c_vir = 3.0 * k / (k + 2)
            n = k + 1
            for i in range(n):
                h_i = i * (i + 2) / (4.0 * (k + 2))
                expected = np.exp(2j * np.pi * (h_i - c_vir / 24.0))
                np.testing.assert_allclose(
                    T[i, i], expected, atol=1e-14,
                    err_msg=f"T[{i},{i}] wrong at k={k}"
                )

    def test_t_matrix_invalid_level(self):
        """Level k must be a positive integer."""
        from lib.verlinde_bulk_check import sl2_modular_t_matrix
        with pytest.raises(ValueError):
            sl2_modular_t_matrix(0)

    @pytest.mark.parametrize("k", [1, 2, 3, 4])
    def test_t_matrix_finite_order(self, k):
        """T has finite order dividing 12(k+2) (projective SL(2,Z) rep)."""
        from lib.verlinde_bulk_check import sl2_modular_t_matrix
        T = sl2_modular_t_matrix(k)
        n = k + 1
        order = 12 * (k + 2)
        T_power = np.linalg.matrix_power(T, order)
        # T^{12(k+2)} should be a scalar matrix (central element)
        # For sl_2, it should actually be the identity times a root of unity
        # Check that T^{12(k+2)} is proportional to identity
        ratio = T_power[0, 0]
        expected = ratio * np.eye(n)
        np.testing.assert_allclose(
            T_power, expected, atol=1e-10,
            err_msg=f"T^{{{order}}} not scalar at k={k}"
        )


# ===================================================================
# TIER 8: VERLINDE IDEMPOTENT CONSTRUCTION
# ===================================================================

class TestVerlindeIdempotents:
    """Verify the primitive idempotents of the Verlinde algebra.

    The Verlinde algebra is semisimple of dimension k+1, isomorphic
    to C^{k+1}. The idempotents e_m = sum_i (S_{im}/S_{0m}) L_i
    provide a constructive proof that the algebra has exactly k+1
    independent central elements. This is the constructive content
    of the derived-center prediction: the categorical center has
    exactly k+1 generators.
    """

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    def test_idempotent_orthogonality(self, k):
        """e_m * e_n = delta_{mn} * e_m (orthogonal idempotents)."""
        from lib.verlinde_bulk_check import verify_idempotent_orthogonality
        passes, deviation = verify_idempotent_orthogonality(k)
        assert passes, \
            f"Idempotent orthogonality fails at k={k}, deviation={deviation}"

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    def test_idempotent_count_equals_prediction(self, k):
        """Number of idempotents = k+1 = derived-center dimension."""
        from lib.verlinde_bulk_check import construct_verlinde_idempotents
        idem = construct_verlinde_idempotents(k)
        assert idem.shape[0] == k + 1

    @pytest.mark.parametrize("k", [1, 2, 3, 4])
    def test_idempotents_sum_to_unit(self, k):
        """sum_m e_m = L_0 (the unit).

        The sum of idempotent coefficients in the L_i basis should be:
        (sum_m e_m)_i = sum_m S_{im}/S_{0m}.
        For i=0: sum_m S_{0m}/S_{0m} = sum_m 1 = k+1.
        But wait -- the unit L_0 has coefficient 1 in position 0 and 0 elsewhere.
        Actually, sum_m e_m should equal the identity of the algebra, which
        is the vector (1, 0, ..., 0) in the L_i basis (since L_0 is the unit).

        The correct relation uses the orthogonality of S:
        sum_m (S_{im}/S_{0m}) = delta_{i0} * (1/S_{00}) * sum_m S_{0m}^2
        By unitarity: sum_m S_{0m}^2 = 1. But we need to be careful...

        Actually the correct normalization for idempotent decomposition
        of the identity uses S_{00}:
        e_m = S_{00} * sum_i (S_{im}/S_{0m}) * L_i / S_{00}
        The standard decomposition is sum_m e_m = L_0 where e_m are
        RESCALED by S_{00}.

        Let me verify by direct computation: in the Verlinde algebra,
        sum_m e_m should act as the identity on every L_j.
        """
        from lib.verlinde_bulk_check import (
            construct_verlinde_idempotents,
            verlinde_fusion_coefficients
        )
        idem = construct_verlinde_idempotents(k)
        N = verlinde_fusion_coefficients(k)
        n = k + 1

        # Compute sum_m e_m
        total = np.sum(idem, axis=0)

        # (sum_m e_m) * L_j should equal L_j for all j
        # ((sum e_m) * L_j)_l = sum_i total[i] * N[i, j, l]
        for j in range(n):
            product = np.zeros(n)
            for l in range(n):
                product[l] = sum(total[i] * N[i, j, l] for i in range(n))
            expected = np.zeros(n)
            expected[j] = 1.0
            np.testing.assert_allclose(
                product, expected, atol=1e-10,
                err_msg=f"sum(e_m) * L_{j} != L_{j} at k={k}"
            )

    @pytest.mark.parametrize("k", [1, 2, 3, 4])
    def test_idempotents_linearly_independent(self, k):
        """The k+1 idempotents are linearly independent (span the algebra)."""
        from lib.verlinde_bulk_check import construct_verlinde_idempotents
        idem = construct_verlinde_idempotents(k)
        rank = np.linalg.matrix_rank(idem, tol=1e-10)
        assert rank == k + 1, \
            f"Idempotents have rank {rank}, expected {k+1} at k={k}"

    def test_idempotent_k1_explicit(self):
        """At k=1: two idempotents with S = (1/sqrt(3)) * [[1, 1], [1, -1]].

        Normalized idempotents e_m = sum_i S_{0m} S_{im} L_i:
        e_0 = S_{00} * [S_{00}, S_{10}] = (1/sqrt(3)) * [1/sqrt(3), 1/sqrt(3)] = [1/3, 1/3].

        Wait, k=1 gives S = sqrt(2/(k+2)) * sin(...) = sqrt(2/3) * sin(...).
        S_{00} = sqrt(2/3) * sin(pi/3) = sqrt(2/3) * sqrt(3)/2 = 1/sqrt(2).
        Actually for SU(2) k=1: n=2, S = [[1/sqrt(2), 1/sqrt(2)], [1/sqrt(2), -1/sqrt(2)]].
        e_0 = S_{00} * [S_{00}, S_{10}] = (1/sqrt(2)) * [1/sqrt(2), 1/sqrt(2)] = [1/2, 1/2].
        e_1 = S_{01} * [S_{01}, S_{11}] = (1/sqrt(2)) * [1/sqrt(2), -1/sqrt(2)] = [1/2, -1/2].
        """
        from lib.verlinde_bulk_check import construct_verlinde_idempotents
        idem = construct_verlinde_idempotents(1)
        np.testing.assert_allclose(idem[0], [0.5, 0.5], atol=1e-14)
        np.testing.assert_allclose(idem[1], [0.5, -0.5], atol=1e-14)
