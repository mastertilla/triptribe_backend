

from sqlalchemy import Column, DateTime, Float, Integer, String, func

from app.models.app_base import Base


class Place(Base):
    __tablename__ = "places"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)

    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)

    rating = Column(Float, nullable=True)

    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())
