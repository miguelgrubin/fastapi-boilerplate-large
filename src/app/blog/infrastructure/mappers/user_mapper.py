from app.blog.domain.user import User
from app.blog.infrastructure.server.user_dtos import ProfileResponse, UserResponse


class UserMapper:
    @staticmethod
    def to_dto(user: User) -> UserResponse:
        user_profile = ProfileResponse(bio=user.profile.bio, image=user.profile.image)
        return UserResponse(
            id=user.id,
            email=user.email,
            username=user.username,
            profile=user_profile,
            crated_at=user.crated_at,
            updated_at=user.crated_at,
            followers=user.followers,
            following=user.following,
        )
