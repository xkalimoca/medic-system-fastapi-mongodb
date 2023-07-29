from pydantic import BaseModel
from typing import Optional

class Cita(BaseModel):
    medico:str
    fecha:str
    hora:str
    confirmacion:str
    codigo:str