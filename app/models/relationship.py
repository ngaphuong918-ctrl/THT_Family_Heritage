from datetime import date, datetime

from sqlalchemy import Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from ...database import Base


class Relationship(Base):
    """
    Bảng lưu MỌI quan hệ giữa 2 Person.

    type = "parent_child":
        person_id   = cha hoặc mẹ
        related_id  = con
        subtype     = "biological" (ruột) | "adopted" (nuôi) | "step" (kế)

    type = "marriage":
        person_id   = người thứ nhất (thường là chồng)
        related_id  = người thứ hai (thường là vợ)
        order_index = đời vợ/chồng thứ mấy (1, 2, 3...)
        subtype     = "married" (đang chung sống) | "divorced" (ly hôn) | "widowed" (góa)
        start_date  = ngày kết hôn
        end_date    = ngày ly hôn / ngày người kia mất (để trống nếu vẫn còn)
    """

    __tablename__ = "relationships"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    person_id: Mapped[int] = mapped_column(
        ForeignKey("persons.id"),
        nullable=False
    )

    related_id: Mapped[int] = mapped_column(
        ForeignKey("persons.id"),
        nullable=False
    )

    type: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )

    subtype: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True
    )

    order_index: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    start_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True
    )

    end_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )
