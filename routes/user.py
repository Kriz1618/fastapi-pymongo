from fastapi import APIRouter

from models.user import User
from config.db import db
from schemas.user import serializeDict, serializeList
from bson import ObjectId

user = APIRouter()
user_collection = db['user']

@user.get('/')
async def find_all_users():
    return serializeList(user_collection.user.find())

@user.get('/{id}')
async def find_one_user(id):
    return serializeDict(user_collection.find_one({"_id":ObjectId(id)}))

@user.post('/')
async def create_user(user: User):
    user_collection.user.insert_one(dict(user))
    return serializeList(user_collection.user.find())

@user.put('/{id}')
async def update_user(id, user: User):
    user_collection.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(user)
    })
    return serializeDict(user_collection.find_one({"_id":ObjectId(id)}))

@user.delete('/{id}')
async def delete_user(id):
    return serializeDict(user_collection.find_one_and_delete({"_id":ObjectId(id)}))