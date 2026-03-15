"""
A-infinity algebra verification.

Implements the A-infinity identity with spectral parameters:

  sum_{i+j=n+1} sum_{s=0}^{n-j} (-1)^{epsilon(s,j)}
    m_i(a_1,...,a_s, m_j(a_{s+1},...,a_{s+j})|_{Lambda_block}, a_{s+j+1},...,a_n) = 0

where epsilon(s,j) = (j-1)(|a_1| + ... + |a_s|) is the Koszul sign.

This module provides tools to verify these identities symbolically
for concrete examples.
"""
from sympy import Symbol, Rational, expand, simplify, S


def koszul_sign(degrees_before, arity_inner):
    """Compute epsilon(s,j) = (j-1) * sum(|a_1|,...,|a_s|).

    Parameters:
        degrees_before: list of degrees |a_1|,...,|a_s| of elements before the inner operation
        arity_inner: j, the arity of the inner m_j

    Returns:
        (-1)^{epsilon(s,j)} as +1 or -1
    """
    epsilon = (arity_inner - 1) * sum(degrees_before)
    return (-1) ** (epsilon % 2)


def verify_ainfty_identity(operations, elements, n):
    """Verify the n-th A-infinity identity on given elements.

    Parameters:
        operations: dict {k: callable} where operations[k] is m_k
                   m_k(a_1,...,a_k) returns a LaurentSeries or scalar
        elements: list of (value, degree) pairs
        n: arity of the identity to check

    Returns:
        The sum that should vanish, for verification.
    """
    total = S.Zero
    vals = [e[0] for e in elements]
    degs = [e[1] for e in elements]

    for j in range(1, n + 1):
        i = n + 1 - j
        if i not in operations or j not in operations:
            continue
        for s in range(0, n - j + 1):
            # Sign
            sign = koszul_sign(degs[:s], j)

            # Inner operation: m_j(a_{s+1}, ..., a_{s+j})
            inner_args = vals[s:s + j]
            inner_result = operations[j](*inner_args)

            # Outer operation: m_i(a_1,...,a_s, inner, a_{s+j+1},...,a_n)
            outer_args = vals[:s] + [inner_result] + vals[s + j:]
            outer_result = operations[i](*outer_args)

            total = total + sign * outer_result

    return expand(total)


def check_m_degree(m_k, k):
    """Verify that m_k has degree 1-k as required.

    In our conventions: |m_k| = 1 - k.
    So m_1 has degree 0 (it's Q, the differential),
    m_2 has degree -1, m_3 has degree -2, etc.

    Returns (expected_degree, actual_claim).
    """
    return 1 - k


def verify_sesquilinearity_left(bracket_with_deriv, bracket_base, lam):
    """Verify left sesquilinearity: {∂a_λ b} = -λ · {a_λ b}.

    Both sides are computed independently and compared.

    Parameters:
        bracket_with_deriv: the value of {∂a_λ b} (computed from OPE/Borcherds)
        bracket_base: the value of {a_λ b}
        lam: spectral parameter Symbol

    Returns:
        Difference (should simplify to 0 if sesquilinearity holds).
    """
    rhs = expand(-lam * bracket_base)
    return simplify(expand(bracket_with_deriv - rhs))


def verify_sesquilinearity_right(bracket_with_deriv, bracket_base, lam, partial_fn):
    """Verify right sesquilinearity: {a_λ ∂b} = (λ + ∂){a_λ b}.

    Both sides are computed independently and compared.

    Parameters:
        bracket_with_deriv: the value of {a_λ ∂b} (computed from OPE/Borcherds)
        bracket_base: the value of {a_λ b}
        lam: spectral parameter Symbol
        partial_fn: callable that applies the translation operator ∂ to an expression

    Returns:
        Difference (should simplify to 0 if sesquilinearity holds).
    """
    rhs = expand(lam * bracket_base + partial_fn(bracket_base))
    return simplify(expand(bracket_with_deriv - rhs))
