from pydantic import BaseModel


class TodoOutSchema(BaseModel):
    todo_id: int
    title: str
    description: str | None
    priority: int
    done: bool

    model_config = {"from_attributes": True}
