from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from app.schemas.hotel import HotelSimpleView


# Admin login schema
class AdminLogin(BaseModel):
  email: str
  password: str


# Base hotel manager schema
class HotelManagerBase(BaseModel):
  name: str
  email: str
  phone: str | None = None


# Input Schema Hotel Manager
class HotelManagerCreate(HotelManagerBase):
  password: str


# Output Schema Hotel Manager
class HotelManagerDisplay(HotelManagerBase):
  id: int
  hotel: Optional[HotelSimpleView] = None

  class Config:
    orm_mode = True


# Hotel manager login
class HotelManagerLogin(BaseModel):
  email: str
  password: str


# Hotel manager update password
class HotelManagerPasswordUpdate(BaseModel):
  current_password: str
  new_password: str


# Hotel Manager forget password
class HotelManagerForgetPassword(BaseModel):
  email: str


class HotelManagerResetPassword(BaseModel):
  new_password: str
  token: str

# Guest Output
class GuestDisplay(BaseModel):
  id: int
  email: str
  full_name: str
  avater_url: str
  created_at: datetime

  model_config = {
    'from_attributes': True
  }

  # class Config:
  #   orm_mode = True
