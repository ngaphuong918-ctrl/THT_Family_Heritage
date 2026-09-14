from datetime import date

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from app.models import init_database
from app.models.database import SessionLocal
from app.models.family import Family
from app.models.person import Person
from app.models.person_service import create_person
from app.models.relationship_service import (
    add_parent_child,
    add_marriage,
    get_children,
    get_parents,
    get_spouses,
)


app = FastAPI(
    title="THT Gia Phả – Family Heritage",
    version="1.0.0"
)


# =========================================================
# TỰ TẠO BẢNG DATABASE KHI SERVER KHỞI ĐỘNG
# (chạy 1 lần, không xóa dữ liệu cũ nếu bảng đã tồn tại)
# =========================================================

@app.on_event("startup")
async def on_startup():
    init_database()


# =========================================================
# STATIC FILES
# =========================================================

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)


# =========================================================
# HTML TEMPLATES
# =========================================================

templates = Jinja2Templates(
    directory="app/templates"
)


# =========================================================
# MODEL DỮ LIỆU: TẠO DÒNG HỌ (FAMILY)
# =========================================================

class FamilyCreate(BaseModel):

    name: str

    description: str | None = None


# =========================================================
# MODEL DỮ LIỆU THÊM THÀNH VIÊN
# =========================================================

class PersonCreate(BaseModel):

    family_id: int

    full_name: str

    chi_ho: str | None = None

    gender: str | None = None

    birth_date: date | None = None

    death_date: date | None = None

    birth_place: str | None = None

    death_place: str | None = None

    biography: str | None = None

    photo_url: str | None = None

    youtube_url: str | None = None


# =========================================================
# MODEL DỮ LIỆU: QUAN HỆ CHA/MẸ -> CON
# =========================================================

class ParentChildCreate(BaseModel):

    parent_id: int

    child_id: int

    subtype: str = "biological"  # biological | adopted | step


# =========================================================
# MODEL DỮ LIỆU: QUAN HỆ VỢ/CHỒNG
# =========================================================

class MarriageCreate(BaseModel):

    person_id: int

    spouse_id: int

    order_index: int = 1

    subtype: str = "married"  # married | divorced | widowed

    start_date: date | None = None

    end_date: date | None = None


# =========================================================
# API: TẠO DÒNG HỌ MỚI
# =========================================================

@app.post("/api/families")
async def create_family_api(data: FamilyCreate):

    db = SessionLocal()

    try:
        family = Family(
            name=data.name,
            description=data.description,
        )

        db.add(family)
        db.commit()
        db.refresh(family)

        return {
            "success": True,
            "message": "Tạo dòng họ thành công.",
            "family": {
                "id": family.id,
                "name": family.name,
                "description": family.description,
            }
        }

    finally:
        db.close()


# =========================================================
# API: XEM DANH SÁCH DÒNG HỌ
# =========================================================

@app.get("/api/families")
async def list_families_api():

    db = SessionLocal()

    try:
        families = db.query(Family).all()

        return [
            {
                "id": f.id,
                "name": f.name,
                "description": f.description,
            }
            for f in families
        ]

    finally:
        db.close()


# =========================================================
# API: THÊM THÀNH VIÊN
# =========================================================

@app.post("/api/persons")
async def create_person_api(person_data: PersonCreate):

    person = create_person(
        family_id=person_data.family_id,
        full_name=person_data.full_name,
        chi_ho=person_data.chi_ho,
        gender=person_data.gender,
        birth_date=person_data.birth_date,
        death_date=person_data.death_date,
        birth_place=person_data.birth_place,
        death_place=person_data.death_place,
        biography=person_data.biography,
        photo_url=person_data.photo_url,
        youtube_url=person_data.youtube_url,
    )

    return {
        "success": True,
        "message": "Thêm thành viên thành công.",
        "person": {
            "id": person.id,
            "family_id": person.family_id,
            "full_name": person.full_name,
            "chi_ho": person.chi_ho,
            "gender": person.gender,
            "birth_date": person.birth_date,
            "death_date": person.death_date,
            "birth_place": person.birth_place,
            "death_place": person.death_place,
            "biography": person.biography,
            "photo_url": person.photo_url,
            "youtube_url": person.youtube_url,
        }
    }


# =========================================================
# API: THÊM QUAN HỆ CHA/MẸ -> CON
# =========================================================

@app.post("/api/relationships/parent-child")
async def create_parent_child_api(data: ParentChildCreate):

    rel = add_parent_child(
        parent_id=data.parent_id,
        child_id=data.child_id,
        subtype=data.subtype,
    )

    return {
        "success": True,
        "message": "Thêm quan hệ cha/mẹ - con thành công.",
        "relationship_id": rel.id,
    }


# =========================================================
# API: THÊM QUAN HỆ VỢ/CHỒNG
# =========================================================

@app.post("/api/relationships/marriage")
async def create_marriage_api(data: MarriageCreate):

    rel = add_marriage(
        person_id=data.person_id,
        spouse_id=data.spouse_id,
        order_index=data.order_index,
        subtype=data.subtype,
        start_date=data.start_date,
        end_date=data.end_date,
    )

    return {
        "success": True,
        "message": "Thêm quan hệ vợ/chồng thành công.",
        "relationship_id": rel.id,
    }


# =========================================================
# API: XEM CON, CHA MẸ, VỢ CHỒNG CỦA MỘT NGƯỜI
# =========================================================

@app.get("/api/persons/{person_id}/family-links")
async def person_family_links_api(person_id: int):

    children = get_children(person_id)
    parents = get_parents(person_id)
    spouses = get_spouses(person_id)

    return {
        "children": [{"id": c.id, "full_name": c.full_name} for c in children],
        "parents": [{"id": p.id, "full_name": p.full_name} for p in parents],
        "spouses_relationship_count": len(spouses),
    }


# =========================================================
# TRANG CHỦ
# =========================================================

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "title": "THT Gia Phả – Family Heritage"
        }
    )


# =========================================================
# TRANG THÀNH VIÊN
# =========================================================

@app.get("/members", response_class=HTMLResponse)
async def members_page(request: Request):

    db = SessionLocal()

    try:
        persons = db.query(Person).all()
    finally:
        db.close()

    return templates.TemplateResponse(
        request=request,
        name="members/index.html",
        context={
            "title": "Thành viên – THT Gia Phả",
            "persons": persons,
        }
    )
