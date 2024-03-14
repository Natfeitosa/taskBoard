from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Date, Enum
from sqlalchemy.orm import relationship
import enum

class Status(enum.Enum):
    PROPOSED = 0
    IN_PROGRESS = 1
    COMPLETED = 2
    
class User(Base):
    __tablename__ = "users"
    
    email = Column(String, nullable=False, unique=True)
    user_id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    
class Project(Base):
    __tablename__ = "projects"
    
    tasks = relationship("Task", backref="project")
    owner = relationship("User")
    project_id = Column(Integer, primary_key=True, nullable=False)
    last_modified = Column(DateTime, nullable=False)
    date_created = Column(Date, nullable=False)
    author_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    
class Task(Base):
    __tablename__ = "tasks"
    
    status = Column(Enum(Status), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(String)
    date_created = Column(Date, nullable=False)
    last_modified = Column(DateTime, nullable=False)
    task_id = Column(Integer, primary_key=True)
    assignee_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    project_id = Column(Integer, ForeignKey("projects.project_id"))
    