from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://127.0.0.1",
        "http://localhost:5500",
        "http://127.0.0.1:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)