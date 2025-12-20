from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from app.database import Base


class PasswordResetToken(Base):
  __tablename__ = 'password_reset_tokens'

  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey('hotel_managers.id'), nullable=False)
  token_hash = Column(String, nullable=False, index=True)
  expires_at = Column(DateTime, nullable=False)
  is_used = Column(Boolean, default=False)
  created_at = Column(DateTime, default=datetime.utcnow)
