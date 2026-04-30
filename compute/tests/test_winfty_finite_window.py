"""Finite-window tests for the Winfty endpoint."""

from __future__ import annotations

import pytest

from compute.lib.winfty_finite_window import (
    finite_rung_e_top_depth,
    finite_window_diagnostic,
    minimal_spin_cutoff_for_window,
    spin4_window_diagnostic,
    two_slot_required_spin,
    two_slot_window_terms,
    weight_window_threshold,
)


def test_weight_window_threshold_formula():
    assert weight_window_threshold(1) == 1
    assert weight_window_threshold(4) == 7
    assert weight_window_threshold(5) == 9


def test_weight4_two_slot_window_arithmetic():
    terms = two_slot_window_terms(4)
    observed = {
        (term.left_spin, term.right_spin): term.required_spin_cutoff
        for term in terms
    }
    assert observed == {
        (2, 2): 3,
        (2, 3): 4,
        (2, 4): 5,
        (3, 3): 5,
        (3, 4): 6,
        (4, 4): 7,
    }
    assert max(observed.values()) == 7
    assert two_slot_required_spin(4, 4) == 7


def test_spin4_window_checks_e5_but_not_weight_window_limit():
    diagnostic = spin4_window_diagnostic()
    assert diagnostic.spin_cutoff == 4
    assert diagnostic.weight_max == 4
    assert diagnostic.e_top_depth == 5
    assert diagnostic.max_two_slot_spin == 7
    assert diagnostic.checks_stress_dunn_input is True
    assert diagnostic.weight_window_threshold == 7
    assert diagnostic.meets_weight_window_threshold is False
    assert diagnostic.proves_einfty_endpoint is False
    assert {
        (term.left_spin, term.right_spin, term.required_spin_cutoff)
        for term in diagnostic.missing_two_slot_terms
    } == {
        (2, 4, 5),
        (3, 3, 5),
        (3, 4, 6),
        (4, 4, 7),
    }


def test_minimal_cutoff_for_weight4_window_is_w7():
    cutoff = minimal_spin_cutoff_for_window(4)
    diagnostic = finite_window_diagnostic(spin_cutoff=cutoff, weight_max=4)
    assert cutoff == 7
    assert diagnostic.meets_weight_window_threshold is True
    assert diagnostic.e_top_depth == 8
    assert diagnostic.missing_two_slot_terms == ()
    assert diagnostic.proves_einfty_endpoint is False


def test_invalid_windows_raise():
    with pytest.raises(ValueError):
        weight_window_threshold(0)
    with pytest.raises(ValueError):
        two_slot_window_terms(1)
    with pytest.raises(ValueError):
        finite_rung_e_top_depth(1)
