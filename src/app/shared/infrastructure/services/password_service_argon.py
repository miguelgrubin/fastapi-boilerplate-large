from passlib.hash import argon2

from app.shared.domain.services.password_service import PasswordService


class PasswordServiceArgon(PasswordService):
    def hash(self, password: str) -> str:
        return str(argon2.hash(password))

    def check(self, password: str, password_hash: str) -> bool:
        return bool(argon2.verify(password, password_hash))
