from typing import TypeVar, Generic

from pydantic import BaseModel

from configs.trace import trace_id_ctx

T = TypeVar("T")


class SuccessResponse(BaseModel, Generic[T]):
    success: bool = True
    data: T
    message: str | None = None
    trace_id: str | None = None

    @classmethod
    def of(cls, data: T, message: str | None = None):
        return cls(
            data=data,
            message=message,
            trace_id=trace_id_ctx.get(),
        )
