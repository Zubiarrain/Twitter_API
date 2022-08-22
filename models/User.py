# Models
from .UserBase import UserBase

# Python
from datetime import date
from typing import Optional

# Pydantic
from pydantic import Field


class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Nahuel"
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Zubiarrain"
    )
    birth_date: Optional[date] = Field(default=None)
