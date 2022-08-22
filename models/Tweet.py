# Models
from .User import User

# Python
from datetime import datetime
from typing import Optional
from uuid import UUID

# Pydantic
from pydantic import BaseModel
from pydantic import Field


class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        max_length=256,
        min_length=1
    )
    created_at: datetime = Field(default=datetime.now())
    update_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)
