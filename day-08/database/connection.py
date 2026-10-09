import sqlite3
from pathlib import Path


# Default database location for persistent application connections
DATABASE_PATH = Path(__file__).resolve().parent.parent / "learning.db"


# Open either the default database or a caller-selected database
def get_connection(
    database_path: str | Path = DATABASE_PATH,
) -> sqlite3.Connection:
    """Create and return a connection to a SQLite database."""
    return sqlite3.connect(database_path)