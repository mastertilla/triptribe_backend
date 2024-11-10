from typing import Type

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base: Type = declarative_base()


class PlaceComments(Base):
    __tablename__ = 'table_comments'

    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String, nullable=False)
    place_id = Column(Integer, ForeignKey('places.id'), nullable=False)
    # Need to add link to user
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
