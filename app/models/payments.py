from sqlalchemy import Column, String, DateTime, Float, ForeignKey, Integer, Enum as SQLEnum

from datetime import datetime
from enum import Enum

from app.database import Base


class PaymentStatus(str, Enum):
  UNPAID = 'unpaid'
  PAID = 'paid'
  FAILD = 'faild'
  REFUNDED = 'refunded'


class PaymentMethod(str, Enum):
  CASH = 'cash'
  CARD = 'card'
  MOBILE = 'mobile'
  DEMO = 'demo'


class Payment(Base):
  __tablename__ = 'payments'

  id = Column(Integer, primary_key=True, index=True)

  booking_id = Column(Integer, ForeignKey('bookings.id'), nullable=False)
  guest_id = Column(Integer, ForeignKey('guests.id'), nullable=False)

  amount = Column(Float, nullable=False)
  method = Column(SQLEnum(PaymentMethod), nullable=False)
  status = Column(SQLEnum(PaymentStatus), nullable=False)

  transaction_ref = Column(String, nullable=True)

  created_at = Column(DateTime, default=datetime.utcnow)
