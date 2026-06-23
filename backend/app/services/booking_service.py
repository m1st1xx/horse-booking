from backend.app.database.models import Booking


def check_capacity(
    db,
    start_time,
    end_time,
    people_count
):
    overlapping = (
        db.query(Booking)
        .filter(
            Booking.booking_time < end_time,
            Booking.end_time > start_time
        )
        .all()
    )
    current_people = sum(
        booking.people_count
        for booking in overlapping
    )
    if current_people + people_count > 15:
        return False