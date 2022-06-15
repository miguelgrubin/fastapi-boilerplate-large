from app.shared.domain.events.domain_event import DomainEvent
from app.shared.domain.events.event_types import EventType


class UserFollowed(DomainEvent):
    def __init__(self, user_id: str) -> None:
        super().__init__(EventType.USER_FOLLOWED)
        self.followed_id = user_id
