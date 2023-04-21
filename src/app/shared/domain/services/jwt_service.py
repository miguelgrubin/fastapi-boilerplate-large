from abc import ABC, abstractmethod
from datetime import timedelta

from app.shared.domain.token_data import TokenData


class JwtService(ABC):
    @abstractmethod
    def create_access_token(self, data: dict, expires_delta: timedelta | None = None) -> str:
        pass

    @abstractmethod
    def decode_access_token(self, token: str) -> TokenData:
        pass
