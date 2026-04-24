"""Tests for the K3 x E Hall--Borcherds gravity-line residual."""

from fractions import Fraction
import os
import sys


sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from lib.hall_borcherds_gravity_residual import (
    CURRENT_ENVELOPE_ON_E,
    DERIVED_CENTER_TRACE_COMPATIBILITY,
    DRINFELD_DOUBLE_COMPLETION,
    K3BorcherdsScalarShadow,
    POSITIVE_HALF_HALL_BORCHERDS,
    REQUIRED_CHAIN_DATA,
    SCCHTOP_GRAVITY_LINE_MORPHISM,
    can_promote_scalar_to_gravity_line,
    classify_k3_hall_bridge,
    missing_chain_data,
)


def test_scalar_constants_are_the_borcherds_shadow_only():
    scalar = K3BorcherdsScalarShadow()
    assert scalar.c1_zero == 10
    assert scalar.bkm_weight == Fraction(5)
    assert scalar.delta5_weight == 5
    assert scalar.phi10_weight == 2 * scalar.delta5_weight
    assert scalar.scalar_equalities_hold()


def test_scalar_data_alone_cannot_promote_to_gravity_line():
    assert missing_chain_data(()) == REQUIRED_CHAIN_DATA
    assert can_promote_scalar_to_gravity_line(()) is False
    assert classify_k3_hall_bridge(()) == "scalar_shadow_only"


def test_positive_half_comparison_is_not_enough():
    blocks = (POSITIVE_HALF_HALL_BORCHERDS,)
    assert can_promote_scalar_to_gravity_line(blocks) is False
    assert missing_chain_data(blocks) == (
        DRINFELD_DOUBLE_COMPLETION,
        CURRENT_ENVELOPE_ON_E,
        SCCHTOP_GRAVITY_LINE_MORPHISM,
        DERIVED_CENTER_TRACE_COMPATIBILITY,
    )


def test_double_and_current_still_need_scchtop_trace():
    blocks = (
        POSITIVE_HALF_HALL_BORCHERDS,
        DRINFELD_DOUBLE_COMPLETION,
        CURRENT_ENVELOPE_ON_E,
    )
    assert can_promote_scalar_to_gravity_line(blocks) is False
    assert missing_chain_data(blocks) == (
        SCCHTOP_GRAVITY_LINE_MORPHISM,
        DERIVED_CENTER_TRACE_COMPATIBILITY,
    )


def test_full_named_data_give_only_conditional_candidate():
    assert can_promote_scalar_to_gravity_line(REQUIRED_CHAIN_DATA) is True
    assert classify_k3_hall_bridge(REQUIRED_CHAIN_DATA) == (
        "conditional_chain_level_candidate"
    )

