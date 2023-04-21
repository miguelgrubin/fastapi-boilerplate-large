from app.shared.domain.domain_error import DomainError


class InvalidCredentials(DomainError):
    def __init__(self, message: str) -> None:
        super().__init__(f"Invalid JWT: {message}")
