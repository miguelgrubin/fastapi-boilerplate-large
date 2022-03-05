from src.application.blog.domain.user import User
from src.shared.domain.events.domain_event import DomainEvent
from src.shared.domain.events.event_types import EventType


class UserFollowed(DomainEvent):
    def __init__(self, user: User, user_id: str) -> None:
        super().__init__(EventType.USER_FOLLOWED)
        self.user = user
        self.followed_id = user_id
