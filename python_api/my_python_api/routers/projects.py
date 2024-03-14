from hmac import new
from h11 import Request
from pytest import Session
from .. import schemas, models
from ..config import settings
from ..database import get_db
from .users import current_user
from fastapi import Depends, status, HTTPException, APIRouter, Response, Request
from sqlalchemy.orm import Session
import requests

authServerURL = f'{settings.auth_database_url}'
router = APIRouter(
    tags=['Projects']
)

# Register endpoint
@router.post("/projects", status_code=status.HTTP_201_CREATED)
def create_project(request: Request, newProject: schemas.ProjectBase, db: Session = Depends(get_db)):
    currentUser = current_user(request, db)
    if not currentUser:
        raise HTTPException(status_code=401, detail="Unauthorized")
    newProject = models.Project(author_id=currentUser.email,**newProject.model_dump())
    db.add(newProject)
    db.commit()
    db.refresh(newProject)
    
    return newProject