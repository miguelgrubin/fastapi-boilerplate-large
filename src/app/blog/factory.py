from fastapi import FastAPI

from app.blog import ARTICLE_REPOSITORY, USER_CREATOR, USER_LOGGER, USER_REPOSITORY
from app.blog.application.use_cases.user_creator import UserCreator
from app.blog.application.use_cases.user_logger import UserLogger
from app.blog.infrastructure.server.user_routes import user_routes
from app.blog.infrastructure.storage.article_repository_memory import ArticleRepositoryMemory
from app.blog.infrastructure.storage.user_repository_memory import UserRepositoryMemory
from app.blog.types import RepositoriesType, ServicesType, UseCasesType
from app.shared import PASSWORD_SERVICE
from app.shared.factory import create_password_service


def create_services() -> ServicesType:
    return {PASSWORD_SERVICE: create_password_service("argon2")}


def create_repositories() -> RepositoriesType:
    return {
        USER_REPOSITORY: UserRepositoryMemory(),
        ARTICLE_REPOSITORY: ArticleRepositoryMemory(),
    }


def create_use_cases(repositories: RepositoriesType, services: ServicesType) -> UseCasesType:
    return {
        USER_CREATOR: UserCreator(
            user_repository=repositories.get(USER_REPOSITORY),
            password_service=services.get(PASSWORD_SERVICE),
        ),
        USER_LOGGER: UserLogger(
            user_repository=repositories.get(USER_REPOSITORY),
            password_service=services.get(PASSWORD_SERVICE),
        ),
    }


def create_blog_server(app_router: FastAPI) -> FastAPI:
    services = create_services()
    repositories = create_repositories()
    use_cases = create_use_cases(repositories, services)
    app_router.include_router(user_routes(use_cases), prefix="/v1")

    return app_router
