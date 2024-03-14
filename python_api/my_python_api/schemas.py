
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
    projectId: int
    lastModified: datetime
    dateCreated: date
    authorId: int
