from hmac import new
from pytest import Session
from .. import schemas, models
from ..config import settings
from ..database import get_db
from fastapi import Depends, status, HTTPException, APIRouter, Response
from sqlalchemy.orm import Session
import requests

authServerURL = f'{settings.auth_database_url}'
router = APIRouter(
    tags=['Projects']
)

# Register endpoint
@router.post("/projects", status_code=status.HTTP_201_CREATED)
def create_project(newProject: schemas.ProjectBase, db: Session = Depends(get_db)):
    newProject = models.Project(**newProject.model_dump())
    db.add(newProject)
    db.commit()
    db.refresh(newProject)
    
    return newProject