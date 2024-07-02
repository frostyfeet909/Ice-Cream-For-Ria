"""Utility functions for FastAPI routes.

Provides:
- get_or_404: Return obj if obj else raise exception.
"""

from typing import TYPE_CHECKING, TypeVar

from fastapi import HTTPException, status

if TYPE_CHECKING:
    from fastapi import APIRouter, Response

    from api.schemas import CustomModel, CustomSQLModel

get_or_error_type = TypeVar(
    "get_or_error_type", bound="CustomModel"
)  # - Intentionally loose typing
RESPONSE_GET_OBJECT_FROM_ID_NOT_FOUND = {
    status.HTTP_404_NOT_FOUND: {
        "name": "instanceNotFoundError",
        "message": "The specified item does not exist.",
        "details": {
            "item": "{item}",
            "id": "{id}",
        },
    },
}


def get_or_404(
    obj: get_or_error_type | None,  # - Intentionally loose typing
    item: str,
    id_: str,
    status_code: int = status.HTTP_404_NOT_FOUND,
) -> get_or_error_type:  # - Intentionally loose typing
    """Check if the object is not None otherwise raise an HTTPException.

    Args:
        obj (Any): The object to check.
        item (str): The name of the object.
        id_ (str): The ID of the object.
        status_code (int, optional): The status code to raise. Defaults to status.HTTP_404_NOT_FOUND.

    Raises:
        HTTPException: If the object is None.

    Returns:
        Any: The object.
    """
    if obj:
        return obj

    raise HTTPException(
        status_code=status_code,
        detail={
            "name": "instanceNotFoundError",
            "message": "The specified item does not exist.",
            "details": {
                "item": item,
                "id": id_,
            },
        },
    )


def attach_location_header_to_response(
    response: "Response", router: "APIRouter", item: "CustomSQLModel"
) -> "Response":
    """Attach the Location header of the item to the response.

    Args:
        response (Response): The response object.
        router (APIRouter): The router object.
        item (CustomSQLModel): The item to get the ID from.

    Returns:
        Response: The response object with the Location header attached.
    """
    response.headers["Location"] = router.prefix + f"/{item.id}"
    return response
