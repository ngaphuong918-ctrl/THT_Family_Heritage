# THT DocStudio AI — Tài liệu Tính năng & Hướng dẫn sử dụng
### (Dùng để làm video giới thiệu sản phẩm)

**Phiên bản:** 1.0
**Thuộc bộ:** THT Studio Suite (cùng THT Audiobook Studio, THT PhotoStudio AI)
**Đối tượng:** Cá nhân & cộng đồng — miễn phí, chạy trên máy Windows

---

## 1. GIỚI THIỆU TỔNG QUAN (mở đầu video)

**THT DocStudio AI** là phần mềm desktop dùng AI để:
- Tự động phát hiện và sửa lỗi chính tả, ngữ pháp, văn phong tiếng Việt trong văn bản.
- Đọc chữ từ ảnh chụp (OCR) — kể cả PDF dạng ảnh scan.
- Phiên âm và dịch nghĩa chữ Hán/Nôm cổ từ ảnh sách xưa hoặc từ văn bản có sẵn.
- Hoàn toàn **miễn phí**, có thể chạy AI ngay trên máy tính cá nhân (không bắt buộc phải trả tiền dịch vụ đám mây).

**Điểm khác biệt:** Phần mềm không phụ thuộc vào một nhà cung cấp AI duy nhất — người dùng tự chọn dùng **Gemini (miễn phí, cần API key riêng)** hoặc **model chạy ngay trên máy (Ollama, hoàn toàn offline)**, và có thể để 2 bên **tự động hỗ trợ nhau** khi một bên gặp sự cố.

---

## 2. DANH SÁCH ĐẦY ĐỦ TÍNH NĂNG

### A. Đọc tài liệu — hỗ trợ nhiều định dạng
- File `.txt`, `.docx` (Word mới), `.doc` (Word cũ — cần máy có cài Microsoft Word).
- File `.pdf` có sẵn chữ (đọc trực tiếp).
- File `.pdf` dạng ảnh scan — **tự động OCR từng trang** rồi gộp thành văn bản để sửa lỗi.
- Dán văn bản trực tiếp vào ô nhập (không cần file).
- Tải ảnh chụp trang văn bản tiếng Việt lên — AI đọc chữ ra rồi đưa vào sửa lỗi luôn.

### B. Sửa lỗi chính tả bằng AI
- Phân loại lỗi theo 3 màu: 🔴 Chính tả — 🟡 Ngữ pháp — 🔵 Văn phong.
- Lỗi được **tô màu trực tiếp trong văn bản**, kèm bảng đề xuất sửa chi tiết bên cạnh.
- Từng lỗi có nút **[✓ Chấp nhận]** / **[✕ Bỏ qua]** riêng, hoặc **[⚡ Áp dụng tất cả]** một lần.
- Tính **Điểm chất lượng văn bản (0–100)**, tự cập nhật theo thời gian thực khi sửa lỗi.
- Danh sách "từ được bảo vệ" — chỉ định từ AI không được sửa (tên thương hiệu, thuật ngữ riêng...).
- AI được huấn luyện để **xét ngữ cảnh cả câu** trước khi sửa (tránh sửa đúng chính tả nhưng sai nghĩa).

### C. Chỉnh sửa thủ công (như Word)
- Chế độ "Chỉnh sửa thủ công" — gõ sửa trực tiếp bất cứ chỗ nào AI bỏ sót.
- Thanh công cụ định dạng: chọn **Font chữ**, **cỡ chữ**, **In đậm / Nghiêng / Gạch chân**, **Màu chữ**, **Căn lề** (trái/giữa/phải/đều).
- **Hoàn tác / Làm lại** (Undo/Redo).
- **Tìm kiếm trong văn bản (Ctrl+F)** — tô sáng tất cả kết quả, nhảy tới từng kết quả.
- Nút **"🔄 Phân tích lại"** để AI kiểm tra lại sau khi tự sửa tay.

### D. Xuất kết quả
- Xuất file **`.docx`** — giữ nguyên định dạng gốc (tiêu đề, bảng biểu...) nếu file gốc là Word.
- Nút **"🎙️ Copy sang Audiobook"** — copy văn bản đã sửa vào clipboard để dán thẳng sang THT Audiobook Studio, biến thành sách nói.

### E. Dịch Hán-Nôm (tính năng đặc biệt)
- **3 cách nhập liệu:**
  1. 🖼️ Tải ảnh trang sách chữ Hán/Nôm.
  2. 📋 Dán trực tiếp chữ Hán/Nôm dạng văn bản (không cần ảnh).
  3. 📚 **Xử lý hàng loạt** — chọn nhiều ảnh trang sách cùng lúc, dịch tuần tự từng trang.
