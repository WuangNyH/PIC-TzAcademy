from http import HTTPStatus

from sqlalchemy.orm import Session

from exceptions.app_exceptions import AppException
from models import Todo
from repositories import TodoRepository
from schemas import TodoCreate, TodoOut


class TodoService:
    def __init__(self, db: Session):
        self.db = db
        self.todo_repository = TodoRepository(db)

    def create_todo(self, data: TodoCreate) -> TodoOut:
        if self.is_exist_by_title(data.title):
            raise AppException(
                status_code=HTTPStatus.CONFLICT,
                code="TODO_ALREADY_EXISTS",
                message=f"Todo with title '{data.title}' already exists.",
            )

        new_todo = Todo(**data.model_dump())
        created_todo = self.todo_repository.create(new_todo)
        return TodoOut.model_validate(created_todo)

    def is_exist_by_title(self, title: str) -> bool:
        existed_todo = self.todo_repository.get_by_title(title)
        return existed_todo is not None
