# Hướng dẫn cài đặt – THT Gia Phả

## 1. Các file mới/cập nhật cần chép vào dự án

Chép đè (ghi đè lên file cũ) đúng theo đường dẫn sau trong VS Code:

| File bạn nhận được | Chép vào đúng vị trí |
|---|---|
| `app/models/relationship.py` | file **mới**, tạo file mới trong `app/models/` |
| `app/models/relationship_service.py` | file **mới**, tạo file mới trong `app/models/` |
| `app/models/database.py` | **ghi đè** file cũ |
| `app/models/__init__.py` | **ghi đè** file cũ |
| `app/main.py` | **ghi đè** file cũ |
| `requirements.txt` | đặt ở **thư mục gốc** (`THT_Family_Heritage/`, ngang hàng với thư mục `app/`) |

## 2. Chạy thử trên máy bạn (không cần internet)

Mở Terminal trong VS Code (`Terminal` → `New Terminal`), gõ lần lượt:

```
pip install -r requirements.txt --break-system-packages
python -m app.models.create_family
uvicorn app.main:app --reload
```

Mở trình duyệt vào `http://127.0.0.1:8000` — nếu thấy trang chủ hiện ra là thành công.
Vào `http://127.0.0.1:8000/members` để xem trang thành viên (sẽ trống vì chưa thêm ai).

Khi chạy trên máy mình như trên, dữ liệu tự lưu vào file `data/family.db` như cũ — **chưa cần** Neon/Render ở bước này.

## 3. Khi sẵn sàng đưa lên mạng cho cả dòng họ xem

### Bước 1 — Tạo database miễn phí trên Neon (giữ dữ liệu vĩnh viễn)

1. Vào https://neon.tech, đăng ký tài khoản miễn phí (có thể đăng nhập bằng Google).
2. Tạo 1 project mới, đặt tên tùy ý, ví dụ `tht-gia-pha`.
3. Neon sẽ đưa cho bạn 1 dòng chữ dạng:
   `postgresql://user:password@ep-xxxx.neon.tech/neondb?sslmode=require`
   → **Copy và lưu lại dòng này**, sẽ dùng ở bước 3.

### Bước 2 — Đưa code lên GitHub

1. Vào https://github.com, tạo tài khoản miễn phí nếu chưa có.
2. Tạo 1 repository mới (ví dụ tên `tht-gia-pha`), để chế độ Private.
3. Trong VS Code, dùng biểu tượng "Source Control" (bên trái) để đẩy toàn bộ dự án lên repository vừa tạo (VS Code có nút "Publish to GitHub" rất dễ dùng).

### Bước 3 — Deploy trên Render (miễn phí)

1. Vào https://render.com, đăng ký bằng tài khoản GitHub ở trên.
2. Chọn **New +** → **Web Service** → chọn đúng repository `tht-gia-pha`.
3. Điền:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
4. Ở mục **Environment Variables**, thêm 1 biến:
   - Key: `DATABASE_URL`
   - Value: dòng chữ Neon bạn đã copy ở Bước 1
5. Bấm **Create Web Service**. Chờ khoảng 2–3 phút, Render sẽ cho bạn 1 địa chỉ dạng:
   `https://tht-gia-pha.onrender.com` — đây là địa chỉ để cả dòng họ ở VN/Mỹ/Trung Quốc cùng truy cập.

> Lưu ý: gói free của Render sẽ "ngủ" sau ~15 phút không có người truy cập, lần truy cập đầu tiên sau đó có thể mất khoảng 30–50 giây để "thức dậy" — đây là bình thường với gói miễn phí, không phải lỗi.

## 4. Việc còn lại (mình sẽ làm tiếp sau)

- Thêm form nhập liệu trên giao diện (hiện các API `/api/persons`, `/api/relationships/...` đã sẵn sàng nhưng chưa có form đẹp để bạn bấm nhập — bạn không cần dùng Postman hay code, mình sẽ làm giao diện nhập liệu sau)
- Vẽ cây gia phả trực quan trên trang `/`
- Đa ngôn ngữ Việt / English / 中文
- Lưu ảnh thành viên (hiện `photo_url` mới là đường link ảnh, cần thêm chức năng tải ảnh lên)
