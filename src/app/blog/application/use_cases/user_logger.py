from app.blog.domain.errors.login_error import LoginError
from app.blog.domain.user_repository import UserRepository
from app.shared.domain.services.password_service import PasswordService


class UserLogger:
    def __init__(self, user_repository: UserRepository, password_service: PasswordService) -> None:
        self.user_repository = user_repository
        self.password_service = password_service

    def execute(self, username: str, password: str):
        user = self.user_repository.find_one_by_username(username)
        if not user or not self.password_service.check(password, user.password_hash):
            raise LoginError()
        return user
