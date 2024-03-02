from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings


# yes this should not be hardcoded here
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.postgres_database_username}:{settings.postgres_database_password}@{settings.postgres_database_hostname}/{settings.postgres_database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()