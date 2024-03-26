from python_api.my_python_api import models, database
from python_api.my_python_api.routers import users, projects
from .. import schemas, config
from fastapi import Body, Depends, APIRouter, HTTPException, Request, status, Response
from sqlalchemy.orm import Session
from typing import List, Optional

authServerURL = f'{config.settings.auth_database_url}'
router = APIRouter(
    tags=['Tasks'],
    prefix="/projects/{project_id}"
)

# Helper function that validates a task, and returns it
def validTaskAndReturn(task_id: int, db: Session):
    task = db.query(models.Task).filter(models.Task.task_id == task_id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task

# Create a task under a specified project id
@router.post("/tasks")
def create_task(request: Request, project_id: int, task: schemas.TaskBase = Body(...), db: Session = Depends(database.get_db)):
    # validate token
    users.checkAuthorization(request)
    
    # Check if project exists
    projects.validProjectAndReturn(project_id, db)
   
    # Default to the current user as assignee
    userID = request.cookies.get("user_id")

    # Create the task and associate it with the project
    task = models.Task(assignee_id=userID, project_id=project_id, **task.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

# Get all tasks
@router.get("/tasks", response_model=List[schemas.TaskOut])
def get_tasks(project_id: int, limit: int = 10, skip: int = 0, search: Optional[str] = "", db: Session = Depends(database.get_db)):
    tasks = db.query(models.Task).filter(models.Task.project_id == project_id).filter(models.Task.title.contains(search)).limit(limit).offset(skip).all()
    return tasks

# Get one task
@router.get("/tasks/{task_id}", response_model=schemas.TaskOut)
def get_one_task(task_id: int, db: Session = Depends(database.get_db)):
    task = validTaskAndReturn(task_id, db)
    return task

# Update a task
@router.put("/tasks/{task_id}", response_model=schemas.TaskOut)
def update_task(request: Request, task_id: int, updateTask: schemas.TaskUpdate, db: Session = Depends(database.get_db)):
    # validate token
    users.checkAuthorization(request)
    
    task = validTaskAndReturn(task_id, db)
    
    # Reassigns task assignee
    if updateTask.email is not None:
            newUserInfo = users.userInformation(updateTask.email, db)
            task.assignee_id = newUserInfo.user_id
    
    # Update task attributes
    for field, value in updateTask.model_dump(exclude_unset=True).items():
        setattr(task, field, value)
    db.add(task)
    db.commit()
    return task

# Delete a task
@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(request: Request, task_id: int, db: Session = Depends(database.get_db)):
    # validate token
    users.checkAuthorization(request)
    task = validTaskAndReturn(task_id, db)
    db.delete(task)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)