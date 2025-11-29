from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


# For a demo purpose need modification later
class HotelManager(Base):
  '''Hotel Manager Model'''
  __tablename__ = 'hotel_managers'

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, nullable=False)
  email = Column(String, nullable=False, unique=True)
  phone = Column(String, nullable=True)
  password = Column(String, nullable=True)

  hotel = relationship('Hotel', back_populates='manager', uselist=False)


# Guest User
class Guest(Base):
  '''Guest User Model'''
  __tablename__ = 'guest'

  id = Column(Integer, primary_key=True, index=True)
  google_id = Column(String, unique=True)
  email = Column(String, unique=True)
  full_name = Column(String, nullable=True)
  avater_url = Column(String, nullable=True)
  created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
