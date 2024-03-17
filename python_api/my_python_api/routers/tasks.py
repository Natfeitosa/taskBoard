from typing import List, Optional
from python_api.my_python_api import models
from python_api.my_python_api.database import get_db
from .. import schemas
from ..config import settings
from .projects import validProject
from fastapi import Body, Depends, APIRouter, HTTPException, Request
from sqlalchemy.orm import Session

authServerURL = f'{settings.auth_database_url}'
router = APIRouter(
    tags=['Tasks'],
    prefix="/projects/{project_id}"
)

# Create a task under a specified project id
@router.post("/tasks")
def create_task(request: Request, project_id: int, task: schemas.TaskBase = Body(...), db: Session = Depends(get_db)):
    # Check if project exists
    validProject(project_id, db)
   
    # Default to the current user as assignee
    userID = request.cookies.get("user_id")
    # # Default to the proposed state
    # currentState = models.State.PROPOSED
    
    # Create the task and associate it with the project
    task = models.Task(assignee_id=userID, project_id=project_id, **task.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

# Get all tasks
@router.get("/tasks", response_model=List[schemas.TaskOut])
def get_tasks(project_id: int, limit: int = 10, skip: int = 0, search: Optional[str] = "", db: Session = Depends(get_db)):
    tasks = db.query(models.Task).filter(models.Task.project_id == project_id).filter(models.Task.title.contains(search)).limit(limit).offset(skip).all()
    return tasks

# Get one task
@router.get("/tasks/{task_id}", response_model=schemas.TaskOut)
def get_one_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.task_id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# Update a task
@router.put("/tasks/{task_id}", response_model=schemas.TaskOut)
def update_task(request: Request, task_id: int, updateTask: schemas.TaskUpdate, db: Session = Depends(get_db)):
    
    task = db.query(models.Task).filter(models.Task.task_id == task_id).first()
    
    # Reassigns task assignee
    
    #
    if updateProject.email is not None:
        userID = request.cookies.get("user_id")
        if userID == project.author_id:
            newUserInfo = current_userInformation(updateProject.email, db)
            project.author_id = newUserInfo.user_id
        else:
            # to do: add actual stuff here
            print("didnt run")

    # Update project attributes
    for field, value in updateProject.model_dump(exclude_unset=True).items():
        setattr(project, field, value)
    
    db.add(task)
    db.commit()
    return task

# Delete a project
# @router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_project(id: int, db: Session = Depends(get_db)):
#     project = validProjectAndReturn(id, db)
#     db.delete(project)
#     db.commit()
#     return Response(status_code=status.HTTP_204_NO_CONTENT)