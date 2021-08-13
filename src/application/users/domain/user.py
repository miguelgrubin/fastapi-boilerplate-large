""" User Domain """

from src.shared.domain.hex.aggregate_root import AggregateRoot
from src.shared.domain.value_objects.datetime_wrapper import DatetimeWrapper
from src.shared.domain.value_objects.domain_id import DomainId

from .value_objects.email_address import EmailAddress
from .value_objects.full_name import FullName
from .value_objects.password_hash import PasswordHash


class User(AggregateRoot):
    """ Das """
    domain_id: DomainId
    full_name: FullName
    email: EmailAddress
    password: PasswordHash
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
