from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    postgres_database_hostname: str
    postgres_database_port: str
    postgres_database_password: str
    postgres_database_name: str
    postgres_database_username: str
    auth_database_url: str
    auth_database_sql_string: str
    auth_database_key: str
        
settings = Settings()