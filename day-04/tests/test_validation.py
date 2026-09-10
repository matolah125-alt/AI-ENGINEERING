import pytest

from learning_tracker.validation import validate_month


def test_validate_month_returns_positive_month():
	assert validate_month(5) == 5


def test_validate_month_accepts_zero():
	assert validate_month(0) == 0


def test_validate_month_rejects_negative_month():
	with pytest.raises(ValueError, match="month"):
		validate_month(-1)
