from datetime import timedelta

from backend.app.database.models import Booking


MALE_CAPACITY = 6
FEMALE_CAPACITY = 9


def can_book(
    db,
    gender: str,
    people_count: int,
    start_time,
    duration
):

    end_time = start_time + timedelta(hours=duration)

    overlapping = (
        db.query(Booking)
        .filter(
            Booking.booking_time < end_time,
            Booking.end_time > start_time
        )
        .all()
    )

    male_people = 0
    female_people = 0

    for booking in overlapping:

        if booking.gender == "male":
            male_people += booking.people_count

        else:
            female_people += booking.people_count

    if gender == "male":

        return (
            male_people + people_count
            <= MALE_CAPACITY
        )

    return (
        female_people + people_count
        <= FEMALE_CAPACITY
    )