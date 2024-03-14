
from typing import List
from pydantic import BaseModel, EmailStr, ConfigDict
from pydantic.dataclasses import dataclass
from datetime import date, datetime

class UserLogin(BaseModel):
    username: EmailStr
    password: str
    
@dataclass(config=ConfigDict(validate_assignment=True, from_attributes=True))
class UserLoginOut(BaseModel):
    username: EmailStr

class UserRegister(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    password: str
    
@dataclass(config=ConfigDict(validate_assignment=True, from_attributes=True))
class UserRegisterOut(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    
    
class ProjectBase(BaseModel):
    last_modified: datetime
    date_created: date
    title: str
    
@dataclass(config=ConfigDict(validate_assignment=True, from_attributes=True))
class ProjectOut(ProjectBase):
    author_id: str
    project_id: int
    
class TaskBase(BaseModel):
    title: str
    description: str
    date_created: date
    last_modified: datetime