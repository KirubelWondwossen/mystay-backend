from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from app.core.security import create_admin_token, verify_password

from app.database import get_db
from app.models.users import Admin
from app.schemas.users import AdminLogin


router = APIRouter(prefix='/admin', tags=['Admin'])

# Handle Admin Login
@router.post('/login')
def admin_login(credentials: AdminLogin, db:Session = Depends(get_db)):
  admin = db.query(Admin).filter(Admin.email == credentials.email).first()

  if not admin or not verify_password(credentials.password, admin.password_hash):
    raise HTTPException(status_code=401, detail='Invalid credentials')

  token = create_admin_token(admin)

  return {
    "access_token": token,
    "token_type": "bearer",
    "admin_name": admin.full_name,
    "admin_email": admin.email,
    "admin_id": admin.id,
  }
