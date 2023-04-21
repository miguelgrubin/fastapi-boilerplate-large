from typing import List, Optional

from app.blog.domain.user import User
from app.blog.domain.user_repository import UserRepository


class UserRepositoryMemory(UserRepository):
    _users: List[User] = []

    def save(self, user: User) -> None:
        self._users.append(user)

    def delete(self, user_id: str) -> None:
        if user := self.find_one(user_id):
            self._users.remove(user)

    def find_one(self, user_id: str) -> Optional[User]:
        return next(filter(lambda x: (x.id == user_id), self._users), None)

    def find_one_by_username(self, username: str) -> Optional[User]:
        return next(filter(lambda x: (x.username == username), self._users), None)

    def find_one_by_email_or_username(self, email: str, username: str) -> Optional[User]:
        return next(
            filter(lambda x: (x.email == email or x.username == username), self._users), None
        )

    def find_all(self) -> List[User]:
        return self._users.copy()

    def clear(self) -> None:
        self._users = []
