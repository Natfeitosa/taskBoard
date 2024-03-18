from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Date, Enum
from sqlalchemy.orm import relationship
import enum

class State(enum.IntEnum):
    PROPOSED = 0
    IN_PROGRESS = 1
    COMPLETED = 2
    
class User(Base):
    __tablename__ = "users"
    
    email = Column(String(length=255), nullable=False, unique=True)
    user_id = Column(String(length=36), primary_key=True, nullable=False)
    first_name = Column(String(length=50), nullable=True)
    last_name = Column(String(length=50), nullable=True)
    
class Project(Base):
    __tablename__ = "projects"
    
    tasks = relationship("Task", back_populates="project", cascade="all, delete-orphan")
    owner = relationship("User")
    title = Column(String(255), nullable=False)
    project_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    last_modified = Column(DateTime, nullable=False)
    date_created = Column(Date, nullable=False)
    author_id = Column(String(length=36), ForeignKey("users.user_id"), nullable=False)
    
class Task(Base):
    __tablename__ = "tasks"
    
    project = relationship("Project", back_populates="tasks")
    state = Column(Enum(State, create_constraint=True, name="state_enum"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(String)
    date_created = Column(Date, nullable=False)
    last_modified = Column(DateTime, nullable=False)
    task_id = Column(Integer, primary_key=True, autoincrement=True)
    assignee_id = Column(String(length=36), ForeignKey("users.user_id"), nullable=False)
    project_id = Column(Integer, ForeignKey("projects.project_id"))
    