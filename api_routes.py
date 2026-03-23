"""API Routes for the application."""
from fastapi import APIRouter, HTTPException, Depends
from typing import Optional
from auth import AuthManager

router = APIRouter(prefix="/api/v1")
auth_manager = AuthManager()

@router.post("/login")
async def login(username: str, password: str):
    """Authenticate user and return token."""
    try:
        token = auth_manager.authenticate(username, password)
        if not token:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return {"token": token, "expires_in": 3600}
    except PermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))

@router.post("/logout")
async def logout(token: str):
    """Invalidate session token."""
    auth_manager.logout(token)
    return {"message": "Logged out successfully"}

@router.get("/me")
async def get_current_user(token: str):
    """Get current authenticated user."""
    user = auth_manager.validate_session(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return {"username": user}

@router.get("/health")
async def health_check():
    """Application health check endpoint."""
    return {"status": "healthy", "version": "2.0.0"}
