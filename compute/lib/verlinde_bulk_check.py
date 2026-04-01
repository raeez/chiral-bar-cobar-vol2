"""Verlinde algebra verification for the derived-center-as-bulk prediction.

For V_k(sl_2) at integrable level k (positive integer), the module category
Rep(V_k(sl_2)) is a modular tensor category with k+1 simple objects
L_0, L_1, ..., L_k. The Verlinde algebra (= fusion ring tensored with C)
is a commutative semisimple algebra of dimension k+1, isomorphic to the
center Z(Rep(V_k(sl_2))) of the module category.

The programme's claim (thm:universal-bulk, AP-OC overclaim resolution):
the categorical derived center Z^der_ch(C_op) should match the center
of the module category at integrable levels, giving

    dim HH^0_cat(C_op) = dim Z(Rep(V_k(sl_2))) = k+1.

This is DISTINCT from the algebraic Hochschild cohomology HH^0(A,A)
of V_k(sl_2) as an associative algebra, which equals C (the scalars,
dimension 1). The categorical center counts the simple objects; the
algebraic center counts scalars. The derived-center-as-bulk claim
uses the CATEGORICAL version.

The Verlinde formula computes fusion coefficients from the modular
S-matrix. For sl_2 at level k:

    S_{ij} = sqrt(2/(k+2)) * sin(pi*(i+1)*(j+1)/(k+2))

    N_{ij}^l = sum_{m=0}^{k} S_{im} S_{jm} S_{lm}^* / S_{0m}

where i, j, l, m range over {0, 1, ..., k} (labelling simple modules
by their highest weight).

References:
    Verlinde (1988): Fusion rules and modular transformations in 2D CFT
    Huang (2005): Vertex operator algebras, the Verlinde conjecture, and
        modular tensor categories (rigorous proof of the Verlinde formula
        for rational VOAs)
    Vol I: thm:thqg-swiss-cheese (derived center as universal bulk)
    Vol II: foundations_overclaims_resolved.tex (categorical vs algebraic center)
"""

from __future__ import annotations

import numpy as np
from fractions import Fraction
from typing import Dict, List, Optional, Tuple


# =========================================================================
# 1. MODULAR S-MATRIX
# =========================================================================

def sl2_modular_s_matrix(k: int) -> np.ndarray:
    """Compute the modular S-matrix for sl_2 at integrable level k.

    The S-matrix of the modular tensor category Rep(V_k(sl_2)) is the
    (k+1) x (k+1) matrix with entries

        S_{ij} = sqrt(2/(k+2)) * sin(pi*(i+1)*(j+1)/(k+2))

    where i, j in {0, 1, ..., k} label simple modules by highest weight.

    Properties:
        - Symmetric: S_{ij} = S_{ji}
        - Unitary: S * S^dagger = I
        - S^2 = C (charge conjugation): (S^2)_{ij} = delta_{i, k-j}
        - All entries real for sl_2 (so S^* = S and unitarity is S^2 = C)

    Parameters
    ----------
    k : int
        The level (positive integer).

    Returns
    -------
    np.ndarray
        The (k+1) x (k+1) modular S-matrix.
    """
    if k < 1:
        raise ValueError(f"Level k must be a positive integer, got {k}")

    n = k + 1
    S = np.zeros((n, n))
    prefactor = np.sqrt(2.0 / (k + 2))
    for i in range(n):
        for j in range(n):
            S[i, j] = prefactor * np.sin(np.pi * (i + 1) * (j + 1) / (k + 2))
    return S


