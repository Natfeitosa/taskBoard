from hmac import new
from uuid import uuid4
from h11 import Request
from pytest import Session
from .. import schemas, models
from ..config import settings
from ..database import get_db
from fastapi import Depends, status, HTTPException, APIRouter, Response, Request
from sqlalchemy.orm import Session

authServerURL = f'{settings.auth_database_url}'
router = APIRouter(
    tags=['Projects']
)

# Register endpoint
@router.post("/projects", status_code=status.HTTP_201_CREATED)
def create_project(request: Request, newProject: schemas.ProjectBase, db: Session = Depends(get_db)):
    # Retrives the current user via cookie
    userID = request.cookies.get("user_id")
    # Adds onto database
    newProject = models.Project(author_id=userID, **newProject.model_dump())
    db.add(newProject)
    db.commit()
    db.refresh(newProject)
    return newProject