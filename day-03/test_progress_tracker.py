import pytest

from progress_tracker import calculate_progress


def test_calculate_progress_basic():
    assert calculate_progress(3, 12) == 25.0


def test_calculate_progress_zero_months():
    assert calculate_progress(0, 12) == 0.0


def test_calculate_progress_exact_target():
    assert calculate_progress(12, 12) == 100.0


def test_calculate_progress_caps_at_100():
    assert calculate_progress(15, 12) == 100.0


def test_calculate_progress_rejects_negative_current_month():
    with pytest.raises(ValueError, match="current_month"):
        calculate_progress(-1, 12)


def test_calculate_progress_rejects_zero_target():
    with pytest.raises(ValueError, match="target_months"):
        calculate_progress(3, 0)


def test_calculate_progress_rejects_negative_target():
    with pytest.raises(ValueError, match="target_months"):
        calculate_progress(3, -12)