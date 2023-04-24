from datetime import datetime, timedelta

from jose import jwt, JWTError

from app.shared.domain.errors.invalid_credentials import InvalidCredentials
from app.shared.domain.services.jwt_service import JwtService
from app.shared.domain.token_data import TokenData
from config import JwtConfig


class JwtServiceJOSE(JwtService):
    def __init__(self) -> None:
        super().__init__()
        config = JwtConfig()
        self._algorithm = config.algorithm
        self._secret = config.secret
        self._expiration_minutes = config.expiration_minutes

    def create_access_token(self, data: dict, expires_delta: timedelta | None = None) -> str:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=self._expiration_minutes)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self._secret, algorithm=self._algorithm)
        return encoded_jwt

    def decode_access_token(self, token: str) -> TokenData:
        try:
            payload = jwt.decode(token, self._secret, algorithms=[self._algorithm])
            sub: str = payload.get("sub")
            if sub is None:
                raise InvalidCredentials("sub is not present")
            token_data = TokenData(username=sub)
        except JWTError as e:
            raise InvalidCredentials(str(e))
        return token_data
