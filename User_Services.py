from dataclasses import dataclass
from typing import Optional
import logging

logger = logging.getLogger(__name__)


@dataclass
class User:
    id: int
    username: str
    email: str
    is_active: bool = True


class UserService:
    def __init__(self, db):
        self.db = db

    def get_user(self, user_id: int) -> Optional[User]:
        if not isinstance(user_id, int) or user_id <= 0:
            raise ValueError(f"Invalid user_id: {user_id}")

        user = self.db.query(User).filter(User.id == user_id).first()

        if not user:
            logger.warning(f"User {user_id} not found")
            return None

        return user

    def deactivate_user(self, user_id: int) -> bool:
        user = self.get_user(user_id)

        if not user:
            return False

        user.is_active = False
        self.db.commit()
        logger.info(f"User {user_id} deactivated")
        return True
