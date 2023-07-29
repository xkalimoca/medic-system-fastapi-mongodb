from fastapi import APIRouter
from src.models.paciente import Paciente 
from config.db import conn 
from schemas.paciente import serializeDict, serializeList
from bson import ObjectId
paciente = APIRouter() 

@paciente.get('/pacientes/',tags=["pacientes"])
async def find_all_paciente():
    return serializeList(conn.local.paciente.find())

@paciente.get('/pacientes/{id}',tags=["pacientes"])
async def find_one_paciente(id):
    return serializeDict(conn.local.paciente.find_one({"_id":ObjectId(id)}))

@paciente.post('/pacientes/',tags=["pacientes"])
async def create_paciente(paciente: Paciente):
    conn.local.paciente.insert_one(dict(paciente))
    return serializeList(conn.local.paciente.find())

@paciente.put('/pacientes/{id}',tags=["pacientes"])
async def update_paciente(id,paciente: Paciente):
    conn.local.paciente.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(paciente)
    })
    return serializeDict(conn.local.paciente.find_one({"_id":ObjectId(id)}))

@paciente.delete('/pacientes/{id}',tags=["pacientes"])
async def delete_paciente(id,paciente: Paciente):
    return serializeDict(conn.local.paciente.find_one_and_delete({"_id":ObjectId(id)}))