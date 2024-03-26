import pytest
from unittest.mock import patch
from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


@pytest.fixture(params=[
    ("nicholas", "string", "nicholas@example.com", "password123"),
    ("carl", "stringer", "carl@example.com", "123password"),
    ("example", "stringist", "example@example.com", "pass123word")
    ])

def register_userData(request):
    return request.param

@pytest.fixture(params=[
    ("nicholas@example.com", "password123",
     "carl@example.com", "123password",
     "example@example.com", "pass123word")
])

def login_userData(request):
    return request.param

@patch("my_python_api.routers.users.requests.post")
def test_register_successful(mock_register, register_userData):
    mock_register.return_value.status_code = 201
    
    newUser = {
        "firstName" : register_userData[0],
        "lastName" : register_userData[1],
        "email" : register_userData[2],
        "password" : register_userData[3]
    }
    
    response = client.post("/register", json=newUser)
    assert response.status_code == 201
    

@patch("my_python_api.routers.users.requests.post")
def test_register_failure_invalidEmail(mock_register, register_userData):
    mock_register.return_value.status_code = 400
    newUser = {
        "firstName" : register_userData[0],
        "lastName" : register_userData[1],
        "email" : 123,
        "password" : register_userData[3]
    }
    response = client.post("/register", json=newUser)
    assert response.status_code == 422
    

@patch("my_python_api.routers.users.requests.post")
def test_login_successful(mock_login, login_userData):
    mock_login.return_value.status_code = 200
    currentUser = {
        "username" : login_userData[0],
        "password" : login_userData[1]
    }
    response = client.post("/login", json=currentUser)
    assert response.status_code == 200
    

@patch("my_python_api.routers.users.requests.post")
def test_login_failure_invalidPassword(mock_login, login_userData):
    mock_login.return_value.status_code = 401
    currentUser = {
        "username" : login_userData[0],
        "password" : "password"
    }
    response = client.post("/login", json=currentUser)
    assert response.status_code == 401
    
