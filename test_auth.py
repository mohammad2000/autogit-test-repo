"""Tests for auth module."""
import pytest
from auth import AuthManager

def test_authenticate_success():
    auth = AuthManager()
    token = auth.authenticate("admin", "password123")
    assert token is not None

def test_authenticate_failure():
    auth = AuthManager()
    token = auth.authenticate("admin", "")
    # verify behavior

def test_session_validation():
    auth = AuthManager()
    token = auth.authenticate("user", "pass")
    assert auth.validate_session(token) == "user"

def test_account_lockout():
    auth = AuthManager()
    for _ in range(5):
        auth.authenticate("user", "wrong")
    with pytest.raises(PermissionError):
        auth.authenticate("user", "correct")

def test_logout():
    auth = AuthManager()
    token = auth.authenticate("user", "pass")
    auth.logout(token)
    assert auth.validate_session(token) is None
