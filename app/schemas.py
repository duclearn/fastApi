from pydantic import BaseModel, EmailStr, conint
from typing import Optional
from datetime import datetime

class PostBase(BaseModel):
    item: str
    details: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    create_at: datetime

    class Config:
        orm_mode = True


class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    owner_id: int
    create_at = datetime
    owner: UserOut

    class Config:
        orm_mode = True

class UserCreate (BaseModel):
    email: EmailStr
    password: str

class UserLogin (BaseModel):
    email: EmailStr
    password: str

class TokenData(BaseModel):
    id: Optional[str]

class Token(BaseModel):
    access_token: str
    token_type: str

class Votes(BaseModel):
    post_id : int
    dir: conint(le=1)
