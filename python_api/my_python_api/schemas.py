from pydantic import BaseModel, EmailStr, ValidationError
from datetime import datetime

class UserRegister(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    password: str
    
class UserOut(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
class UserLoginOut(BaseModel):
    email: EmailStr
    
    class Config:
        orm_model = True