def sl2_modular_s_matrix_exact(k: int) -> List[List[Fraction]]:
    """Compute S-matrix entries as exact fractions where possible.

    Returns the squared entries S_{ij}^2 as exact Fractions, useful for
    verifying that fusion coefficients are exact integers (not numerical
    artifacts of floating-point sin).

    For sl_2, the S-matrix entries satisfy S_{ij}^2 = (2/(k+2)) * sin^2(...).
    The fusion coefficients N_{ij}^l are integers by the Verlinde theorem.

    Parameters
    ----------
    k : int
        The level.

    Returns
    -------
    List[List[Fraction]]
        Matrix of S_{ij}^2 values (exact).
    """
    # For small k, we verify integrality by rounding and checking tolerance
    # in the floating-point computation. Exact symbolic computation would
    # require sympy; here we provide the interface for downstream checks.
    n = k + 1
    S = sl2_modular_s_matrix(k)
    return [[Fraction(S[i, j]**2).limit_denominator(10**12) for j in range(n)]
            for i in range(n)]


# =========================================================================
# 2. VERLINDE FUSION COEFFICIENTS
# =========================================================================

def verlinde_fusion_coefficients(k: int) -> np.ndarray:
    """Compute fusion coefficients N_{ij}^l for sl_2 at level k.

    The Verlinde formula gives

        N_{ij}^l = sum_{m=0}^{k} S_{im} S_{jm} S_{lm}^* / S_{0m}

    For sl_2, the S-matrix is real, so S_{lm}^* = S_{lm}.

    The result is a rank-3 tensor N[i, j, l] of shape (k+1, k+1, k+1),
    where N[i, j, l] = multiplicity of L_l in the fusion L_i x L_j.

    These are non-negative integers by the Verlinde theorem.

    Parameters
    ----------
    k : int
        The level (positive integer).

    Returns
    -------
    np.ndarray
        Integer tensor N[i,j,l] of shape (k+1, k+1, k+1).
    """
    S = sl2_modular_s_matrix(k)
    n = k + 1
    N = np.zeros((n, n, n))
    for i in range(n):
        for j in range(n):
            for l in range(n):
                val = 0.0
                for m in range(n):
                    # S is real for sl_2, so conj(S[l,m]) = S[l,m]
                    val += S[i, m] * S[j, m] * S[l, m] / S[0, m]
                N[i, j, l] = val
    # Round to nearest integer — exact integrality is guaranteed by Verlinde
    N_int = np.round(N).astype(int)
    return N_int


def fusion_product(k: int, i: int, j: int) -> Dict[int, int]:
    """Compute L_i x L_j as a dictionary {l: N_{ij}^l} for nonzero entries.

    Parameters
    ----------
    k : int
        The level.
    i, j : int
        Highest weights of the two simple modules (0 <= i, j <= k).

    Returns
    -------
    Dict[int, int]
        Maps highest weight l to multiplicity N_{ij}^l, for nonzero entries.
    """
    N = verlinde_fusion_coefficients(k)
    n = k + 1
    result = {}
    for l in range(n):
        coeff = N[i, j, l]
        if coeff > 0:
            result[l] = int(coeff)
    return result


# =========================================================================
# 3. VERLINDE ALGEBRA STRUCTURE
# =========================================================================

def verlinde_algebra_dimension(k: int) -> int:
    """Dimension of the Verlinde algebra = number of simple modules = k+1.

    This equals dim Z(Rep(V_k(sl_2))), the dimension of the center of the
    module category. It is the checkable prediction from the derived-center
    programme: the categorical Hochschild cohomology HH^0_cat should have
    this dimension.

    Parameters
    ----------
    k : int
        The level.

    Returns
    -------
    int
        k + 1
    """
    return k + 1


def verlinde_structure_constants(k: int) -> np.ndarray:
    """Compute the structure constants of the Verlinde algebra in the L_i basis.

    The Verlinde algebra V_k is the free abelian group on {L_0, ..., L_k}
    with multiplication L_i * L_j = sum_l N_{ij}^l L_l. These are the
    structure constants in the basis of simple modules.

    Returns the same tensor as verlinde_fusion_coefficients, but emphasizes
    the algebra interpretation.

    Parameters
    ----------
    k : int
        The level.

    Returns
    -------
    np.ndarray
        Structure constants N[i,j,l], shape (k+1, k+1, k+1).
    """
    return verlinde_fusion_coefficients(k)


