"""Classes for the api configuration.

Provides:
- config: The configuration for the api.
"""

import re
from pathlib import Path

from pydantic import (
    Field,
    HttpUrl,
)
from pydantic_settings import BaseSettings, SettingsConfigDict

from api.config.enums import AppMode
from api.utils.constants_config import PREFIX__api_config

PATTERN__postgres_login_info = re.compile(r"\/\/(\w)+:([^\:@])*@")


class ApiConfig(BaseSettings):
    """Config generic to the entire application.

    It is however prefered to load this in in services and pass paramaters when needed.
    i.e. disable queues and threading globally. As well as globally defining the progress store.

    Attributes:
        MODE (str): The mode the application is running in.
        QUEUE_IS_ALLOWED (bool): Whether the queue is allowed to be used.
        DISABLE_ALL_THREADING (bool): Disable all threading.
        POSTGRES_CONNECTION_STRING (PostgresDsn): The connection string to the postgres database.
        TOKEN_EXPIRES_MINUTES (int): The token expiry time.
        TOKEN_ALGORITHM (str): The token algorithm.
        SECRET_KEY (SecretStr): The secret key.
        ALLOWED_ORIGINS (list[HttpUrl]): The allowed origins.
    """

    MODE: str = Field(
        default=AppMode.LOCAL, description="The mode the application is running in."
    )
    
    ALLOWED_ORIGINS: list[HttpUrl] = Field(
        default=[], description="The allowed origins."
    )

    model_config = SettingsConfigDict(
        env_file=Path(".env"), env_prefix=PREFIX__api_config, extra="ignore"
    )

    _prefix = PREFIX__api_config


config = ApiConfig()
