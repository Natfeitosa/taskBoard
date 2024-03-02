from pydantic import BaseModel, EmailStr, ValidationError
from datetime import datetime


class UserBase(BaseModel):
    email: EmailStr
    password: str
    
class UserRegister(UserBase):
    firstName: str
    lastName: str
    
class UserOut(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    
    class Config:
        orm_mode = True
