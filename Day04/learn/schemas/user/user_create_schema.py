from pydantic import BaseModel, Field


class UserCreateSchema(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=50,
        pattern=r"^[A-Za-z ]+$",
        description="User name (2-50 characters) contains only letters",
        examples=["Taro Kun"],
    )
    age: int = Field(ge=0)
    address: str | None = None
