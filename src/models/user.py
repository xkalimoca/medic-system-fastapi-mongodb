from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name:str
    email:str
    username:str
    password:str