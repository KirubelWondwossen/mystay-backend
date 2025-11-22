from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from app.crud.users import create_hotel_manager, get_all_hotel_managers, get_hotel_manager
from app.database import get_db

from app.schemas.users import HotelManagerCreate, HotelManagerDisplay


router = APIRouter(prefix='/hotelmanager', tags=['HotelManager'])

# Create Manager
@router.post('/', response_model=HotelManagerDisplay)
def create_manager(new_manager: HotelManagerCreate, db: Session = Depends(get_db)):
  return create_hotel_manager(db, new_manager)

# Get all managers
@router.get('/', response_model=list[HotelManagerDisplay])
def get_managers(db: Session = Depends(get_db)):
  return get_all_hotel_managers(db)

# Get one manager by ID
@router.get('/{manager_id}', response_model=HotelManagerDisplay)
def get_manager(manager_id: int, db: Session = Depends(get_db)):
  db_manager = get_hotel_manager(db, manager_id)

  if not db_manager:
    raise HTTPException(status_code=404, detail='Manager not found')

  return db_manager