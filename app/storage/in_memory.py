import asyncio
from typing import Dict, Optional


class InMemoryStorage:
    def __init__(self):
        self._data: Dict[str, str] = {}
        self._lock = asyncio.Lock()

    async def save(self, short_id: str, original_url: str) -> None:
        async with self._lock:
            self._data[short_id] = original_url

    async def get(self, short_id: str) -> Optional[str]:
        async with self._lock:
            return self._data.get(short_id)
