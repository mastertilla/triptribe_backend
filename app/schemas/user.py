from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UserCreate(BaseModel):
    username: Optional[str]
    user_email: str
    country_residence: Optional[str]
    city_residence: Optional[str]

class UserUpdate(BaseModel):
    username: Optional[str]
    user_email: Optional[str]
    country_residence: Optional[str]
    city_residence: Optional[str]

class UserInDB(BaseModel):
    user_id: int
    username: Optional[str]
    user_email: str
    country_residence: Optional[str]
    city_residence: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
