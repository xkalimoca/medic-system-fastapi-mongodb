from fastapi.testclient import TestClient
from main import app
from bson.objectid import ObjectId

client = TestClient(app)

def test_create_user():
    # Create a new user
    response = client.post(
        "/users/",
        json={
            "_id": ObjectId("64bed4bf3c8a59fd9439b6d1"),
            "name": "juan",
            "email": "juanx@gmail.com",
            "username": "juanx",
            "password": "1234"
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "_id": str(ObjectId("64bed4bf3c8a59fd9439b6d1")),
        "name": "juan",
        "email": "juanx@gmail.com",
        "username": "juanx",
        "password": "1234"
    }

def test_read_user():
    # Read a user
    response = client.get("/users/64bed4bf3c8a59fd9439b6d1")
    assert response.status_code == 200
    assert response.json() == {
        "_id": str(ObjectId("64bed4bf3c8a59fd9439b6d1")),
        "name": "juan",
        "email": "juanx@gmail.com",
        "username": "juanx",
        "password": "1234"
    }

def test_update_user():
    # Update a user
    response = client.put(
        "/users/64bed4bf3c8a59fd9439b6d1",
        json={
            "_id": ObjectId("64bed4bf3c8a59fd9439b6d1"),
            "name": "juan updated",
            "email": "juanx_updated@gmail.com",
            "username": "juanx_updated",
            "password": "12345"
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "_id": str(ObjectId("64bed4bf3c8a59fd9439b6d1")),
        "name": "juan updated",
        "email": "juanx_updated@gmail.com",
        "username": "juanx_updated",
        "password": "12345"
    }

def test_delete_user():
    # Delete a user
    response = client.delete("/users/64bed4bf3c8a59fd9439b6d1")
    assert response.status_code == 200


