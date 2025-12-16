from fastapi import APIRouter

from homework.schemas.error.error_schema import ErrorSchema
from homework.schemas.todo.todo_create_schema import TodoCreateSchema
from homework.schemas.todo.todo_out_schema import TodoOutSchema
from homework.schemas.todo.todo_update_schema import TodoUpdateSchema
from homework.services import todo_service

todo_router = APIRouter(prefix="/todos", tags=["todos"])


@todo_router.post(
    "/",
    response_model=TodoOutSchema,
    status_code=201,
    responses={
        400: {"model": ErrorSchema, "description": "Invalid input data"},
        409: {"model": ErrorSchema, "description": "Todo title already exists"},
    },
)
def create_todo(todo: TodoCreateSchema) -> TodoOutSchema:
    return todo_service.create_todo(todo)


@todo_router.get(
    "/",
    response_model=list[TodoOutSchema],
    status_code=200,
)
def get_todos_by_attribute(
    keywork: str | None = None, done: bool | None = None, limit: int = 10
) -> list[TodoOutSchema]:
    return todo_service.get_todos_by_attribute(keywork, done, limit)


@todo_router.get(
    "/{todo_id}",
    response_model=TodoOutSchema,
    status_code=200,
    responses={404: {"model": ErrorSchema, "description": "Todo not found"}},
)
def get_todo_by_id(todo_id: int) -> TodoOutSchema:
    return todo_service.get_todo_by_id(todo_id)


@todo_router.put(
    "/{todo_id}",
    response_model=TodoOutSchema,
    status_code=200,
    responses={
        400: {"model": ErrorSchema, "description": "Invalid input data"},
        404: {"model": ErrorSchema, "description": "Todo not found"},
        409: {"model": ErrorSchema, "description": "Todo title already exists"},
    },
)
def update_all_attribute(todo_id: int, request: TodoCreateSchema) -> TodoOutSchema:
    return todo_service.update_all_attribute(todo_id, request)


@todo_router.patch(
    "/{todo_id}",
    response_model=TodoOutSchema,
    status_code=200,
    responses={
        400: {"model": ErrorSchema, "description": "Invalid input data"},
        404: {"model": ErrorSchema, "description": "Todo not found"},
        409: {"model": ErrorSchema, "description": "Todo title already exists"},
    },
)
def update_partial_attribute(todo_id: int, request: TodoUpdateSchema) -> TodoOutSchema:
    return todo_service.update_partial_attribute(todo_id, request)


@todo_router.delete(
    "/{todo_id}",
    status_code=204,
    responses={
        404: {"model": ErrorSchema, "description": "Todo not found"},
    },
)
def delete_todo(todo_id: int) -> None:
    return todo_service.delete_todo_by_id(todo_id)
