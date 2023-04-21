from app.shared.domain.domain_error import DomainError


class UserAlreadyExits(DomainError):
    def __init__(self) -> None:
        super().__init__("User with this username or email already exits.")
