"""Router endpoints for the API.

This module will provide the router endpoints for the API.
Each file will be a seperate prefix for the API.

Each file should import the relevant CRUD and schema files as {endpoint}_crud and {endpoint}_schema.

Note that TH001 and TCH002 are turned off here as fastapi instantiaes the dependaincys
from the arguemnts and the type is required at runtime for this.

https://docs.astral.sh/ruff/rules/typing-only-first-party-import/
"""

from fastapi.routing import APIRouter

from .health import ROUTER as SCENARIOS_ROUTER

app = APIRouter(prefix="/default", tags=["Default"])
app.include_router(SCENARIOS_ROUTER)

__all__ = ["app"]
