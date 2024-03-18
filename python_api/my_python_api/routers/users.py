import uuid
from .. import schemas, models, config, database
from fastapi import Request, status, HTTPException, APIRouter, Response, Depends
from sqlalchemy.orm import Session
import requests

authServerURL = f'{config.settings.auth_database_url}'
router = APIRouter(
    tags=['Users']
)

# Register endpoint
@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=schemas.UserRegisterOut)
def register_user(newUser: schemas.UserRegister, db: Session = Depends(database.get_db)):
    # Sends call to auth server
    address = f"{authServerURL}/register"
    response = requests.post(address, json=newUser.model_dump(), headers={"Content-Type": "application/json"})
    
    # Handles response
    if response.status_code == status.HTTP_200_OK:
        # passes user data onto postgres database
        try:
            create_user(newUser.model_dump(exclude={"password"}), db=db)
        except Exception as error:
            print(f"Error creating postgres user: {error}")
        return newUser
    else:
        raise HTTPException(status_code=response.status_code, detail="Unexpected Error")

# Login endpoint
@router.post("/login", status_code=status.HTTP_200_OK, response_model=schemas.UserLoginOut)
def login_user(loginData: schemas.UserLogin, request: Request, responseCookie: Response, db: Session = Depends(database.get_db)):
    # Sends call to auth server
    address = f"{authServerURL}/login"
    response = requests.post(address, json=loginData.model_dump(), headers={"Content-Type": "application/json"})
    
    # Handles response
    if response.status_code == status.HTTP_200_OK:
        # Setup Cookies
        tokens = response.json()
        accessToken = tokens.get("accessToken")
        responseCookie.set_cookie(key="access_token", value=accessToken, httponly=True, secure=True, samesite='lax')
  
        currentUser = userInformation(loginData.username, db)
        responseCookie.set_cookie(key="user_id", value=str(currentUser.user_id), httponly=True, secure=True, samesite='lax')
        return loginData
    else:
        raise HTTPException(status_code=response.status_code, detail="Invalid credentials")

# Create user in postgres database
def create_user(user_data: dict, db: Session = Depends(database.get_db)):
    # Generate a unique ID & add onto user cookie
    unique_id = str(uuid.uuid4())

    # Create user without password and with unique ID
    new_user = models.User(
        user_id=unique_id,
        email=user_data["email"],
        first_name=user_data["firstName"],
        last_name=user_data["lastName"]
    )
    # Add onto database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

# Returns user information via email
def userInformation(userEmail: str, db: Session):
    # Finds the first instance of the user with the provided email
    currentUser = db.query(models.User).filter(models.User.email == userEmail).first()
    if not currentUser:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not Found")
    return currentUser
