import sqlite3

from database.connection import DATABASE_PATH, get_connection


def test_get_connection_returns_sqlite_connection(tmp_path):
    database_path = tmp_path / "test.db"

    connection = get_connection(database_path)

    try:
        assert isinstance(connection, sqlite3.Connection)
        assert database_path.exists()
    finally:
        connection.close()


def test_get_connection_uses_default_database():
    connection = get_connection()

    try:
        assert isinstance(connection, sqlite3.Connection)
        assert DATABASE_PATH.exists()
    finally:
        connection.close()