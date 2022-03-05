from typing import List, NoReturn, Optional

from abc import ABC, abstractmethod

from src.application.blog.domain.user import User


class UserRepository(ABC):
    """docstring for UserRepository"""

    @abstractmethod
    def save(self, user: User) -> User:
        raise NotImplementedError

    @abstractmethod
    def delete(self, user: User) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    def find_one(self, find_filters) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def find_all(self, find_filters, find_order, find_limits) -> List[User]:
        raise NotImplementedError
