r"""C4 strictification obstruction for Kac-Moody algebras with root multiplicities > 1.

Implements the analysis of the spectral Drinfeld strictification obstruction
(Theorem thm:complete-strictification in dg_shifted_factorization_bridge.tex)
beyond simple Lie algebras.

MATHEMATICAL SUMMARY
--------------------

For simple Lie algebras, root multiplicity = 1 forces the spectral Drinfeld
class to vanish at every filtration (thm:complete-strictification).  The
mechanism: the multilinear Lie space at each root sector is one-dimensional,
so the obstruction is a scalar determined by a single equation that coproduct
rigidity supplies.

For Kac-Moody algebras with root multiplicities > 1, this mechanism fails.
Two weaker conditions can still force vanishing:

  (i)  ROOT-SPACE ONE-DIMENSIONALITY: mult(gamma) = 1 at the target root
       gamma.  Applies to all real roots of any KM algebra.

  (ii) ROOT-SPACE ABELIANNESS: the root space g_gamma is abelian
       ([g_gamma, g_gamma] = 0).  Then the Cartan gauge-twist /
       abelian strictification theorem (thm:abelian-strictification)
       makes the exponential exact.  Applies to imaginary root spaces
       of affine KM algebras, where g_{n*delta} ~ h^n is abelian
       (the Cartan subalgebra tensored with loop powers).

The combined condition --- at every root sector, either mult = 1 or
g_gamma is abelian --- is satisfied by:
  - All simple Lie algebras (all roots have mult 1)
  - All untwisted affine Lie algebras (imaginary root spaces abelian)

It FAILS for:
  - Hyperbolic KM algebras (non-abelian root spaces with mult > 1)
  - General indefinite KM algebras

ROOT MULTIPLICITIES
-------------------

For simple Lie algebras: all mult = 1 (by the root-space theorem).

For untwisted affine g^hat (g simple of rank r):
  - Real roots alpha + n*delta: mult = 1
  - Imaginary roots n*delta (n >= 1): mult = r = rank(g)

For the rank-2 hyperbolic KM algebra with Cartan matrix [[2,-a],[-a,2]]
(a >= 3, so det = 4 - a^2 < 0): root multiplicities grow exponentially,
computed via the Weyl-Kac denominator identity.

REFERENCES
----------
  Vol II: dg_shifted_factorization_bridge.tex, Theorem thm:complete-strictification
  Vol II: dg_shifted_factorization_bridge.tex, Conjecture conj:affine-strictification
  Vol II: dg_shifted_factorization_bridge.tex, Theorem thm:abelian-strictification
  Kac: Infinite-dimensional Lie Algebras, 3rd ed., Ch. 11 (denominator identity)
  Kang (1994): Root multiplicities of Kac-Moody algebras
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from math import gcd, factorial
from typing import Any, Dict, List, Optional, Tuple


# =========================================================================
# 1. CARTAN MATRIX UTILITIES
# =========================================================================

def cartan_matrix_type(A: List[List[int]]) -> str:
    """Classify a 2x2 symmetric Cartan matrix as finite, affine, or indefinite.

    For a 2x2 GCM [[2, a01], [a10, 2]] with a01, a10 <= 0:
      det = 4 - a01*a10
      det > 0: finite type
      det = 0: affine type
      det < 0: indefinite (hyperbolic for rank 2)

    Parameters
    ----------
    A : list of list of int
        2x2 generalized Cartan matrix.

    Returns
    -------
    str
        One of 'finite', 'affine', 'indefinite'.
    """
    if len(A) != 2 or len(A[0]) != 2:
        raise ValueError("Only 2x2 Cartan matrices supported")
    det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    if det > 0:
        return 'finite'
    elif det == 0:
        return 'affine'
    else:
        return 'indefinite'


def inner_product(alpha: Tuple[int, ...], beta: Tuple[int, ...],
                  A: List[List[int]]) -> int:
    r"""Compute the bilinear form (alpha | beta) from the Cartan matrix.

    For alpha = sum_i m_i alpha_i and beta = sum_j n_j alpha_j:
      (alpha | beta) = sum_{i,j} m_i A_{ij} n_j

    Assumes the Cartan matrix is symmetrizable with all d_i = 1.
    """
    rank = len(A)
    return sum(alpha[i] * A[i][j] * beta[j]
               for i in range(rank) for j in range(rank))


def norm_squared(alpha: Tuple[int, ...], A: List[List[int]]) -> int:
    """Compute (alpha | alpha)."""
    return inner_product(alpha, alpha, A)


# =========================================================================
# 2. SIMPLE LIE ALGEBRA: ROOT MULTIPLICITY = 1
# =========================================================================

_SIMPLE_LIE_TYPES = {'A', 'B', 'C', 'D', 'E', 'F', 'G'}


def simple_root_multiplicity(lie_type: str, rank: int) -> Dict[str, Any]:
    """Root multiplicity data for a simple Lie algebra: always 1.

    Parameters
    ----------
    lie_type : str
        Lie type: 'A', 'B', 'C', 'D', 'E', 'F', 'G'.
    rank : int
        Rank of the algebra.

    Returns
    -------
    dict
        Keys: 'max_mult', 'all_mult_one', 'c4_holds', 'mechanism'.
    """
    if lie_type not in _SIMPLE_LIE_TYPES:
        raise ValueError(f"Unknown type '{lie_type}'")
    return {
        'max_mult': 1,
        'all_mult_one': True,
        'c4_holds': True,
        'mechanism': 'root_space_one_dimensionality',
        'lie_type': lie_type,
        'rank': rank,
    }


# =========================================================================
# 3. AFFINE KM: ROOT MULTIPLICITIES
# =========================================================================

def affine_root_multiplicities(finite_rank: int,
                               max_height: int = 10) -> Dict[Tuple[int, ...], int]:
    r"""Root multiplicities for an untwisted affine KM algebra g^hat.

    In the 2-node realization (simple roots alpha_0, alpha_1 for rank-1
    finite part), or the general (rank+1)-node affine Cartan matrix:

      Real roots: mult = 1
      Imaginary roots n*delta (n >= 1): mult = finite_rank

    For sl_2^hat: finite_rank = 1, so ALL multiplicities = 1.
    For sl_N^hat (N >= 3): finite_rank = N-1 >= 2.
    For g^hat in general: finite_rank = rank(g).

    Parameters
    ----------
    finite_rank : int
        Rank of the finite-dimensional simple Lie algebra g.
    max_height : int
        Maximum height (sum of simple root coefficients) to enumerate.

    Returns
    -------
    dict
        Maps root (as tuple of simple root coefficients) to multiplicity.
        For the 2-node realization (sl_2^hat only, finite_rank=1):
          (m, n) represents m*alpha_0 + n*alpha_1.
        For finite_rank > 1, returns a symbolic description.
    """
    if finite_rank < 1:
        raise ValueError(f"finite_rank must be >= 1, got {finite_rank}")

    result = {
        'finite_rank': finite_rank,
        'real_root_mult': 1,
        'imaginary_root_mult': finite_rank,
        'all_mult_one': (finite_rank == 1),
        'imaginary_abelian': True,  # g_{n*delta} ~ h * t^n is always abelian
    }

    # For sl_2^hat, give explicit root list in 2-node realization
    if finite_rank == 1:
        mults = {}
        for n in range(0, max_height):
            if n + (n + 1) <= 2 * max_height:
                mults[(n, n + 1)] = 1  # alpha_1 + n*delta
                mults[(n + 1, n)] = 1  # alpha_0 + n*delta
            if n >= 1 and 2 * n <= 2 * max_height:
                mults[(n, n)] = 1  # n*delta, mult = rank = 1
        result['explicit_mults'] = mults

    return result


def affine_c4_analysis(finite_rank: int) -> Dict[str, Any]:
    r"""C4 strictification analysis for untwisted affine KM.

    Three sectors:
      (1) Real roots: mult = 1, standard one-dimensionality argument.
      (2) Imaginary root sectors via multilinear brackets: surjective onto
          g_{n*delta} ~ h*t^n (abelian), so abelian strictification applies.
      (3) Higher imaginary sectors via repeated generators: handled by
          power series structure + abelianness.

    Returns
    -------
    dict
        Analysis results including c4_holds, mechanism, sectors.
    """
    return {
        'finite_rank': finite_rank,
        'c4_holds': True,
        'mechanism': 'root_one_dim_plus_abelian_gauge_twist',
        'sectors': {
            'real': {
                'mult': 1,
                'mechanism': 'root_space_one_dimensionality',
                'status': 'proved',
            },
            'imaginary': {
                'mult': finite_rank,
                'abelian': True,
                'mechanism': 'abelian_strictification',
                'status': 'proved_conditional' if finite_rank > 1 else 'proved',
                'note': ('g_{n*delta} ~ h*t^n is abelian; '
                         'Cartan gauge-twist applies' if finite_rank > 1
                         else 'all mult = 1, standard argument'),
            },
            'mixed': {
                'mechanism': 'real_root_target',
                'status': 'proved',
                'note': 'mixed sectors land in real root spaces (mult=1)',
            },
        },
    }


# =========================================================================
# 4. HYPERBOLIC KM: ROOT MULTIPLICITIES VIA DENOMINATOR IDENTITY
# =========================================================================

def _compute_weyl_terms(a01: int, a10: int,
                        max_height: int) -> Dict[Tuple[int, int], int]:
    r"""Compute the RHS of the Weyl-Kac denominator identity for rank-2 KM.

    The denominator identity:
      prod_{alpha>0} (1 - e^{-alpha})^{mult(alpha)}
        = sum_{w in W} (-1)^{l(w)} e^{w(rho) - rho}

    Returns the RHS as a dict mapping exponents to coefficients.
    """
    A = [[2, a01], [a10, 2]]
    det_A = 4 - a01 * a10

    # Compute rho: (rho, alpha_i) = 1
    # 2*rho_a + a10*rho_b = 1
    # a01*rho_a + 2*rho_b = 1
    rho_b = (2 - a01) / det_A
    rho_a = (1 - a10 * rho_b) / 2
    rho = (rho_a, rho_b)

    # Weyl reflections: s_i(v) = v - (v, alpha_i^vee) alpha_i
    # s_1(m, n) = (-m - n*a10, n)
    # s_2(m, n) = (m, -n - m*a01)
    def s_1(v):
        return (-v[0] - v[1] * a10, v[1])

    def s_2(v):
        return (v[0], -v[1] - v[0] * a01)

    # BFS over Weyl group
    w_rho_set = {rho}
    all_elements = [(1, rho)]  # (sign, w(rho))
    frontier = [(1, rho)]

    for _ in range(max_height + 15):
        new_frontier = []
        for sgn, wrho in frontier:
            for refl in [s_1, s_2]:
                nw = refl(wrho)
                if nw not in w_rho_set:
                    w_rho_set.add(nw)
                    ns = -sgn
                    all_elements.append((ns, nw))
                    new_frontier.append((ns, nw))
        frontier = new_frontier
        if not frontier:
            break

    # Collect RHS: rho - w(rho) for each w
    rhs = defaultdict(int)
    for sgn, wrho in all_elements:
        dm = rho[0] - wrho[0]
        dn = rho[1] - wrho[1]
        im, in_ = round(dm), round(dn)
        if abs(dm - im) < 1e-10 and abs(dn - in_) < 1e-10:
            if im >= 0 and in_ >= 0 and im + in_ <= max_height:
                rhs[(im, in_)] += sgn

    return dict(rhs)


def _formal_ps_multiply(a: Dict[Tuple[int, int], float],
                        b: Dict[Tuple[int, int], float],
                        max_h: int) -> Dict[Tuple[int, int], float]:
    """Multiply two formal power series truncated at height max_h."""
    result = defaultdict(float)
    for (m1, n1), c1 in a.items():
        if m1 + n1 > max_h:
            continue
        for (m2, n2), c2 in b.items():
            if m1 + n1 + m2 + n2 > max_h:
                continue
            result[(m1 + m2, n1 + n2)] += c1 * c2
    return dict(result)


def hyperbolic_root_multiplicities(a01: int, a10: int,
                                   max_height: int = 12
                                   ) -> Dict[Tuple[int, int], int]:
    r"""Root multiplicities for rank-2 hyperbolic KM algebra.

    Cartan matrix A = [[2, a01], [a10, 2]] with a01, a10 < 0
    and a01*a10 > 4 (indefinite/hyperbolic).

    Uses the Weyl-Kac denominator identity:
      prod_{alpha>0} (1-q^alpha)^{mult(alpha)} = RHS(q)

    Taking -log and applying Moebius inversion to extract mult.

    Parameters
    ----------
    a01, a10 : int
        Off-diagonal Cartan matrix entries (both negative).
    max_height : int
        Maximum root height to compute.

    Returns
    -------
    dict
        Maps (m, n) -> mult for positive roots m*alpha_1 + n*alpha_2.
    """
    det_A = 4 - a01 * a10
    if det_A >= 0:
        raise ValueError(f"Not indefinite: det(A) = {det_A} >= 0")

    rhs = _compute_weyl_terms(a01, a10, max_height)

    # Compute f = rhs_series - 1 (non-constant part)
    f = {}
    for (m, n), coeff in rhs.items():
        if m == 0 and n == 0:
            continue
        f[(m, n)] = float(coeff)

    # Compute -log(1 + f) = sum_{k>=1} (-1)^k / k * f^k
    neg_log: Dict[Tuple[int, int], float] = defaultdict(float)
    f_power = dict(f)  # f^1

    for k in range(1, max_height + 1):
        coeff_k = ((-1) ** k) / k
        for (m, n), c in f_power.items():
            if m + n <= max_height:
                neg_log[(m, n)] += coeff_k * c
        if k < max_height:
            f_power = _formal_ps_multiply(f_power, f, max_height)

    # Moebius inversion: c(m,n) = sum_{d | gcd(m,n)} (1/d) mult(m/d, n/d)
    # => mult(m,n) = c(m,n) - sum_{d >= 2, d | gcd(m,n)} (1/d) mult(m/d, n/d)
    mult = {}
    for h in range(1, max_height + 1):
        for m in range(h + 1):
            n = h - m
            c_val = neg_log.get((m, n), 0.0)

            g = gcd(m, n) if (m > 0 and n > 0) else max(m, n)
            for d in range(2, g + 1):
                if m % d == 0 and n % d == 0:
                    red = (m // d, n // d)
                    if red in mult:
                        c_val -= mult[red] / d

            m_val = round(c_val)
            if abs(c_val - m_val) < 0.01 and m_val > 0:
                mult[(m, n)] = m_val

    return mult


# =========================================================================
# 5. ROOT CLASSIFICATION
# =========================================================================

def classify_root(alpha: Tuple[int, ...], A: List[List[int]],
                  mult: int) -> Dict[str, Any]:
    r"""Classify a root by type and C4 status.

    Parameters
    ----------
    alpha : tuple of int
        Root in simple root coordinates.
    A : list of list of int
        Cartan matrix.
    mult : int
        Root multiplicity.

    Returns
    -------
    dict
        Classification including root_type, c4_status, mechanism.
    """
    ns = norm_squared(alpha, A)

    if ns > 0:
        root_type = 'real'
    elif ns == 0:
        root_type = 'lightlike'
    else:
        root_type = 'imaginary'

    km_type = cartan_matrix_type(A)

    # C4 analysis
    if mult == 1:
        c4_status = 'vanishes'
        mechanism = 'root_space_one_dimensionality'
    elif km_type == 'affine' and root_type in ('lightlike', 'imaginary'):
        c4_status = 'vanishes'
        mechanism = 'abelian_gauge_twist'
    else:
        c4_status = 'potentially_nontrivial'
        mechanism = 'no_known_vanishing_mechanism'

    return {
        'root': alpha,
        'mult': mult,
        'norm_squared': ns,
        'root_type': root_type,
        'km_type': km_type,
        'c4_status': c4_status,
        'mechanism': mechanism,
    }


# =========================================================================
# 6. MULTILINEAR LIE SPACE DIMENSION
# =========================================================================

def free_multilinear_lie_dim(n: int) -> int:
    r"""Dimension of the multilinear part of the free Lie algebra on n generators.

    By the Dynkin-Specht-Wever theorem, the multilinear degree-n component
    of the free Lie algebra on n generators has dimension (n-1)!.

    This is an UPPER BOUND for the multilinear Lie space in a KM algebra
    (the Jacobi identity and Serre relations reduce the dimension).
    """
    if n < 1:
        raise ValueError(f"n must be >= 1, got {n}")
    return factorial(n - 1)


def path_multilinear_lie_dim(n: int) -> int:
    r"""Dimension of the multilinear part of the path Lie algebra on n generators.

    The path Lie algebra L_path(n) has generators X_1,...,X_n with
    [X_i, X_j] = 0 for |i-j| >= 2.

    By Theorem thm:path-one-dim, this is always 1.
    """
    if n < 1:
        raise ValueError(f"n must be >= 1, got {n}")
    return 1


def star_multilinear_lie_dim_free() -> int:
    r"""Dimension of the multilinear part of the D4-star free Lie algebra.

    The D4-star has 4 generators X_1, X_c, X_2, X_3 with:
      [X_1, X_2] = [X_1, X_3] = [X_2, X_3] = 0
      [X_i, X_c] potentially nonzero for i = 1, 2, 3.

    In the FREE Lie algebra modulo non-adjacency, this is 2.
    In any simple Lie algebra, the Jacobi collapse (lem:jacobi-collapse)
    reduces it to 1.
    """
    return 2


def star_multilinear_lie_dim_simple() -> int:
    """After Jacobi collapse in a simple Lie algebra, the D4-star gives dim 1."""
    return 1


# =========================================================================
# 7. SPECTRAL DRINFELD CLASS ANALYSIS
# =========================================================================

def spectral_drinfeld_class_analysis(
    alpha: Tuple[int, ...],
    mult: int,
    A: List[List[int]],
    is_abelian: bool = False,
) -> Dict[str, Any]:
    r"""Analyze the spectral Drinfeld class at a given root sector.

    The spectral Drinfeld class D_spec at filtration n, root sector gamma,
    is a cohomology class valued in g_gamma.

    Vanishing mechanisms:
      (i)   mult(gamma) = 1: target is 1-dim, scalar, coproduct rigidity kills.
      (ii)  g_gamma abelian: Cartan gauge-twist / abelian strictification.
      (iii) Neither: potentially nontrivial obstruction.

    Parameters
    ----------
    alpha : tuple
        Target root in simple root coordinates.
    mult : int
        mult(gamma) = dim(g_gamma).
    A : list of list of int
        Cartan matrix.
    is_abelian : bool
        Whether the root space g_gamma is abelian.

    Returns
    -------
    dict
        Analysis with keys: vanishes, mechanism, obstruction_dim, etc.
    """
    height = sum(alpha)
    ns = norm_squared(alpha, A)

    if mult == 1:
        return {
            'root': alpha,
            'mult': mult,
            'height': height,
            'norm_squared': ns,
            'vanishes': True,
            'mechanism': 'root_space_one_dimensionality',
            'obstruction_dim': 0,
            'explanation': ('Target root space is 1-dimensional. '
                            'Obstruction is a scalar determined by '
                            'coproduct rigidity.'),
        }

    if is_abelian:
        return {
            'root': alpha,
            'mult': mult,
            'height': height,
            'norm_squared': ns,
            'vanishes': True,
            'mechanism': 'abelian_gauge_twist',
            'obstruction_dim': 0,
            'explanation': ('Root space g_gamma is abelian. '
                            'Cartan gauge-twist / abelian strictification '
                            '(thm:abelian-strictification) applies. '
                            'Exponential is exact.'),
        }

    # mult > 1 and not abelian: potential obstruction
    # Upper bound on multilinear Lie space dimension
    ml_dim_upper = min(free_multilinear_lie_dim(height), mult)
    # The obstruction can have up to mult components
    # Coproduct rigidity provides mult equations
    # But the cocycle space can be larger
    obstruction_dim_estimate = max(0, mult - 1)

    return {
        'root': alpha,
        'mult': mult,
        'height': height,
        'norm_squared': ns,
        'vanishes': False,
        'mechanism': 'none',
        'obstruction_dim': obstruction_dim_estimate,
        'multilinear_dim_upper': ml_dim_upper,
        'explanation': (f'Root space has mult = {mult} > 1 and is non-abelian. '
                        f'The spectral Drinfeld class is valued in a '
                        f'{mult}-dimensional space. Neither root-space '
                        f'one-dimensionality nor abelian gauge-twist applies. '
                        f'Obstruction is potentially nontrivial.'),
    }


# =========================================================================
# 8. FULL C4 ANALYSIS FOR A KM ALGEBRA
# =========================================================================

def c4_full_analysis(
    cartan_type: str,
    A: Optional[List[List[int]]] = None,
    finite_rank: Optional[int] = None,
    max_height: int = 10,
) -> Dict[str, Any]:
    r"""Complete C4 strictification analysis for a Kac-Moody algebra.

    Parameters
    ----------
    cartan_type : str
        One of 'simple', 'affine', 'hyperbolic'.
    A : list of list of int, optional
        Cartan matrix (required for 'hyperbolic').
    finite_rank : int, optional
        Rank of the finite part (required for 'affine').
    max_height : int
        Maximum root height for hyperbolic computation.

    Returns
    -------
    dict
        Complete analysis including c4_holds, mechanism, root data.
    """
    if cartan_type == 'simple':
        return {
            'cartan_type': 'simple',
            'c4_holds': True,
            'mechanism': 'root_space_one_dimensionality',
            'max_root_mult': 1,
            'obstruction_sectors': [],
        }

    if cartan_type == 'affine':
        if finite_rank is None:
            raise ValueError("finite_rank required for affine type")
        analysis = affine_c4_analysis(finite_rank)
        analysis['cartan_type'] = 'affine'
        analysis['max_root_mult'] = finite_rank
        analysis['obstruction_sectors'] = []
        return analysis

    if cartan_type == 'hyperbolic':
        if A is None:
            raise ValueError("Cartan matrix A required for hyperbolic type")
        a01, a10 = A[0][1], A[1][0]
        mults = hyperbolic_root_multiplicities(a01, a10, max_height)

        # Find obstruction sectors: roots with mult > 1
        obstruction_sectors = []
        for alpha, m in sorted(mults.items(), key=lambda x: (sum(x[0]), x[0])):
            if m > 1:
                ns = norm_squared(alpha, A)
                obstruction_sectors.append({
                    'root': alpha,
                    'mult': m,
                    'norm_squared': ns,
                    'height': sum(alpha),
                    'c4_status': 'potentially_nontrivial',
                })

        c4_holds = len(obstruction_sectors) == 0
        max_mult = max(mults.values()) if mults else 0

        return {
            'cartan_type': 'hyperbolic',
            'cartan_matrix': A,
            'c4_holds': c4_holds,
            'mechanism': ('root_space_one_dimensionality' if c4_holds
                          else 'FAILS_non_abelian_mult_gt_1'),
            'max_root_mult': max_mult,
            'total_roots': len(mults),
            'roots_with_mult_gt_1': len(obstruction_sectors),
            'first_obstruction_height': (obstruction_sectors[0]['height']
                                         if obstruction_sectors else None),
            'obstruction_sectors': obstruction_sectors,
            'all_mults': mults,
        }

    raise ValueError(f"Unknown cartan_type: {cartan_type}")


# =========================================================================
# 9. AFFINE sl_3^hat: EXPLICIT MULTILINEAR BRACKET COMPUTATION
# =========================================================================

def sl3hat_delta_brackets() -> Dict[str, Any]:
    r"""Compute the multilinear brackets at the delta root space of sl_3^hat.

    In sl_3^hat:
      E_0 = E_31 * t,  E_1 = E_12,  E_2 = E_23
      delta = alpha_0 + alpha_1 + alpha_2
      g_delta = span{h_1*t, h_2*t}, dim = 2, ABELIAN

    Multilinear brackets (each E_i used once):
      [E_0, [E_1, E_2]] = -(h_1 + h_2) * t
      [E_1, [E_0, E_2]] = -h_1 * t

    These are linearly independent and span g_delta.

    Returns
    -------
    dict
        Bracket computation results.
    """
    return {
        'algebra': 'sl_3^hat',
        'root': 'delta = alpha_0 + alpha_1 + alpha_2',
        'root_space_dim': 2,
        'root_space_basis': ['h_1 * t', 'h_2 * t'],
        'root_space_abelian': True,
        'brackets': {
            '[E_0, [E_1, E_2]]': '-(h_1 + h_2) * t',
            '[E_1, [E_0, E_2]]': '-h_1 * t',
        },
        'linearly_independent': True,
        'multilinear_dim': 2,
        'surjective': True,
        'c4_vanishes': True,
        'mechanism': 'abelian_gauge_twist',
        'note': ('The multilinear map is surjective onto g_delta, '
                 'but g_delta is abelian, so the Cartan gauge-twist '
                 '(thm:abelian-strictification) applies. The spectral '
                 'Drinfeld class vanishes despite mult > 1.'),
    }


# =========================================================================
# 10. WEAKER CONDITION THEOREM
# =========================================================================

def weaker_vanishing_condition(mult: int, is_abelian: bool) -> Dict[str, Any]:
    r"""Check whether the weaker vanishing condition holds at a root sector.

    The weaker condition (sufficient for C4 vanishing):
      EITHER mult(gamma) = 1 (root-space one-dimensionality)
      OR g_gamma is abelian (Cartan gauge-twist applies)

    This is the PRECISE boundary of C4 strictification:
      - Satisfied by: all simple Lie algebras, all untwisted affine
      - Failed by: hyperbolic with non-abelian root spaces

    Parameters
    ----------
    mult : int
        Root multiplicity.
    is_abelian : bool
        Whether the root space is abelian.

    Returns
    -------
    dict
        Analysis result.
    """
    if mult == 1:
        return {
            'vanishes': True,
            'condition': 'mult_one',
            'mechanism': 'root_space_one_dimensionality',
        }
    if is_abelian:
        return {
            'vanishes': True,
            'condition': 'abelian',
            'mechanism': 'abelian_gauge_twist',
        }
    return {
        'vanishes': False,
        'condition': 'neither',
        'obstruction': f'mult = {mult}, non-abelian root space',
    }
