# Day 06 — Application Logging

## Goal

Learn to create and configure reusable application loggers that write structured messages to a file.

## What I Built

- `app_logger/logger.py` — logger factory with an optional log file path
- `tests/test_logger.py` — tests for logger configuration and file output
- `logs/app.log` — default destination for application log messages

## Features

- Creates named loggers set to the `INFO` level
- Writes to `logs/app.log` by default, with support for a custom path
- Creates the parent directory when needed
- Formats log entries with a timestamp, level, and message
- Avoids adding duplicate handlers to a named logger
- Supports `INFO`, `WARNING`, and `ERROR` messages

## Engineering Concepts

- Python's built-in `logging` module
- Named loggers, file handlers, and formatters
- `pathlib.Path` for portable paths
- Optional function arguments
- `pytest` fixtures and temporary directories
- Preventing duplicate handlers

## Testing

9 tests passed.

## Coverage Result

100% statement coverage.
100% branch coverage.