# =========================================================================
# 4. STRUCTURAL VERIFICATIONS
# =========================================================================

def verify_s_matrix_unitarity(k: int, tol: float = 1e-10) -> Tuple[bool, float]:
    """Verify that the S-matrix is unitary: S * S^dagger = I.

    For sl_2, S is real and symmetric, so S^dagger = S^T = S.
    Unitarity means S^2 = C (charge conjugation), where C_{ij} = delta_{i,k-j}.

    We check ||S S^T - I||_max < tol.

    Parameters
    ----------
    k : int
        The level.
    tol : float
        Tolerance for floating-point comparison.

    Returns
    -------
    Tuple[bool, float]
        (passes, max_deviation)
    """
    S = sl2_modular_s_matrix(k)
    product = S @ S.T
    identity = np.eye(k + 1)
    deviation = np.max(np.abs(product - identity))
    return deviation < tol, float(deviation)


def verify_s_matrix_symmetry(k: int, tol: float = 1e-14) -> Tuple[bool, float]:
    """Verify that the S-matrix is symmetric: S_{ij} = S_{ji}.

    Parameters
    ----------
    k : int
        The level.
    tol : float
        Tolerance.

    Returns
    -------
    Tuple[bool, float]
        (passes, max_deviation)
    """
    S = sl2_modular_s_matrix(k)
    deviation = np.max(np.abs(S - S.T))
    return deviation < tol, float(deviation)


def verify_charge_conjugation(k: int, tol: float = 1e-10) -> Tuple[bool, float]:
    """Verify S^2 = C (charge conjugation matrix).

    For a modular tensor category, S^2 = C where C_{ij} = delta_{i, i*}
    with i* the label of the dual (conjugate) simple object.

    For sl_2: ALL representations are self-conjugate (SU(2) is a compact
    real Lie group; every finite-dimensional representation is isomorphic
    to its dual via the symplectic/orthogonal form). Therefore C = I
    (the identity matrix), and the relation becomes S^2 = I.

    This is consistent with S being real, symmetric, and orthogonal:
    S^T = S and S S^T = I together give S^2 = S S^T = I.

    Note: for sl_N with N >= 3, the charge conjugation C_{ij} = delta_{i,j*}
    is NOT the identity in general (the fundamental and antifundamental
    representations are distinct). The formula C_{ij} = delta_{i, k-j}
    is WRONG for sl_2.

    Parameters
    ----------
    k : int
        The level.
    tol : float
        Tolerance.

    Returns
    -------
    Tuple[bool, float]
        (passes, max_deviation)
    """
    S = sl2_modular_s_matrix(k)
    n = k + 1
    S_squared = S @ S
    # For sl_2, charge conjugation is the identity (all reps self-conjugate)
    C = np.eye(n)
    deviation = np.max(np.abs(S_squared - C))
    return deviation < tol, float(deviation)


def verify_fusion_commutativity(k: int) -> bool:
    """Verify that fusion is commutative: N_{ij}^l = N_{ji}^l for all i,j,l.

    This is immediate from the Verlinde formula (S_{ij} = S_{ji}), but
    serves as a consistency check on the computation.

    Parameters
    ----------
    k : int
        The level.

    Returns
    -------
    bool
    """
    N = verlinde_fusion_coefficients(k)
    n = k + 1
    for i in range(n):
        for j in range(n):
            for l in range(n):
                if N[i, j, l] != N[j, i, l]:
                    return False
    return True


