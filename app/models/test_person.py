from datetime import date

from .person_service import create_person


person = create_person(
    family_id=1,
    full_name="Trần Văn Minh",
    chi_ho="Chi 1",
    gender="Nam",
    birth_date=date(1950, 5, 10),
    birth_place="Việt Nam",
    biography="Thành viên thử nghiệm của gia phả Họ Trần.",
    photo_url="https://photos.google.com/",
    youtube_url="https://www.youtube.com/",
)

print("Person created successfully.")
print("ID:", person.id)
print("Họ tên:", person.full_name)
print("Chi họ:", person.chi_ho)
print("Giới tính:", person.gender)
print("Ngày sinh:", person.birth_date)
print("Ngày tạ thế:", person.death_date)
print("Ảnh:", person.photo_url)
print("YouTube:", person.youtube_url)