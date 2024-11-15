
from sqlalchemy import Column, DateTime, Integer, String, func

from app.models.app_base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=True)
    user_email = Column(String, nullable=False, index=True)

    country_residence = Column(String, nullable=True)
    city_residence = Column(String, nullable=True)

    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())
