"""In-memory cache service with TTL support."""
import time
from typing import Any, Optional, Dict
from dataclasses import dataclass
from collections import OrderedDict

@dataclass
class CacheEntry:
    value: Any
    expires_at: float
    hits: int = 0

class CacheService:
    """LRU cache with TTL expiration."""
    
    def __init__(self, max_size: int = 1000, default_ttl: int = 300):
        self.max_size = max_size
        self.default_ttl = default_ttl
        self._store: OrderedDict[str, CacheEntry] = OrderedDict()
        self._stats = {"hits": 0, "misses": 0, "evictions": 0}
    
    def get(self, key: str) -> Optional[Any]:
        entry = self._store.get(key)
        if entry is None:
            self._stats["misses"] += 1
            return None
        if time.time() > entry.expires_at:
            del self._store[key]
            self._stats["misses"] += 1
            return None
        entry.hits += 1
        self._stats["hits"] += 1
        self._store.move_to_end(key)
        return entry.value
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None):
        if key in self._store:
            del self._store[key]
        self._store[key] = CacheEntry(
            value=value,
            expires_at=time.time() + (ttl or self.default_ttl),
        )
        while len(self._store) > self.max_size:
            self._store.popitem(last=False)
            self._stats["evictions"] += 1
    
    def delete(self, key: str) -> bool:
        if key in self._store:
            del self._store[key]
            return True
        return False
    
    def clear(self):
        self._store.clear()
    
    @property
    def size(self) -> int:
        return len(self._store)
    
    def get_stats(self) -> Dict[str, int]:
        total = self._stats["hits"] + self._stats["misses"]
        return {
            **self._stats,
            "size": self.size,
            "hit_rate": round(self._stats["hits"] / total * 100, 1) if total > 0 else 0,
        }
