from pydantic_settings import BaseSettings


class APISettings(BaseSettings):
    api_key: str
    api_key_secret: str

class DBSettings(BaseSettings):
    host: str
    port: int
    userame: str
    password: str
    database: str

API_SETTINGS = APISettings()
DB_SETTINGS = DBSettings()
