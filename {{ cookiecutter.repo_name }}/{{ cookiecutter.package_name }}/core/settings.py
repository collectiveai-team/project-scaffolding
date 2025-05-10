import os
from typing import Literal

from dotenv import load_dotenv
from pydantic import ConfigDict, SecretStr
from pydantic_settings import BaseSettings


try:
    from {{ cookiecutter.package_name }}.core.version import __version__
except ImportError:
    __version__ = "0.0.0"


def load_env():
    load_dotenv(".env")

    # Load the stage-specific .env file (if it exists)
    stage = os.getenv("STAGE")
    if stage:
        env_file = f".env.{stage}"
        if os.path.exists(env_file):
            load_dotenv(env_file)


class Settings(BaseSettings):
    model_config = ConfigDict(case_sensitive=True)

    ##########################################################################
    # Application settings
    ##########################################################################

    APP_NAME: str = ""
    APP_VERSION: str = __version__

    ENV: str | None = None

    ###############################################################################
    # Other settings
    ###############################################################################
    CUSTOM_LITERAL: Literal['opt1', 'opt2', 'opt3'] = 'opt1'
    CUSTOM_SECRET: SecretStr | None = None



load_env()
settings = Settings()
