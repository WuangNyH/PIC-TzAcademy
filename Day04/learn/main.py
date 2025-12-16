from fastapi import FastAPI

from controllers.user_controller import user_router

app = FastAPI()
app.include_router(user_router, prefix="/users")
