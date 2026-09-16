import os
import time
from PIL import ImageGrab, Image
from google import genai

# Thay trực tiếp API Key của bạn vào giữa 2 dấu ngoặc kép bên dưới
API_KEY = "AIzaSy..." 

client = genai.Client(api_key=API_KEY)
last_image = None

print("==================================================")
print("   GEMINI CLIPBOARD AUTO SOLVER")
print("==================================================")
print("[*] Đang lắng nghe khay nhớ tạm (Clipboard)...")
print("[*] Nhấn (Win + Shift + S) để chụp câu hỏi trên màn hình.")
print("[*] Nhấn Ctrl + C trong cửa sổ này để dừng chương trình.\n")

while True:
    try:
        img = ImageGrab.grabclipboard()
        
        if isinstance(img, Image.Image) and img != last_image:
            last_image = img
            print("[+] Đã phát hiện ảnh mới! Đang xử lý qua Gemini API...")

            prompt = (
                "Hãy đọc và giải câu hỏi trong ảnh theo cấu trúc:\n"
                "1. Đáp án đúng: [Chọn đáp án]\n"
                "2. Giải thích ngắn gọn trong 1-2 câu."
            )

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[img, prompt]
            )

            print("\n---------------- KẾT QUẢ ----------------")
            print(response.text)
            print("-----------------------------------------\n")

    except KeyboardInterrupt:
        print("\n[*] Đã dừng chương trình.")
        break
    except Exception as e:
        print(f"[!] Lỗi: {e}")
        
    time.sleep(1)
