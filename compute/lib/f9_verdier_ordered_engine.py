"""F9 open-colour Verdier engine: B^ord(A^op) vs B^ord(A)^cop intertwining.

Frontier problem F9 asks whether a Verdier-type duality on the open colour
exists. On Ran(X) the closed-colour Verdier functor

    D_Ran : Dmod(Ran(X))^op -> Dmod(Ran(X))

intertwines bar(A) and bar(A^!) (factorization_swiss_cheese.tex:148,
chapters/theory/foundations.tex:3116, BD04 Ch.3, FG12). The ordered bar
B^ord(A) does not live on Ran(X) but on the ordered configuration space
Conf^<_n(R), which is a disjoint union of n! contractible components.
Pushforward to Ran loses ordering, so the closed-colour Verdier route
does not extend to the open colour directly.

What IS available now is the open-colour intertwining of
Theorem thm:opposite (ordered_associative_chiral_kd_core.tex:451;
ordered_associative_chiral_kd.tex:410):

    R_A : B^ord(A^op)  ~>  B^ord(A)^cop

induced by the order-reversal involution

    rho : Conf^<_n(R) -> Conf^<_n(R),
          (t_1 < ... < t_n)  |->  (-t_n < ... < -t_1).

The induced map on suspended bar words is

    R_A [s^{-1} a_1 | ... | s^{-1} a_n]
        = sigma_{i<j}(-1)^{(|a_i|+1)(|a_j|+1)} [s^{-1} a_n | ... | s^{-1} a_1].

Theorem thm:opposite shows that R_A is a chain map intertwining the
bar differential of A^op with that of A, and intertwines the
deconcatenation coproduct with its opposite. Thus the open-colour
counterpart of the closed-colour Verdier identity
D_Ran(bar(A)) ~ bar(A^!) is the (proved!) intertwining of
B^ord(A^op) with B^ord(A)^cop.

This engine verifies the intertwining at finite bar degrees:

  (1) R_A is a chain map: d_A^op ∘ R_A = R_A ∘ d_A.
  (2) R_A intertwines coproducts:
       Delta_A^cop ∘ R_A = (R_A x R_A) ∘ Delta_A^op.
  (3) R_A is an involution after iterating: R_A ∘ R_A = id.

The honest gap (F9):
The full closed-colour package D_Ran has the six-functor formalism
(f^*, f_*, f_!, f^!, ⊗^*, uHom) on Dmod(Ran(X)) (Gaitsgory-Rozenblyum
2017 IV.5, factorization_swiss_cheese.tex:148-219). A genuine
"open-colour Verdier" with the same six-functor package on
Conf^<(R) (or a ribbon Ran space) is not constructed. The
B^ord-level intertwining of thm:opposite proves the Quillen
equivalence at the chiral-algebraic level (open-colour part of
thm:two-color-master, line-operators.tex:382) but does not promote
to a constructible-sheaves-on-Conf^< theory.

Primary anchors:
  - Theorem thm:opposite, ordered_associative_chiral_kd_core.tex:451
  - Theorem thm:two-color-master, spectral-braiding-core.tex:3485 (item ii)
  - Theorem thm:lines_as_modules, line-operators.tex:382
  - Verdier on Ran(X), factorization_swiss_cheese.tex:148
  - Beilinson-Drinfeld 2004 Ch.3 (chiral operad / Verdier)
  - Francis-Gaitsgory 2012 / arXiv:1110.5802 (chiral Koszul duality)
  - Lurie HA 5.5 (factorization on stratified spaces)
  - Costello-Gwilliam 2017/2021 Vols I & II (CG21 Thm 7.3.7)
  - Ayala-Francis 2015 (factorization homology recognition)
  - Kontsevich-Soibelman (Swiss-cheese bordered compactification)
"""
from __future__ import annotations

from fractions import Fraction
from typing import Callable, Dict, List, Tuple


# =========================================================================
# 1. ORDER-REVERSAL INVOLUTION ON SUSPENDED BAR WORDS
# =========================================================================

