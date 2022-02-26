from src.shared.domain.errors.domain_error import DomainError
from src.shared.domain.errors.domain_error_code import DomainErrorCode


class ArgumentsError(DomainError):
    def __init__(self, message) -> None:
        super().__init__(code=DomainErrorCode.ARGUMENTS_ERROR, message=message)
