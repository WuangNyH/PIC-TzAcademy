from fastapi import APIRouter

from controllers.todo_controller import todo_router

router = APIRouter(prefix="/api/v1")
router.include_router(todo_router)
