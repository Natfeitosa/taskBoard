from pydantic import BaseModel, EmailStr, ConfigDict
from pydantic.dataclasses import dataclass

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