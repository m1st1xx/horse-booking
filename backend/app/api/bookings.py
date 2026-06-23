from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from backend.app.database.database import get_db
from backend.app.database.models import Booking
from backend.app.schemas.booking import (BookingCreate,BookingResponse)
from datetime import timedelta
from fastapi import HTTPException
from backend.app.services.booking_service import can_book
from datetime import date
from datetime import datetime
from datetime import timedelta
from backend.app.database.models import Instructor
from backend.app.services.google_sheets import add_booking_row

router = APIRouter()


@router.post("/")
def create_booking(
    booking: BookingCreate,
    db: Session = Depends(get_db)
):

    available = can_book(
        db=db,
        gender=booking.gender,
        people_count=booking.people_count,
        start_time=booking.booking_time,
        duration=booking.duration
    )

    if not available:
        raise HTTPException(
            status_code=400,
            detail="На выбранное время нет свободных мест"
        )

    end_time = (
        booking.booking_time
        + timedelta(hours=booking.duration)
    )

    new_booking = Booking(
        client_name=booking.client_name,
        phone=booking.phone,
        gender=booking.gender,
        people_count=booking.people_count,
        duration=booking.duration,
        booking_time=booking.booking_time,
        end_time=end_time
    )

    db.add(new_booking)

    db.commit()

    db.refresh(new_booking)
    add_booking_row(new_booking)
    return new_booking

@router.get(
    "/",
    response_model=list[BookingResponse]
)
def get_bookings(
    db: Session = Depends(get_db)
):

    return db.query(Booking).all()

@router.get("/available-slots")
def available_slots(
    selected_date: date,
    gender: str,
    people_count: int,
    duration: int,
    db: Session = Depends(get_db)
):

    slots = []

    for hour in range(10, 20):

        start_time = datetime.combine(
            selected_date,
            datetime.min.time()
        ).replace(hour=hour)

        if can_book(
            db=db,
            gender=gender,
            people_count=people_count,
            start_time=start_time,
            duration=duration
        ):
            slots.append(
                start_time.strftime("%H:%M")
            )

    return slots
@router.get("/instructors")
def get_instructors(
    db: Session = Depends(get_db)
):

    return (
        db.query(Instructor)
        .all()
    )