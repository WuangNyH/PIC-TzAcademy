from typing import Optional

from pydantic import BaseModel, Field, field_validator


class TodoCreateSchema(BaseModel):
    title: str = Field(min_length=3)
    description: Optional[str] = None
    priority: int
    done: bool = False

    @field_validator("title", "description", mode="before")
    @classmethod
    def strip_whitespace(cls, v):
        return v.strip()
