from pydantic_settings import BaseSettings
from pydantic import BaseModel


class RunSettings(BaseModel):
    host: str = '0.0.0.0' 
    port: int = 8000


class ApiSettings(BaseModel):
    prefix: str = '/api'


class Settings(BaseSettings):
    run: RunSettings = RunSettings()
    api: ApiSettings = ApiSettings()


settings = Settings()  # initializing settings