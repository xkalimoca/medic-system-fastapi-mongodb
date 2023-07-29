from typing import Annotated

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel


fake_secret_token = "testunit"

fake_db = {
    "cita": {"id": "1", "medico": "vsabando", "fecha": "23 de agosto", "hora":"10:30 pm", "confirmacion": "SI","codigo": "28963"},
    "cita": {"id": "2", "medico": "dyanez", "fecha": "14 de septiembre", "hora":"8:30 pm", "confirmacion": "SI","codigo": "22015"},
}

app = FastAPI()


class Cita(BaseModel):
    id: str
    medico: str
    fecha: str | None = None
    hora: str
    confirmacion: str
    codigo: str


@app.get("/citas/{cita_id}", response_model=Cita)
async def read_main(cita_id: str, x_token: str | None = Header(default=None)):
    print('x_token', x_token)
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if cita_id not in fake_db:
        raise HTTPException(status_code=404, detail="cita not found")
    
    return fake_db[cita_id]


@app.post("/citas/", response_model=Cita)
async def create_item(cita: Cita, x_token: str | None = Header(default=None)):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if cita.id in fake_db:
        raise HTTPException(status_code=400, detail="cita already exists")

    fake_db[cita.id] = cita
    
    return cita