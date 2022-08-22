# Models
from .UserBase import UserBase

# Pydantic
from pydantic import Field


class UserLogin(UserBase):
    password: str = Field(
        ...,
        max_length=50
    )
