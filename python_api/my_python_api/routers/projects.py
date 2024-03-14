from h11 import Request
from pytest import Session
from .. import schemas, models
from ..config import settings
from ..database import get_db
from fastapi import Depends, status, HTTPException, APIRouter, Request
from sqlalchemy.orm import Session
from typing import List, Optional

authServerURL = f'{settings.auth_database_url}'
router = APIRouter(
    tags=['Projects']
)


# Helper function that validates the existence of a project
def validProject(project_id: int, db: Session) -> bool:
    project = db.query(models.Project).filter(models.Project.project_id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return True

# Create project
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

# Get all projects
@router.get("/projects", response_model=List[schemas.ProjectOut])
def get_projects(db: Session = Depends(get_db), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    projects = db.query(models.Project).filter(models.Project.title.contains(search)).limit(limit).offset(skip).all()
    return projects
