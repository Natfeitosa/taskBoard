from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Date, Enum
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
import enum

class Status(enum.Enum):
    PROPOSED = 0
    IN_PROGRESS = 1
    COMPLETED = 2
    
class Project(Base):
    __tablename__ = "projects"
    
    project_id = Column(Integer, primary_key=True, nullable=False)
    tasks = relationship("Task", backref="project")
    last_modified = Column(DateTime, nullable=False)
    date_created = Column(Date, nullable=False)
    author_id = Column(Integer)
    
class Task(Base):
    __tablename__ = "tasks"
    
    status = Column(Enum(Status), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(String)
    date_created = Column(Date, nullable=False)
    last_modified = Column(DateTime, nullable=False)
    task_id = Column(Integer, primary_key=True)
    assignee_id = Column(Integer, nullable=False)
    # probably don't need this
    #project_id = Column(Integer, ForeignKey("projects.project_id"))