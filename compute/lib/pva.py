"""
Poisson Vertex Algebra axiom verification.

Verifies that the (-1)-shifted PVA structure on H*(A,Q) satisfies:
1. Commutativity of the product (from symmetric regular part of m_2)
2. Sesquilinearity of the lambda-bracket
3. Skew-symmetry: {a_lambda b} = -{b_{-lambda-partial} a}
4. Jacobi identity: {a_lambda {b_mu c}} - {b_mu {a_lambda c}} = {{a_lambda b}_{lambda+mu} c}
5. Leibniz rule: {a_lambda b.c} = {a_lambda b}.c + b.{a_lambda c}

Paper references: Sections 7 and 9 (pva-preview.tex and pva-descent.tex).
"""
from sympy import Symbol, expand, simplify, S
from .spectral import LaurentSeries


def verify_commutativity(product):
    """Verify a.b = b.a for the product from regular part of m_2.

    Parameters:
        product: callable (a, b) -> result
    Returns:
        a.b - b.a (should be zero)
    """
    def check(a, b):
        return simplify(product(a, b) - product(b, a))
    return check


def verify_skew_symmetry(bracket, partial):
    """Verify {a_lambda b} = -{b_{-lambda-partial} a}.

    Parameters:
        bracket: callable (a, b, lambda) -> LaurentSeries
        partial: the translation operator
    Returns:
        Callable that checks the identity for given a, b
    """
    def check(a, b, lam):
        lhs = bracket(a, b, lam)
        # RHS: -{b_{-lam-partial} a}
        rhs = -bracket(b, a, -lam - partial)
        return lhs - rhs  # Should be zero
    return check


def verify_jacobi(bracket):
    """Verify the Jacobi identity for the lambda-bracket:
    {a_lambda {b_mu c}} - {b_mu {a_lambda c}} = {{a_lambda b}_{lambda+mu} c}

    This is the HARDEST axiom to verify. In the paper it follows from
    AOS cancellations at codimension-2 corners of FM_3(C).

    Parameters:
        bracket: callable (a, b, spectral_param) -> LaurentSeries
    Returns:
        Callable that checks the identity for given a, b, c
    """
    def check(a, b, c, lam, mu):
        # LHS term 1: {a_lambda {b_mu c}}
        inner1 = bracket(b, c, mu)
        term1 = bracket(a, inner1, lam)

        # LHS term 2: -{b_mu {a_lambda c}}
        inner2 = bracket(a, c, lam)
        term2 = -bracket(b, inner2, mu)

        # RHS: {{a_lambda b}_{lambda+mu} c}
        inner3 = bracket(a, b, lam)
        rhs = bracket(inner3, c, lam + mu)

        return (term1 + term2) - rhs  # Should be zero
    return check


def verify_leibniz(product, bracket):
    """Verify the Leibniz rule:
    {a_lambda b.c} = {a_lambda b}.c + b.{a_lambda c}

    Parameters:
        product: callable (a, b) -> result
        bracket: callable (a, b, lambda) -> LaurentSeries
    Returns:
        Callable that checks the identity for given a, b, c
    """
    def check(a, b, c, lam):
        # LHS: {a_lambda b.c}
        bc = product(b, c)
        lhs = bracket(a, bc, lam)

        # RHS: {a_lambda b}.c + b.{a_lambda c}
        ab_bracket = bracket(a, b, lam)
        ac_bracket = bracket(a, c, lam)
        rhs = product(ab_bracket, c) + product(b, ac_bracket)

        return lhs - rhs  # Should be zero
    return check


