from pydantic import BaseModel, field_serializer

from enums import Priority


class TodoOut(BaseModel):
    id: int
    title: str
    description: str | None
    priority: Priority
    done: bool

    @field_serializer("priority")
    def serialize_priority(self, priority: Priority):
        return priority.name

    class Config:
        from_attributes = True