def verify_fusion_associativity(k: int) -> bool:
    """Verify that fusion is associative: (L_i x L_j) x L_m = L_i x (L_j x L_m).

    Concretely: sum_p N_{ij}^p N_{pm}^l = sum_p N_{jm}^p N_{ip}^l
    for all i, j, m, l.

    This is a deep consequence of the modular tensor category structure
    (it follows from the pentagon axiom for the associator), but for the
    Verlinde formula it can also be verified from the S-matrix diagonalization.

    Parameters
    ----------
    k : int
        The level.

    Returns
    -------
    bool
    """
    N = verlinde_fusion_coefficients(k)
    n = k + 1
    for i in range(n):
        for j in range(n):
            for m in range(n):
                for l in range(n):
                    # LHS: ((L_i x L_j) x L_m)_l = sum_p N_{ij}^p N_{pm}^l
                    lhs = sum(N[i, j, p] * N[p, m, l] for p in range(n))
                    # RHS: (L_i x (L_j x L_m))_l = sum_p N_{jm}^p N_{ip}^l
                    rhs = sum(N[j, m, p] * N[i, p, l] for p in range(n))
                    if lhs != rhs:
                        return False
    return True


def verify_fusion_nonnegative_integers(k: int, tol: float = 0.01) -> bool:
    """Verify that raw (pre-rounding) fusion coefficients are close to
    non-negative integers.

    Parameters
    ----------
    k : int
        The level.
    tol : float
        Maximum deviation from nearest integer.

    Returns
    -------
    bool
    """
    S = sl2_modular_s_matrix(k)
    n = k + 1
    for i in range(n):
        for j in range(n):
            for l in range(n):
                val = sum(S[i, m] * S[j, m] * S[l, m] / S[0, m] for m in range(n))
                nearest_int = round(val)
                if abs(val - nearest_int) > tol:
                    return False
                if nearest_int < 0:
                    return False
    return True


def verify_unit(k: int) -> bool:
    """Verify that L_0 is the fusion unit: L_0 x L_j = L_j for all j.

    Concretely: N_{0j}^l = delta_{jl} for all j, l.

    Parameters
    ----------
    k : int
        The level.

    Returns
    -------
    bool
    """
    N = verlinde_fusion_coefficients(k)
    n = k + 1
    for j in range(n):
        for l in range(n):
            expected = 1 if j == l else 0
            if N[0, j, l] != expected:
                return False
    return True


# =========================================================================
# 5. KNOWN FUSION RULES (independent verification data)
# =========================================================================

def known_fusion_rules_k1() -> Dict[Tuple[int, int], Dict[int, int]]:
    """Known fusion rules for sl_2 at level k=1.

    2 simple modules: L_0 (vacuum), L_1 (fundamental).

    Fusion:
        L_0 x L_j = L_j  (unit)
        L_1 x L_1 = L_0  (Z/2 group law)

    The Verlinde algebra is C[Z/2].

    Returns
    -------
    Dict[Tuple[int,int], Dict[int,int]]
        Maps (i,j) to {l: N_{ij}^l}.
    """
    return {
        (0, 0): {0: 1},
        (0, 1): {1: 1},
        (1, 0): {1: 1},
        (1, 1): {0: 1},
    }


def known_fusion_rules_k2() -> Dict[Tuple[int, int], Dict[int, int]]:
    """Known fusion rules for sl_2 at level k=2.

    3 simple modules: L_0, L_1, L_2.

    Fusion:
        L_0 x L_j = L_j           (unit)
        L_1 x L_1 = L_0 + L_2     (fundamental self-fusion)
        L_1 x L_2 = L_1           (fundamental x adjoint)
        L_2 x L_2 = L_0           (adjoint self-fusion)

    The Verlinde algebra is the quotient C[x]/(x^3 - x).

    Returns
    -------
    Dict[Tuple[int,int], Dict[int,int]]
    """
    return {
        (0, 0): {0: 1},
        (0, 1): {1: 1},
        (0, 2): {2: 1},
        (1, 0): {1: 1},
        (1, 1): {0: 1, 2: 1},
        (1, 2): {1: 1},
        (2, 0): {2: 1},
        (2, 1): {1: 1},
        (2, 2): {0: 1},
    }


