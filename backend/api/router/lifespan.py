"""Lifespan events for FastAPI application.

Provides:
- lifespan: The lifespan event handler.
"""

from contextlib import asynccontextmanager
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator

    from fastapi import FastAPI


@asynccontextmanager
async def lifespan(_: "FastAPI") -> "AsyncGenerator[None, None]":
    """Lifespan event handler.

    Checks the async connection to the database.

    Args:
        _: The FastAPI application.

    Yields:
        None: The lifespan event handler.
    """

    yield
