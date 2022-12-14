# Models
from doctest import Example
from .UserBase import UserBase

# Pydantic
from pydantic import Field


class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        example="nahuelitoperez123"
    )
