
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func

from app.models.app_base import Base


class PlaceComment(Base):
    __tablename__ = 'table_comments'

    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String, nullable=False)
    place_id = Column(Integer, ForeignKey('places.id'), nullable=False, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)

    # Need to add link to user
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())
