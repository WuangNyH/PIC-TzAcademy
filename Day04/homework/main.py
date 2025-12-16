import uvicorn
from fastapi import FastAPI

from homework.controllers.todo_controller import todo_router

app = FastAPI()

app.include_router(todo_router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
