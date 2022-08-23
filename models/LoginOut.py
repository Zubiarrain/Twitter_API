# Python
from typing import Optional

# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

class LoginOut(BaseModel):
    email: EmailStr = Field(...)
    message: Optional[str] = Field(default="Login Succesfully")