from typing import List, NoReturn, Optional

from abc import ABC, abstractmethod

from src.application.users.domain.user import User
from src.shared.domain.value_objects.domain_id import DomainId


class UserRepository(ABC):
    """docstring for UserRepository"""

    @abstractmethod
    def create(self, user: User) -> User:
        raise NotImplementedError

    @abstractmethod
    def update(self, user_id: DomainId, user: User) -> User:
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
