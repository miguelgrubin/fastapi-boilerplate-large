from typing import List, NoReturn, Optional

from abc import ABC, abstractmethod

from app.blog.domain.article import Article


class ArticleRepository(ABC):
    """docstring for ArticleRepository"""

    @abstractmethod
    def save(self, article: Article) -> Article:
        raise NotImplementedError

    @abstractmethod
    def delete(self, article_id: str) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    def find_one(self, article_id: str) -> Optional[Article]:
        raise NotImplementedError

    @abstractmethod
    def find_all(self, find_filters, find_order, find_limits) -> List[Article]:
        raise NotImplementedError
