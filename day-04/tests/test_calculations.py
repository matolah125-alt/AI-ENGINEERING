import pytest

from learning_tracker.calculations import calculate_progress


def test_calculate_progress_basic_calculation():
	assert calculate_progress(3, 12) == 25.0


def test_calculate_progress_zero_progress():
	assert calculate_progress(0, 12) == 0.0


def test_calculate_progress_caps_at_one_hundred_percent():
	assert calculate_progress(15, 12) == 100.0


def test_calculate_progress_rejects_invalid_target():
	with pytest.raises(ValueError, match="target_months"):
		calculate_progress(3, 0)
