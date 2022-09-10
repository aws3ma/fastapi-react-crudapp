from fastapi import APIRouter
from models.student import Student
from config.database import connection
from schemas.student import list_of_students, student_entity
from bson import ObjectId
student_router = APIRouter()


@student_router.get("/students")
async def get_all_students():
    return list_of_students(connection.local.student.find())


@student_router.post("/student")
async def create_student(st: Student):
    connection.local.student.insert_one(dict(st))
    return list_of_students(connection.local.student.find())


@student_router.put("/student/{student_id}")
async def update_student(student_id: str, st: Student):
    connection.local.student.find_one_and_update(
        {"_id": ObjectId(student_id)},
        {"$set": dict(st)}
    )
    return student_entity(connection.local.student.find_one({"_id": ObjectId(student_id)}))


@student_router.get("/student/{student_id}")
async def get_student_by_id(student_id: str):
    return student_entity(connection.local.student.find_one({"_id": ObjectId(student_id)}))


@student_router.delete("/student/{student_id}")
async def delete_student(student_id: str):
    connection.local.student.find_one_and_delete(
        {"_id": ObjectId(student_id)}
    )
    return {"response": "deleted"}
