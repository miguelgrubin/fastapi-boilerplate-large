from typing import List, NoReturn, Optional

from abc import ABC, abstractmethod

from src.app.blog.domain.article import Article


class ArticleRepository(ABC):
    """docstring for UserRepository"""

    @abstractmethod
    def save(self, user: Article) -> Article:
        raise NotImplementedError

    @abstractmethod
    def delete(self, user: Article) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    def find_one(self, find_filters) -> Optional[Article]:
        raise NotImplementedError

    @abstractmethod
    def find_all(self, find_filters, find_order, find_limits) -> List[Article]:
        raise NotImplementedError
