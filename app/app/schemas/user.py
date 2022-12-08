import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class UserBase(BaseModel):
    name: Optional[str]


# Properties to receive via API on creation
class UserCreate(UserBase):
    profile_url: Optional[str] 
    credits: Optional[int]
    gender: Optional[str]
    city: Optional[str]
    province: Optional[str]
    country: Optional[str]
    openid: Optional[str]
    unionid: Optional[str]
    created_at: Optional[datetime.datetime]

# Properties to receive via API on update
class UserUpdate(UserBase):
    pass


class UserInDBBase(UserBase):
    pass

# Additional properties to return via API
class User(UserInDBBase):
    pass
