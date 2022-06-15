from app.shared.domain.events.domain_event import DomainEvent
from app.shared.domain.events.event_types import EventType


class UserUpdated(DomainEvent):
    def __init__(self, payload) -> None:
        super().__init__(EventType.USER_UPDATED)
        self.payload = payload
