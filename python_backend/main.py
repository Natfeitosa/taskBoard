from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
from dotenv import dotenv_values
import psycopg
import time

app = FastAPI()
secrets = dotenv_values(".env")

class Login(BaseModel):
    firstName: str
    lastName: str
    email: str
    password: str

# Connects to the database
while True:
    try:
        conn  = psycopg.connect(
            # TO DO. DONT HARDCODE THIS
            host=secrets['DATABASE_HOST'],
            dbname=secrets['DATABASE_NAME'], 
            user=secrets['DATABASE_USER'],
            password=secrets['DATABASE_PASSWORD'])
        cursor = conn.cursor()
        print("Database connection was successful.\n")
        break
    
    except Exception as error:
        print(f"Database connection failed. Error: {error}\n")
        time.sleep(2)
        
@app.get("/")
def root():
    return {"message" : "Hello World"}
 
@app.get("/login")
def get_login():
    cursor.execute("""SELECT * FROM login""")
    posts2 = cursor.fetchall()
    print(posts2)
    return {"data" : "test successful"}

@app.post("/register", status_code=status.HTTP_201_CREATED)
def post_register(login: Login):
    cursor.execute("""INSERT INTO login (first_name, last_name, email, password) VALUES
                   (%s, %s, %s, %s) RETURNING * """,
                   (login.firstName, login.lastName, login.email, login.password))
    new_register = cursor.fetchone()
    conn.commit()
    return {"data" : new_register}