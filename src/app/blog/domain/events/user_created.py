from src.application.blog.domain.user import User
from src.shared.domain.events.domain_event import DomainEvent
from src.shared.domain.events.event_types import EventType


class UserCreated(DomainEvent):
    def __init__(self, user: User) -> None:
        super().__init__(EventType.USER_CREATED)
        self.user = user
