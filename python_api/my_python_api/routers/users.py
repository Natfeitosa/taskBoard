from .. import models, schemas, utils
from fastapi import status, HTTPException, Depends, APIRouter, Header, Cookie
from sqlalchemy.orm import Session
from ..database import get_db
from typing import Annotated
import requests
import os

authServerURL = os.environ.get("AUTH_SERVER_URL")
router = APIRouter(
    tags=['Users']
)

# Register endpoint
@router.post("/register", response_model=schemas.UserOut)
def register_user(newUser: schemas.UserRegister):
    # Hash the password
    hashedPassword = utils.hash(newUser.password)
    newUser.password = hashedPassword
    # Send call to auth server
    address = authServerURL + "/register"
    response = requests.post(address)
    if response.status_code == 500:
        
    return new_register

@router.get("/health")
def auth_login(authorization: Annotated[str | None, Header() ] = None):
    header = {"Authorization": f"{authorization}"}
    address = authServerURL + "/Health"
    response = requests.get(address, headers=header)
    if response.status_code == 200:
        return response
    elif response.status_code == 401:
        return "invalid token"
    else:
        return "server died"


@router.get("/login", status_code=status.HTTP_200_OK, response_model=schemas.UserOut)
def test_login(user: schemas.UserBase, db: Session = Depends(get_db)):
    logins = db.query(models.Login).first()
    return {"status": logins}
