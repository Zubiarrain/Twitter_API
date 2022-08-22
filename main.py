# Models
from models.UserBase import UserBase
from models.User import User
from models.UserLogin import UserLogin
from models.Tweet import Tweet

# Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"Twitter API": "Working"}
