def calculate_progress(current_month: int, target_months: int) -> float:
    """
    Calculate learning progress as a percentage capped at 100.0%.

    Args:
        current_month: Number of months already completed.
        target_months: Total number of months in the goal.

    Returns:
        Progress percentage rounded to one decimal place.

    Raises:
        ValueError: If current_month is negative or target_months is not positive.
    """
    if current_month < 0 or target_months <= 0:
        raise ValueError(
            "current_month must be non-negative and target_months must be positive."
        )

    raw_percentage = (current_month / target_months) * 100.0
    capped_percentage = min(raw_percentage, 100.0)

    return round(capped_percentage, 1)