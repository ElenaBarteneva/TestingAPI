from pydantic import BaseModel, field_validator


class Category(BaseModel):
    id: int
    name: str


class Tags(BaseModel):
    id: int
    name: str


class CreatePetSchema(BaseModel):
    id: int
    category: Category
    photoUrls: list[str] = []
    tags: list[Tags] = []
    status: str


@field_validator("status")
def check_status(cls, v: str) -> str:
    if v not in ['available', 'pending', 'sold']:
        raise ValueError(f"invalid status: {v}. Status must be one of ['available', 'pending', 'sold']")
    return v

