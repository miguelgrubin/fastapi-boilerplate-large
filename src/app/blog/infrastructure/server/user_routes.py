from fastapi import FastAPI

from app.blog import USER_CREATOR
from app.blog.types import use_cases_type
from app.blog.infrastructure.server.user_dtos import UserCreationDTO, UserResponse
from app.blog.use_cases.user_creator import UserCreator


def user_routes(blog_app: FastAPI, use_cases: use_cases_type) -> None:
    @blog_app.post("/users", response_model=UserResponse)
    def create_user(payload: UserCreationDTO) -> UserResponse:
        use_case: UserCreator = use_cases.get(USER_CREATOR)
        user = use_case.execute(payload.username, payload.password, payload.email)
        return UserResponse(**user)
