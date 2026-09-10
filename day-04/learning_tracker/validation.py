def validate_month(month: int) -> int:
	"""Return a non-negative month value or raise ValueError."""
	if month < 0:
		raise ValueError("month must be a non-negative integer")
	return month
