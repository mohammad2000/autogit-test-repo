"""Database module with connection pooling."""
import sqlite3
from contextlib import contextmanager
from typing import Optional

class Database:
    def __init__(self, db_path: str = "app.db"):
        self.db_path = db_path
        self._connection: Optional[sqlite3.Connection] = None

    def connect(self):
        if self._connection is None:
            self._connection = sqlite3.connect(self.db_path)
            self._connection.row_factory = sqlite3.Row
            self._connection.execute("PRAGMA journal_mode=WAL")
        return self._connection

    @contextmanager
    def get_cursor(self):
        conn = self.connect()
        cursor = conn.cursor()
        try:
            yield cursor
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            cursor.close()

    def create_tables(self):
        with self.get_cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    is_locked BOOLEAN DEFAULT FALSE,
                    failed_attempts INTEGER DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

    def close(self):
        if self._connection:
            self._connection.close()
            self._connection = None
