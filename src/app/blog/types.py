from typing import Any, Dict, Union

from app.blog.domain.article_repository import ArticleRepository
from app.blog.domain.user_repository import UserRepository
from app.blog.use_cases.user_creator import UserCreator
from app.shared.services.domain.password_service import PasswordService

services_type = Dict[str, PasswordService]
repositories_type = Dict[str, Union[UserRepository, ArticleRepository]]
use_cases_type = Dict[str, Union[UserCreator, Any]]
