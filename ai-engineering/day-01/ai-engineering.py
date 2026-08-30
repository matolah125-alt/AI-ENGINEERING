"""
Day 01: Hello Engineering!
A mini progress-tracker built with clear validation boundaries and accurate specifications.
"""


def calculate_progress(current_month: int, target_months: int) -> float:
    """
    Calculates learning progress as a percentage capped at 100.0%.

    Specification / Validation Contract:
    - current_month: Non-negative integer (>= 0)
    - target_months: Positive integer (> 0)
    """
    # Clean, single-source validation rule for calculation logic
    if current_month < 0 or target_months <= 0:
        raise ValueError(
            "Invalid inputs: current_month must be non-negative (>= 0) and target_months must be positive (> 0)."
        )

    # Calculate raw percentage and clamp ceiling to 100.0% using min()
    raw_percentage = (current_month / target_months) * 100.0
    capped_percentage = min(raw_percentage, 100.0)

    return round(capped_percentage, 1)


def get_valid_name() -> str:
    """Prompts for user's name and ensures it isn't left blank."""
    while True:
        name = input("What is your name? ").strip()
        if name:
            return name
        print("❌ Oops! Your name cannot be empty. Please try again.\n")


def get_valid_interest() -> str:
    """Prompts for learning interest and ensures it isn't left blank."""
    while True:
        interest = input("What interests you about AI or Software Engineering? ").strip()
        if interest:
            return interest
        print("❌ Oops! Please share a short thought about your interest.\n")


def get_non_negative_integer(prompt: str) -> int:
    """
    Safely prompts for a non-negative integer (>= 0).
    Uses standard try/except for type conversion and ensures unreachable code is eliminated.
    """
    while True:
        raw_input = input(prompt).strip()
        try:
            value = int(raw_input)
            if value >= 0:
                return value
            
            # FIX #1 & #2: Print statement is placed BEFORE any return/continue,
            # accurately describing that non-negative numbers (>= 0) are allowed.
            print("❌ Please enter a non-negative whole number (0 or higher).\n")
        except ValueError:
            print("❌ Invalid input! Please enter a whole number (e.g., 0, 3, 6, 12).\n")


def main() -> None:
    print("=" * 50)
    print("Welcome to your AI & Software Engineering Journey!")
    print("=" * 50 + "\n")

    # Step 1: User Profile Input
    user_name = get_valid_name()
    user_interest = get_valid_interest()

    print(f"\nHello, {user_name}!")
    print(f"Main Goal: '{user_interest}'")
    print("-" * 50)
    print("Let me calculate your learning progress!\n")

    # Step 2: Time Tracking Input Collection
    current_month = get_non_negative_integer("How many months have you been learning so far? ")

    # Loop specifically for target_months to satisfy business rule: target_months > 0
    while True:
        target_months = get_non_negative_integer("How many total months is your goal? ")
        if target_months > 0:
            break
        print("❌ Target goal must be at least 1 month! Try again.\n")

    # Step 3: Domain Requirement Check
    if current_month > target_months:
        print(
            f"\nNotice: You've completed {current_month} months, exceeding your target goal of {target_months} months!"
        )

    # Step 4: Perform Calculation
    percentage = calculate_progress(current_month=current_month, target_months=target_months)

    print("\n" + "=" * 50)
    print(f"Progress Update for {user_name}:")
    print(f" You are {percentage}% of the way to your goal!")
    if percentage == 100.0:
        print("Goal status: Complete / Exceeded!")
        
    print("=" * 50)


if __name__ == "__main__":
    main()