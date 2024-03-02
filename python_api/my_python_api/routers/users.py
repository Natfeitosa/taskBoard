from .. import models, schemas, utils
from fastapi import status, HTTPException, Depends, APIRouter, Header, Cookie
from sqlalchemy.orm import Session
from ..database import get_db
from typing import Annotated
import requests
import os

os.environ["AUTH_SERVER_URL"] = "http://localhost:5013"
authServerURL = os.environ.get("AUTH_SERVER_URL")
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
def login_user(loginData: schemas.UserLogin):
    # Sends call to auth server
    address = f"{authServerURL}/login"
    response = requests.post(address, json=loginData.model_dump(), headers={"Content-Type": "application/json"})
    
    # Handles response
    if response.status_code == 200:
        token = response.json().get("token")
        return loginData
    else:
        raise HTTPException(status_code=response.status_code, detail="Invalid credentials")
