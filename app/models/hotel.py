from sqlalchemy import JSON, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Hotel(Base):
  __tablename__ = 'hotels'

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(255), nullable=False)
  description = Column(String, nullable=True)
  address = Column(String, nullable=False)
  rating = Column(Float, default=0.0)
  exact_location = Column(JSON, nullable=False)
  contact_number = Column(String, nullable=False)
  email = Column(String, nullable=False)

  manager_id = Column(Integer, ForeignKey('hotel_managers.id'), unique=True)
  manager = relationship('HotelManager', back_populates='hotel')

  rooms = relationship('Room', back_populates='hotel', cascade='all, delete-orphan')
