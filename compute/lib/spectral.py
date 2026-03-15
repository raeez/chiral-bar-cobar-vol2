"""
Spectral parameter algebra: formal Laurent series in lambda.

Implements the algebraic structure underlying A-infinity chiral operations:
  m_k: A^{otimes k} -> A((lambda_1))...((lambda_{k-1}))

Elements are represented as truncated Laurent series with symbolic coefficients.
"""
from sympy import Symbol, Rational, oo, Poly, cancel, expand, simplify, S
from sympy import symbols, Function


class LaurentSeries:
    """Truncated Laurent series in one variable: sum_{n >= -N} a_n lambda^n.

    Stored as dict {power: coefficient}, with a truncation order for the
    regular part (max positive power kept).
    """

    def __init__(self, coeffs, var=None):
        """
        coeffs: dict {int_power: symbolic_coeff}
        var: sympy Symbol for the spectral parameter (default: lambda)
        """
        self.var = var or Symbol('lambda')
        self.coeffs = {k: v for k, v in coeffs.items() if v != 0}

    @classmethod
    def from_pole(cls, residue, var=None):
        """Create a simple pole: residue / lambda."""
        return cls({-1: residue}, var)

    @classmethod
    def from_regular(cls, const, var=None):
        """Create a constant (regular) series."""
        return cls({0: const}, var)

    @property
    def singular_part(self):
        """Return the singular part (negative powers of lambda)."""
        return LaurentSeries(
            {k: v for k, v in self.coeffs.items() if k < 0},
            self.var
        )

    @property
    def regular_part(self):
        """Return the regular part (non-negative powers of lambda)."""
        return LaurentSeries(
            {k: v for k, v in self.coeffs.items() if k >= 0},
            self.var
        )

    def __add__(self, other):
        if isinstance(other, (int, float)):
            other = LaurentSeries({0: other}, self.var)
        result = dict(self.coeffs)
        for k, v in other.coeffs.items():
            result[k] = result.get(k, 0) + v
        return LaurentSeries(result, self.var)

    def __radd__(self, other):
        return self.__add__(other)

    def __neg__(self):
        return LaurentSeries({k: -v for k, v in self.coeffs.items()}, self.var)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return LaurentSeries(
                {k: v * other for k, v in self.coeffs.items()}, self.var
            )
        result = {}
        for k1, v1 in self.coeffs.items():
            for k2, v2 in other.coeffs.items():
                p = k1 + k2
                result[p] = result.get(p, 0) + expand(v1 * v2)
        return LaurentSeries(result, self.var)

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return self.__mul__(other)
        return NotImplemented

    def coeff(self, power):
        """Get coefficient of lambda^power."""
        return self.coeffs.get(power, 0)

    def evaluate(self, val):
        """Evaluate at lambda = val."""
        return sum(c * val**k for k, c in self.coeffs.items())

    def is_zero(self):
        """Check if all coefficients vanish."""
        return all(simplify(v) == 0 for v in self.coeffs.values())

    def symmetrize(self, partial_fn=None):
        """Compute (f(λ) + f(−λ)) / 2, the symmetric (even) part.

        When partial_fn is None, ignores ∂ and computes the even part
        in the spectral parameter. This extracts the portion of the
        Laurent series that survives symmetrization.

        For extracting the commutative product from m₂(a,b;λ):
        The product a·b is the constant term of the symmetrized regular part.
        The antisymmetric part gives the λ-bracket via the singular part.

        Parameters:
            partial_fn: optional callable that applies ∂ to coefficient expressions.
                       If None, computes (f(λ) + f(-λ))/2 (ignoring ∂).

        Returns:
            LaurentSeries: the symmetrized series (only even-power terms survive).
        """
        # Substitute λ → -λ: coefficient of λ^k picks up factor (-1)^k
        # Use k % 2 to avoid float issues with negative exponents
        swapped = LaurentSeries(
            {k: v * (1 if k % 2 == 0 else -1) for k, v in self.coeffs.items()},
            self.var
        )
        total = self + swapped
        return LaurentSeries(
            {k: expand(Rational(1, 2) * v) for k, v in total.coeffs.items()},
            self.var
        )

    def __repr__(self):
        if not self.coeffs:
            return "0"
        parts = []
        for k in sorted(self.coeffs.keys()):
            c = self.coeffs[k]
            if k == 0:
                parts.append(f"{c}")
            elif k == 1:
                parts.append(f"({c})*{self.var}")
            elif k == -1:
                parts.append(f"({c})/{self.var}")
            else:
                parts.append(f"({c})*{self.var}^{k}")
        return " + ".join(parts)

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            other = LaurentSeries({0: other}, self.var)
        if isinstance(other, LaurentSeries):
            all_keys = set(self.coeffs.keys()) | set(other.coeffs.keys())
            return all(
                simplify(self.coeffs.get(k, 0) - other.coeffs.get(k, 0)) == 0
                for k in all_keys
            )
        return NotImplemented


def reg_sing_decompose(series):
    """Decompose m_2(a,b;lambda) into regular and singular parts.

    The regular part (non-negative powers of lambda) gives the commutative
    product on cohomology.
    The singular part (negative powers) gives the lambda-bracket.

    Paper reference: Section 4, regular/singular decomposition of m_2.
    """
    return series.regular_part, series.singular_part
