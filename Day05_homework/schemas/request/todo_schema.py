from pydantic import Field, BaseModel

from enums import Priority


class TodoCreate(BaseModel):
    title: str = Field(min_length=3)
    description: str | None = Field(default=None)
    priority: Priority = Field(default=Priority.MEDIUM)
    done: bool = Field(default=False)


class TodoUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=3)
    description: str | None = Field(default=None)
    priority: Priority | None = Field(default=None)
    done: bool | None = Field(default=None)


class TodoFilter(BaseModel):
    keyword: str | None = None
    done: bool | None = None
    offset: int = Field(default=0, ge=0)
    limit: int = Field(default=100, ge=1)
