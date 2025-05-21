import os
import logging

from pathlib import Path
from fastapi import FastAPI, Request, status
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from config import settings
from app.core.lifetime import lifespan
from app.core.routers import router as router_api_v1


APP_ROOT = Path(__file__).parent.parent

DESCRIPTION = """
This API for Agent platform.
"""


def get_app() -> FastAPI:
    """
    Create FastAPI application.

    :return: FastAPI application.
    """

    app = FastAPI(
        title="SUN API",
        description=DESCRIPTION,
        version="0.1.1",
        lifespan=lifespan,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        docs_url=f"{settings.API_V1_STR}/docs",
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins="*",
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
    app.include_router(router_api_v1, prefix="/api")
    os.makedirs(os.path.join(settings.STORAGE, 'files'), exist_ok=True)
    app.mount("/resources/files",
              StaticFiles(directory=os.path.join(settings.STORAGE, 'files')), name="file")

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        logging.error(f"RequestValidationError: {exc.errors()}")

        errors = []
        for error in exc.errors():
            errors.append({
                "field": ".".join(str(loc) for loc in error["loc"]),
                "message": error["msg"]
            })

        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"detail": "Invalid data", "errors": errors},
        )

    return app
