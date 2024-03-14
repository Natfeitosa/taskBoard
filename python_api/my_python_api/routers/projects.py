from .. import schemas
from ..config import settings
from fastapi import status, HTTPException, APIRouter, Response
import requests

authServerURL = f'{settings.auth_database_url}'
router = APIRouter(
    tags=['Projects']
)

# Register endpoint
@router.post("/projects", status_code=status.HTTP_201_CREATED, response_model=schemas.Project)
def create_project(newProject: schemas.ProjectCreate):
    # Sends call to auth server
    address = f"{authServerURL}/register"
    response = requests.post(address, json=newUser.model_dump(), headers={"Content-Type": "application/json"})
    
    # Handles response
    if response.status_code == 201:
        return newUser
    else:
        raise HTTPException(status_code=response.status_code, detail="Unexpected Error")