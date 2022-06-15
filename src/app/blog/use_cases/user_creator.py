from app.blog.domain.errors.username_aready_exits import UsernameAlreadyExits
from app.blog.domain.user_repository import UserRepository
from app.blog.domain.user import User
from app.shared.services.domain.password_service import PasswordService


class UserCreator:
    def __init__(self, user_repository: UserRepository, password_service: PasswordService) -> None:
        self.user_repository = user_repository
        self.password_service = password_service

    def execute(self, username: str, password: str, email: str):
        recorded = self.user_repository.find_one_by_email(email)
        if recorded:
            raise UsernameAlreadyExits(username)
        password_hash = self.password_service.hash(password)
        user = User.create(username, password_hash, email)
        self.user_repository.save(user)
        return user
