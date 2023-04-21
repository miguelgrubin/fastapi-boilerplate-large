import os
from dataclasses import dataclass, field


@dataclass(frozen=True, kw_only=True)
class JwtConfig:
    secret: str
    algorithm: str
    expiration_minutes: int


def _create_jwt_config() -> JwtConfig:
    return JwtConfig(
        algorithm=os.environ.get("", ""),
        secret=os.environ.get("", ""),
        expiration_minutes=int(os.environ.get("", "30")),
    )


@dataclass(frozen=True, kw_only=True)
class Config:
    jwt: JwtConfig = field(default_factory=_create_jwt_config)
