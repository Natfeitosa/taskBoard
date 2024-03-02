from fastapi import FastAPI
from .my_python_api.database import engine
from .my_python_api.models import Base
from .my_python_api.routers import users
import os

os.environ["AUTH_SERVER_URL"] = "http://localhost:5013"

app = FastAPI()
app.include_router(users.router)
Base.metadata.create_all(bind=engine)
authServerURL = os.environ.get("AUTH_SERVER_URL")

@app.get("/")
async def root():
    return {"Welcome to the home page"}
