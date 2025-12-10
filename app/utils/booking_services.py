from sqlalchemy.orm import Session

from datetime import date

from app.models.bookings import Booking


def is_room_available(db : Session, room_id: int, check_in , check_out):
    conflicting = db.query(Booking).filter(
        Booking.room_id == room_id,
        Booking.status.in_(["pending", "confirmed"]),
        Booking.check_in < check_out,
        Booking.check_out > check_in
    ).first()

    return not conflicting
