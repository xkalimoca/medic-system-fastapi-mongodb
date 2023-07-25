from pydantic import BaseModel
from typing import Optional

class Paciente(BaseModel):
    name:str
    apellidos:str
    correo:str
    telefono:str