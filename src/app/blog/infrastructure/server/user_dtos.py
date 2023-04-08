from datetime import datetime
from typing import List, Optional
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
