from pydantic import BaseModel, EmailStr

class UserLogin(BaseModel):
    username: EmailStr
    password: str
    
class UserLoginOut(BaseModel):
    username: EmailStr
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    class Config:
        orm_mode = True

class UserRegister(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    password: str
    
class UserRegisterOut(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    
    class Config:
        orm_mode = True
