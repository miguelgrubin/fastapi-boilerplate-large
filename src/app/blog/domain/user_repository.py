from typing import List, Optional

from abc import ABC, abstractmethod

from app.blog.domain.user import User


class UserRepository(ABC):
    """docstring for UserRepository"""

    @abstractmethod
    def save(self, user: User) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, user_id: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def find_one(self, user_id: str) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def find_one_by_username(self, username: str) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def find_one_by_email_or_username(self, email: str, username: str) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def find_all(self, find_filters, find_order, find_limits) -> List[User]:
        raise NotImplementedError
