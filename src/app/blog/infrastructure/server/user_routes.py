from fastapi import APIRouter
from fastapi.security.oauth2 import OAuth2PasswordBearer

from app.blog import USER_CREATOR, USER_LOGGER
from app.blog.application.use_cases.user_creator import UserCreator
from app.blog.application.use_cases.user_logger import UserLogger
from app.blog.infrastructure.mappers.user_mapper import UserMapper
from app.blog.infrastructure.server.user_dtos import (
    LoginDTO,
    LoginResponse,
    UserCreationDTO,
    UserResponse,
)
from app.blog.infrastructure.server.user_error_handlers import user_error_handler
from app.blog.types import UseCasesType


def user_routes(use_cases: UseCasesType) -> APIRouter:
    user_router = APIRouter(
        prefix="/users",
        tags=["users"],
        responses={404: {"description": "Not found"}},
    )

    @user_router.post("/", response_model=UserResponse)
    @user_error_handler
    def create_user(payload: UserCreationDTO) -> UserResponse:
        use_case: UserCreator = use_cases.get(USER_CREATOR)
        user = use_case.execute(payload.username, payload.password, payload.email)
        return UserMapper.to_dto(user)

    @user_router.post("/login", response_model=UserResponse)
    @user_error_handler
    def login_user(payload: LoginDTO) -> LoginResponse:
        use_case: UserLogger = use_cases.get(USER_LOGGER)
        user = use_case.execute(payload.username, payload.password)
        return UserMapper.to_dto(user)

    return user_router