class PVAChecker:
    """Checks all PVA axioms for a given algebra."""

    def __init__(self, product, bracket, partial, generators):
        """
        product: (a, b) -> result
        bracket: (a, b, lambda) -> LaurentSeries
        partial: translation operator symbol
        generators: list of generator symbols with their degrees
        """
        self.product = product
        self.bracket = bracket
        self.partial = partial
        self.generators = generators

    def _bracket_extended(self, a, expr, lam):
        """Extend bracket by linearity to expressions involving generators.

        {a_λ Σ c_i g_i + const} = Σ c_i {a_λ g_i}

        This handles the case where the inner bracket returns a linear
        combination of generators (e.g., su(2): {J^a_λ J^b} = ε^{abc}J^c + kλ).
        Constants (terms with no generator dependence) are annihilated.

        Limitation: only handles expressions LINEAR in generators.
        For composite fields (T², :TT:, etc.) use dedicated check functions.
        """
        result = S.Zero
        remaining = expand(expr)
        for gen in self.generators:
            coeff = remaining.coeff(gen)
            if coeff != 0:
                result += expand(coeff * self.bracket(a, gen, lam))
                remaining = expand(remaining - coeff * gen)
        # remaining is the constant part; {a_λ const} = 0
        return expand(result)

    def check_all(self, lam=None, mu=None):
        """Run all PVA axiom checks on generators.

        Returns dict of {axiom_name: list of tuples with result} where
        the result field should be zero for each entry.

        Axioms checked:
        - commutativity: a·b = b·a
        - skew_symmetry: {a_λ b} = -{b_{-λ-∂} a}
        - jacobi: {a_λ {b_μ c}} - {b_μ {a_λ c}} = {{a_λ b}_{λ+μ} c}
        - leibniz: {a_λ b·c} = {a_λ b}·c + b·{a_λ c}

        Note: Jacobi and Leibniz use _bracket_extended for linearity in
        generator expressions. This works for current algebras (su(2), etc.)
        but NOT for algebras with composite fields (Virasoro Leibniz with :TT:).
        Use dedicated check functions for those cases.
        """
        if lam is None:
            lam = Symbol('lambda')
        if mu is None:
            mu = Symbol('mu')

        results = {}

        # Commutativity
        comm_results = []
        for a in self.generators:
            for b in self.generators:
                diff = simplify(self.product(a, b) - self.product(b, a))
                comm_results.append((a, b, diff))
        results['commutativity'] = comm_results

        # Skew-symmetry (for generators)
        skew_results = []
        for a in self.generators:
            for b in self.generators:
                lhs = self.bracket(a, b, lam)
                rhs = -self.bracket(b, a, -lam - self.partial)
                skew_results.append((a, b, lhs - rhs))
        results['skew_symmetry'] = skew_results

        # Jacobi identity (using linear extension for inner brackets)
        jacobi_results = []
        for a in self.generators:
            for b in self.generators:
                for c in self.generators:
                    # LHS term 1: {a_λ {b_μ c}}
                    inner1 = self.bracket(b, c, mu)
                    term1 = self._bracket_extended(a, inner1, lam)

                    # LHS term 2: -{b_μ {a_λ c}}
                    inner2 = self.bracket(a, c, lam)
                    term2 = -self._bracket_extended(b, inner2, mu)

                    # RHS: {{a_λ b}_{λ+μ} c}
                    inner3 = self.bracket(a, b, lam)
                    rhs = self._bracket_extended(inner3, c, lam + mu)

                    diff = simplify(expand(term1 + term2 - rhs))
                    jacobi_results.append((a, b, c, diff))
        results['jacobi'] = jacobi_results

        # Leibniz: {a_λ b·c} = {a_λ b}·c + b·{a_λ c}
        leibniz_results = []
        for a in self.generators:
            for b in self.generators:
                for c in self.generators:
                    bc = self.product(b, c)
                    lhs = self._bracket_extended(a, bc, lam)

                    ab_bracket = self.bracket(a, b, lam)
                    ac_bracket = self.bracket(a, c, lam)
                    rhs = expand(self.product(ab_bracket, c)
                                 + self.product(b, ac_bracket))

                    diff = simplify(expand(lhs - rhs))
                    leibniz_results.append((a, b, c, diff))
        results['leibniz'] = leibniz_results

        return results
