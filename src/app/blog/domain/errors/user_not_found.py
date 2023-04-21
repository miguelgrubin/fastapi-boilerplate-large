from app.shared.domain.domain_error import DomainError


class UserNotFound(DomainError):
    def __init__(self, user_id: str) -> None:
        super().__init__(f"User with ID {user_id} not found.")
        self.user_id = user_id
