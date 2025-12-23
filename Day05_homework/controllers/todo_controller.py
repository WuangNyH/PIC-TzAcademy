from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse, Response

from dependencies.db import get_db
from schemas import TodoOut, TodoCreate
from schemas.response.error_response import ErrorSchema
from services.todo_service import TodoService
from utils.response import response_success

todo_router = APIRouter(prefix="/todos", tags=["Todo Controller"])


@todo_router.post(
    "/",
    response_model=TodoOut,
    status_code=HTTPStatus.CREATED,
    responses={
        409: {"model": ErrorSchema, "description": "Todo title already exists"},
        422: {"model": ErrorSchema, "description": "Validation Error"},
    },
)
async def create_todo(
    request: TodoCreate, response: Response, db: Session = Depends(get_db)
) -> JSONResponse:
    todo = TodoService(db).create_todo(request)

    response.headers["location"] = f"/todos/{todo.id}"

    return response_success(todo, HTTPStatus.CREATED)
