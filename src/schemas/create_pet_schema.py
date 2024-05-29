from pydantic import BaseModel, field_validator
from src.logger import get_logger

logger = get_logger(__name__)


class Category(BaseModel):
    id: int
    name: str


class Tag(BaseModel):
    id: int
    name: str


class CreatePetSchema(BaseModel):
    id: int
    name: str
    category: Category
    photoUrls: list[str] = []
    tag: list[Tag] = []
    status: str

    @field_validator("status")
    def check_status(cls, v: str) -> str:
        if v not in ["available", "pending", "sold"]:
            logger.error(f"Invalid status: {v}")
            raise ValueError(f'Invalid status: {v}. Status must be one of ["available", "pending", "sold"]')
        return v

