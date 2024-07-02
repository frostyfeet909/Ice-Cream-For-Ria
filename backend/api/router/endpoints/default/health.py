
from fastapi import APIRouter

ROUTER = APIRouter(prefix="/health", tags=["Health"])


@ROUTER.get(
    "/",
    response_model=bool,
    summary="Check the API is healthy.",
)
async def endpoint_get_single(

):
    return True