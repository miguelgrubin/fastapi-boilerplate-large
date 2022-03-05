""" User Domain """

from datetime import datetime

from src.shared.domain.domain_model import DomainModel


class Article(DomainModel):
    """Das"""

    updated_at: datetime
    crated_at: datetime

    def create(self):
        """D"""

    def update(self):
        """D"""
