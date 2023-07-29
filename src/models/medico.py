from pydantic import BaseModel
from typing import Optional


class Medico(BaseModel):
    name:str
    apellidos:str
    correo:str
    telefono:str
    especialidad:str