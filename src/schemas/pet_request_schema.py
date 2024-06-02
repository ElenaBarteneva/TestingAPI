from typing import List
from pydantic import BaseModel

class Category(BaseModel):
    id: int
    name: str

class Tag(BaseModel):
    id: int
    name: str

class PetRequestSchema(BaseModel):
    id: int
    name: str
    category: Category
    photoUrls: List[str]
    tags: List[Tag]
    status: str