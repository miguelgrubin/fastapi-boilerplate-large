from app.shared.domain.events.domain_event import DomainEvent
from app.shared.domain.events.event_types import EventType


class UserCreated(DomainEvent):
    def __init__(self) -> None:
        super().__init__(EventType.USER_CREATED)
