from datetime import date

from .database import SessionLocal
from .relationship import Relationship
from .person import Person


# =========================================================
# THÊM QUAN HỆ CHA/MẸ -> CON
# =========================================================

def add_parent_child(
    parent_id: int,
    child_id: int,
    subtype: str = "biological",
):
    """
    parent_id: id của cha hoặc mẹ
    child_id:  id của con
    subtype:   "biological" (ruột) | "adopted" (nuôi) | "step" (kế)
    """
    db = SessionLocal()

    try:
        rel = Relationship(
            person_id=parent_id,
            related_id=child_id,
            type="parent_child",
            subtype=subtype,
        )

        db.add(rel)
        db.commit()
        db.refresh(rel)

        return rel

    finally:
        db.close()


# =========================================================
# THÊM QUAN HỆ VỢ/CHỒNG
# =========================================================

def add_marriage(
    person_id: int,
    spouse_id: int,
    order_index: int = 1,
    subtype: str = "married",
    start_date: date | None = None,
    end_date: date | None = None,
):
    """
    person_id / spouse_id: id của 2 người kết hôn với nhau
    order_index:           đời vợ/chồng thứ mấy (1 = đầu tiên, 2 = tái hôn...)
    subtype:                "married" | "divorced" | "widowed"
    """
    db = SessionLocal()

    try:
        rel = Relationship(
            person_id=person_id,
            related_id=spouse_id,
            type="marriage",
            subtype=subtype,
            order_index=order_index,
            start_date=start_date,
            end_date=end_date,
        )

        db.add(rel)
        db.commit()
        db.refresh(rel)

        return rel

    finally:
        db.close()


# =========================================================
# TRA CỨU: CÁC CON CỦA MỘT NGƯỜI
# =========================================================

def get_children(person_id: int):
    db = SessionLocal()

    try:
        rows = (
            db.query(Person)
            .join(Relationship, Relationship.related_id == Person.id)
            .filter(
                Relationship.person_id == person_id,
                Relationship.type == "parent_child",
            )
            .all()
        )
        return rows

    finally:
        db.close()


# =========================================================
# TRA CỨU: CHA/MẸ CỦA MỘT NGƯỜI
# =========================================================

def get_parents(person_id: int):
    db = SessionLocal()

    try:
        rows = (
            db.query(Person)
            .join(Relationship, Relationship.person_id == Person.id)
            .filter(
                Relationship.related_id == person_id,
                Relationship.type == "parent_child",
            )
            .all()
        )
        return rows

    finally:
        db.close()


# =========================================================
# TRA CỨU: VỢ/CHỒNG CỦA MỘT NGƯỜI (qua các thời kỳ)
# =========================================================

def get_spouses(person_id: int):
    db = SessionLocal()

    try:
        rows = (
            db.query(Relationship)
            .filter(
                Relationship.type == "marriage",
            )
            .filter(
                (Relationship.person_id == person_id)
                | (Relationship.related_id == person_id)
            )
            .order_by(Relationship.order_index)
            .all()
        )
        return rows

    finally:
        db.close()
