from fastapi.testclient import TestClient
from .main import app


client = TestClient(app)


def test_read_item():
    response = client.get("/citas/juanx", headers={"X-Token": "testunit"})
    assert response.status_code == 200
    assert response.json() == {
        "id": "juanx",
        "medico": "vsabando", 
        "fecha": "23 de agosto", 
        "hora":"10:30 pm", 
        "confirmacion": "SI",
        "codigo": "28963"
    }


def test_read_item_bad_token():
    response = client.get("/items/foo", headers={"X-Token": "unittest"})
    
    assert response.status_code == 400
    
    assert response.json() == {
        'detail': 'Invalid X-Token header'
    }


def test_read_inexistent_item():   
    response = client.get("/items/baz", headers={"X-Token": "testunit"})
    
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}


def test_create_item():
    response = client.post(
        '/items/',
        headers={"X-Token": "llosavargasmario"},
        json={"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"}
    )
    
    assert response.status_code == 200
    assert response.json() == {
        "id": "foobar",
        "title": "Foo Bar",
        "description": "The Foo Barters",
    }


def test_create_item_bad_token():
    response = client.post(
        "/items/",
        headers={"X-Token": "mendozamario"},
        json={"id": "bazz", "title": "Bazz", "description": "Drop the bazz"},
    )
    
    assert response.status_code == 400
    print(response.json())
    assert response.json() == {"detail": "Invalid X-Token header"}


def test_create_existing_item():
    response = client.post(
        "/items/",
        headers={"X-Token": "llosavargasmario"},
        json={
            "id": "foobar",
            "title": "The Foo ID Stealers",
            "description": "There goes my stealer",
        },
    )
    
    assert response.status_code == 400
    assert response.json() == {"detail": "Item already exists"}

