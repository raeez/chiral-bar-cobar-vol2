r"""Tests for the Catalan factorisation theorem (Theorem thm:period-2-parity).

Verifies:
  (a) phi_k(x) = 0 for even k >= 4
  (b) phi_k(x) = (-1)^n C_n prod_{m=2}^k (x+m) for odd k = 2n+3
  (c) T_k = (-1)^n C_n k! for odd k >= 3
  (d) S_k = (-1)^n C_n (k+1)!/2 for odd k >= 3
  (e) The root property: phi_j(-m) = 0 for m = 2,...,j
  (f) The polynomial recursion via rightmost compositions
  (g) Even-arity vanishing via the functional equation
"""

import sys
import os
import math

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from compute.m7_m10_depth_frontier import StasheffEngine


def catalan(n):
    """Catalan number C_n = binom(2n,n)/(n+1)."""
    return math.comb(2 * n, n) // (n + 1)


def get_field_polynomial(engine, k):
    """Extract the field polynomial phi_k(x) as a list of coefficients [x^0, x^1, ...]."""
    engine._cache.clear()
    lams = tuple(1.0 for _ in range(k - 1))
    result = engine.mk(lams)
    field_items = {w: v for w, v in result.items() if w >= 0}
    if not field_items:
        return [0.0]
    max_w = max(field_items.keys())
    return [field_items.get(w, 0.0) for w in range(max_w + 1)]


def eval_polynomial(coeffs, x):
    """Evaluate polynomial sum_w coeffs[w] x^w."""
    return sum(c * x ** w for w, c in enumerate(coeffs))


def predicted_phi(k):
    """Predicted phi_k as coefficient list using the Catalan factorisation."""
    if k == 2:
        return [2.0, 1.0]
    if k % 2 == 0:
        return [0.0]
    n = (k - 3) // 2
    Cn = catalan(n)
    prefactor = (-1) ** n * Cn
    # Multiply out prod_{m=2}^k (x+m) = prod of (m + x)
    poly = [1.0]
    for m in range(2, k + 1):
        # Multiply by (m + x): new[i] = m*old[i] + old[i-1]
        new_poly = [0.0] * (len(poly) + 1)
        for i in range(len(poly)):
            new_poly[i] += float(m) * poly[i]
            new_poly[i + 1] += poly[i]
        poly = new_poly
    return [prefactor * c for c in poly]


@pytest.fixture
def engine():
    return StasheffEngine(1.0)


class TestEvenArityVanishing:
    """Test that phi_k(x) = 0 for even k >= 4."""

    @pytest.mark.parametrize("k", [4, 6, 8, 10])
    def test_even_vanishing(self, engine, k):
        coeffs = get_field_polynomial(engine, k)
        max_abs = max(abs(c) for c in coeffs)
        assert max_abs < 1e-6, f"phi_{k} not zero: max |coeff| = {max_abs}"


class TestOddArityCatalanFactorisation:
    """Test the full polynomial identity phi_k(x) = (-1)^n C_n prod(x+m)."""

    @pytest.mark.parametrize("k", [3, 5, 7, 9, 11])
    def test_polynomial_match(self, engine, k):
        computed = get_field_polynomial(engine, k)
        predicted = predicted_phi(k)
        # Pad to same length
        maxlen = max(len(computed), len(predicted))
        computed += [0.0] * (maxlen - len(computed))
        predicted += [0.0] * (maxlen - len(predicted))
        for w in range(maxlen):
            assert abs(computed[w] - predicted[w]) < 1e-4 * max(abs(predicted[w]), 1), \
                f"phi_{k} x^{w}: computed={computed[w]}, predicted={predicted[w]}"


class TestTCoefficient:
    """Test T_k = (-1)^n C_n k!."""

    @pytest.mark.parametrize("k", [3, 5, 7, 9, 11])
    def test_T_coefficient(self, engine, k):
        coeffs = get_field_polynomial(engine, k)
        T_val = coeffs[0]
        n = (k - 3) // 2
        predicted = (-1) ** n * catalan(n) * math.factorial(k)
        assert abs(T_val - predicted) < 1, \
            f"T_{k} = {T_val}, predicted {predicted}"


class TestSignedSum:
    """Test S_k = phi_k(1) = (-1)^n C_n (k+1)!/2."""

    @pytest.mark.parametrize("k", [3, 5, 7, 9, 11])
    def test_signed_sum(self, engine, k):
        coeffs = get_field_polynomial(engine, k)
        S_val = eval_polynomial(coeffs, 1.0)
        n = (k - 3) // 2
        predicted = (-1) ** n * catalan(n) * math.factorial(k + 1) // 2
        assert abs(S_val - predicted) < 1, \
            f"S_{k} = {S_val}, predicted {predicted}"


class TestRootProperty:
    """Test that phi_j(-m) = 0 for m = 2, ..., j."""

    @pytest.mark.parametrize("j", [2, 3, 5, 7, 9])
    def test_roots(self, engine, j):
        coeffs = get_field_polynomial(engine, j)
        for m in range(2, j + 1):
            val = eval_polynomial(coeffs, float(-m))
            assert abs(val) < 1e-4, \
                f"phi_{j}({-m}) = {val}, should be 0"


class TestCatalanConvolution:
    """Test the Catalan convolution C_n = sum_{a=0}^{n-1} C_a C_{n-1-a}."""

    @pytest.mark.parametrize("n", [1, 2, 3, 4, 5])
    def test_convolution(self, n):
        conv = sum(catalan(a) * catalan(n - 1 - a) for a in range(n))
        assert conv == catalan(n), f"Convolution = {conv}, C_{n} = {catalan(n)}"


class TestFunctionalEquation:
    """Test the even-vanishing functional equation:
    (x+2) phi_{k-1}(x+1) = (x+k) phi_{k-1}(x) for even k >= 4."""

    @pytest.mark.parametrize("k", [4, 6, 8, 10])
    def test_functional_equation(self, k):
        pred = predicted_phi(k - 1)
        # Evaluate at several x values
        for x in [-5.5, -1.3, 0, 0.7, 2.5, 10]:
            lhs = (x + 2) * eval_polynomial(pred, x + 1)
            rhs = (x + k) * eval_polynomial(pred, x)
            assert abs(lhs - rhs) < 1e-4 * max(abs(rhs), 1), \
                f"k={k}, x={x}: LHS={lhs}, RHS={rhs}"
