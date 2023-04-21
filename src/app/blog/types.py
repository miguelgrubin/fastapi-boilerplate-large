from typing import Any, Dict, Union

from app.blog.application.use_cases.user_creator import UserCreator
from app.blog.application.use_cases.user_logger import UserLogger
from app.blog.domain.article_repository import ArticleRepository
from app.blog.domain.user_repository import UserRepository
from app.shared.domain.services.password_service import PasswordService

ServicesType = Dict[str, PasswordService]
RepositoriesType = Dict[str, Union[UserRepository, ArticleRepository]]
UseCasesType = Dict[str, Union[UserCreator, UserLogger, Any]]
