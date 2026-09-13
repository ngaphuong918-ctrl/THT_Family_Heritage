from .database import SessionLocal
from .family import Family


def create_family():
    db = SessionLocal()

    try:
        family = Family(
            name="Họ Trần",
            description="Gia phả và lịch sử dòng họ Trần."
        )

        db.add(family)
        db.commit()
        db.refresh(family)

        print("Family created successfully.")
        print(f"ID: {family.id}")
        print(f"Name: {family.name}")

    finally:
        db.close()


if __name__ == "__main__":
    create_family()