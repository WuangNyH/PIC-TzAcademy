from starlette.responses import JSONResponse


def response_success(data):
    return JSONResponse(status_code=200, content={"success": True, "data": data})
