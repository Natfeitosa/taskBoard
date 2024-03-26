from fastapi import FastAPI, Depends, Request, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from .my_python_api.routers import users, projects, tasks
from .my_python_api.database import Base, engine

Base.metadata.create_all(engine)

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(users.router)
app.include_router(projects.router)
app.include_router(tasks.router)


def getTokenFromCookie(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid access token")
    return token

@app.get("/")
async def root():
    return {"Welcome to the home page"}

# DEV ONLY. 
@app.get("/token")
def return_token(request: Request):
    token = request.cookies.get("access_token")
    userID = request.cookies.get("user_id")
    return f"Current user is: {userID}, your token is: {token}"
