from fastapi import FastAPI, Depends, APIRouter, Request, HTTPException, status
from .my_python_api.database import engine
from .my_python_api.models import Base
from .my_python_api.routers import users
import os

app = FastAPI()
app.include_router(users.router)
Base.metadata.create_all(bind=engine)

def getTokenFromCookie(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid access token")
    return token

@app.get("/")
async def root():
    return {"Welcome to the home page"}

@app.get("/protected")
def protected_endpoint(token: str = Depends(getTokenFromCookie)):
    return f"Your token is: {token}"

