from fastapi import APIRouter
from src.models.cita import Cita 
from src.config.db import conn 
from src.schemas.cita import serializeDict, serializeList
from bson import ObjectId

cita = APIRouter() 

@cita.get('/citas/',tags=["citas"])
async def find_all_cita():
    return serializeList(conn.local.cita.find())

@cita.get('/citas/{id}',tags=["citas"])
async def find_one_cita(id):
    return serializeDict(conn.local.cita.find_one({"_id":ObjectId(id)}))


@cita.post('/citas/',tags=["citas"])
async def create_cita(cita: Cita):
    conn.local.cita.insert_one(dict(cita))
    return serializeList(conn.local.cita.find())

@cita.put('/citas/{id}',tags=["citas"])
async def update_cita(id,cita: Cita):
    conn.local.cita.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(cita)
    })
    return serializeDict(conn.local.cita.find_one({"_id":ObjectId(id)}))

@cita.delete('/citas/{id}',tags=["citas"])
async def delete_cita(id,cita: Cita):
    return serializeDict(conn.local.cita.find_one_and_delete({"_id":ObjectId(id)}))