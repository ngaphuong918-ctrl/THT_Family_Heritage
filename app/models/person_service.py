from datetime import date

from .database import SessionLocal
from .person import Person


def create_person(
    family_id: int,
    full_name: str,
    chi_ho: str | None = None,
    gender: str | None = None,
    birth_date: date | None = None,
    death_date: date | None = None,
    birth_place: str | None = None,
    death_place: str | None = None,
    biography: str | None = None,
    photo_url: str | None = None,
    youtube_url: str | None = None,
):
    db = SessionLocal()

    try:
        person = Person(
            family_id=family_id,
            chi_ho=chi_ho,
            full_name=full_name,
            gender=gender,
            birth_date=birth_date,
            death_date=death_date,
            birth_place=birth_place,
            death_place=death_place,
            biography=biography,
            photo_url=photo_url,
            youtube_url=youtube_url,
        )

        db.add(person)
        db.commit()
        db.refresh(person)

        return person

    finally:
        db.close()