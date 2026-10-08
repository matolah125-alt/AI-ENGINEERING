# Day 07 — Reusable API Client

## Goal

Build a reusable API client with separate configuration, clear input validation, request timeouts, and tested error handling.

## Behavior

- `get_user(user_id, timeout=5)` validates that `user_id` is a positive integer before making a request.
- The API base URL comes from the `API_BASE_URL` environment variable, defaulting to `https://jsonplaceholder.typicode.com`.
- A successful response returns its JSON data.
- An HTTP 404 returns `None`; other HTTP errors, connection errors, and timeout errors propagate to the caller.
- Tests mock `requests.get`, so the suite does not contact the live API.

## Run the tests

From this directory:

```bash
pytest -q
```

## Configuration

Set `API_BASE_URL` in the process environment to use another API host. Tests set environment values with pytest's `monkeypatch` fixture and do not modify a `.env` file.