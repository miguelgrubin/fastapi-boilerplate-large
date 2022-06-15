""" User Domain """

from typing import List, Optional, TypedDict, TypeVar

from copy import copy
from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4

from app.blog.domain.errors.user_not_following import UserNotFollowing
from app.blog.domain.events.user_created import UserCreated
from app.blog.domain.events.user_followed import UserFollowed
from app.blog.domain.events.user_unfollowed import UserUnfollowed
from app.blog.domain.events.user_updated import UserUpdated
from app.shared.domain.domain_model import DomainModel

Self = TypeVar("Self", bound="User")


class UserUpdateParams(TypedDict):
    email: Optional[str]
    username: Optional[str]
    bio: Optional[str]
    image: Optional[str]


@dataclass
class Profile:
    username: str
    bio: Optional[str] = None
    image: Optional[str] = None


class User(DomainModel):
    """User from blog (writer)"""

    id: str
    email: str
    password_hash: str
    profile: Profile
    following: List[str] = []
    followers: List[str] = []
    updated_at: datetime
    crated_at: datetime

    @classmethod
    def create(cls, username: str, password: str, email: str):
        """Creates a new User."""
        user = User()
        user.id = str(uuid4())
        user.email = email
        user.profile.username = username
        user.password_hash = password
        user.updated_at = datetime.now()
        user.crated_at = datetime.now()

        cls.record(UserCreated())
        return user

    def update(self, payload: UserUpdateParams):
        """Updates email and profile info."""
        origin = copy(self)
        self.email = payload.get("email", self.email)
        self.profile.username = payload.get("username", self.profile.username)
        self.profile.bio = payload.get("bio", self.profile.bio)
        self.profile.image = payload.get("image", self.profile.image)
        self.updated_at = datetime.now()
        self.record(UserUpdated(payload))

    def follow(self, user_id: str):
        self.following.append(user_id)
        self.record(UserFollowed(copy(self), user_id))

    def unfollow(self, user_id: str):
        if user_id not in self.following:
            raise UserNotFollowing(user_id)
        self.following.remove(user_id)
        self.record(UserUnfollowed(copy(self), user_id))
