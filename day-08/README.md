# Day 08 — SQLite and Database Persistence

## Overview

This project introduces persistence with Python's built-in `sqlite3` module. It
implements a small learning-record system backed by a SQLite database.

## Where to Look

```text
day-08/
├── database/
│   ├── __init__.py
│   ├── connection.py   # Opens SQLite connections and defines the default DB path
│   └── records.py      # Table setup and record create/read/update/delete operations
├── tests/
│   ├── test_connection.py  # Connection behavior and default database path
│   └── test_records.py     # CRUD behavior, input validation, and SQL constraints
└── README.md
```

### Main code flow

1. `database/connection.py` opens a connection to the default `learning.db` or
   to a database path supplied by the caller.
2. `database/records.py` creates the `learning_records` table.
3. The same module provides functions to add, list, update, and delete records.
   Input is validated before parameterized SQL statements are executed.
4. The tests create isolated in-memory databases, exercise these operations,
   and check both application validation and SQLite constraints.

Each learning record stores an ID, month, topic, progress percentage, and status.

## Features

- Connect to a SQLite database using a configurable path.
- Create the `learning_records` table.
- Insert learning records and return generated IDs.
- Retrieve saved records in ID order.
- Update and delete records.
- Validate input types and values, and enforce database-level constraints.
- Use parameterized SQL queries.
- Test database behavior using in-memory databases.

## Testing

Run the test suite from this directory:

```powershell
python -m pytest -v
```

Measure statement and branch coverage with:

```powershell
python -m pytest --cov=database --cov-branch --cov-report=term-missing
```

## Key Lessons

- SQLite provides persistent local storage without requiring a separate database server.
- Parameterized queries separate SQL commands from supplied values.
- Application validation and database constraints provide complementary protection.
- Database operations should handle missing records and invalid inputs predictably.
- In-memory databases make isolated, repeatable tests easier.
- Coverage reports help identify untested execution paths.

## Next Steps

Build on these database fundamentals by integrating persistence with application
logic, improving transaction handling, and exploring more advanced database
design.
