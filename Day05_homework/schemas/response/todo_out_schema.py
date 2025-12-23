from pydantic import BaseModel

from enums import Priority


class TodoOut(BaseModel):
    id: int
    title: str
    description: str
    priority: Priority
    done: bool

    class Config:
        from_attributes = True
        use_enum_values = False
