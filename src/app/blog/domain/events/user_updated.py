from src.application.blog.domain.user import User, UserUpdateParams
from src.shared.domain.events.domain_event import DomainEvent
from src.shared.domain.events.event_types import EventType


class UserUpdated(DomainEvent):
    def __init__(self, user: User, payload: UserUpdateParams) -> None:
        super().__init__(EventType.USER_UPDATED)
        self.user = user
        self.payload = payload
