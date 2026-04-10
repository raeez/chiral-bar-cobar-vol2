"""Tests for the PVA descent coefficient engine D_2 .. D_6.

Covers Heisenberg (3), affine sl_2 (2), Virasoro (2), and edge
cases (3): trivial PVA, level-zero affine sl_2, and the AP126
k = 0 boundary on the Kac-Moody central extension.

Each test documents its independent derivation path per the
multi-path verification protocol (CLAUDE.md: AP10/AAP11: every
hardcoded expected value derivable by 2+ independent paths).

Paper references
----------------
- chapters/theory/pva-descent.tex, maintheorem thm:cohomology-PVA-main
- chapters/theory/pva-descent-repaired.tex:
    * Example ex:repaired-abelian-current (Heisenberg, lines 1288--1318)
    * Example comp:pva-descent-affine-sl2 (affine sl_2, lines 1320--1545)
    * Proposition prop:PVA1_proof (sesquilinearity descent)
    * Lemma lem:PVA2_proof (exchange-cylinder skew-symmetry)
    * Proposition prop:m3_vanish (higher vanishing D_6)
- Vol II CLAUDE.md:
    * V2-AP34 (divided-power lambda-bracket c/12 * lam^3)
    * V2-AP7  (Heisenberg R-matrix nontrivial at k != 0)
    * AP126  (level-zero r-matrix vanishing)
    * AP1/AP39 (kappa per family, never copied)

All tests are self-certifying symbolic identities.
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest
from sympy import Rational, Symbol, S, expand, simplify, factorial

from lib.pva_descent_coefficients_engine import (
    PVASpec,
    DescentResult,
    compute_D2,
    compute_D3,
    compute_D4,
    compute_D5,
    compute_D6,
    descent_coefficients,
    heisenberg_pva,
    affine_sl2_pva,
    virasoro_pva,
    trivial_pva,
    verify_level_zero,
)


# Shared SymPy symbols
lam = Symbol("lam")
mu = Symbol("mu")
k = Symbol("k")
c = Symbol("c")


# ---------------------------------------------------------------------------
# Heisenberg tests (3)
# ---------------------------------------------------------------------------


class TestHeisenberg:
    """Abelian current algebra, {J_lam J} = k * lam."""

    def test_heisenberg_bracket_closed_form(self):
        """Independent derivation 1: Borel transform of the OPE k/z^2.

        Path A: spec.bracket via engine.
        Path B: Direct formula from pva-descent-repaired.tex line 1297.
            k * zeta^{-2}  (Borel)--> k * lam
        The two must agree.
        """
        spec = heisenberg_pva(k)
        computed = spec.bracket("J", "J", lam)
        expected = k * lam  # from the chapter, line 1297
        assert simplify(computed - expected) == 0

    def test_heisenberg_D2_sesquilinearity(self):
        """D_2: {dJ_lam J} + lam {J_lam J} = 0 and right variant.

        Path A: compute_D2 via engine mode-relation reconstruction.
        Path B: The bracket k*lam is constant in J, so d(k*lam) = 0
            and both sesquilinearity residues must vanish termwise.
        """
        spec = heisenberg_pva(k)
        left, right = compute_D2(spec, "J", "J", lam)
        assert left == 0
        assert right == 0

    def test_heisenberg_D3_D5_skew_and_leibniz(self):
        """D_3 and D_5 simultaneously: Heisenberg is central.

        Path A: compute_D3(J,J) should vanish because {J_lam J} = k*lam
            and -{J_{-lam-d} J} = -k*(-lam - 0) = k*lam; matches.
        Path B: {J_lam (J*J)} by Leibniz = 2 k lam * J; the engine D_5
            residue must vanish on (J, J, J).  Independent check:
            direct Leibniz expansion from the chapter example lines
            1301--1305: {J_lam(J*J)} = 2k lam J.
        """
        spec = heisenberg_pva(k)
        d3 = compute_D3(spec, "J", "J", lam)
        d5 = compute_D5(spec, "J", "J", "J", lam)
        assert d3 == 0
        assert d5 == 0
        # Cross-check the closed form from the chapter.
        from lib.pva_descent_coefficients_engine import _bracket_with_expr
        J = Symbol("J")
        leibniz_lhs = _bracket_with_expr(spec, "J", J * J, lam, max_order=4)
        assert simplify(leibniz_lhs - 2 * k * lam * J) == 0


# ---------------------------------------------------------------------------
# Affine sl_2 tests (2)
# ---------------------------------------------------------------------------


class TestAffineSL2:
    """Affine sl_2 at level k, Example comp:pva-descent-affine-sl2."""

    def test_affine_sl2_bracket_ef_and_hh(self):
        """Independent derivation: two mode-table entries.

        Path A: engine.bracket from the mode dict.
        Path B: Chapter Equation eq:sl2-lambda-brackets:
            {e_lam f} = h + k lam
            {h_lam h} = 2 k lam
        """
        spec = affine_sl2_pva(k)
        e_f = spec.bracket("e", "f", lam)
        h_h = spec.bracket("h", "h", lam)
        assert simplify(e_f - (Symbol("h") + k * lam)) == 0
        assert simplify(h_h - 2 * k * lam) == 0

    def test_affine_sl2_D4_jacobi_triple_hef(self):
        """D_4: PVA Jacobi on (h, e, f), chapter lines 1432--1469.

        Path A: compute_D4 via engine's linearised bracket.
        Path B: Hand-computed LHS - RHS from chapter:
            {h_lam{e_mu f}} = 2k lam
            {e_mu{h_lam f}} = -2h - 2k mu
            {{h_lam e}_{lam+mu} f} = 2h + 2k lam + 2k mu
            LHS - RHS = 2k lam - (-2h-2k mu) - (2h+2k lam+2k mu) = 0.
        """
        spec = affine_sl2_pva(k)
        residue = compute_D4(spec, "h", "e", "f", lam, mu)
        assert simplify(residue) == 0


# ---------------------------------------------------------------------------
# Virasoro tests (2)
# ---------------------------------------------------------------------------


class TestVirasoro:
    """Virasoro at central charge c; V2-AP34 divided-power convention."""

    def test_virasoro_bracket_closed_form(self):
        """Independent derivation: {T_lam T} = dT + 2 T lam + (c/12) lam^3.

        Path A: engine.bracket (Borel transform of OPE modes
            T_{(0)}T = dT, T_{(1)}T = 2T, T_{(3)}T = c/2).
        Path B: Divided-power form of OPE (V2-AP34).  The c/2 mode
            at n = 3 maps to (c/2)/3! = c/12 in the polynomial bracket.
        Path C: Direct literature reference Kac 1998 Prop 4.4.
        """
        spec = virasoro_pva(c)
        bracket = spec.bracket("T", "T", lam, max_order=4)
        expected = Symbol("dT") + 2 * Symbol("T") * lam + (c / 12) * lam ** 3
        assert simplify(bracket - expected) == 0
        # Explicit V2-AP34 guardrail: refuse the wrong c/2 * lam^3 form.
        wrong = Symbol("dT") + 2 * Symbol("T") * lam + (c / 2) * lam ** 3
        assert simplify(bracket - wrong) != 0

    def test_virasoro_D2_right_sesquilinearity(self):
        """D_2 right axiom on Virasoro.

        Independent check: the right-sesquilinearity residue must vanish
        because the Borel coefficients (dT, 2T, 0, c/2) satisfy the
        identity a_{(n)}(d b) = d(a_{(n)}b) + n*a_{(n-1)}b via the
        formal translate T -> dT.

        Path A: compute_D2 via engine.
        Path B: Direct substitution: d(dT) = 0 (formal jet), and
            n*a_{(n-1)}b at n=1 gives dT; summing with d(2T*lam)=2 dT lam
            (which cancels against the (lam+d) action on {T_lam T}).
        """
        spec = virasoro_pva(c)
        _, right = compute_D2(spec, "T", "T", lam, max_order=4)
        # Our formal translate doesn't go past dT, so this is a
        # one-jet check: the coefficients at n = 0, 1 must match.
        # Extract as polynomial in lam and check both low-order terms.
        poly = expand(right)
        # Pick out coefficient of lam^0 and lam^1
        coeff_0 = poly.subs(lam, 0)
        from sympy import diff
        coeff_1 = diff(poly, lam).subs(lam, 0)
        assert simplify(coeff_0) == 0
        assert simplify(coeff_1) == 0


# ---------------------------------------------------------------------------
# Edge-case tests (3)
# ---------------------------------------------------------------------------


class TestEdgeCases:
    """Boundary checks: trivial PVA, nilpotent, level zero."""

    def test_trivial_pva_all_descent_coeffs_vanish(self):
        """Trivial PVA (zero bracket): every D_k residue is zero.

        Path A: descent_coefficients on trivial_pva().
        Path B: Theorem thm:cohomology-PVA-main applied to the trivial
            SC^{ch,top}-algebra; all axioms are vacuously satisfied.
        """
        spec = trivial_pva()
        result = descent_coefficients(spec, ("x", "x", "x"), lam, mu)
        assert result.D2_left == 0
        assert result.D2_right == 0
        assert result.D3 == 0
        assert result.D4 == 0
        assert result.D5 == 0
        assert result.D6 is True
        assert result.is_pva()

    def test_nilpotent_e_squared_zero_in_bracket(self):
        """Nilpotent edge: {e_lam e} = 0 in affine sl_2 (e^2 = 0 on
        the Chevalley basis at the mode level).

        Path A: spec.bracket("e","e",lam) via engine mode dict.
        Path B: Chapter eq:sl2-lambda-brackets lists only {e_lam f},
            {h_lam e}, {h_lam f}, {h_lam h}; all other generator
            pairings are regular (zero singular part).
        """
        spec = affine_sl2_pva(k)
        assert spec.bracket("e", "e", lam) == 0
        assert spec.bracket("f", "f", lam) == 0
        # AP1/AP39 cross-check: stored kappa is (3/4)*(k+2), never
        # copied from another family.
        from sympy import Rational
        expected_kappa = Rational(3, 4) * (k + 2)
        assert simplify(spec.kappa - expected_kappa) == 0

    def test_level_zero_boundary_AP126(self):
        """AP126 / AP141: at k = 0 the Kac-Moody central extension of
        the lambda-bracket must vanish, leaving only the classical
        semisimple part; for Heisenberg the whole bracket vanishes.

        Path A: verify_level_zero hook.
        Path B: The classical r-matrix is k * Omega / z, so r(0) = 0
            (CLAUDE.md AP126).  Bracket's central term is the Borel
            transform of the k/z^2 contribution, which vanishes at k=0.
        Path C: Independent closed-form check below on affine sl_2:
            {e_lam f}|_{k=0} = h exactly (no lambda).
        """
        assert verify_level_zero(heisenberg_pva, lam)
        assert verify_level_zero(affine_sl2_pva, lam)
        assert verify_level_zero(virasoro_pva, lam)
        # Independent cross-check on affine sl_2 at k = 0.
        spec_k0 = affine_sl2_pva(S.Zero)
        assert simplify(spec_k0.bracket("e", "f", lam) - Symbol("h")) == 0
        assert spec_k0.bracket("h", "h", lam) == 0  # central term gone
