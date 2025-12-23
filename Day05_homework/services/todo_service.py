from sqlalchemy.orm import Session

from models import Todo
from repositories import TodoRepository
from schemas import TodoCreate, TodoOut


class TodoService:
    def __init__(self, db: Session):
        self.db = db
        self.todo_repository = TodoRepository(db)

    def create_todo(self, data: TodoCreate) -> TodoOut:
        new_todo = Todo(**data.model_dump())
        created_todo = self.todo_repository.create(new_todo)
        return TodoOut.model_validate(created_todo)

    def is_exist_by_title(self, title: str) -> bool:
        existed_todo = self.todo_repository.get_by_title(title)
        return existed_todo is not None