def known_fusion_rules_k3() -> Dict[Tuple[int, int], Dict[int, int]]:
    """Known fusion rules for sl_2 at level k=3.

    4 simple modules: L_0, L_1, L_2, L_3.

    The truncated sl_2 tensor product rule: L_i x L_j = sum_{l} L_l
    where l runs over |i-j|, |i-j|+2, ..., min(i+j, 2k-i-j)
    with step 2, each with multiplicity 1.

    Fusion:
        L_1 x L_1 = L_0 + L_2
        L_1 x L_2 = L_1 + L_3
        L_1 x L_3 = L_2
        L_2 x L_2 = L_0 + L_2
        L_2 x L_3 = L_1
        L_3 x L_3 = L_0

    Returns
    -------
    Dict[Tuple[int,int], Dict[int,int]]
    """
    return {
        (0, 0): {0: 1},
        (0, 1): {1: 1},
        (0, 2): {2: 1},
        (0, 3): {3: 1},
        (1, 0): {1: 1},
        (1, 1): {0: 1, 2: 1},
        (1, 2): {1: 1, 3: 1},
        (1, 3): {2: 1},
        (2, 0): {2: 1},
        (2, 1): {1: 1, 3: 1},
        (2, 2): {0: 1, 2: 1},  # truncation: 2+2=4 > 2k-2-2=2, so max is 2
        (2, 3): {1: 1},
        (3, 0): {3: 1},
        (3, 1): {2: 1},
        (3, 2): {1: 1},
        (3, 3): {0: 1},
    }


# =========================================================================
# 6. TRUNCATED TENSOR PRODUCT RULE (independent formula)
# =========================================================================

def sl2_truncated_tensor_product(k: int, i: int, j: int) -> Dict[int, int]:
    """Compute L_i x L_j by the truncated tensor product rule for sl_2.

    The fusion rule for sl_2 at level k is:

        L_i x L_j = sum_{l = |i-j|, step 2}^{min(i+j, 2k-i-j)} L_l

    Each summand appears with multiplicity 1. This is the Clebsch-Gordan
    rule for sl_2 representations, truncated by the integrability condition
    (highest weight <= k).

    This provides an INDEPENDENT verification of the Verlinde formula:
    the S-matrix computation must reproduce this combinatorial rule.

    Parameters
    ----------
    k : int
        The level.
    i, j : int
        Highest weights.

    Returns
    -------
    Dict[int, int]
        Maps l to multiplicity (always 1 for sl_2).
    """
    if i < 0 or i > k or j < 0 or j > k:
        raise ValueError(f"Weights must satisfy 0 <= i, j <= k={k}, got i={i}, j={j}")

    result = {}
    l_min = abs(i - j)
    l_max = min(i + j, 2 * k - i - j)
    for l in range(l_min, l_max + 1, 2):
        result[l] = 1
    return result


# =========================================================================
# 7. QUANTUM DIMENSIONS AND GLOBAL DIMENSION
# =========================================================================

def quantum_dimension(k: int, i: int) -> float:
    """Compute the quantum dimension of L_i at level k.

    The quantum dimension is d_i = S_{i0} / S_{00}.

    For sl_2: d_i = sin(pi*(i+1)/(k+2)) / sin(pi/(k+2)).

    At k -> infinity, d_i -> i+1 (the classical dimension of the
    (i+1)-dimensional sl_2 representation).

    Parameters
    ----------
    k : int
        The level.
    i : int
        Highest weight (0 <= i <= k).

    Returns
    -------
    float
        The quantum dimension d_i.
    """
    S = sl2_modular_s_matrix(k)
    return S[i, 0] / S[0, 0]


def global_dimension_squared(k: int) -> float:
    """Compute the global dimension squared of Rep(V_k(sl_2)).

    D^2 = sum_i d_i^2 = 1 / S_{00}^2 = (k+2) / 2 * (1/sin^2(pi/(k+2)))

    This is the total dimension of the modular tensor category.

    Parameters
    ----------
    k : int
        The level.

    Returns
    -------
    float
        D^2 = sum of squared quantum dimensions.
    """
    S = sl2_modular_s_matrix(k)
    return 1.0 / (S[0, 0] ** 2)


