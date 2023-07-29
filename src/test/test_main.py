from fastapi.testclient import TestClient
from .main import app


client = TestClient(app)


def test_read_cita():
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


def test_read_cita_bad_token():
    response = client.get("/cita/juanx", headers={"X-Token": "unittest"})
    
    assert response.status_code == 400
    
    assert response.json() == {
        'detail': 'Invalid X-Token header'
    }


def test_read_inexistent_cita():   
    response = client.get("/cita/robertog", headers={"X-Token": "testunit"})
    
    assert response.status_code == 404
    assert response.json() == {"detail": "Cita not found"}


def test_create_cita():
    response = client.post(
        '/citas/',
        headers={"X-Token": "testunit"},
        json={"id": "tatianat", "medico": "atorres", "fecha": "02 de julio", "hora":"12:00 pm", "confirmacion": "SI","codigo": "78416"}
    )
    
    assert response.status_code == 200
    assert response.json() == {
        "id": "tatianat", 
        "medico": "atorres", 
        "fecha": "02 de julio", 
        "hora":"12:00 pm", 
        "confirmacion": "SI",
        "codigo": "78416"
    }


def test_create_cita_bad_token():
    response = client.post(
        "/citas/",
        headers={"X-Token": "unittest"},
        json={"id": "gmoran", "medico": "atorres", "fecha": "03 de julio", "hora":"11:00 pm", "confirmacion": "SI","codigo": "25798"},
    )
    
    assert response.status_code == 400
    print(response.json())
    assert response.json() == {"detail": "Invalid X-Token header"}


def test_create_existing_cita():
    response = client.post(
        "/citas/",
        headers={"X-Token": "testunit"},
        json={
        "id": "tatianat", 
        "medico": "atorres", 
        "fecha": "02 de julio", 
        "hora":"12:00 pm", 
        "confirmacion": "SI",
        "codigo": "78416",
        },
    )
    
    assert response.status_code == 400
    assert response.json() == {"detail": "Cita already exists"}

