from fastapi.testclient import TestClient
from fastapi import status
from .index import app

client = TestClient(app)

def test_index_returns_correct():
    response = client.get('/')

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message":"Hello World"}
