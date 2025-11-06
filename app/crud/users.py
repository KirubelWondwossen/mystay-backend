from sqlalchemy.orm import Session
from app.models.users import HotelManager

from app.schemas.users import HotelManagerCreate

# Creating new hotel manager
def create_hotel_manager(db: Session, new_manager: HotelManagerCreate):
  db_manager = HotelManager(
    name = new_manager.name,
    email = new_manager.email,
    phone = new_manager.phone,
    password = new_manager.password
  )

  db.add(db_manager)
  db.commit()
  db.refresh(db_manager)

  return db_manager

# Get all hotel managers
def get_all_hotel_managers(db: Session):
  return db.query(HotelManager).all()

# Get hotel manager
def get_hotel_manager(db: Session, manager_id: int):
  return db.query(HotelManager).filter(HotelManager.id == manager_id).first()
