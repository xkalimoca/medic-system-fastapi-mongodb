from typing import Annotated

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel


fake_secret_token = "testunit"

fake_db = {
    "cita": {"id": "1", "medico": "vsabando", "fecha": "23 de agosto", "hora":"10:30 pm", "confirmacion": "SI","codigo": "28963"},
    "paciente": {"id": "3", "name": "Minnie", "apellidos": "Yontararak","correo": "mnicha@gmail.com","telefone": "12456822"},
}

app = FastAPI()


class Item(BaseModel):
    """
    Representación de un item.
    """
    id: str
    title: str
    description: str | None = None


@app.get("/items/{item_id}", response_model=Item)
async def read_main(item_id: str, x_token: str | None = Header(default=None)):
    """
    Busca un item en la base de datos.
    
    :param item_id: ID del item a buscar.
    :param x_token: Token de autenticación.
    """
    print('x_token', x_token)
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return fake_db[item_id]


@app.post("/items/", response_model=Item)
async def create_item(item: Item, x_token: str | None = Header(default=None)):
    """
    Crea un item en la base de datos.
    
    :param item: Item a crear.
    :param x_token: Token de autenticación.
    """
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if item.id in fake_db:
        raise HTTPException(status_code=400, detail="Item already exists")

    fake_db[item.id] = item
    
    return item