from src.application.blog.domain.user import User


class UserNotFollowing(Exception):
    def __init__(self, user: User, unfollowed_user_id: str):
        super().__init__(
            f"User with id {unfollowed_user_id} can not be unfollowed, becouse is not followed."
        )
        self.user = user
