from datetime import date, datetime

from sqlalchemy import Date, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class Person(Base):
    __tablename__ = "persons"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    family_id: Mapped[int] = mapped_column(
        ForeignKey("families.id"),
        nullable=False
    )

    chi_ho: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True
    )

    full_name: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    gender: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True
    )

    birth_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True
    )

    death_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True
    )

    birth_place: Mapped[str | None] = mapped_column(
        String(300),
        nullable=True
    )

    death_place: Mapped[str | None] = mapped_column(
        String(300),
        nullable=True
    )

    biography: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    photo_url: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True
    )

    youtube_url: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )