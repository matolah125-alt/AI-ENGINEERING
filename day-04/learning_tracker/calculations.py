from learning_tracker.validation import validate_month


def calculate_progress(current_month: int, target_months: int) -> float:
	"""Calculate capped learning progress as a percentage."""
	current_month = validate_month(current_month)
	target_months = validate_month(target_months)
	if target_months <= 0:
		raise ValueError("target_months must be greater than zero")

	return float(round(min((current_month / target_months) * 100, 100.0), 1))
