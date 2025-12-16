from fastapi import APIRouter

from learn.schemas.common.error_schema import ErrorResponse
from learn.schemas.user.user_create_schema import UserCreateSchema
from learn.schemas.user.user_out_schema import UserOut
from learn.services import user_service

user_router = APIRouter()


@user_router.post(
    "",
    status_code=201,
    response_model=UserOut,
    responses={
        400: {"model": ErrorResponse, "description": "Invalid input on business logic"}
    },
)
def create_user(user: UserCreateSchema) -> UserOut:
    return user_service.create_user(user)
