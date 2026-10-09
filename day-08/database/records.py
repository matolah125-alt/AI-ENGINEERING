import sqlite3


def create_records_table(connection: sqlite3.Connection) -> None:
    """Create the learning records table if it does not exist."""
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS learning_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            month INTEGER NOT NULL CHECK (month > 0),
            topic TEXT NOT NULL,
            progress REAL NOT NULL CHECK (progress BETWEEN 0 AND 100),
            status TEXT NOT NULL
        )
        """
    )
    
    

def add_record(
    connection: sqlite3.Connection,
    month: int,
    topic: str,
    progress: float,
    status: str,
) -> int:
    """Validate and insert a learning record, returning its generated ID."""
    if isinstance(month, bool) or not isinstance(month, int):
        raise TypeError("month must be an integer")
    if month <= 0:
        raise ValueError("month must be greater than zero")

    if not isinstance(topic, str):
        raise TypeError("topic must be a string")
    if not topic.strip():
        raise ValueError("topic must not be empty")

    if isinstance(progress, bool) or not isinstance(progress, (int, float)):
        raise TypeError("progress must be a number")
    if not 0 <= progress <= 100:
        raise ValueError("progress must be between 0 and 100")

    if not isinstance(status, str):
        raise TypeError("status must be a string")
    if not status.strip():
        raise ValueError("status must not be empty")

    cursor = connection.execute(
        """
        INSERT INTO learning_records (month, topic, progress, status)
        VALUES (?, ?, ?, ?)
        """,
        (month, topic.strip(), progress, status.strip()),
    )
    connection.commit()
    return cursor.lastrowid


def get_records(
    connection: sqlite3.Connection,
) -> list[tuple]:
    """Return all learning records ordered by ID."""
    cursor = connection.execute(
        """
        SELECT id, month, topic, progress, status
        FROM learning_records
        ORDER BY id
        """
    )
    return cursor.fetchall()


def update_record(
    connection: sqlite3.Connection,
    record_id: int,
    month: int,
    topic: str,
    progress: float,
    status: str,
) -> bool:
    """Update an existing learning record."""
    if isinstance(record_id, bool) or not isinstance(record_id, int):
        raise TypeError("record_id must be an integer")
    if record_id <= 0:
        raise ValueError("record_id must be positive")

    # Reuse the existing validation rules before updating.
    if isinstance(month, bool) or not isinstance(month, int):
        raise TypeError("month must be an integer")
    if month <= 0:
        raise ValueError("month must be greater than zero")

    if not isinstance(topic, str):
        raise TypeError("topic must be a string")
    if not topic.strip():
        raise ValueError("topic must not be empty")

    if isinstance(progress, bool) or not isinstance(progress, (int, float)):
        raise TypeError("progress must be a number")
    if not 0 <= progress <= 100:
        raise ValueError("progress must be between 0 and 100")

    if not isinstance(status, str):
        raise TypeError("status must be a string")
    if not status.strip():
        raise ValueError("status must not be empty")

    cursor = connection.execute(
        """
        UPDATE learning_records
        SET month = ?, topic = ?, progress = ?, status = ?
        WHERE id = ?
        """,
        (month, topic.strip(), progress, status.strip(), record_id),
    )
    connection.commit()

    return cursor.rowcount > 0


def delete_record(
    connection: sqlite3.Connection,
    record_id: int,
) -> bool:
    """Delete a learning record by ID."""
    if isinstance(record_id, bool) or not isinstance(record_id, int):
        raise TypeError("record_id must be an integer")
    if record_id <= 0:
        raise ValueError("record_id must be positive")

    cursor = connection.execute(
        "DELETE FROM learning_records WHERE id = ?",
        (record_id,),
    )
    connection.commit()

    return cursor.rowcount > 0