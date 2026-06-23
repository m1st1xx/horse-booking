from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from backend.app.database.database import Base


class Booking(Base):

    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)

    client_name = Column(
        String,
        nullable=False
    )

    phone = Column(
        String,
        nullable=False
    )

    gender = Column(
        String,
        nullable=False
    )

    people_count = Column(
        Integer,
        nullable=False
    )

    duration = Column(
        Integer,
        nullable=False
    )

    booking_time = Column(
        DateTime,
        nullable=False
    )
    end_time = Column(
        DateTime,
        nullable=False
    )