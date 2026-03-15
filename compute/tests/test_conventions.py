"""
Tests for LV (Vol I) vs Koszul (Vol II) sign convention comparison.

KEY FINDING: The two conventions are related by a PREDICTABLE factor:
  LV_on_elements = (-1)^{i-1} · Koszul
where i = n+1-j is the outer arity.

This means both conventions define the SAME A∞ algebras — the signs
differ term-by-term but the identities they encode are equivalent.

The factor (-1)^{i-1} is absorbed by redefining m_k → (-1)^{...} m_k.
See Loday-Vallette §9.2.10 for the precise correspondence.

Test tier: Tier 1 (structural) — verifying mathematical identities.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lib.convention_check import (
    lv_sign, koszul_sign_on_elements, compare_signs_on_term,
    verify_conventions_equivalent, analyze_convention_relationship,
)


class TestLVSign:
    """Basic tests for the Loday-Vallette sign formula."""

    def test_lv_r0_s1_t0(self):
        """(r,s,t)=(0,1,0): sign = (-1)^0 = +1."""
        assert lv_sign(0, 1, 0) == 1

    def test_lv_r1_s1_t0(self):
        """(r,s,t)=(1,1,0): sign = (-1)^1 = -1."""
        assert lv_sign(1, 1, 0) == -1

    def test_lv_r0_s2_t0(self):
        """(r,s,t)=(0,2,0): sign = (-1)^0 = +1."""
        assert lv_sign(0, 2, 0) == 1

    def test_lv_r1_s2_t0(self):
        """(r,s,t)=(1,2,0): sign = (-1)^2 = +1."""
        assert lv_sign(1, 2, 0) == 1

    def test_lv_r0_s1_t1(self):
        """(r,s,t)=(0,1,1): sign = (-1)^1 = -1."""
        assert lv_sign(0, 1, 1) == -1


class TestKoszulSign:
    """Basic tests for the Koszul sign formula."""

    def test_no_elements_before(self):
        """s=0: sign = +1 regardless of j."""
        assert koszul_sign_on_elements([], 1) == 1
        assert koszul_sign_on_elements([], 2) == 1
        assert koszul_sign_on_elements([], 5) == 1

    def test_one_deg0_before(self):
        """One degree-0 element before: sign = +1 always."""
        assert koszul_sign_on_elements([0], 2) == 1
        assert koszul_sign_on_elements([0], 3) == 1

    def test_one_deg1_before_j2(self):
        """One degree-1 element before m_2: ε=(2-1)*1=1, sign=-1."""
        assert koszul_sign_on_elements([1], 2) == -1

    def test_one_deg1_before_j3(self):
        """One degree-1 element before m_3: ε=(3-1)*1=2, sign=+1."""
        assert koszul_sign_on_elements([1], 3) == 1


class TestConventionRelationship:
    """Verify: LV_on_elements = (-1)^{i-1} · Koszul for all terms."""

    def test_n2_deg0(self):
        """n=2, degree-0 elements."""
        result = verify_conventions_equivalent(2, [0, 0])
        assert result['relationship_holds'], \
            f"Relationship failed for n=2, deg0"

    def test_n2_deg1(self):
        """n=2, degree-1 elements."""
        result = verify_conventions_equivalent(2, [1, 1])
        assert result['relationship_holds']

    def test_n3_deg0(self):
        """n=3, degree-0 elements (homotopy associativity)."""
        result = verify_conventions_equivalent(3, [0, 0, 0])
        assert result['relationship_holds']

    def test_n3_deg1(self):
        """n=3, degree-1 elements."""
        result = verify_conventions_equivalent(3, [1, 1, 1])
        assert result['relationship_holds']

    def test_n3_mixed(self):
        """n=3, mixed degrees [0,1,0]."""
        result = verify_conventions_equivalent(3, [0, 1, 0])
        assert result['relationship_holds']

    def test_n4_deg0(self):
        """n=4, degree-0 elements."""
        result = verify_conventions_equivalent(4, [0, 0, 0, 0])
        assert result['relationship_holds']

    def test_n4_deg1(self):
        """n=4, degree-1 elements."""
        result = verify_conventions_equivalent(4, [1, 1, 1, 1])
        assert result['relationship_holds']

    def test_n4_mixed(self):
        """n=4, mixed degrees [0,1,1,0]."""
        result = verify_conventions_equivalent(4, [0, 1, 1, 0])
        assert result['relationship_holds']

    def test_n5_deg0(self):
        """n=5, degree-0 elements."""
        result = verify_conventions_equivalent(5, [0, 0, 0, 0, 0])
        assert result['relationship_holds']

    def test_n5_mixed(self):
        """n=5, mixed degrees."""
        result = verify_conventions_equivalent(5, [0, 1, 0, 1, 0])
        assert result['relationship_holds']

    def test_n5_deg2(self):
        """n=5, degree-2 elements."""
        result = verify_conventions_equivalent(5, [2, 2, 2, 2, 2])
        assert result['relationship_holds']

    def test_n6_mixed(self):
        """n=6, mixed degrees — thorough check."""
        result = verify_conventions_equivalent(6, [0, 1, 2, 0, 1, 0])
        assert result['relationship_holds']


class TestConventionAnalysis:
    """Systematic analysis of convention relationship."""

    def test_all_arities_relationship_holds(self):
        """For arities 1-6, verify LV_on_elements = (-1)^{i-1} · Koszul.

        This is the KEY verification: the two conventions used in Vol I
        and Vol II are related by a predictable, term-dependent factor
        that preserves the algebraic content.
        """
        results = analyze_convention_relationship(max_n=6)
        failures = []
        for key, result in results.items():
            if not result['relationship_holds']:
                failures.append(f"n={key[0]}, pattern={key[1]}")
        assert not failures, \
            f"Convention relationship failed for:\n" + "\n".join(failures)
