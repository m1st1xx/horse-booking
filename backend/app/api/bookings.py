from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.app.database.database import get_db

from backend.app.database.models import Booking

from backend.app.schemas.booking import (
    BookingCreate,
    BookingResponse
)

router = APIRouter()


@router.post(
    "/",
    response_model=BookingResponse
)
def create_booking(
    booking: BookingCreate,
    db: Session = Depends(get_db)
):

    new_booking = Booking(
        client_name=booking.client_name,
        phone=booking.phone,
        gender=booking.gender,
        people_count=booking.people_count,
        duration=booking.duration,
        booking_time=booking.booking_time
    )

    db.add(new_booking)

    db.commit()

    db.refresh(new_booking)

    return new_booking


@router.get(
    "/",
    response_model=list[BookingResponse]
)
def get_bookings(
    db: Session = Depends(get_db)
):

    return db.query(Booking).all()