from .database import SessionLocal
from .person import Person


def create_person(
    family_id: int,
    full_name: str,
    chi_ho: str | None = None,
    ten_huy: str | None = None,
    ten_tu: str | None = None,
    ten_hieu: str | None = None,
    gender: str | None = None,
    birth_date: str | None = None,
    death_date: str | None = None,
    birth_place: str | None = None,
    death_place: str | None = None,
    que_quan: str | None = None,
    nghe_nghiep: str | None = None,
    is_alive: bool = True,
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
            ten_huy=ten_huy,
            ten_tu=ten_tu,
            ten_hieu=ten_hieu,
            gender=gender,
            birth_date=birth_date,
            death_date=death_date,
            birth_place=birth_place,
            death_place=death_place,
            que_quan=que_quan,
            nghe_nghiep=nghe_nghiep,
            is_alive=is_alive,
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


def get_person(person_id: int):
    db = SessionLocal()

    try:
        return db.query(Person).filter(Person.id == person_id).first()

    finally:
        db.close()


def update_person(
    person_id: int,
    full_name: str,
    chi_ho: str | None = None,
    ten_huy: str | None = None,
    ten_tu: str | None = None,
    ten_hieu: str | None = None,
    gender: str | None = None,
    birth_date: str | None = None,
    death_date: str | None = None,
    birth_place: str | None = None,
    death_place: str | None = None,
    que_quan: str | None = None,
    nghe_nghiep: str | None = None,
    is_alive: bool = True,
    biography: str | None = None,
    photo_url: str | None = None,
    youtube_url: str | None = None,
):
    db = SessionLocal()

    try:
        person = db.query(Person).filter(Person.id == person_id).first()

        if person is None:
            return None

        person.full_name = full_name
        person.chi_ho = chi_ho
        person.ten_huy = ten_huy
        person.ten_tu = ten_tu
        person.ten_hieu = ten_hieu
        person.gender = gender
        person.birth_date = birth_date
        person.death_date = death_date
        person.birth_place = birth_place
        person.death_place = death_place
        person.que_quan = que_quan
        person.nghe_nghiep = nghe_nghiep
        person.is_alive = is_alive
        person.biography = biography

        # Chỉ cập nhật ảnh nếu có ảnh mới (photo_url không phải None)
        if photo_url is not None:
            person.photo_url = photo_url

        person.youtube_url = youtube_url

        db.commit()
        db.refresh(person)

        return person

    finally:
        db.close()


def delete_person(person_id: int):
    db = SessionLocal()

    try:
        person = db.query(Person).filter(Person.id == person_id).first()

        if person is None:
            return False

        db.delete(person)
        db.commit()

        return True

    finally:
        db.close()