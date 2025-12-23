from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from configs.app_logging import setup_logging
from configs.env import settings_config
from exceptions.app_exceptions import AppException
from handlers.exception_handler import (
    app_exception_handler,
    validation_exception_handler,
)
from middlewares import DBSessionMiddleware, TraceIDMiddleware
from router import router

settings = settings_config()
setup_logging(sql_echo=settings.environment.lower() == "dev")

app = FastAPI()
app.include_router(router)

__MIDDLEWARES__ = [DBSessionMiddleware, TraceIDMiddleware]
for middleware in __MIDDLEWARES__:
    app.add_middleware(middleware)

__EXCEPTION_HANDLERS__ = [
    (AppException, app_exception_handler),
    (RequestValidationError, validation_exception_handler),
]

for exc, handler in __EXCEPTION_HANDLERS__:
    app.add_exception_handler(exc, handler)
