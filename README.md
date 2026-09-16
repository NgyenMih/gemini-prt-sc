# gemini-prt-sc
Gemini Clipboard Auto Solver là công cụ tự động hóa chạy ẩn trên máy tính. Mỗi khi bạn sử dụng phím tắt chụp màn hình (Win + Shift + S), chương trình sẽ tự động nhận diện hình ảnh từ khay nhớ tạm (Clipboard), gửi dữ liệu đến Gemini API và trả về đáp án kèm lời giải thích ngắn gọn ngay lập tức mà không cần thao tác dán hay mở trình duyệt.
# Gemini Clipboard Auto Solver 🚀

Một công cụ tự động hóa chạy ẩn giúp tự động đọc ảnh câu hỏi từ khay nhớ tạm (Clipboard) và giải bài tập tức thì bằng **Google Gemini API**.

## 📌 Tính năng
* **Tự động nhận diện:** Nhận ảnh tức thì khi sử dụng phím tắt chụp màn hình (`Win + Shift + S`) or PRT
* **Giải nhanh:** Trả về kết quả ngắn gọn bao gồm đáp án đúng và lời giải thích.
* **Hỗ trợ Build Executable:** Có thể đóng gói thành file `.exe` chạy trực tiếp không cần cài Python.

## 🛠️ Cài đặt & Sử dụng

### 1. Yêu cầu hệ thống
* Python 3.9 trở lên
* Gemini API Key từ [Google AI Studio](https://aistudio.google.com/)

### 2. Cài đặt các thư viện cần thiết
```bash
pip install -r requirements.txt
