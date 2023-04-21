from app.shared.domain.domain_error import DomainError


class ArticleNotFound(DomainError):
    def __init__(self, article_id: str) -> None:
        super().__init__(f"Article with ID {article_id} not found.")
        self.article_id = article_id