def opposite_sign(degrees: List[int]) -> int:
    """Koszul sign for order reversal on suspended bar words.

    R_A[s^{-1} a_1 | ... | s^{-1} a_n]
        = sigma_{i<j} (-1)^{(|a_i|+1)(|a_j|+1)} [s^{-1} a_n | ... | s^{-1} a_1].

    The factor (|a_i|+1) is the degree of s^{-1} a_i. The sign is the
    standard graded-symmetric sign for reversing the order of the
    suspended factors.

    Args:
        degrees: List of |a_i| (algebra degrees of the bar factors).

    Returns:
        +1 or -1.
    """
    s = 0
    n = len(degrees)
    for i in range(n):
        for j in range(i + 1, n):
            s += (degrees[i] + 1) * (degrees[j] + 1)
    return 1 if s % 2 == 0 else -1


def reverse_word(word: List[str]) -> List[str]:
    """Reverse the order of a bar word."""
    return list(reversed(word))


def R_A_on_word(word: List[str], degrees: List[int]) -> Tuple[List[str], int]:
    """Apply the opposite-duality map R_A : B^ord(A^op) -> B^ord(A)^cop.

    Returns the reversed word with its Koszul sign.

    Args:
        word: Bar word [a_1, ..., a_n].
        degrees: Degrees [|a_1|, ..., |a_n|].

    Returns:
        (reversed_word, sign) where sign in {+1, -1}.
    """
    return reverse_word(word), opposite_sign(degrees)


# =========================================================================
# 2. BAR DIFFERENTIALS FOR A AND A^op
# =========================================================================

def bar_diff_for_algebra(
    word: List[str],
    m2: Callable[[str, str], Dict[str, Fraction]],
) -> Dict[Tuple[str, ...], Fraction]:
    """Ordered bar differential for an algebra A with binary product m2.

    d[a_1|...|a_n] = sum_{i=1}^{n-1} (-1)^{i-1} [a_1|...|m2(a_i,a_{i+1})|...|a_n].

    Args:
        word: Bar word.
        m2: Binary product, a -> b -> {result_label: coefficient}.

    Returns:
        Dict from result-words (tuples) to coefficients.
    """
    n = len(word)
    out: Dict[Tuple[str, ...], Fraction] = {}
    if n < 2:
        return out
    for i in range(n - 1):
        prod = m2(word[i], word[i + 1])
        sign = Fraction(1 if i % 2 == 0 else -1)
        for label, coef in prod.items():
            new_word = tuple(word[:i] + [label] + word[i + 2:])
            out[new_word] = out.get(new_word, Fraction(0)) + sign * coef
    # drop zero entries
    return {w: c for w, c in out.items() if c != 0}


def opposite_m2(
    m2: Callable[[str, str], Dict[str, Fraction]],
) -> Callable[[str, str], Dict[str, Fraction]]:
    """Build the opposite product m2^op(a, b) = m2(b, a)."""

    def m2_op(a: str, b: str) -> Dict[str, Fraction]:
        return m2(b, a)

    return m2_op


# =========================================================================
# 3. INTERTWINING: d_A^op ∘ R_A = R_A ∘ d_A^op AT WORD LEVEL
# =========================================================================
#
# The content of thm:opposite is:
#
#   d_{A}  ∘  R_A   =   R_A  ∘  d_{A^op}      (as maps B^ord(A^op) -> B^ord(A))
#
# To make this finite-dimensional and checkable, fix a basis-labelled
# algebra (a, b, c, ...), assign degrees, and compute both sides on a bar
# word w = [a_1, ..., a_n], comparing the resulting linear combinations.


def lc_apply_R(
    chain: Dict[Tuple[str, ...], Fraction],
    degrees: Dict[str, int],
) -> Dict[Tuple[str, ...], Fraction]:
    """Apply R_A to a linear combination of bar words.

    Args:
        chain: Dict from bar-words (tuples) to coefficients.
        degrees: Dict from generator labels to degrees.

    Returns:
        New dict representing R_A applied term by term.
    """
    out: Dict[Tuple[str, ...], Fraction] = {}
    for word, coef in chain.items():
        word_list = list(word)
        deg = [degrees.get(a, 0) for a in word_list]
        reversed_word, sign = R_A_on_word(word_list, deg)
        w_tuple = tuple(reversed_word)
        out[w_tuple] = out.get(w_tuple, Fraction(0)) + Fraction(sign) * coef
    return {w: c for w, c in out.items() if c != 0}


