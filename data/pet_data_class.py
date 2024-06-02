from dataclasses import dataclass

@dataclass
class PetDataClass:
    uid: int
    category: dict
    name: str
    photo_urls: str
    tags: dict
    status: str
