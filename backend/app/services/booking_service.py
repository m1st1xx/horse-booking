from datetime import timedelta
from backend.app.database.models import Instructor
from backend.app.database.models import Booking




def can_book(
    db,
    gender: str,
    people_count: int,
    start_time,
    duration
):
    capacity = get_capacity(
        db,
        gender
    )
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
                <= capacity
        )

    return (
            female_people + people_count
            <= capacity
    )


def get_capacity(
    db,
    gender
):

    instructors_count = (
        db.query(Instructor)
        .filter(
            Instructor.gender == gender,
            Instructor.active == True
        )
        .count()
    )

    return instructors_count * 3