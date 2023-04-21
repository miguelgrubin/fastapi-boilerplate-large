from app.blog.domain.event_types import EventType
from app.shared.domain.events.domain_event import DomainEvent


class UserUnfollowed(DomainEvent):
    def __init__(self, user_id: str) -> None:
        super().__init__(EventType.USER_UNFOLLOWED)
        self.unfollowed_id = user_id
