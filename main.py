# Models
from models.UserBase import UserBase
from models.User import User
from models.UserLogin import UserLogin

# Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"Twitter API": "Working"}
