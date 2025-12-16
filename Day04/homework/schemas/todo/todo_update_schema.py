from typing import Optional

from pydantic import BaseModel, Field, field_validator


class TodoUpdateSchema(BaseModel):
    title: Optional[str] = Field(min_length=3, default=None)
    description: Optional[str] = None
    priority: Optional[int] = None
    done: Optional[bool] = None

    @field_validator("title", "priority", "done", mode="before")
    @classmethod
    def forbid_null(cls, v):
        if v is None:
            raise ValueError("Field không được phép là null")
        return v

    @field_validator("title", "description", mode="before")
    @classmethod
    def strip_whitespace(cls, v):
        return v.strip()
