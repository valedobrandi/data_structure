from pydantic_settings import baseSettings, SettingsConfigDict


class Settings(baseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    app_name: str = "Hello World!"
    minute_rate_limit: int = 100
    mongo_uri: str
