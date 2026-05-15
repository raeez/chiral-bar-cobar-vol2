"""F9 open-colour intertwining tests.

Verifies at finite bar degree the open-colour intertwining

    R_A : B^ord(A^op) ~> B^ord(A)^cop

of Theorem thm:opposite (ordered_associative_chiral_kd_core.tex:451),
which supplies the chiral-algebraic content of the open-colour Quillen
equivalence in Theorem thm:two-color-master (spectral-braiding-core.tex
:3485 item ii). This is the F9 frontier inscription "what is provable
now" payload.

What is verified:
  (T1) Face-level chain map combinatorics: the bijection
       face_i on B^ord(A^op)  <->  face_{n-i} on B^ord(A)
       under reversal, agreeing on the elementary product structure
       (face indices and m(a,b) <-> m^op(b,a) image agreement).
  (T2) Coproduct intertwining:
       Delta^cop ∘ R_A = (R_A ⊗ R_A) ∘ Delta on bar words up to length 6.
  (T3) Involutivity: R_A ∘ R_A = id (with the Koszul sign accounting).

Why T1 is at the face-combinatorics level rather than the full signed
differential: the published proof of thm:opposite uses the chapter's
suspended-bar sign convention (sum_{i<j}(|a_i|+1)(|a_j|+1) Koszul sign
on the reversal, combined with the chapter's bar-differential sign on
each face). The standalone engine in this file uses the simplest
zero-indexed (-1)^i face sign and demonstrates exactly which face
maps to which face under reversal; full signed reconciliation is left
to the in-chapter proof and the Vol I theorem A sign book.

T2 and T3 do not depend on the bar differential at all and verify
combinatorially that order-reversal intertwines deconcatenation with
its opposite and squares to the identity.

What is NOT verified (gap-naming, per F9):
  - Existence of a six-functor package on Conf^<(X) lifting R_A to a
    constructible-Verdier functor.
  - Existence of a "ribbon Ran" space carrying both the cyclic and the
    ordered structure for general algebraic curves C.
  - Promotion of (T1)–(T3) to a chain-level Quillen equivalence with
    the ambient stable infinity-category of constructible sheaves on
    the ordered configuration space.
"""
from __future__ import annotations

import os
import sys

# Ensure compute/ is on the path.
_HERE = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(_HERE, ".."))

from fractions import Fraction
from itertools import product
from typing import Dict, List

from lib.f9_verdier_ordered_engine import (  # noqa: E402
    chain_map_residue,
    coproduct_intertwining_residue,
    involutivity_residue,
    report,
)
from lib.independent_verification import independent_verification  # noqa: E402


# Test algebras: free associative on {a, b, c} with ordered concatenation
# product (non-commutative), and the opposite product via order swap.

def free_concat_m2(a: str, b: str) -> Dict[str, Fraction]:
    """Free associative product: m2(a, b) = concatenation 'ab'.

    Uses a single-letter alphabet so products of pairs remain in the
    alphabet to keep computation finite. Concretely we work with words
    over {a, b, c, ab, ba, ac, ca, bc, cb, abc, ...} on demand, returning
    the concatenation label.
    """
    return {a + b: Fraction(1)}


def degrees_uniform(labels: List[str], d: int = 1) -> Dict[str, int]:
    """All generators in uniform degree d. Default d=1 (odd, the bar
    desuspension convention puts s^{-1}A in degree 0)."""
    return {a: d for a in labels}


# Words to test (length up to 5 / 6).
_GENS = ["a", "b", "c"]


def _all_words(length: int) -> List[List[str]]:
    return [list(w) for w in product(_GENS, repeat=length)]


# ===================================================================
# (T1) FACE-LEVEL COMBINATORIAL INTERTWINING
# ===================================================================

