from pydantic import Field, BaseModel, field_validator

from enums import Priority


class TodoCreate(BaseModel):
    title: str = Field(min_length=3)
    description: str | None = Field(default=None)
    priority: Priority = Field(default=Priority.MEDIUM)
    done: bool = Field(default=False)

    @field_validator("title", "description", mode="before")
    def strip_whitespace(cls, v):
        return v.strip()


class TodoUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=3)
    description: str | None = Field(default=None)
    priority: Priority | None = Field(default=None)
    done: bool | None = Field(default=None)

    @field_validator("title", "description", "priority", "done", mode="before")
    def validate_not_null_and_strip(cls, v):
        if v is None:
            raise ValueError("Field cannot be null")

        if isinstance(v, str):
            return v.strip()

        return v


class TodoFilter(BaseModel):
    keyword: str | None = None
    done: bool | None = None
    offset: int = Field(default=0, ge=0)
    limit: int = Field(default=100, ge=1)