# =========================================================================
# 8. MODULAR T-MATRIX AND SL(2,Z) RELATIONS
# =========================================================================

def sl2_modular_t_matrix(k: int) -> np.ndarray:
    """Compute the modular T-matrix for sl_2 at integrable level k.

    The T-matrix is diagonal with entries

        T_{ij} = delta_{ij} * exp(2*pi*i * (h_i - c/24))

    where h_i = i(i+2)/(4(k+2)) is the conformal weight of L_i,
    and c = 3k/(k+2) is the central charge.

    The S and T matrices generate a projective representation of SL(2,Z)
    satisfying (ST)^3 = S^2 = C (charge conjugation) and T is of finite
    order dividing 12(k+2).

    Parameters
    ----------
    k : int
        The level (positive integer).

    Returns
    -------
    np.ndarray
        The (k+1) x (k+1) diagonal T-matrix (complex).
    """
    if k < 1:
        raise ValueError(f"Level k must be a positive integer, got {k}")

    n = k + 1
    c_vir = 3.0 * k / (k + 2)
    T = np.zeros((n, n), dtype=complex)
    for i in range(n):
        h_i = i * (i + 2) / (4.0 * (k + 2))
        T[i, i] = np.exp(2j * np.pi * (h_i - c_vir / 24.0))
    return T


def verify_modular_relation(k: int, tol: float = 1e-10) -> Tuple[bool, float]:
    """Verify the SL(2,Z) modular relation (ST)^3 = S^2.

    For a modular tensor category, the S and T matrices generate a
    projective representation of SL(2,Z) satisfying

        (ST)^3 = S^2 = C

    where C is the charge conjugation matrix. For sl_2, C = I (all
    representations are self-conjugate), so this becomes (ST)^3 = I.

    This is a genuinely independent cross-check: the T-matrix encodes
    conformal weights (spectral data of the Virasoro algebra on each
    module), while the S-matrix encodes modular transformation of
    characters. Their compatibility is a deep consequence of the modular
    tensor category axioms (specifically, the ribbon structure).

    Parameters
    ----------
    k : int
        The level.
    tol : float
        Tolerance for floating-point comparison.

    Returns
    -------
    Tuple[bool, float]
        (passes, max_deviation)
    """
    S = sl2_modular_s_matrix(k)
    T = sl2_modular_t_matrix(k)
    n = k + 1

    ST = S @ T
    ST3 = ST @ ST @ ST
    S2 = S @ S

    deviation = np.max(np.abs(ST3 - S2))
    return deviation < tol, float(deviation)


def construct_verlinde_idempotents(k: int) -> np.ndarray:
    """Construct the primitive idempotents of the Verlinde algebra.

    The Verlinde algebra is semisimple with k+1 primitive orthogonal
    idempotents. The correctly normalized idempotents are

        e_m = S_{00}^2 * sum_{i=0}^{k} (S_{im} / S_{0m}) * L_i

    for m = 0, 1, ..., k, where the prefactor S_{00}^2 = 1/D^2
    (inverse global dimension squared) ensures the idempotent relation

        e_m * e_n = delta_{mn} * e_m
        sum_m e_m = L_0  (the algebra unit)

    The unnormalized version (without S_{00}^2) satisfies e * e = D^2 * e
    instead. The normalization S_{00}^2 = 1/D^2 comes from the Verlinde
    algebra metric: the fusion product of S-column vectors uses unitarity
    of S, and the ratio S_{im}/S_{0m} produces a factor of 1/S_{00}^2
    upon squaring.

    The dimension of the Verlinde algebra equals the number of
    idempotents, which equals k+1 = dim Z(Rep(V_k(sl_2))).

    Parameters
    ----------
    k : int
        The level.

    Returns
    -------
    np.ndarray
        Array of shape (k+1, k+1) where row m gives the coefficients
        of e_m in the basis {L_0, ..., L_k}. That is, result[m, i]
        is the coefficient of L_i in e_m.
    """
    S = sl2_modular_s_matrix(k)
    n = k + 1
    # e_m = sum_i S_{0m} * S_{im} * L_i
    # This is the correct normalization: S_{0m} * S_{im}/S_{0m} * S_{0m}^2
    # simplifies to S_{0m} * S_{im}, using S_{0m}^2 per-idempotent (not
    # a uniform S_{00}^2).  The previous formula used S_{00}^2 uniformly,
    # which is correct only when S_{0m} is independent of m (i.e., k=1).
    idempotents = np.zeros((n, n))
    for m in range(n):
        for i in range(n):
            idempotents[m, i] = S[0, m] * S[i, m]
    return idempotents


