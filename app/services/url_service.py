from ..storage.in_memory import InMemoryStorage
from ..utils.id_generator import generate_short_id


class URLService:
    def __init__(self):
        self._storage = InMemoryStorage()

    async def create_short_url(self, original_url: str) -> str:
        short_id = generate_short_id()
        await self._storage.save(short_id, original_url)
        return short_id

    async def get_original_url(self, short_id: str) -> str | None:
        return await self._storage.get(short_id)
