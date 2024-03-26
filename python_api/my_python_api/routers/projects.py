from pytest import Session
from python_api.my_python_api.routers import users
from .. import schemas, models, config, database
from fastapi import Depends, Response, status, HTTPException, APIRouter, Request
from sqlalchemy.orm import Session
from typing import List, Optional

authServerURL = f'{config.settings.auth_database_url}'
router = APIRouter(
    tags=['Projects'],
    prefix="/projects"
)

# Helper function that validates a project, and returns it
def validProjectAndReturn(project_id: int, db: Session):
    project = db.query(models.Project).filter(models.Project.project_id == project_id).first()
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    return project

# Create project
@router.post("", status_code=status.HTTP_201_CREATED)
def create_project(request: Request, newProject: schemas.ProjectBase, db: Session = Depends(database.get_db)):
    # Retrives the current user via cookie
    userID = request.cookies.get("user_id")
    # Adds onto database
    newProject = models.Project(author_id=userID, **newProject.model_dump())
    db.add(newProject)
    db.commit()
    db.refresh(newProject)
    return newProject

# Get all projects
@router.get("", response_model=List[schemas.ProjectOut])
def get_all_projects(db: Session = Depends(database.get_db), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    projects = db.query(models.Project).filter(models.Project.title.contains(search)).limit(limit).offset(skip).all()
    return projects

# Get specific project
@router.get("/{id}", response_model=schemas.ProjectOut)
def get_one_project(id: int, db: Session = Depends(database.get_db)):
    project = validProjectAndReturn(id, db)
    return project

# Update a project
@router.put("/{id}", response_model=schemas.ProjectOut)
def update_project(request: Request, id: int, updateProject: schemas.ProjectUpdate, db: Session = Depends(database.get_db)):
    project = validProjectAndReturn(id, db)

    # Reassigns project owner
    if updateProject.email is not None:
        userID = request.cookies.get("user_id")
        # Checks if project owner is current user
        if userID == project.author_id:
            newUserInfo = users.userInformation(updateProject.email, db)
            project.author_id = newUserInfo.user_id
        else:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User must own project")

    # Update project attributes
    for field, value in updateProject.model_dump(exclude_unset=True).items():
        setattr(project, field, value)
    
    db.add(project)
    db.commit()
    return project

# Delete a project
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(request: Request, id: int, db: Session = Depends(database.get_db)):
    project = validProjectAndReturn(id, db)
    
    # Check if current user is project owner
    userID = request.cookies.get("user_id")
    if userID != project.author_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")
    
    db.delete(project)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)