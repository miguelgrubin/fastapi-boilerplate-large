# mypy: ignore-errors

import functools

from fastapi import HTTPException, status

from app.blog.domain.errors.login_error import LoginError
from app.blog.domain.errors.user_aready_exits import UserAlreadyExits
from app.blog.domain.errors.user_not_following import UserNotFollowing
from app.blog.domain.errors.user_not_found import UserNotFound


def user_error_handler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            response = func(*args, **kwargs)
            return response
        except UserNotFound as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)
        except UserAlreadyExits as e:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=e.message)
        except UserNotFollowing as e:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=e.message)
        except LoginError as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=e.message,
                headers={"WWW-Authenticate": "Bearer"},
            )

    return wrapper
