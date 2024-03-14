from typing import List, Optional
from python_api.my_python_api import models
from python_api.my_python_api.database import get_db
from python_api.my_python_api.models import Project, Task
from .. import schemas
from ..config import settings
from fastapi import Body, Depends, status, HTTPException, APIRouter, Response, Request
from sqlalchemy.orm import Session
import requests

authServerURL = f'{settings.auth_database_url}'
router = APIRouter(
    tags=['Tasks'],
    prefix="/projects"
)

# Create a task under a specified project id
@router.post("/{project_id}/tasks")
def create_task(request: Request, project_id: int, task: schemas.TaskBase = Body(...), db: Session = Depends(get_db)):
    # Check if project exists
    project = db.query(Project).filter(Project.project_id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    # Default to the current user as assignee
    userID = request.cookies.get("user_id")
    # Default to the proposed state
    currentState = models.State.PROPOSED
    
    # Create the task and associate it with the project
    task = models.Task(assignee_id=userID, project_id=project_id, status=currentState, **task.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

# Get all tasks
@router.get("/{project_id}/tasks", response_model=List[schemas.ProjectOut])
def get_projects(db: Session = Depends(get_db), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    projects = db.query(models.Project).filter(models.Project.title.contains(search)).limit(limit).offset(skip).all()
    return projects