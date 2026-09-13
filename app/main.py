from datetime import date

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from app.models.person_service import create_person


app = FastAPI(
    title="THT Gia Phả – Family Heritage",
    version="1.0.0"
)


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