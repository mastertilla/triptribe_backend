from sqlalchemy import Column, String, Integer, ARRAY, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PlaceComments(Base):
    __tablename__ = "table_comments"

    id = Column(Integer, primary_key=True, index=True)
    comments = Column(ARRAY(String), nullable=False)
    place_id = Column(Integer, ForeignKey('places.id'), nullable=False)