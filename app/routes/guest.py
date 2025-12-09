from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.core.dependencies import require_guest
from app.database import get_db
from app.models.users import Guest
from app.schemas.users import GuestDisplay


router = APIRouter(prefix='/guest', tags=['Guest'])

@router.get('/profile', response_model=GuestDisplay)
def guest_profile(token = Depends(require_guest), db: Session = Depends(get_db)):
  guest = db.query(Guest).filter(Guest.id == int(token['sub'])).first()

  if not guest:
    return HTTPException(status_code=404, detail='No guest found')

  return guest
