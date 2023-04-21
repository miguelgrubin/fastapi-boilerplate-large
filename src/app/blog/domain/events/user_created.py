from app.blog.domain.event_types import EventType
from app.shared.domain.events.domain_event import DomainEvent


class UserCreated(DomainEvent):
    def __init__(self) -> None:
        super().__init__(EventType.USER_CREATED)
