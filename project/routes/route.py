from fastapi import APIRouter

from models.todo import TODO
from config.database import collection_name
from schema.schemas import list_serial, indiviual_serial

from bson import ObjectId

router = APIRouter()

# GET request method
@router.get("/")
async def get_todos():
    todos = list_serial(collection_name.find())
    return todos


@router.post("/")
async def post_todos(todo:TODO):
    collection_name.insert_one(dict(todo))

@router.get("/{id}")
async def detail_todos(id: str):
    todo = collection_name.find_one({"_id": ObjectId(id)})
    return indiviual_serial(todo)


@router.patch("/{id}")
async def update_todos(id: str, todo: TODO):
    collection_name.find_one_and_update({"_id":ObjectId(id)}, {"$set": dict(todo)})