from datetime import datetime

from pydantic import BaseModel


class PlaceCommentCreate(BaseModel):
    comment: str
    place_id: int
    user_id: int

class PlaceCommentUpdate(BaseModel):
    comment: str

class PlaceCommentInDB(BaseModel):
    id: int
    comment: str
    place_id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
