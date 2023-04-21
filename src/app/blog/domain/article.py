""" User Domain """

from typing import TypeVar

from datetime import datetime
from uuid import uuid4

from app.shared.domain.domain_model import DomainModel

Self = TypeVar("Self", bound="Article")


class Article(DomainModel):
    """Article on blog"""

    id: str
    updated_at: datetime
    crated_at: datetime

    @classmethod
    def create(cls: type[Self]) -> Self:
        article = cls()
        article.id = str(uuid4())
        article.updated_at = datetime.now()
        article.crated_at = datetime.now()
        return article

    def update(self) -> None:
        """D"""
