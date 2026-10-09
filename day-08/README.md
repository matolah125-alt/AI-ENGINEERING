Day 08 — SQLite and Database Persistence
Overview

This project introduces database persistence using Python's built-in sqlite3 module. It implements a small learning-record system that stores progress in a SQLite database.

Project Structure
day-08/
├── README.md
├── database/
│   ├── __init__.py
│   ├── connection.py
│   └── records.py
└── tests/
    ├── test_connection.py
    └── test_records.py
Features
Connect to a SQLite database using a configurable path.
Create the learning_records table.
Insert learning records and return generated IDs.
Retrieve saved records in ID order.
Update existing records.
Delete records by ID.
Validate input types and values.
Enforce database-level constraints.
Use parameterized SQL queries.
Test database behavior using in-memory databases.

Each learning record contains an ID, month, topic, progress percentage, and status.

Testing

Run the test suite from this directory:

python -m pytest -v

Measure statement and branch coverage with:

python -m pytest --cov=database --cov-branch --cov-report=term-missing

Latest verification: 47 tests passed with 100% statement and branch coverage.

Key Lessons
SQLite provides persistent local storage without requiring a separate database server.
Parameterized queries separate SQL commands from supplied values.
Application validation and database constraints provide complementary protection.
Database operations should handle missing records and invalid inputs predictably.
In-memory databases make isolated, repeatable tests easier.
Coverage reports help identify untested execution paths.
Next Steps

Build on these database fundamentals in future projects by integrating persistence with application logic, improving transaction handling, and exploring more advanced database design.