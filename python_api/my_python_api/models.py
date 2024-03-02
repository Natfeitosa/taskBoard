from .database import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

class User(Base):
    __tablename__ = "users"
    
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    email = Column(String, primary_key=True, nullable=False) 
    password = Column(String, nullable=True)
    #id = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    