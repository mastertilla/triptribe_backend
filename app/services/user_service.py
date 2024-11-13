from typing import Any

from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserUpdate


class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def get_user(self, db: Session, user_id: int) -> Any:
        return self.repository.get_user(db, user_id)

    def get_user_by_email(self, db: Session, user_email: str) -> Any:
        return self.repository.get_user_by_email(db, user_email)

    def get_all_users(self, db: Session, skip: int = 0, limit: int = 20) -> Any:
        return self.repository.get_all_users(db, skip, limit)

    def create_user(self, db: Session, user: UserCreate) -> Any:
        return self.repository.create_user(db, user)

    def update_user(self, db: Session, user_id: int, user: UserUpdate) -> Any:
        return self.repository.update_user(db, user_id, user)

    def delete_user(self, db: Session, user_id: int) -> Any:
        return self.repository.delete_user(db, user_id)
