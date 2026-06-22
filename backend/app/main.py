from fastapi import FastAPI

from backend.app.database.database import engine

from backend.app.database.models import Base

from backend.app.api.bookings import router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Horse Booking API"
)

app.include_router(
    router,
    prefix="/bookings",
    tags=["Bookings"]
)