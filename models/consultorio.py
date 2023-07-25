from pydantic import BaseModel
from typing import Optional

class Consultorio(BaseModel):
    name:str
    direccion:str
    telefono:str