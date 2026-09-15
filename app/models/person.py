from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Text
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

    # Các tên gọi truyền thống (thường dùng trong gia phả người Việt gốc Hoa)
    ten_huy: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True
    )

    ten_tu: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True
    )

    ten_hieu: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True
    )

    gender: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True
    )

    # Lưu dạng chữ tự do (vd: "1974", "khoảng 1850", "22 tháng 5 năm 1974"...)
    # vì gia phả thường chỉ nhớ năm hoặc theo âm lịch, không phải lúc nào
    # cũng có đủ ngày/tháng/năm chính xác.
    birth_date: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    death_date: Mapped[str | None] = mapped_column(
        String(100),
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

    que_quan: Mapped[str | None] = mapped_column(
        String(300),
        nullable=True
    )

    nghe_nghiep: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True
    )

    # Tình trạng tách riêng khỏi ngày mất - vì có người đã mất nhưng
    # không nhớ/không ghi ngày mất, và ngược lại.
    is_alive: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
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