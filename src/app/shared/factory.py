from app.shared.domain.services.password_service import PasswordService
from app.shared.infrastructure.services.password_service_argon import PasswordServiceArgon
from app.shared.infrastructure.services.password_service_fake import PasswordServiceFake


def create_password_service(keyword: str) -> PasswordService:
    if keyword == "argon2":
        return PasswordServiceArgon()
    return PasswordServiceFake()
