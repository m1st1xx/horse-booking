from datetime import datetime

from pydantic import BaseModel



class BookingCreate(BaseModel):
    client_name: str

    phone: str

    gender: str

    people_count: int

    duration: int

    booking_time: datetime


class BookingResponse(BaseModel):

    id: int

    client_name: str

    phone: str

    gender: str

    people_count: int

    duration: int

    booking_time: datetime

    end_time: datetime

    class Config:
        from_attributes = True