from fastapi import FastAPI
from app.blog import (
    ARTICLE_REPOSITORY,
    USER_REPOSITORY,
    USER_CREATOR,
)
from app.blog.types import (
    repositories_type,
    services_type,
    use_cases_type,
)
from app.blog.infrastructure.server.user_routes import user_routes
from app.blog.use_cases.user_creator import UserCreator
from app.blog.infrastructure.storage.user_repository_memory import UserRepositoryMemory
from app.blog.infrastructure.storage.article_repository_memory import ArticleRepositoryMemory
from app.shared import PASSWORD_SERVICE
from app.shared.services.factories import create_password_service


def create_services() -> services_type:
    return {PASSWORD_SERVICE: create_password_service("argon2")}


def create_repositories() -> repositories_type:
    return {
        USER_REPOSITORY: UserRepositoryMemory(),
        ARTICLE_REPOSITORY: ArticleRepositoryMemory(),
    }


def create_use_cases(repositories: repositories_type, services: services_type) -> use_cases_type:
    return {
        USER_CREATOR: UserCreator(
            user_repository=repositories.get(USER_REPOSITORY),
            password_service=services.get(PASSWORD_SERVICE),
        )
    }


def create_server(use_cases: use_cases_type) -> FastAPI:
    blog_app = FastAPI()
    user_routes(blog_app, use_cases)
    return blog_app


def create_blog() -> FastAPI:
    services = create_services()
    repositories = create_repositories()
    use_cases = create_use_cases(repositories, services)
    server = create_server(use_cases)
    return server
