from fastapi import HTTPException

from homework.models.Todo import Todo
from homework.schemas.todo.todo_create_schema import TodoCreateSchema
from homework.schemas.todo.todo_out_schema import TodoOutSchema
from homework.schemas.todo.todo_update_schema import TodoUpdateSchema

__todos: list[Todo] = []
_id_counter = 1


def create_todo(todo: TodoCreateSchema) -> TodoOutSchema:
    global _id_counter

    if is_exist_by_name(todo.title):
        raise HTTPException(status_code=409, detail="Tiêu đề công việc đã tồn tại")

    if not is_valid_priority(todo.priority):
        raise HTTPException(status_code=400, detail="Mức độ ưu tiên phải từ 1 đến 5")

    new_todo = Todo(todo_id=_id_counter, **todo.model_dump())

    __todos.append(new_todo)
    _id_counter += 1

    return TodoOutSchema(**new_todo.model_dump())


def get_todos_by_attribute(
    keywork: str | None = None, done: bool | None = None, limit: int = 10
) -> list[TodoOutSchema]:
    filtered_todos = __todos

    if keywork:
        filtered_todos = [
            todo
            for todo in filtered_todos
            if keywork.lower() in todo.title.lower()
            or keywork.lower() in todo.description.lower()
        ]

    if done is not None:
        filtered_todos = [todo for todo in filtered_todos if todo.done == done]

    return [TodoOutSchema(**todo.model_dump()) for todo in filtered_todos[:limit]]


def get_todo_by_id(todo_id: int) -> TodoOutSchema:
    for todo in __todos:
        if todo.todo_id == todo_id:
            return TodoOutSchema(**todo.model_dump())

    raise HTTPException(status_code=404, detail="Công việc không tồn tại")


def update_all_attribute(todo_id: int, request: TodoCreateSchema) -> TodoOutSchema:
    todo = next((t for t in __todos if t.todo_id == todo_id), None)

    if todo is None:
        raise HTTPException(status_code=404, detail="Công việc không tồn tại")

    if todo.title != request.title and is_exist_by_name(request.title):
        raise HTTPException(status_code=409, detail="Tiêu đề công việc đã tồn tại")

    if not is_valid_priority(request.priority):
        raise HTTPException(status_code=400, detail="Mức độ ưu tiên phải từ 1 đến 5")

    update_data = request.model_dump()

    for field, value in update_data.items():
        setattr(todo, field, value)

    return TodoOutSchema(**todo.model_dump())


def update_partial_attribute(todo_id: int, request: TodoUpdateSchema) -> TodoOutSchema:
    todo = next((t for t in __todos if t.todo_id == todo_id), None)

    if todo is None:
        raise HTTPException(status_code=404, detail="Công việc không tồn tại")

    if (
        request.title is not None
        and todo.title != request.title
        and is_exist_by_name(request.title)
    ):
        raise HTTPException(status_code=409, detail="Tiêu đề công việc đã tồn tại")

    if request.priority is not None and not is_valid_priority(request.priority):
        raise HTTPException(status_code=400, detail="Mức độ ưu tiên phải từ 1 đến 5")

    update_data = request.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(todo, field, value)

    return TodoOutSchema(**todo.model_dump())


def delete_todo_by_id(todo_id: int) -> None:
    global __todos
    todo = next((t for t in __todos if t.todo_id == todo_id), None)

    if todo is None:
        raise HTTPException(status_code=404, detail="Công việc không tồn tại")

    __todos.remove(todo)


def is_exist_by_name(title: str) -> bool:
    return any(todo.title == title for todo in __todos)


def is_valid_priority(priority: int) -> bool:
    return 1 <= priority <= 5
