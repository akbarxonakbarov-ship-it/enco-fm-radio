from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    bot_token: str
    admin_user_id: int

    database_url: str

    radio_name: str = "Enco FM"
    radio_channel: str = "@encofm"
    autodj_bot: str = "@Encofm_bot"
    database_bot: str = "@Encofmdatabase_bot"
    timezone: str = "Europe/Helsinki"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
