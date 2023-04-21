from typing import Dict, Union

from app.shared.domain.services.jwt_service import JwtService
from app.shared.domain.services.password_service import PasswordService

ServicesType = Dict[str, Union[PasswordService, JwtService]]
