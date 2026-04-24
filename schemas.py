from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class GameBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    platform: str = Field(..., min_length=1, max_length=50)
    genre: Optional[str] = None
    release_year: Optional[int] = Field(None, ge=1970, le=2030)
    status: Optional[str] = Field("wishlist", pattern="^(wishlist|playing|completed|dropped)$")
    rating: Optional[float] = Field(None, ge=1.0, le=10.0)
    notes: Optional[str] = None


class GameCreate(GameBase):
    pass


class GameUpdate(BaseModel):
    title: Optional[str] = None
    platform: Optional[str] = None
    genre: Optional[str] = None
    release_year: Optional[int] = None
    status: Optional[str] = Field(None, pattern="^(wishlist|playing|completed|dropped)$")   
    rating: Optional[float] = Field(None, ge=1.0, le=10.0)
    notes: Optional[str] = None


class GameResponse(GameBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True