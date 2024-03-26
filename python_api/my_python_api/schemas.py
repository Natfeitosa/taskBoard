from enum import IntEnum
from typing import List, Optional
from pydantic import BaseModel, EmailStr, ConfigDict, Field, dataclasses
from datetime import date, datetime
 
class State(IntEnum):
    PROPOSED = 0
    IN_PROGRESS = 1
    COMPLETED = 2

class TaskId(BaseModel):
    task_id: int
    
class UserLogin(BaseModel):
    username: EmailStr
    password: str
    
@dataclasses.dataclass(config=ConfigDict(validate_assignment=True, from_attributes=True))
class UserLoginOut(BaseModel):
    username: EmailStr

class UserRegister(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    password: str
    
@dataclasses.dataclass(config=ConfigDict(validate_assignment=True, from_attributes=True))
class UserRegisterOut(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    
    
class ProjectBase(BaseModel):
    last_modified: datetime
    date_created: date
    title: str
    tasks: List[TaskId] = []
    
@dataclasses.dataclass(config=ConfigDict(validate_assignment=True, from_attributes=True))
class ProjectOut(ProjectBase):
    author_id: str
    project_id: int

class ProjectUpdate(BaseModel):
    title: Optional[str] = None
    last_modified: datetime
    email: Optional[EmailStr] = None
    
class TaskBase(BaseModel):
    title: str
    description: str
    date_created: date
    last_modified: datetime
    state: Optional[State] = Field(default=State.PROPOSED)
    
@dataclasses.dataclass(config=ConfigDict(validate_assignment=True, from_attributes=True))
class TaskOut(TaskBase):
    task_id: int
    assignee_id: str
    project_id: int
    state: State

class TaskUpdate(BaseModel):
    last_modified: datetime
    title: Optional[str] = None
    description: Optional[str] = None
    state: Optional[State] = Field(default=State.PROPOSED)
    email: Optional[EmailStr] = None