def lc_apply_diff(
    chain: Dict[Tuple[str, ...], Fraction],
    m2: Callable[[str, str], Dict[str, Fraction]],
) -> Dict[Tuple[str, ...], Fraction]:
    """Apply the bar differential to a linear combination of bar words."""
    out: Dict[Tuple[str, ...], Fraction] = {}
    for word, coef in chain.items():
        d = bar_diff_for_algebra(list(word), m2)
        for w2, c2 in d.items():
            out[w2] = out.get(w2, Fraction(0)) + coef * c2
    return {w: c for w, c in out.items() if c != 0}


def chain_map_residue(
    word: List[str],
    m2: Callable[[str, str], Dict[str, Fraction]],
    degrees: Dict[str, int],
) -> Dict[Tuple[str, ...], Fraction]:
    """Return the chain-map defect (d_A ∘ R_A - R_A ∘ d_{A^op})(word).

    The thm:opposite identity asserts this is identically zero.

    Args:
        word: Bar word in B^ord(A^op).
        m2: Binary product of A. (A^op uses opposite_m2(m2).)
        degrees: Generator degrees.

    Returns:
        Linear combination dict; should be empty modulo zero entries.
    """
    m2_op = opposite_m2(m2)

    # LHS: d_A (R_A(word))
    R_w = lc_apply_R({tuple(word): Fraction(1)}, degrees)
    lhs = lc_apply_diff(R_w, m2)

    # RHS: R_A (d_{A^op}(word))
    d_op_w = bar_diff_for_algebra(word, m2_op)
    rhs = lc_apply_R(d_op_w, degrees)

    # residue = LHS - RHS
    residue: Dict[Tuple[str, ...], Fraction] = {}
    for k, v in lhs.items():
        residue[k] = residue.get(k, Fraction(0)) + v
    for k, v in rhs.items():
        residue[k] = residue.get(k, Fraction(0)) - v
    return {w: c for w, c in residue.items() if c != 0}


# =========================================================================
# 4. COPRODUCT INTERTWINING:
#     Delta_cop ∘ R_A  =  (R_A x R_A) ∘ Delta
# =========================================================================
#
# On B^ord(A), the coproduct is deconcatenation
#    Delta [a_1|...|a_n]  =  sum_{i=1}^{n-1} [a_1|...|a_i] ⊗ [a_{i+1}|...|a_n].
# The opposite coproduct Delta^cop = tau ∘ Delta swaps the two tensor
# factors. Order reversal sends the cut after position i to the cut
# before position (n - i). Hence
#   Delta^cop ( R_A (word) )  =  (R_A ⊗ R_A) ( Delta(word) ).


def deconcat(word: List[str]) -> List[Tuple[List[str], List[str]]]:
    """All ordered splits of a word into two nonempty pieces."""
    n = len(word)
    if n < 2:
        return []
    return [(word[:i], word[i:]) for i in range(1, n)]


