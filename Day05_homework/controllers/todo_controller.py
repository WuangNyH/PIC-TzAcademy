from fastapi import APIRouter

todo_router = APIRouter(prefix="/todos", tags=["Todo Controller"])

# @todo_router.post(
#     "/",
#     response_model=TodoOut,
#     status_code=201,
#     responses={
#         400: {"model": ErrorSchema, "description": "Invalid input data"},
#         409: {"model": ErrorSchema, "description": "Todo title already exists"},
#     },
# )
