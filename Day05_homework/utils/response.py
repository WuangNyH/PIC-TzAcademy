from typing import Any

from starlette.responses import JSONResponse

from schemas import SuccessResponse


def response_success(data: Any) -> JSONResponse:
    return JSONResponse(SuccessResponse.of(data).model_dump())
