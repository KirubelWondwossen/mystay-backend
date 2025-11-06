from typing import Optional
from pydantic import BaseModel

from app.schemas.hotel import HotelDisplay


# Input Schema Hotel Manager
class HotelManagerCreate(BaseModel):
  name: str
  email: str
  phone: str | None = None
  password: str | None = None

# Output Schema Hotel Manager
class HotelManagerDisplay(BaseModel):
  id: int
  name: str
  email: str
  phone: str | None = None
  hotel: Optional[HotelDisplay] = None

  class Config:
    orm_mode = True