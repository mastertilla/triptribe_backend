from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class APISettings(BaseSettings):
    API_KEY: str = 'test'
    API_KEY_SECRET: str = 'test'

class DBSettings(BaseSettings):
    HOST: str
    PORT: int
    USERNAME: str
    PASSWORD: str
    DATABASE: str

API_SETTINGS = APISettings()
DB_SETTINGS = DBSettings()
