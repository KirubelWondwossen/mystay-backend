from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.hotel import HotelCreate, HotelDisplay
from app.crud.hotel import create_new_hotel, get_all_hotels, get_one_hotel


router = APIRouter(prefix='/hotels', tags=['Hotels'])

# Create Hotel
@router.post('/', response_model=HotelDisplay)
def create_hotel(new_hotel: HotelCreate, db: Session = Depends(get_db)):
  return create_new_hotel(db, new_hotel)

# Get all Hotels
@router.get('/', response_model=list[HotelDisplay])
def get_hotels(db: Session = Depends(get_db)):
  return get_all_hotels(db)

# Get one Hotel by ID
@router.get('/{hotel_id}', response_model=HotelDisplay)
def get_hotel(hotel_id, db: Session = Depends(get_db)):
  db_hotel = get_one_hotel(db, hotel_id)

  if not db_hotel:
    raise HTTPException(status_code=404, detail='Hotel not found')

  return db_hotel
