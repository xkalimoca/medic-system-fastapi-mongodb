from fastapi import APIRouter
from models.user import User 
from config.db import conn 
from schemas.user import serializeDict, serializeList
from bson import ObjectId
user = APIRouter() 

@user.get('/users/',tags=["users"])
async def find_all_users():
    return serializeList(conn.local.user.find())

@user.get('/users/{id}',tags=["users"])
async def find_one_user(id):
    return serializeDict(conn.local.user.find_one({"_id":ObjectId(id)}))

@user.post('/users/',tags=["users"])
async def create_user(user: User):
    conn.local.user.insert_one(dict(user))
    return serializeList(conn.local.user.find())

@user.put('/users/{id}',tags=["users"])
async def update_user(id,user: User):
    conn.local.user.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(user)
    })
    return serializeDict(conn.local.user.find_one({"_id":ObjectId(id)}))

@user.delete('/users/{id}',tags=["users"])
async def delete_user(id,user: User):
    return serializeDict(conn.local.user.find_one_and_delete({"_id":ObjectId(id)}))