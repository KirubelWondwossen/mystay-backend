from typing import Optional
from pydantic import BaseModel

from app.models.room import BedType, RoomType

class RoomBase(BaseModel):
  room_number: str
  room_type: RoomType
  price_per_night: float
  description: str
  bed_type: BedType
  image_url: str
  available: bool


class RoomUpdate(BaseModel):
  room_number: Optional[str]
  room_type: Optional[RoomType]
  price_per_night: Optional[float]
  description: Optional[str]
  bed_type: Optional[BedType]
  image_url: Optional[str]
  available: Optional[bool]


class RoomDisaply(RoomBase):
  id: int
  hotel_id: int

  class config:
    orm_mode = True
