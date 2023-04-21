from app.shared.domain.domain_error import DomainError


class LoginError(DomainError):
    def __init__(self) -> None:
        super().__init__("Incorrect username or password")
