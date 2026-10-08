# AI Engineering

This repository is a small Python learning workspace focused on practical software engineering habits for AI and general application development. It contains a progression of short exercises that build up from simple input validation and calculation logic into packaged modules, environment-based configuration, and reusable logging.

The project is intentionally educational and beginner-friendly: each exercise demonstrates a specific engineering concept, with automated tests in the test-focused projects.

## What this repo covers

- Input validation and safe user prompts
- Progress calculation and business rules
- Modular package structure and separation of concerns
- Configuration management with environment variables and `.env`
- Reusable file logging with Python’s standard `logging` module
- Test-driven development with `pytest`
- Good project hygiene such as `.gitignore` and clean folder organization

## Repository structure

- [ai-engineering/day-01](ai-engineering/day-01) — a simple interactive “AI & Software Engineering Journey” app
- [day-03](day-03) — a standalone progress tracker with validation rules and tests
- [day-04](day-04) — package-based learning tracker with validation and progress calculations
- [day-05](day-05) — configuration manager using environment variables and `.env`
- [day-06](day-06) — reusable application logger with file output and formatting
- [day-07](day-07) — configurable API client with input validation and mocked HTTP tests

## Daily project highlights

### Day 01 — Hello Engineering

The first exercise introduces a simple interactive CLI that collects a user’s name, interest area, and learning timeline, then calculates progress toward a learning goal. It emphasizes user input validation, clear error messages, and a clean calculation contract.

Key files:
- [ai-engineering/day-01/ai-engineering.py](ai-engineering/day-01/ai-engineering.py)

### Day 03 — Progress Tracker

This exercise focuses on a pure function for calculating progress as a percentage while enforcing valid input rules. It introduces strict validation boundaries and test coverage for invalid values.

Key files:
- [day-03/progress_tracker.py](day-03/progress_tracker.py)
- [day-03/test_progress_tracker.py](day-03/test_progress_tracker.py)

### Day 04 — Package Structure and Testing

The project is reorganized into a package with dedicated modules for validation and calculations. This demonstrates separation of concerns and how to write reusable logic that is easy to test.

Key files:
- [day-04/learning_tracker/validation.py](day-04/learning_tracker/validation.py)
- [day-04/learning_tracker/calculations.py](day-04/learning_tracker/calculations.py)
- [day-04/tests/test_validation.py](day-04/tests/test_validation.py)
- [day-04/tests/test_calculations.py](day-04/tests/test_calculations.py)

### Day 05 — Configuration and Environment Management

This exercise separates application settings from application logic. It uses environment variables and a `.env` file for runtime configuration while preventing secrets from being committed to version control.

Key files:
- [day-05/config_manager/settings.py](day-05/config_manager/settings.py)
- [day-05/tests/test_settings.py](day-05/tests/test_settings.py)

### Day 06 — Application Logging

This project introduces structured logging with Python’s built-in `logging` module. It creates reusable loggers, writes logs to a file, and avoids duplicate handlers when named loggers are reused.

Key files:
- [day-06/app_logger/logger.py](day-06/app_logger/logger.py)
- [day-06/tests/test_logger.py](day-06/tests/test_logger.py)
- [day-06/logs/app.log](day-06/logs/app.log)

### Day 07 — Reusable API Client

This exercise builds a reusable JSON API client with a configurable base URL, input validation, request timeouts, and distinct handling for not-found responses versus other HTTP and network errors. Tests mock the HTTP layer, so they do not depend on external network access.

Key files:
- [day-07/config/settings.py](day-07/config/settings.py)
- [day-07/api_client/client.py](day-07/api_client/client.py)
- [day-07/tests/test_settings.py](day-07/tests/test_settings.py)
- [day-07/tests/test_client.py](day-07/tests/test_client.py)

## Running the exercises

Each folder is designed to be run or tested independently.

Examples:

```bash
cd day-04
pytest -q
```

```bash
cd day-05
pytest -q
```

```bash
cd day-06
pytest -q
```

```bash
cd day-07
pytest -q
```

For the interactive script in Day 01:

```bash
cd "ai-engineering/day-01"
python ai-engineering.py
```

## Tools and dependencies

This repo primarily uses:

- Python 3
- `pytest` for automated tests
- `python-dotenv` for environment loading in the configuration example
- `requests` for the Day 07 API client
- standard library modules such as `logging`, `os`, and `pathlib`

Install the third-party dependencies from the repository root with:

```bash
python -m pip install -r requirements.txt
```

## Notes

This repository is best viewed as a learning lab and a record of progressively improving engineering fundamentals. It is not a production application, but it demonstrates how small, well-tested Python modules can grow into cleaner application patterns.

## License

This project is intended for learning and personal experimentation. If you plan to reuse it, check the repository’s licensing status and adapt it appropriately for your environment.
