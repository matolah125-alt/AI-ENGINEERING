# Day 05 — Configuration and Environment Management

## Goal

Learn how to separate application configuration from application code and keep local configuration out of Git.

## What I Built

- `config_manager/settings.py` — application configuration functions
- `tests/test_settings.py` — configuration tests
- `.env` — local environment configuration
- `.gitignore` — prevents `.env` from being committed

## Configuration

The application reads:

- `APP_NAME`
- `APP_ENV`

Supported environments:

- `development`
- `testing`
- `production`

Invalid environment values raise `ValueError`.

## Engineering Concepts

- Environment variables
- Configuration management
- `.env` files
- `python-dotenv`
- Secret protection
- `pytest` and `monkeypatch`
- Git hygiene

## Test Result

6 tests passed.