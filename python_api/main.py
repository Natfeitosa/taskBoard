from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from sqlalchemy.orm import Session
from my_python_api.database import engine, get_db
from my_python_api import models, schemas, utils


app = FastAPI()
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message" : "Hello World"}

@app.post("/register", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def register_user(user: schemas.UserRegister, db: Session = Depends(get_db)):
    # hash the password
    hashedPassword = utils.hash(user.password)
    user.password = hashedPassword
    
    new_register = models.User(**user.dict())
    db.add(new_register)
    db.commit()
    db.refresh(new_register)
    return new_register

@app.get("/login", status_code=status.HTTP_200_OK, response_model=schemas.UserLoginOut)
def test_login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    logins = db.query(models.Login).first()
    return {"status": logins}
