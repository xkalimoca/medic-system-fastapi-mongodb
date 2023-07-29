# tests/test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_docs_url():
    response = client.get("/api/v2/docs")
    assert response.status_code == 200

def test_redoc_url():
    response = client.get("/api/v2/redocs")
    assert response.status_code == 200