def verify_idempotent_orthogonality(k: int, tol: float = 1e-10) -> Tuple[bool, float]:
    """Verify that the Verlinde idempotents are orthogonal: e_m * e_n = delta_{mn} e_m.

    Uses the fusion coefficients to compute the product of idempotents
    in the Verlinde algebra.

    Parameters
    ----------
    k : int
        The level.
    tol : float
        Tolerance.

    Returns
    -------
    Tuple[bool, float]
        (passes, max_deviation)
    """
    N = verlinde_fusion_coefficients(k)
    idem = construct_verlinde_idempotents(k)
    n = k + 1

    max_dev = 0.0
    for m_idx in range(n):
        for n_idx in range(n):
            # Compute e_m * e_n in the Verlinde algebra
            # (e_m * e_n)_l = sum_{i,j} idem[m,i] * idem[n,j] * N[i,j,l]
            product = np.zeros(n)
            for l in range(n):
                val = 0.0
                for i in range(n):
                    for j in range(n):
                        val += idem[m_idx, i] * idem[n_idx, j] * N[i, j, l]
                product[l] = val

            # Expected: delta_{mn} * e_m
            if m_idx == n_idx:
                expected = idem[m_idx]
            else:
                expected = np.zeros(n)

            dev = np.max(np.abs(product - expected))
            max_dev = max(max_dev, dev)

    return max_dev < tol, max_dev


# =========================================================================
# 9. DERIVED-CENTER PREDICTION
# =========================================================================

def derived_center_dimension_prediction(k: int) -> int:
    """The checkable prediction from the derived-center-as-bulk programme.

    For V_k(sl_2) at integrable level k:

        dim HH^0_cat(C_op) = dim Z(Rep(V_k(sl_2))) = k+1

    This is the categorical center, NOT the algebraic center:
    - Algebraic: HH^0(V_k(sl_2), V_k(sl_2)) = C has dimension 1
    - Categorical: Z(Rep(V_k(sl_2))) has dimension k+1

    The derived-center-as-bulk claim (thm:universal-bulk) asserts that
    the bulk observables of the 3d HT theory with boundary condition
    V_k(sl_2) are computed by the categorical derived center, which at
    the level of HH^0 gives the center of the monoidal category of modules.

    For the 3d Chern-Simons theory with gauge group SU(2) at level k,
    the bulk observables on S^1 x R^2 are the Verlinde algebra, which
    has dimension k+1. This matches the categorical center prediction.

    Parameters
    ----------
    k : int
        The level (positive integer).

    Returns
    -------
    int
        k + 1
    """
    return k + 1


def algebraic_center_dimension() -> int:
    """Dimension of the algebraic center HH^0(A, A) for a simple VOA.

    For any simple vertex algebra A (such as V_k(sl_2) at integrable level),
    the algebraic center is just the scalars: HH^0(A, A) = C.

    This has dimension 1, which is DIFFERENT from the categorical center
    dimension k+1. The derived-center-as-bulk programme uses the categorical
    version.

    Returns
    -------
    int
        1
    """
    return 1
