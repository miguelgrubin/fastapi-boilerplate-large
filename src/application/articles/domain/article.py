""" User Domain """

from src.shared.domain.hex.aggregate_root import AggregateRoot
from src.shared.domain.value_objects.datetime_wrapper import DatetimeWrapper


class Article(AggregateRoot):
    """Das"""

    updated_at: DatetimeWrapper
    crated_at: DatetimeWrapper

    """docstring for User"""

    def __init__(self, *arg, **kargs):
        super().__init__(*arg, **kargs)
        self.arg = arg

    def create(self):
        """D"""

    def update(self):
        """D"""
