import sqlite3
from pathlib import Path


DATABASE_PATH = Path(__file__).resolve().parent.parent / "learning.db"


def get_connection(
    database_path: str | Path = DATABASE_PATH,
) -> sqlite3.Connection:
    """Create and return a connection to a SQLite database."""
    return sqlite3.connect(database_path)