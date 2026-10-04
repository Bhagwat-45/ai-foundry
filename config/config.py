from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    endpoint : str = Field(validation_alias="AZURE_ENDPOINT")
    model_name: str = Field(validation_alias="AZURE_MODEL_NAME")
    key: str = Field(validation_alias="AZURE_KEY")

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()