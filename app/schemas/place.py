from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class PlaceCreate(BaseModel):
    name: str
    longitude: float
    latitude: float
    city: str
    country: str
    rating: Optional[float] = 0.0

class PlaceUpdate(BaseModel):
    name: Optional[str]
    rating: Optional[str]

class PlaceInDB(BaseModel):
    id: int
    name: str
    longitude: float
    latitude: float
    city: str
    country: str
    rating: Optional[float] = 0.0
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
