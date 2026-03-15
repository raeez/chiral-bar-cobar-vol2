"""
Tests for A-infinity sign conventions.

These tests verify the Koszul sign formula epsilon(s,j) = (j-1)*sum(|a_1|,...,|a_s|)
and check it against known examples where the signs are independently computable.

IMPORTANT CONVENTION NOTE:
The paper uses |m_k| = 1-k (cohomological, shifted convention).
In this convention, for degree-0 elements, the n=3 identity gives:
  m_2(m_2(a,b),c) + m_2(a,m_2(b,c)) = 0  (ANTI-associativity)
This is correct: the commutative product on cohomology is extracted via
symmetrization and regular/singular decomposition, NOT by raw m_2.

For the unshifted convention |m_k| = 2-k (Keller, Loday-Vallette), the
sign would use desuspended degrees and yield standard associativity.

Goal: EXPOSE sign errors in the paper's formulas, not just confirm them.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from sympy import Symbol, symbols, S

from lib.ainfty import koszul_sign, verify_ainfty_identity


class TestKoszulSigns:
    """Verify the Koszul sign epsilon(s,j)."""

    def test_trivial_no_elements_before(self):
        """s=0: no elements before inner operation, sign is always +1."""
        for j in range(1, 10):
            assert koszul_sign([], j) == 1

    def test_single_even_element(self):
        """Element of even degree before: sign is +1 regardless of j."""
        for j in range(1, 10):
            assert koszul_sign([0], j) == 1
            assert koszul_sign([2], j) == 1

    def test_single_odd_element(self):
        """Element of degree 1 before m_j:
        epsilon = (j-1)*1, so sign = (-1)^{j-1}.
        """
        assert koszul_sign([1], 1) == 1    # (-1)^0
        assert koszul_sign([1], 2) == -1   # (-1)^1
        assert koszul_sign([1], 3) == 1    # (-1)^2
        assert koszul_sign([1], 4) == -1   # (-1)^3

    def test_two_odd_elements(self):
        """Two elements of degree 1 before m_j:
        epsilon = (j-1)*2, so sign = (-1)^{2(j-1)} = 1 always.
        """
        for j in range(1, 10):
            assert koszul_sign([1, 1], j) == 1

    def test_mixed_degrees(self):
        """Degrees [1, 0, 1] before m_3:
        epsilon = (3-1)*(1+0+1) = 2*2 = 4, sign = +1.
        """
        assert koszul_sign([1, 0, 1], 3) == 1

    def test_degree_3_element(self):
        """Degree 3 element before m_2:
        epsilon = (2-1)*3 = 3, sign = -1.
        """
        assert koszul_sign([3], 2) == -1


class TestAinftyIdentityArity2:
    """Verify the arity-2 A-infinity identity (n=1): m_1(m_1(a)) = 0.

    This is Q^2 = 0 (the differential squares to zero).
    """

    def test_q_squared_zero(self):
        """Q^2 = 0 for any differential."""
        ops = {1: lambda a: S.Zero}  # Q = 0 (trivially)
        elements = [(1, 0)]  # one element of degree 0
        result = verify_ainfty_identity(ops, elements, 1)
        assert result == 0

    def test_q_squared_nontrivial(self):
        """Check Q^2 = 0 with a nontrivial Q.

        Let A = span{x, y} with |x|=0, |y|=1 and Q(x) = y, Q(y) = 0.
        Then Q^2(x) = Q(y) = 0.
        """
        x, y = Symbol('x'), Symbol('y')
        def Q(a):
            if a == x:
                return y
            return S.Zero
        ops = {1: Q}
        result = verify_ainfty_identity(ops, [(x, 0)], 1)
        assert result == 0


class TestAinftyIdentityArity3:
    """Verify the arity-3 identity (n=2):
    m_1(m_2(a,b)) + m_2(m_1(a), b) + (-1)^{epsilon} m_2(a, m_1(b)) = 0

    With Q=0: m_1(m_2(a,b)) = 0 trivially satisfied.
    """

    def test_free_theory_n2(self):
        """Free theory with Q=0: n=2 identity is trivially 0."""
        ops = {
            1: lambda a: S.Zero,
            2: lambda a, b: a * b,
        }
        x, y = Symbol('x'), Symbol('y')
        result = verify_ainfty_identity(ops, [(x, 0), (y, 0)], 2)
        assert result == 0

    def test_leibniz_rule_odd_elements(self):
        """n=2 with odd-degree elements: check sign.

        For |a|=1: m_2(Q(a), b) + (-1)^{epsilon(1,1)} m_2(a, Q(b)) + Q(m_2(a,b)) = 0
        epsilon(1,1) = (1-1)*|a| = 0, so sign = +1.
        For Q=0: trivially 0.
        """
        ops = {
            1: lambda a: S.Zero,
            2: lambda a, b: a * b,
        }
        a, b = Symbol('a'), Symbol('b')
        result = verify_ainfty_identity(ops, [(a, 1), (b, 1)], 2)
        assert result == 0


class TestAinftyIdentityArity4:
    """Verify the arity-4 identity (n=3).

    In the paper's convention (|m_k| = 1-k), for degree-0 elements
    with Q=0 and m_3=0, the n=3 identity gives:
      m_2(m_2(a,b),c) + m_2(a,m_2(b,c)) = 0

    This is ANTI-associativity, which is correct in the shifted convention.
    The commutative product on cohomology is NOT raw m_2 but the
    symmetrized regular part (see axioms.tex eq:prod-def).
    """

    def test_shifted_convention_degree0(self):
        """For degree-0 elements, n=3 identity gives anti-associativity.

        m_2(m_2(a,b),c) + m_2(a,m_2(b,c)) = 0
        => the sum should be 2abc (for formal symbols)
        This identity is satisfied when m_2 ITSELF encodes the shift.
        """
        a, b, c = Symbol('a'), Symbol('b'), Symbol('c')
        ops = {
            1: lambda x: S.Zero,
            2: lambda x, y: x * y,
            3: lambda x, y, z: S.Zero,
        }
        result = verify_ainfty_identity(ops, [(a, 0), (b, 0), (c, 0)], 3)
        # In the paper's convention, this should be 2abc (not zero)
        # because ordinary polynomial multiplication is NOT an A-infinity
        # algebra in the |m_k|=1-k convention.
        from sympy import expand
        assert expand(result) == expand(2 * a * b * c)

    def test_shifted_convention_odd_elements(self):
        """For degree-1 elements: epsilon(1,2) = (2-1)*1 = 1.

        The n=3 identity (Q=0, m_3=0) gives:
        +m_2(m_2(a,b),c) + (-1)^1 m_2(a, m_2(b,c)) = 0
        => m_2(m_2(a,b),c) - m_2(a,m_2(b,c)) = 0
        This IS associativity for degree-1 elements! ✓
        """
        a, b, c = Symbol('a'), Symbol('b'), Symbol('c')
        ops = {
            1: lambda x: S.Zero,
            2: lambda x, y: x * y,
            3: lambda x, y, z: S.Zero,
        }
        result = verify_ainfty_identity(ops, [(a, 1), (b, 1), (c, 1)], 3)
        assert result == 0

    def test_mixed_degree_01(self):
        """Mixed degrees: |a|=0, |b|=1, |c|=0.

        Terms (Q=0, m_3=0):
        s=0, j=2: epsilon(0,2)=(2-1)*0=0, sign=+1: m_2(m_2(a,b),c)
        s=1, j=2: epsilon(1,2)=(2-1)*|a|=(1)(0)=0, sign=+1: m_2(a,m_2(b,c))
        Sum = m_2(m_2(a,b),c) + m_2(a,m_2(b,c)) = 2abc
        """
        a, b, c = Symbol('a'), Symbol('b'), Symbol('c')
        ops = {
            1: lambda x: S.Zero,
            2: lambda x, y: x * y,
            3: lambda x, y, z: S.Zero,
        }
        result = verify_ainfty_identity(ops, [(a, 0), (b, 1), (c, 0)], 3)
        from sympy import expand
        assert expand(result) == expand(2 * a * b * c)
