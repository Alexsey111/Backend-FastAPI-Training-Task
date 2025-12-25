from dataclasses import dataclass


@dataclass
class URLMapping:
    short_id: str
    original_url: str
