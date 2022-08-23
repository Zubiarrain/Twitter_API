# Models
from uuid import UUID
from models.UserRegister import UserRegister
from models.User import User
from models.Tweet import Tweet
from models.LoginOut import LoginOut

# Python
from typing import List
import json

# Pydantic
from pydantic import EmailStr

# FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import HTTPException
from fastapi import Body, Form, Path, Query

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
    response_model=LoginOut,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=["Users"]
)
def login(
    email: EmailStr = Form(...),
    password: str = Form(...)
    ):
    """
    Login

    This path operation Login a user in the app

    Parameters:
    - Form parameter
        - email: str
        - password: str
    
    Returns a Json with the basic User information: 
    - user_id: UUID
    - email: EmailStr
    - first_name: str
    - last_name: str
    _ birth_day: datetime
    """
    with open("users.json","r", encoding="utf-8") as f:
        results = json.loads(f.read())
        for user in results:
            if user["email"] == email and user["password"] == password:
                return LoginOut(email=user["email"])


### Show All users
@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
    tags=["Users"]
)
def show_all_users():
    """
    Show All Users

    This path operation shows all users in the app

    Parameters: none

    Returns a json list with all users in thr app, with the following key:
    - email: EmailStr
    """
    with open("users.json","r",encoding="utf-8") as f:
        results = json.loads(f.read())
        return results


### Show a User
@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tags=["Users"]
)
def show_a_user(
    user_id: UUID = Path(
        ...,
        title="User ID",
        description=" Thi is the user identifier",
        example="3fa85f64-5717-4562-b3fc-2c963f66afa6"
    )
):
    """
    Show a user

    This path operation shows a user in the app

    Parameters:
    - Path parameter
        - user_id: int --> user identifier

    Returns a json list with a user in the app, with the following keys:
    - user_id: UUID
    - email: EmailStr
    - first_name: str
    - last_name: str
    - birth_day: datetime
    """
    with open("users.json","r",encoding="utf-8") as f:
        results = json.loads(f.read())
        for user in results:
            if user["user_id"] == str(user_id):
                return user
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="¡This person doesn't exist!"
        )


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
    """
    Home

    This path operation show all tweet in the app

    Parameters: none
    
    Returns a Json with all the tweets information: 
    - tweet_id: UUID
    - content: str
    - created_at: datetime
    - updated_at: Optional[datetime]
    - by: User
    """
    with open("tweets.json","r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        return results


### Post a tweet
@app.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post tweets",
    tags=["Tweets"]
)
def post(tweet: Tweet = Body(...)):
    """
    Post a Tweet

    This path operation post a tweet in the app

    Parameters:
    - Request Body parameter
        - tweet: Tweet
    
    Returns a Json with the basic tweet information: 
    - tweet_id: UUID
    - content: str
    - created_at: datetime
    - updated_at: Optional[datetime]
    - by: User
    """
    with open("tweets.json","r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        tweet_dict = tweet.dict()
        # A las siguientes variables no se las pasa a json automaticamente
        tweet_dict["tweet_id"] = str(tweet_dict["tweet_id"])
        tweet_dict["created_at"] = str(tweet_dict["created_at"])
        if tweet_dict["updated_at"]:
            tweet_dict["updated_at"] = str(tweet_dict["updated_at"])
        tweet_dict["by"]["user_id"] = str(tweet_dict["by"]["user_id"])
        tweet_dict["by"]["birth_date"] = str(tweet_dict["by"]["birth_date"])
        results.append(tweet_dict)
        f.seek(0) # Me muevo al primer byte
        f.write(json.dumps(results))
        return tweet

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
