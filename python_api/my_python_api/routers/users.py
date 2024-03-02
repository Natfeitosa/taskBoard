from .. import schemas
from ..config import settings
from fastapi import status, HTTPException, APIRouter, Response
import requests
import os


authServerURL = f'{settings.auth_database_url}'
router = APIRouter(
    tags=['Users']
)

# Register endpoint
@router.post("/register", status_code=status.HTTP_200_OK, response_model=schemas.UserRegisterOut)
def register_user(newUser: schemas.UserRegister):
    # Sends call to auth server
    address = f"{authServerURL}/register"
    response = requests.post(address, json=newUser.model_dump(), headers={"Content-Type": "application/json"})
    
    # Handles response
    if response.status_code == 200:
        return newUser
    else:
        raise HTTPException(status_code=response.status_code, detail="Unexpected Error")

# Login endpoint
@router.post("/login", status_code=status.HTTP_200_OK, response_model=schemas.UserLoginOut)
def login_user(loginData: schemas.UserLogin, responseCookie: Response):
    # Sends call to auth server
    address = f"{authServerURL}/login"
    response = requests.post(address, json=loginData.model_dump(), headers={"Content-Type": "application/json"})
    
    # Handles response
    if response.status_code == 200:
        tokens = response.json()
        accessToken = tokens.get("accessToken")
        # TO DO
        refreshToken = tokens.get("refreshToken")
        # Sets token in a cookie
        responseCookie.set_cookie(key="access_token", value=accessToken, httponly=True, secure=True, samesite='lax')
        return loginData
    else:
        raise HTTPException(status_code=response.status_code, detail="Invalid credentials")
