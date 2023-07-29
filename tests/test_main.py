from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_item():
    response = client.get("/users/{id}",headers={"X-Token":"64bed4bf3c8a59fd9439b6d1"})

    assert response.status_code == 200

    assert response.json()=={
        'name': 'juan',
        'email':'juanx@gmail.com',
        'username':'juanx',
        'password':'1234'
    }

    