- Kết quả trả về gồm: **chữ Hán/Nôm phiên âm lại**, **âm Hán-Việt**, **bản dịch tiếng Việt**, và **ghi chú của AI** (loại văn bản, độ tin cậy, chữ không đọc rõ được đánh dấu `[?]`).
- Chế độ hàng loạt: xem trạng thái từng trang (⏳/✅/⚠️/❌), bấm vào từng dòng để xem lại, **nút "Thử lại các trang lỗi"** chỉ chạy lại đúng những trang chưa thành công, và **xuất toàn bộ kết quả thành 1 file Word**.

### F. Độ tin cậy — tự động xử lý sự cố (điểm mạnh kỹ thuật)
- **Tự động thử lại** khi gặp lỗi tạm thời (hết giới hạn miễn phí, máy chủ quá tải) — chờ rồi tự thử lại, không cần người dùng làm gì.
- **Model dự phòng (Fallback):** khi Gemini gặp sự cố, tự động chuyển sang model chạy trên máy (Ollama) để không bị gián đoạn công việc.
- **Lưới an toàn chống crash:** nếu có lỗi bất ngờ, phần mềm hiện thông báo và **tiếp tục chạy** thay vì tự tắt.

### G. Quản lý & Cài đặt
- **⚙️ Cài đặt** ngay trong app — chọn nhà cung cấp AI, nhập API key, chọn model (có **danh sách thả xuống tự dò model đã tải về máy**), bật/tắt model dự phòng — **không cần sửa file cấu hình bằng tay**.
- **🕘 Lịch sử xử lý** — ghi lại mọi lần sửa lỗi/dịch thuật đã làm, bấm vào từng mục để **xem lại toàn bộ nội dung** đã xử lý, xóa lịch sử khi cần.
- Nút **"🔄 LÀM MỚI"** to, dễ thấy — quay lại màn hình ban đầu bất cứ lúc nào.

---

## 3. YÊU CẦU HỆ THỐNG

| Thành phần | Yêu cầu |
|---|---|
| Hệ điều hành | Windows 10/11 |
| Chạy AI online | Cần API key Gemini miễn phí (lấy tại aistudio.google.com/app/apikey) |
| Chạy AI offline (tùy chọn) | Cài thêm Ollama (miễn phí) + tải model (ví dụ qwen2.5:7b) |
| Cấu hình khuyến nghị cho AI local | GPU rời ≥ 6GB VRAM, RAM ≥ 16GB |

---

## 4. KỊCH BẢN GỢI Ý CHO VIDEO GIỚI THIỆU (từng bước quay demo)

**Cảnh 1 — Mở đầu:** Giới thiệu vấn đề ("văn bản tải trên mạng hay sai chính tả") → giới thiệu THT DocStudio AI là giải pháp.

**Cảnh 2 — Sửa lỗi cơ bản:**
1. Kéo-thả 1 file `.docx` hoặc `.pdf` vào app.
2. Cho xem quá trình AI phân tích, lỗi hiện màu trong văn bản.
3. Bấm Chấp nhận vài lỗi, bấm "Áp dụng tất cả", cho xem Điểm chất lượng tăng lên.
4. Xuất file DOCX.

**Cảnh 3 — Các cách nhập liệu khác:**
1. Dán 1 đoạn văn bản trực tiếp → Kiểm tra.
2. Tải 1 ảnh chụp trang sách tiếng Việt → cho xem OCR tự đọc chữ ra.
3. Tải 1 file PDF dạng scan → cho xem hộp thoại hỏi OCR tự động, rồi kết quả.

**Cảnh 4 — Chỉnh sửa thủ công:**
1. Bấm "Chỉnh sửa thủ công", gõ sửa thêm, dùng thử Bold/Màu chữ.
2. Bấm Ctrl+F tìm 1 từ, cho xem kết quả tô sáng.

**Cảnh 5 — Điểm nhấn: Dịch Hán-Nôm:**
1. Mở "Dịch Hán-Nôm" → tải 1 ảnh sách chữ Hán cổ.
2. Cho xem kết quả: chữ gốc, âm Hán-Việt, bản dịch tiếng Việt.
3. Demo nhanh chế độ "Hàng loạt" với vài ảnh cùng lúc.

**Cảnh 6 — Cài đặt & tính linh hoạt:**
1. Mở "⚙️ Cài đặt", cho xem chuyển đổi giữa Gemini và model chạy máy (Ollama) dễ dàng.
2. Nhấn mạnh: miễn phí, dữ liệu riêng tư (chạy offline được), tự chủ hoàn toàn.

**Cảnh 7 — Kết:** Nhắc lại đây là 1 phần trong "THT Studio Suite" cá nhân/cộng đồng, cho xem nút "Copy sang Audiobook" nối sang phần mềm chị em.

---

## 5. CÂU KHẨU HIỆU GỢI Ý (tagline)
- *"Sửa lỗi chính tả bằng AI — miễn phí, riêng tư, ngay trên máy của bạn."*
- *"Từ chữ Quốc ngữ đến chữ Hán-Nôm cổ — một phần mềm, mọi văn bản."*
