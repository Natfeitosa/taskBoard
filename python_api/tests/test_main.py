from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    res = client.get("/")
    assert res.status_code == 200
    
def test_protected():
    res = client.get("/protected")
    assert res.status_code == 401