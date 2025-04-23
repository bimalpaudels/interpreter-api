from starlette import status
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from urllib.request import Request

from model import BaseResponse


def configure_app(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

async def global_exception_handler(request: Request, exception: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=BaseResponse(
            message=str(exception),
            success=False,
            type="server_error",
        ).model_dump(),
    )