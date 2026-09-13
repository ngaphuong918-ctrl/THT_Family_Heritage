from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


# Thư mục gốc của dự án
BASE_DIR = Path(__file__).resolve().parents[2]


# Thư mục database
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)


# Đường dẫn database
DATABASE_URL = f"sqlite:///{DATA_DIR / 'family.db'}"


# Kết nối SQLite
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


# Base cho các model sau này
Base = declarative_base()