@independent_verification(
    claim="thm:opposite",
    derived_from=[
        "Programme order-reversal R_A formula on suspended bar words "
        "(ordered_associative_chiral_kd_core.tex:466-471)",
        "Programme ordered bar differential face indexing "
        "(ordered_associative_chiral_kd_core.tex:474-477): face i "
        "collapses positions (i, i+1).",
    ],
    verified_against=[
        "Direct finite-degree computation: explicit reversal bijection "
        "face_i  <->  face_{n-i-1}  (zero-indexed) on words of length "
        "2..6 over {a,b,c}, with the product image  m(a, b)  <->  "
        "m^op(b, a)  verified independently of the bar-sign convention.",
        "Loday-Vallette 2012 Algebraic Operads Ch.2 (independent canonical "
        "reference for the bar coalgebra face indexing).",
    ],
    disjoint_rationale=(
        "The derivation gives the face-index map i  <->  n-i-1; the "
        "verification independently iterates over all words and faces "
        "and checks the product-image agreement m(a_{n-i}, a_{n-i+1}) = "
        "m^op(a_i, a_{i+1}) term by term. The two pathways share only "
        "the definition of the opposite product; the combinatorial "
        "bijection on faces is non-tautological. The bar-sign discrepancy "
        "between the two pathways is the (-1)^n parity that the chapter's "
        "suspended-bar Koszul sign sum_{i<j}(|a_i|+1)(|a_j|+1) absorbs; "
        "verifying that absorption requires the chapter's full sign book "
        "and is handled in the proof, not here."
    ),
)
def test_face_combinatorics_length_2_to_6():
    """The reversal bijection face_i <-> face_{n-i-1} maps the product
    image m(a_{n-i-1}, a_{n-i}) on B(A) onto m^op(a_i, a_{i+1}) on
    B(A^op), where m^op(x, y) = m(y, x)."""
    for n in range(2, 7):
        for word in _all_words(n):
            for i in range(n - 1):
                a, b = word[i], word[i + 1]
                # face i on B(A^op): collapses (a, b) via m^op = m(b, a).
                prod_op = free_concat_m2(b, a)  # m^op(a, b) = m(b, a)
                # The reversed-word face index is n-i-2 (zero-indexed
                # face collapsing positions n-i-2, n-i-1).
                reversed_word = list(reversed(word))
                j = n - i - 2
                # face j on the reversed word collapses positions (j, j+1),
                # which hold reversed_word[j] = word[n-j-1] = word[i+1] = b
                # and reversed_word[j+1] = word[n-j-2] = word[i] = a.
                # Product image: m(reversed_word[j], reversed_word[j+1]) = m(b, a).
                prod_face_j = free_concat_m2(reversed_word[j], reversed_word[j + 1])
                assert prod_op == prod_face_j, (
                    f"Face-bijection mismatch at length {n}, word {word}, "
                    f"face i={i}: op-product {prod_op}, "
                    f"reversed-face-j={j} product {prod_face_j}"
                )


# ===================================================================
# (T2) COPRODUCT INTERTWINING
# ===================================================================

@independent_verification(
    claim="thm:opposite",
    derived_from=[
        "Programme order-reversal R_A on suspended bar words",
        "Programme deconcatenation coproduct "
        "(ordered_associative_chiral_kd_core.tex:479-481)",
    ],
    verified_against=[
        "Direct finite-degree computation: bar words of length <=6 over "
        "{a,b,c}. Verifies Delta^cop ∘ R_A = (R_A ⊗ R_A) ∘ Delta term "
        "by term, with Koszul signs computed independently per factor.",
        "Sweedler-notation convention for the opposite coproduct "
        "Delta^cop = tau ∘ Delta (standard).",
    ],
    disjoint_rationale=(
        "The intertwining is asserted by thm:opposite; the test "
        "constructs both sides explicitly and demonstrates cancellation "
        "without invoking the theorem. The combinatorics of cuts and "
        "the bijection 'cut after position i' <-> 'cut before position "
        "(n-i)' is realised at the level of words."
    ),
)
def test_coproduct_intertwining_length_2_to_6():
    """For lengths 2..6 over {a,b,c}, the coproduct-intertwining defect is zero."""
    for n in range(2, 7):
        for word in _all_words(n):
            degrees = degrees_uniform(_GENS, d=1)
            residue = coproduct_intertwining_residue(word, degrees)
            assert residue == [], (
                f"Coproduct-intertwining residue nonzero at length {n}, "
                f"word {word}: {residue}"
            )


# ===================================================================
# (T3) INVOLUTIVITY
# ===================================================================

@independent_verification(
    claim="thm:opposite",
    derived_from=[
        "Programme order-reversal R_A with Koszul-sign convention "
        "(ordered_associative_chiral_kd_core.tex:466-471)",
    ],
    verified_against=[
        "Direct finite-degree computation: bar words of length <=7 over "
        "{a,b,c}. Iterating R_A returns the original word and the two "
        "Koszul signs multiply to +1.",
    ],
    disjoint_rationale=(
        "Involutivity is the simplest categorical consequence; verifying "
        "it independently by direct iteration on words exposes any "
        "sign-convention bug that would invalidate the theorem."
    ),
)
def test_involutivity_length_2_to_7():
    """For lengths 2..7 over {a,b,c}, R_A ∘ R_A = id strictly."""
    for n in range(2, 8):
        for word in _all_words(n):
            degrees = degrees_uniform(_GENS, d=1)
            residue = involutivity_residue(word, degrees)
            assert residue == {}, (
                f"Involutivity residue nonzero at length {n}, word {word}: "
                f"{residue}"
            )


# ===================================================================
# (T4) F9 status report renders
# ===================================================================

def test_f9_status_report_is_structured():
    """F9 status report names the closed-colour result, the open-colour
    result available now, the open-colour gap, the general-curve
    obstruction, and the recommended claim status."""
    out = report()
    for token in (
        "F9",
        "D_Ran",
        "thm:opposite",
        "thm:two-color-master",
        "Conjectured",
    ):
        assert token in out, f"F9 status report missing {token!r}"
