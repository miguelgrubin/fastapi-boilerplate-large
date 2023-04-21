from app.shared.domain.domain_error import DomainError


class UserNotFollowing(DomainError):
    def __init__(self, unfollowed_user_id: str) -> None:
        super().__init__(
            f"User with id {unfollowed_user_id} can not be unfollowed, becouse is not followed."
        )
        self.unfollowed_user_id = unfollowed_user_id