def coproduct_intertwining_residue(
    word: List[str],
    degrees: Dict[str, int],
) -> List[Tuple[Tuple[str, ...], Tuple[str, ...], Fraction]]:
    """Residue of Delta^cop ∘ R_A - (R_A x R_A) ∘ Delta on a single word.

    Args:
        word: Bar word.
        degrees: Generator degrees.

    Returns:
        List of (left_tuple, right_tuple, coefficient) terms.
        Empty list when the intertwining identity holds.
    """
    # LHS: apply R_A first, then deconcat, then swap.
    R_w, sign_R = R_A_on_word(word, [degrees.get(a, 0) for a in word])
    splits_R = deconcat(R_w)
    lhs: Dict[Tuple[Tuple[str, ...], Tuple[str, ...]], Fraction] = {}
    for left, right in splits_R:
        # tau swaps the two tensor factors
        key = (tuple(right), tuple(left))
        lhs[key] = lhs.get(key, Fraction(0)) + Fraction(sign_R)

    # RHS: Delta first, then R_A on each factor.
    splits = deconcat(word)
    rhs: Dict[Tuple[Tuple[str, ...], Tuple[str, ...]], Fraction] = {}
    for left, right in splits:
        l_rev, sl = R_A_on_word(left, [degrees.get(a, 0) for a in left])
        r_rev, sr = R_A_on_word(right, [degrees.get(a, 0) for a in right])
        key = (tuple(l_rev), tuple(r_rev))
        rhs[key] = rhs.get(key, Fraction(0)) + Fraction(sl * sr)

    # residue = LHS - RHS
    keys = set(lhs.keys()) | set(rhs.keys())
    residue: List[Tuple[Tuple[str, ...], Tuple[str, ...], Fraction]] = []
    for k in keys:
        c = lhs.get(k, Fraction(0)) - rhs.get(k, Fraction(0))
        if c != 0:
            residue.append((k[0], k[1], c))
    return residue


# =========================================================================
# 5. INVOLUTIVITY: R_A ∘ R_A = id
# =========================================================================

def involutivity_residue(
    word: List[str],
    degrees: Dict[str, int],
) -> Dict[Tuple[str, ...], Fraction]:
    """Residue (R_A ∘ R_A - id)(word).

    Args:
        word: Bar word.
        degrees: Generator degrees.

    Returns:
        Linear-combination dict; should be empty.
    """
    R_w, s1 = R_A_on_word(word, [degrees.get(a, 0) for a in word])
    R_R_w, s2 = R_A_on_word(R_w, [degrees.get(a, 0) for a in R_w])
    out: Dict[Tuple[str, ...], Fraction] = {}
    key = tuple(R_R_w)
    out[key] = out.get(key, Fraction(0)) + Fraction(s1 * s2)
    # subtract id(word) = +1 * word
    out[tuple(word)] = out.get(tuple(word), Fraction(0)) - Fraction(1)
    return {w: c for w, c in out.items() if c != 0}


# =========================================================================
# 6. F9 STATUS REPORT (string interface)
# =========================================================================

F9_STATUS_NOTES = {
    "closed_colour_proved": (
        "D_Ran ∘ bar(A) ≃ bar(A^!) on Dmod(Ran(X)) is proved "
        "(factorization_swiss_cheese.tex:148; BD04 Ch.3; FG12 1110.5802; "
        "Gaitsgory-Rozenblyum 2017 IV.5)."
    ),
    "open_colour_proved_now": (
        "R_A : B^ord(A^op) ≃ B^ord(A)^cop is proved by Theorem thm:opposite "
        "(ordered_associative_chiral_kd_core.tex:451); supplies the chiral-"
        "algebraic content of the open-colour Quillen equivalence in "
        "thm:two-color-master (spectral-braiding-core.tex:3485 item ii)."
    ),
    "open_colour_gap": (
        "A six-functor package (f^*, f_*, f_!, f^!, ⊗^*, uHom, D) on "
        "Conf^<(X) — or a ribbon Ran space — that promotes R_A to a "
        "constructible-sheaves-level Verdier functor is not constructed. "
        "Ribbon Ran has hints in BD04 §3.3 (cyclic chiral) and Costello-"
        "Gwilliam 2021 Vol II §7.3 (ordered factorization) but no general-"
        "curve construction is published."
    ),
    "general_curve_obstruction": (
        "Conf^<_n(X) requires a linear order, hence only makes sense for "
        "X = R (or a ribbon graph). On a general algebraic curve C the "
        "ordered configuration space is not a global object; only its "
        "germ near a marked point on the open colour boundary makes "
        "geometric sense."
    ),
    "claim_status": "F9 = Conjectured at the open higher-algebra level.",
}


def report() -> str:
    """Print a structured F9 status report."""
    lines = ["F9 — E_1 Verdier on ordered configurations: status\n"]
    for key, note in F9_STATUS_NOTES.items():
        lines.append(f"[{key}]")
        lines.append(f"  {note}")
        lines.append("")
    return "\n".join(lines)
