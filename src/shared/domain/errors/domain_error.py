
from src.shared.domain.errors.domain_error_code import DomainErrorCode


class DomainError(Exception):
    code: DomainErrorCode

    def __init__(self, code: DomainErrorCode, message: str) -> None:
        self.code = code
        super().__init__(message)
