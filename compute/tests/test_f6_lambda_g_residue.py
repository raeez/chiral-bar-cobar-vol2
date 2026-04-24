"""F6 genus-three lambda_g residue witness.

The test fixes the first scalar residue beyond the genus-two
curved-Dunn base case:

    lambda_3^FP = int_{Mbar_{3,1}} psi_1^4 lambda_3 = 31 / 967680.

The expected value is computed by disjoint exact routes: the
Faber-Pandharipande Bernoulli formula, direct inversion of the sine
power series, and the one-point specialization of the lambda_g
multinomial formula.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, factorial

from compute.lib.independent_verification import independent_verification


def _bernoulli_number(n: int) -> Fraction:
    """Bernoulli number with B_1 = -1/2 from the defining recursion."""
    if n < 0:
        raise ValueError("n must be non-negative")
    numbers = [Fraction(0)] * (n + 1)
    numbers[0] = Fraction(1)
    for m in range(1, n + 1):
        numbers[m] = -sum(
            Fraction(comb(m + 1, k)) * numbers[k] for k in range(m)
        ) / Fraction(m + 1)
    return numbers[n]


def _lambda_fp_from_bernoulli(g: int) -> Fraction:
    if g < 1:
        raise ValueError("g must be at least 1")
    return (
        Fraction(2 ** (2 * g - 1) - 1, 2 ** (2 * g - 1))
        * abs(_bernoulli_number(2 * g))
        / factorial(2 * g)
    )


def _lambda_fp_from_sine_inverse(g: int) -> Fraction:
    """Coefficient of x^(2g) in (x/2) / sin(x/2)."""
    if g < 1:
        raise ValueError("g must be at least 1")

    # sin(x/2)/(x/2) = sum_j s_j x^(2j).
    s = [
        Fraction((-1) ** j, 2 ** (2 * j) * factorial(2 * j + 1))
        for j in range(g + 1)
    ]
    inverse = [Fraction(0)] * (g + 1)
    inverse[0] = Fraction(1)
    for k in range(1, g + 1):
        inverse[k] = -sum(inverse[j] * s[k - j] for j in range(k))
    return inverse[g]


def _multinomial(parts: tuple[int, ...]) -> int:
    total = sum(parts)
    denominator = 1
    for part in parts:
        denominator *= factorial(part)
    return factorial(total) // denominator


def _lambda_g_multinomial_integral(g: int, exponents: tuple[int, ...]) -> Fraction:
    """Faber-Pandharipande lambda_g theorem from the one-point scalar."""
    n = len(exponents)
    expected_degree = 2 * g + n - 3
    if sum(exponents) != expected_degree:
        raise ValueError("exponents must sum to 2g+n-3")
    return Fraction(_multinomial(exponents)) * _lambda_fp_from_sine_inverse(g)


@independent_verification(
    claim="prop:f6-genus-three-lambda-residue",
    derived_from=[
        "Programme F6 planted-forest scalar-residue claim",
        "Vol II gravitational bar-trace formula F_g = kappa lambda_g^FP",
    ],
    verified_against=[
        "Faber-Pandharipande 2000 lambda_g theorem and Bernoulli formula",
        "Exact Taylor inversion of sin(x/2)/(x/2)",
        "One-point specialization of the lambda_g multinomial formula",
    ],
    disjoint_rationale=(
        "The programme derives F6 from the bar trace and planted-forest "
        "residue lane. The test computes the scalar independently from "
        "Faber-Pandharipande's Hodge-integral formula and from exact "
        "power-series algebra, with no use of the programme's bar complex."
    ),
)
def test_f6_genus_three_lambda_residue_is_31_over_967680():
    expected = Fraction(31, 967680)

    assert _bernoulli_number(6) == Fraction(1, 42)
    assert _lambda_fp_from_bernoulli(3) == expected
    assert _lambda_fp_from_sine_inverse(3) == expected
    assert _lambda_g_multinomial_integral(3, (4,)) == expected


def test_f6_lambda_g_multinomial_normalization_at_genus_three():
    lambda_3 = Fraction(31, 967680)
    assert _lambda_g_multinomial_integral(3, (2, 3)) == 10 * lambda_3
    assert _lambda_g_multinomial_integral(3, (1, 2, 3)) == 60 * lambda_3
