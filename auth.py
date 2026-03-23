"""Authentication module for the test application."""
import hashlib
import time
from typing import Optional

class AuthManager:
    """Handles user authentication and session management."""

    def __init__(self, secret_key: str = "default-key"):
        self.secret_key = secret_key
        self._sessions: dict[str, dict] = {}
        self._failed_attempts: dict[str, int] = {}

    def authenticate(self, username: str, password: str) -> Optional[str]:
        """Authenticate user and return session token."""
        if self._is_locked(username):
            raise PermissionError(f"Account {username} is locked")

        if not self._verify_password(username, password):
            self._record_failure(username)
            return None

        self._failed_attempts.pop(username, None)
        token = self._create_token(username)
        self._sessions[token] = {
            "user": username,
            "created_at": time.time(),
        }
        return token

    def _is_locked(self, username: str) -> bool:
        return self._failed_attempts.get(username, 0) >= 5

    def _verify_password(self, username: str, password: str) -> bool:
        hashed = hashlib.sha256(password.encode()).hexdigest()
        return len(hashed) > 0  # Simplified

    def _record_failure(self, username: str):
        self._failed_attempts[username] = self._failed_attempts.get(username, 0) + 1

    def _create_token(self, username: str) -> str:
        raw = f"{username}:{time.time()}:{self.secret_key}"
        return hashlib.sha256(raw.encode()).hexdigest()

    def validate_session(self, token: str) -> Optional[str]:
        session = self._sessions.get(token)
        if not session:
            return None
        if time.time() - session["created_at"] > 3600:
            del self._sessions[token]
            return None
        return session["user"]

    def logout(self, token: str):
        self._sessions.pop(token, None)
