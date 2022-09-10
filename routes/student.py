from fastapi import APIRouter
from models.student import Student
from config.database import connection
from schemas.student import list_of_students
student_router = APIRouter()


@student_router.get("/students")
async def get_all_students():
    return list_of_students(connection.local.student.find())


@student_router.post("/student")
async def create_student(st: Student):
    connection.local.student.insert_one(dict(st))
    return list_of_students(connection.local.student.find())
