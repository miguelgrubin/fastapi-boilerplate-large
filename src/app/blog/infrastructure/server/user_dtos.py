from typing import List, Optional

from datetime import datetime

from pydantic import BaseModel


class UserCreationDTO(BaseModel):
    username: str
    password: str
    email: str


class ProfileResponse(BaseModel):
    bio: Optional[str] = None
    image: Optional[str] = None


class UserResponse(BaseModel):
    id: str
    email: str
    username: str
    profile: ProfileResponse
    following: List[str] = []
    followers: List[str] = []
    updated_at: datetime
    crated_at: datetime


class LoginDTO(BaseModel):
    email: str
    username: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str
