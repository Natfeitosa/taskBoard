from typing import List, Optional
from python_api.my_python_api import models
from python_api.my_python_api.database import get_db
from .. import schemas
from ..config import settings
from .projects import validProject
from fastapi import Body, Depends, APIRouter, Request
from sqlalchemy.orm import Session

authServerURL = f'{settings.auth_database_url}'
router = APIRouter(
    tags=['Tasks'],
    prefix="/projects"
)

# Create a task under a specified project id
@router.post("/{project_id}/tasks")
def create_task(request: Request, project_id: int, task: schemas.TaskBase = Body(...), db: Session = Depends(get_db)):
    # Check if project exists
    validProject(project_id, db)
   
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
@router.get("/{project_id}/tasks", response_model=List[schemas.TaskOut])
def get_tasks(project_id: int, limit: int = 10, skip: int = 0, search: Optional[str] = "", db: Session = Depends(get_db)):
    tasks = db.query(models.Task).filter(models.Task.project_id == project_id).filter(models.Task.title.contains(search)).limit(limit).offset(skip).all()
    return tasks
