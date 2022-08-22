# Models
from models.UserBase import UserBase
from models.UserRegister import UserRegister
from models.User import User
from models.UserLogin import UserLogin
from models.Tweet import Tweet

# Python
from typing import List
import json

# Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import Body

app = FastAPI()

# Path Operations

## Users

### Register a User
@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"]
)
def signup(user: UserRegister = Body(...)):
    """
    Sign Up

    This path operation register a user in the app

    Parameters:
    - Request Body parameter
        - user: UserRegister
    
    Returns a Json with the basic User information: 
    - user_id: UUID
    - email: EmailStr
    - first_name: str
    - last_name: str
    _ birth_day: datetime
    """
    with open("users.json","r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        user_dict = user.dict()
        # A las siguientes variables no se las pasa a json automaticamente
        user_dict["user_id"] = str(user_dict["user_id"]) 
        user_dict["birth_date"] = str(user_dict["birth_date"])
        results.append(user_dict)
        f.seek(0) # Me muevo al primer byte
        f.write(json.dumps(results))
        return user



### Login a User
@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=["Users"]
)
def login():
    pass


### Show All users
@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
    tags=["Users"]
)
def show_all_users():
    pass


### Show a User
@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tags=["Users"]
)
def show_a_user():
    pass


### Delete a User
@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"]
)
def delete_a_user():
    pass


### Update a User
@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a User",
    tags=["Users"]
)
def update_a_user():
    pass


## Tweets


### Show all tweets
@app.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all tweets",
    tags=["Tweets"]
)
def home():
    return {"Twitter API": "Working"}


### Post a tweet
@app.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post tweets",
    tags=["Tweets"]
)
def post():
    pass

### Show a tweet
@app.get(
    path="/tweet/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show tweets",
    tags=["Tweets"]
)
def show_a_tweet():
    pass

### Delete a tweet
@app.delete(
    path="/tweet/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a tweets",
    tags=["Tweets"]
)
def delete_a_tweet():
    pass

### Update a tweet
@app.put(
    path="/tweet/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a tweets",
    tags=["Tweets"]
)
def update_a_tweet():
    pass
