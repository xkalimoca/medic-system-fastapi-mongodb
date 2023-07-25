from fastapi import APIRouter
from models.consultorio import Consultorio 
from config.db import conn 
from schemas.consultorio import serializeDict, serializeList
from bson import ObjectId
consultorio = APIRouter() 

@consultorio.get('/consultorio/',tags=["consultorio"])
async def find_all_consultorio():
    return serializeList(conn.local.consultorio.find())

@consultorio.get('/consultorio/{id}',tags=["consultorio"])
async def find_one_consultorio(id):
    return serializeDict(conn.local.consultorio.find_one({"_id":ObjectId(id)}))

@consultorio.post('/consultorio/',tags=["consultorio"])
async def create_consultorio(consultorio: Consultorio):
    conn.local.consultorio.insert_one(dict(consultorio))
    return serializeList(conn.local.consultorio.find())

@consultorio.put('/consultorio/{id}',tags=["consultorio"])
async def update_consultorio(id,consultorio: Consultorio):
    conn.local.consultorio.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(consultorio)
    })
    return serializeDict(conn.local.consultorio.find_one({"_id":ObjectId(id)}))

@consultorio.delete('/consultorio/{id}',tags=["consultorio"])
async def delete_consultorio(id):
    return serializeDict(conn.local.consultorio.find_one_and_delete({"_id":ObjectId(id)}))