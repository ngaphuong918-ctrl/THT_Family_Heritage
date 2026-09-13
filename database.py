import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


# Thư mục gốc của dự án
BASE_DIR = Path(__file__).resolve().parents[2]


# Thư mục database (dùng khi chạy trên máy bạn, không dùng khi deploy)
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)


# =========================================================
# CHỌN DATABASE
#
# - Nếu có biến môi trường DATABASE_URL (khi deploy lên Render,
#   trỏ tới Neon Postgres) -> dùng Postgres, dữ liệu lưu vĩnh viễn.
# - Nếu KHÔNG có (khi bạn chạy thử trên máy mình) -> tự dùng
#   SQLite file family.db như cũ, không cần cài gì thêm.
# =========================================================

DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL:

    # Neon đôi khi trả chuỗi kết nối bắt đầu bằng "postgres://",
    # SQLAlchemy cần "postgresql+psycopg2://"
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace(
            "postgres://",
            "postgresql+psycopg2://",
            1,
        )

    engine = create_engine(DATABASE_URL)

else:

    DATABASE_URL = f"sqlite:///{DATA_DIR / 'family.db'}"

    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False}
    )


# Session database
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Base cho các model
Base = declarative_base()
