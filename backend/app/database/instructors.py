from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from backend.app.database.database import Base


class Instructor(Base):

    __tablename__ = "instructors"

    id = Column(Integer, primary_key=True)

    gender = Column(
        String,
        nullable=False
    )