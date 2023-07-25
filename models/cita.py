from pydantic import BaseModel
from typing import Optional
from models.user import User
from models.medico import Medico
from models.consultorio import Consultorio
from models.paciente import Paciente

class Cita(BaseModel):
    medico:str
    fecha:str
    hora:str
    confirmacion:str
    codigo:str