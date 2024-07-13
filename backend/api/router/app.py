"""The main FastAPI application.

Provides:
- app: The FastAPI application.
"""

import datetime
import json
from pathlib import Path
from typing import TYPE_CHECKING

from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware

from api.config import api_config
from api.router.endpoints import config_router
from api.router.lifespan import lifespan
from api.utils.constants_router import (
    API_CONTACT_INFO,
    API_DESCTIPTION,
    API_SUMMARY,
    API_TITLE,
    DOCS_ENABLED_ENVS,
    PATH_FOR_DOCS,
    PATH_FOR_REDOC,
)
from api.utils.utils import get_version

if TYPE_CHECKING:
    from collections.abc import Awaitable, Callable

FILE__openapi_tags = Path(__file__).parent.resolve() / "openapi_tags.json"

openapi_tags = None
with FILE__openapi_tags.open() as file:
    openapi_tags = json.load(file)


app = FastAPI(
    lifespan=lifespan,
    version=get_version(),
    title=API_TITLE,
    summary=API_SUMMARY,
    description=API_DESCTIPTION,
    contact=API_CONTACT_INFO,
    docs_url=PATH_FOR_DOCS if api_config.MODE in DOCS_ENABLED_ENVS else None,
    redoc_url=PATH_FOR_REDOC if api_config.MODE in DOCS_ENABLED_ENVS else None,
)

# Mount Routers
app.include_router(config_router)

# Mount Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(url) for url in api_config.ALLOWED_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def log_request_middleware(
    request: Request, call_next: "Callable[[Request], Awaitable[Response]]"
) -> Response:
    """Log request.

    Args:
        request (Request): The request.
        call_next (Callable[[Request], Awaitable[Response]]): The next middleware in the chain.

    Returns:
        Response: The response.
    """
    start_time = datetime.datetime.now(tz=datetime.UTC)

    response = await call_next(request)

    process_time = datetime.datetime.now(tz=datetime.UTC) - start_time
    print(f"request took {process_time}")

    response.headers["X-Process-Time"] = str(process_time.total_seconds())
    response.headers["X-Request-Id"] = "You found me!"

    return response
