from __future__ import annotations

from fractions import Fraction

from compute.lib.tautological_steinberg_bridge import (
    CleanPullbackData,
    OrientationComparison,
    SteinbergPullbackData,
    clean_pullback_defect,
    clean_pullback_relation_defect,
    keel_mbar04_relation,
    predicted_clutching_relation_defect,
    permutation_sign,
    relation_annihilates_operator,
    split_virtual_pullback_weight,
    tautological_operator_defect,
    weights_from_expected_pullbacks,
    weights_from_parent_pullbacks,
)


def test_keel_relation_annihilates_compatible_steinberg_weights():
    relation = keel_mbar04_relation()
    weights = {"D12_34": 3, "D13_24": 3}

    assert tautological_operator_defect(relation, weights) == 0
    assert relation_annihilates_operator(relation, weights)


def test_missing_class_compatibility_creates_operator_defect():
    relation = keel_mbar04_relation()
    weights = {"D12_34": 3, "D13_24": 5}

    assert tautological_operator_defect(relation, weights) == Fraction(-2)
    assert not relation_annihilates_operator(relation, weights)


def test_clean_pullback_identity_matches_product_weight():
    data = CleanPullbackData(
        parent_weight=6,
        left_weight=2,
        right_weight=3,
    )

    assert data.expected_pullback_weight == 6
    assert clean_pullback_defect(data) == 0
    assert data.is_clean_compatible


def test_excess_euler_class_is_detected_as_class_defect():
    clean = CleanPullbackData(
        parent_weight=6,
        left_weight=2,
        right_weight=3,
        excess_euler=1,
    )
    excess = CleanPullbackData(
        parent_weight=6,
        left_weight=2,
        right_weight=3,
        excess_euler=2,
    )

    assert clean.defect == 0
    assert excess.expected_pullback_weight == 12
    assert excess.defect == Fraction(-6)
    assert not excess.is_clean_compatible


def test_getzler_kapranov_automorphism_factor_is_part_of_formula():
    compatible = CleanPullbackData(
        parent_weight=3,
        left_weight=2,
        right_weight=3,
        automorphism_order=2,
    )
    missing_factor = CleanPullbackData(
        parent_weight=6,
        left_weight=2,
        right_weight=3,
        automorphism_order=2,
    )

    assert compatible.expected_pullback_weight == 3
    assert compatible.defect == 0
    assert missing_factor.defect == 3
    assert not missing_factor.is_clean_compatible


def test_orientation_comparison_computes_epsilon_gamma():
    edge_flip = OrientationComparison(
        reference_edge_order=("e1", "e2", "e3"),
        actual_edge_order=("e2", "e1", "e3"),
    )
    edge_and_cycle_flip = OrientationComparison(
        reference_edge_order=("e1", "e2", "e3"),
        actual_edge_order=("e2", "e1", "e3"),
        reference_cycle_order=("a", "b"),
        actual_cycle_order=("b", "a"),
    )

    assert permutation_sign(("e1", "e2", "e3"), ("e2", "e1", "e3")) == -1
    assert edge_flip.epsilon == -1
    assert edge_and_cycle_flip.epsilon == 1


def test_split_virtual_pullback_combines_orientation_euler_and_automorphism():
    orientation = OrientationComparison(
        reference_edge_order=("node_a", "node_b"),
        actual_edge_order=("node_b", "node_a"),
    )

    assert (
        split_virtual_pullback_weight(
            (2, 5),
            automorphism_order=2,
            excess_euler=3,
            orientation_sign=orientation.epsilon,
        )
        == Fraction(-15)
    )


def test_general_split_pullback_allows_more_than_two_vertices():
    data = SteinbergPullbackData(
        parent_weight=10,
        vertex_weights=(2, 3, 5),
        automorphism_order=3,
        excess_euler=2,
        orientation_sign=-1,
    )

    assert data.expected_pullback_weight == Fraction(-20)
    assert data.defect == 30
    assert not data.is_clean_compatible


def test_boundary_relation_uses_parent_virtual_weights():
    relation = keel_mbar04_relation()
    compatible_pullbacks = {
        "D12_34": CleanPullbackData(parent_weight=6, left_weight=2, right_weight=3),
        "D13_24": CleanPullbackData(parent_weight=6, left_weight=1, right_weight=6),
    }
    incompatible_pullbacks = {
        "D12_34": CleanPullbackData(parent_weight=6, left_weight=2, right_weight=3),
        "D13_24": CleanPullbackData(parent_weight=7, left_weight=1, right_weight=6),
    }

    assert tautological_operator_defect(
        relation, weights_from_parent_pullbacks(compatible_pullbacks)
    ) == 0
    assert tautological_operator_defect(
        relation, weights_from_parent_pullbacks(incompatible_pullbacks)
    ) == Fraction(-1)


def test_cross_check_boundary_relation_detects_euler_orientation_anomaly():
    relation = keel_mbar04_relation()
    pullbacks = {
        "D12_34": CleanPullbackData(parent_weight=6, left_weight=2, right_weight=3),
        "D13_24": CleanPullbackData(
            parent_weight=6,
            left_weight=2,
            right_weight=3,
            excess_euler=2,
        ),
    }

    assert tautological_operator_defect(
        relation, weights_from_parent_pullbacks(pullbacks)
    ) == 0
    assert tautological_operator_defect(
        relation, weights_from_expected_pullbacks(pullbacks)
    ) == Fraction(-6)
    assert clean_pullback_relation_defect(relation, pullbacks) == 6
    assert predicted_clutching_relation_defect(relation, pullbacks) == Fraction(-6)


def test_boundary_relation_detects_orientation_sign_defect():
    relation = keel_mbar04_relation()
    pullbacks = {
        "D12_34": CleanPullbackData(parent_weight=6, left_weight=2, right_weight=3),
        "D13_24": CleanPullbackData(
            parent_weight=6,
            left_weight=2,
            right_weight=3,
            orientation_sign=-1,
        ),
    }

    assert clean_pullback_relation_defect(relation, pullbacks) == -12
    assert predicted_clutching_relation_defect(relation, pullbacks) == 12


def test_independent_boundary_relation_detects_missing_automorphism_factor_defect():
    relation = keel_mbar04_relation()
    pullbacks = {
        "D12_34": CleanPullbackData(
            parent_weight=3,
            left_weight=2,
            right_weight=3,
            automorphism_order=2,
        ),
        "D13_24": CleanPullbackData(
            parent_weight=3,
            left_weight=2,
            right_weight=3,
            automorphism_order=1,
        ),
    }

    assert tautological_operator_defect(
        relation, weights_from_parent_pullbacks(pullbacks)
    ) == 0
    assert clean_pullback_relation_defect(relation, pullbacks) == 3
    assert predicted_clutching_relation_defect(relation, pullbacks) == -3
