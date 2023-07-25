from fastapi import APIRouter
from models.medico import Medico 
from config.db import conn 
from schemas.medico import serializeDict, serializeList
from bson import ObjectId
medico = APIRouter() 

@medico.get('/medicos/',tags=["medicos"])
async def find_all_medico():
    return serializeList(conn.local.medico.find())

@medico.get('/medicos/{id}',tags=["medicos"])
async def find_one_medico(id):
    return serializeDict(conn.local.medico.find_one({"_id":ObjectId(id)}))

@medico.post('/medicos/',tags=["medicos"])
async def create_medico(medico: Medico):
    conn.local.medico.insert_one(dict(medico))
    return serializeList(conn.local.medico.find())

@medico.put('/medicos/{id}',tags=["medicos"])
async def update_medico(id,medico: Medico):
    conn.local.medico.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(medico)
    })
    return serializeDict(conn.local.medico.find_one({"_id":ObjectId(id)}))

@medico.delete('/medicos/{id}',tags=["medicos"])
async def delete_medico(id,medico: Medico):
    return serializeDict(conn.local.medico.find_one_and_delete({"_id":ObjectId(id)}))