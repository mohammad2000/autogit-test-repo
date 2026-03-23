"""Security middleware for rate limiting and request validation."""
import time
import hashlib
from typing import Dict, List
from dataclasses import dataclass, field

@dataclass
class RequestLog:
    timestamp: float
    ip: str
    endpoint: str

class SecurityMiddleware:
    """Rate limiting and security middleware."""
    
    def __init__(self, max_requests: int = 100, window_sec: int = 60):
        self.max_requests = max_requests
        self.window = window_sec
        self._requests: Dict[str, List[float]] = {}
        self._blocked_ips: Dict[str, float] = {}
    
    def check_rate_limit(self, ip: str) -> bool:
        """Check if IP is within rate limit."""
        now = time.time()
        
        # Check if IP is blocked
        if ip in self._blocked_ips:
            if now < self._blocked_ips[ip]:
                return False
            del self._blocked_ips[ip]
        
        # Clean old entries
        requests = self._requests.get(ip, [])
        requests = [t for t in requests if now - t < self.window]
        
        if len(requests) >= self.max_requests:
            self._blocked_ips[ip] = now + (self.window * 2)
            return False
        
        requests.append(now)
        self._requests[ip] = requests
        return True
    
    def validate_request(self, headers: dict) -> bool:
        """Validate request headers for security."""
        required = ["content-type", "user-agent"]
        for h in required:
            if h not in headers:
                return False
        return True
    
    def generate_request_id(self) -> str:
        """Generate unique request ID."""
        raw = f"{time.time()}:{id(self)}"
        return hashlib.sha256(raw.encode()).hexdigest()[:16]

class CORSMiddleware:
    """CORS configuration middleware."""
    
    ALLOWED_ORIGINS = [
        "http://localhost:3000",
        "http://localhost:5173",
        "https://app.gritiva.com",
    ]
    
    def __init__(self, allowed_origins: list = None):
        self.origins = allowed_origins or self.ALLOWED_ORIGINS
    
    def is_allowed_origin(self, origin: str) -> bool:
        return origin in self.origins or "*" in self.origins
    
    def get_cors_headers(self, origin: str) -> dict:
        if self.is_allowed_origin(origin):
            return {
                "Access-Control-Allow-Origin": origin,
                "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE",
                "Access-Control-Allow-Headers": "Content-Type, Authorization",
                "Access-Control-Max-Age": "86400",
            }
        return {}
