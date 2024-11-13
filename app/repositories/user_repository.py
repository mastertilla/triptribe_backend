from core.logger import logger
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


class UserRepository:
    def get_user(self, db: Session, user_id: int) -> User:
        return db.query(User).filter(User.id == user_id).first()

    def create_user(self, db: Session, user: UserCreate) -> User:
        db_user = User(**user.model_dump())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        logger.info(f"User with id {db_user.id} created")
        return db_user

    def update_user(self, db: Session, user_id: int, user: UserUpdate) -> User:
        db_user = db.query(User).filter(User.id == user_id).first()

        if db_user:
            for key, value in user.model_dump(exclude_unset=True).items():
                setattr(db_user, key, value)
            db.commit()
            db.refresh(db_user)
        else:
            logger.error(f"User with id {user_id} not found")
        return db_user

    def delete_user(self, db: Session, user_id: int) -> None:
        db_user = db.query(User).filter(User.id == user_id).first()
        if db_user:
            db.delete(db_user)
            db.commit()
            logger.info(f"User with id {user_id} deleted")
        else:
            logger.error(f"User with id {user_id} not found")

    def get_user_by_email(self, db: Session, user_email: str) -> User:
        return db.query(User).filter(User.user_email == user_email).first()

    def get_all_users(self, db: Session, skip: int = 0, limit: int = 20) -> list[User]:
        return db.query(User).offset(skip).limit(limit).all()
