"""Enums for the application.

Provides:
- AppMode: The mode the application is running in.
"""

from enum import StrEnum


class AppMode(StrEnum):
    """The mode the application is running in."""

    LOCAL = "local"
    DEV = "dev"
    PROD = "prod"
