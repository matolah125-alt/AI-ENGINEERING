import sqlite3
import pytest
from database.connection import get_connection
from database.records import (
    add_record,
    create_records_table,
    delete_record,
    get_records,
    update_record,
)


# Table creation
def test_create_records_table():
    connection = get_connection(":memory:")

    try:
        create_records_table(connection)

        result = connection.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type = 'table'
              AND name = 'learning_records'
            """
        ).fetchone()

        assert result is not None
        assert result[0] == "learning_records"
    finally:
        connection.close()
        
        
# Record creation and retrieval
def test_add_record_returns_generated_id():
    connection = get_connection(":memory:")

    try:
        create_records_table(connection)

        record_id = add_record(
            connection,
            month=1,
            topic="Python",
            progress=80.0,
            status="in progress",
        )

        assert record_id == 1
    finally:
        connection.close()


def test_get_records_returns_saved_records():
    connection = get_connection(":memory:")

    try:
        create_records_table(connection)

        add_record(
            connection,
            month=1,
            topic="Python",
            progress=80.0,
            status="in progress",
        )

        records = get_records(connection)

        assert len(records) == 1
        assert records[0] == (
            1,
            1,
            "Python",
            80.0,
            "in progress",
        )
    finally:
        connection.close()
        
        
# SQLite-level constraints
def test_database_rejects_progress_above_100():
    connection = get_connection(":memory:")

    try:
        create_records_table(connection)

        # Bypass add_record() to test SQLite's own constraint.
        with pytest.raises(sqlite3.IntegrityError):
            connection.execute(
                """
                INSERT INTO learning_records
                    (month, topic, progress, status)
                VALUES (?, ?, ?, ?)
                """,
                (1, "Python", 150.0, "in progress"),
            )
    finally:
        connection.close()


def test_database_rejects_negative_progress():
    connection = get_connection(":memory:")

    try:
        create_records_table(connection)

        # Bypass add_record() to test SQLite's own constraint.
        with pytest.raises(sqlite3.IntegrityError):
            connection.execute(
                """
                INSERT INTO learning_records
                    (month, topic, progress, status)
                VALUES (?, ?, ?, ?)
                """,
                (1, "Python", -5.0, "in progress"),
            )
    finally:
        connection.close()
        
        
# Input validation when adding records
@pytest.mark.parametrize(
    ("month", "error_type"),
    [
        (0, ValueError),
        (-1, ValueError),
        ("1", TypeError),
        (True, TypeError),
    ],
)
def test_add_record_rejects_invalid_month(month, error_type):
    connection = get_connection(":memory:")

    try:
        create_records_table(connection)

        with pytest.raises(error_type):
            add_record(
                connection,
                month=month,
                topic="Python",
                progress=50.0,
                status="in progress",
            )

        assert get_records(connection) == []
    finally:
        connection.close()


@pytest.mark.parametrize(
    ("topic", "error_type"),
    [
        ("", ValueError),
        ("   ", ValueError),
        (123, TypeError),
    ],
)
def test_add_record_rejects_invalid_topic(topic, error_type):
    connection = get_connection(":memory:")

    try:
        create_records_table(connection)

        with pytest.raises(error_type):
            add_record(
                connection,
                month=1,
                topic=topic,
                progress=50.0,
                status="in progress",
            )

        assert get_records(connection) == []
    finally:
        connection.close()
        
        
@pytest.mark.parametrize(
    ("progress", "error_type"),
    [
        (-1, ValueError),
        (101, ValueError),
        ("50", TypeError),
        (True, TypeError),
    ],
)
def test_add_record_rejects_invalid_progress(progress, error_type):
    connection = get_connection(":memory:")

    try:
        create_records_table(connection)

        with pytest.raises(error_type):
            add_record(
                connection,
                month=1,
                topic="Python",
                progress=progress,
                status="in progress",
            )

        assert get_records(connection) == []
    finally:
        connection.close()


@pytest.mark.parametrize(
    ("status", "error_type"),
    [
        ("", ValueError),
        ("   ", ValueError),
        (123, TypeError),
    ],
)
def test_add_record_rejects_invalid_status(status, error_type):
    connection = get_connection(":memory:")

    try:
        create_records_table(connection)

        with pytest.raises(error_type):
            add_record(
                connection,
                month=1,
                topic="Python",
                progress=50.0,
                status=status,
            )

        assert get_records(connection) == []
    finally:
        connection.close()
        
        
# Updating records and validating record IDs
def test_update_record_changes_saved_record():
    connection = get_connection(":memory:")
    try:
        create_records_table(connection)
        record_id = add_record(
            connection,
            month=1,
            topic="Python",
            progress=50.0,
            status="in progress",
        )

        updated = update_record(
            connection,
            record_id=record_id,
            month=1,
            topic="SQLite",
            progress=100.0,
            status="completed",
        )

        assert updated is True
        assert get_records(connection) == [
            (record_id, 1, "SQLite", 100.0, "completed")
        ]
    finally:
        connection.close()


def test_update_record_returns_false_for_missing_id():
    connection = get_connection(":memory:")
    try:
        create_records_table(connection)

        updated = update_record(
            connection,
            record_id=999,
            month=1,
            topic="Python",
            progress=50.0,
            status="in progress",
        )

        assert updated is False
        assert get_records(connection) == []
    finally:
        connection.close()


@pytest.mark.parametrize(
    ("record_id", "error_type"),
    [
        (0, ValueError),
        (-1, ValueError),
        ("1", TypeError),
        (True, TypeError),
    ],
)
def test_update_record_rejects_invalid_id(record_id, error_type):
    connection = get_connection(":memory:")
    try:
        create_records_table(connection)

        with pytest.raises(error_type):
            update_record(
                connection,
                record_id=record_id,
                month=1,
                topic="Python",
                progress=50.0,
                status="in progress",
            )

        assert get_records(connection) == []
    finally:
        connection.close()
        
        
# Deleting records
def test_delete_record_removes_saved_record():
    connection = get_connection(":memory:")
    try:
        create_records_table(connection)
        record_id = add_record(
            connection,
            month=1,
            topic="Python",
            progress=50.0,
            status="in progress",
        )

        deleted = delete_record(connection, record_id)

        assert deleted is True
        assert get_records(connection) == []
    finally:
        connection.close()


def test_delete_record_returns_false_for_missing_id():
    connection = get_connection(":memory:")
    try:
        create_records_table(connection)

        deleted = delete_record(connection, 999)

        assert deleted is False
        assert get_records(connection) == []
    finally:
        connection.close()


# Input validation when updating records
@pytest.mark.parametrize(
    ("record_id", "error_type"),
    [
        (0, ValueError),
        (-1, ValueError),
        ("1", TypeError),
        (True, TypeError),
    ],
)
def test_delete_record_rejects_invalid_id(record_id, error_type):
    connection = get_connection(":memory:")
    try:
        create_records_table(connection)

        with pytest.raises(error_type):
            delete_record(connection, record_id)

        assert get_records(connection) == []
    finally:
        connection.close()


@pytest.mark.parametrize(
    ("month", "error_type"),
    [
        (0, ValueError),
        (-1, ValueError),
        ("1", TypeError),
        (True, TypeError),
    ],
)
def test_update_record_rejects_invalid_month(month, error_type):
    connection = get_connection(":memory:")
    try:
        create_records_table(connection)
        record_id = add_record(
            connection, 1, "Python", 50.0, "in progress"
        )

        with pytest.raises(error_type):
            update_record(
                connection, record_id, month, "Python", 50.0, "in progress"
            )

        assert get_records(connection) == [
            (record_id, 1, "Python", 50.0, "in progress")
        ]
    finally:
        connection.close()


@pytest.mark.parametrize(
    ("topic", "error_type"),
    [
        ("", ValueError),
        ("   ", ValueError),
        (123, TypeError),
    ],
)
def test_update_record_rejects_invalid_topic(topic, error_type):
    connection = get_connection(":memory:")
    try:
        create_records_table(connection)
        record_id = add_record(
            connection, 1, "Python", 50.0, "in progress"
        )

        with pytest.raises(error_type):
            update_record(
                connection, record_id, 1, topic, 50.0, "in progress"
            )

        assert get_records(connection) == [
            (record_id, 1, "Python", 50.0, "in progress")
        ]
    finally:
        connection.close()


@pytest.mark.parametrize(
    ("progress", "error_type"),
    [
        (-1, ValueError),
        (101, ValueError),
        ("50", TypeError),
        (True, TypeError),
    ],
)
def test_update_record_rejects_invalid_progress(progress, error_type):
    connection = get_connection(":memory:")
    try:
        create_records_table(connection)
        record_id = add_record(
            connection, 1, "Python", 50.0, "in progress"
        )

        with pytest.raises(error_type):
            update_record(
                connection, record_id, 1, "Python", progress, "in progress"
            )

        assert get_records(connection) == [
            (record_id, 1, "Python", 50.0, "in progress")
        ]
    finally:
        connection.close()


@pytest.mark.parametrize(
    ("status", "error_type"),
    [
        ("", ValueError),
        ("   ", ValueError),
        (123, TypeError),
    ],
)
def test_update_record_rejects_invalid_status(status, error_type):
    connection = get_connection(":memory:")
    try:
        create_records_table(connection)
        record_id = add_record(
            connection, 1, "Python", 50.0, "in progress"
        )

        with pytest.raises(error_type):
            update_record(
                connection, record_id, 1, "Python", 50.0, status
            )

        assert get_records(connection) == [
            (record_id, 1, "Python", 50.0, "in progress")
        ]
    finally:
        connection.close()