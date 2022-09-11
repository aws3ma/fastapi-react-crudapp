from fastapi import FastAPI
from routes.student import student_router
from fastapi.middleware.cors import CORSMiddleware
client_apps = ["http://localhost:3000"]
app = FastAPI()
app.include_router(student_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=client_apps,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
