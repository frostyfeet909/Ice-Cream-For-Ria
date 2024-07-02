import hashlib
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict
from zoneinfo import ZoneInfo


def convert_datetime_to_iso(dt: datetime) -> str:
    """Convert a datetime object to a string ISO format with UTC timezone."""
    if not dt.tzinfo:
        dt = dt.replace(tzinfo=ZoneInfo("UTC"))

    return dt.isoformat()


class CustomModel(BaseModel):
    """Base class for Pydantic models."""

    model_config = ConfigDict(
        json_encoders={datetime: convert_datetime_to_iso},
        populate_by_name=True,
    )

    def hash(self) -> UUID:
        """Hash the model using md5. Returns a UUID object."""
        return UUID(hashlib.md5(self.model_dump_json().encode()).hexdigest())
