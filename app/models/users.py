from sqlalchemy import Column, Integer, String

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
