@echo off
chcp 65001 > nul
title Bộ cài đặt tài nguyên tự động - Gemini Auto Solver

echo ==========================================================
echo   BẮT ĐẦU CÀI ĐẶT TÀI NGUYÊN (TỰ ĐỘNG KHẮC PHỤC LỖI)
echo ==========================================================
echo.

:: 1. Thử nâng cấp pip trước
echo [*] Đang kiểm tra và cập nhật pip...
py -m pip install --upgrade pip 2>nul || python -m pip install --upgrade pip 2>nul || pip install --upgrade pip 2>nul

echo.
echo [*] Đang tải các thư viện bắt buộc (google-genai, pillow, pyinstaller)...

:: 2. Thử cách 1: Dùng lệnh 'py'
echo [Cách 1] Thử cài đặt bằng 'py -m pip'...
py -m pip install google-genai pillow pyinstaller
if %errorlevel% equ 0 goto SUCCESS

:: 3. Thử cách 2: Dùng lệnh 'python'
echo.
echo [!] Cách 1 thất bại. [Cách 2] Thử cài đặt bằng 'python -m pip'...
python -m pip install google-genai pillow pyinstaller
if %errorlevel% equ 0 goto SUCCESS

:: 4. Thử cách 3: Dùng lệnh 'pip' trực tiếp
echo.
echo [!] Cách 2 thất bại. [Cách 3] Thử cài đặt bằng 'pip'...
pip install google-genai pillow pyinstaller
if %errorlevel% equ 0 goto SUCCESS

:: 5. Thử cách 4: Cài với cờ --user (Khắc phục lỗi thiếu quyền Admin)
echo.
echo [!] Cách 3 thất bại. [Cách 4] Thử cài đặt với quyền User '--user'...
py -m pip install --user google-genai pillow pyinstaller || python -m pip install --user google-genai pillow pyinstaller
if %errorlevel% equ 0 goto SUCCESS

:FAIL
echo.
echo ==========================================================
echo   [X] CÀI ĐẶT THẤT BẠI! 
echo   Vui lòng kiểm tra lại kết nối Internet hoặc cài lại Python.
echo ==========================================================
goto END

:SUCCESS
echo.
echo ==========================================================
echo   [✔] TẢI VÀ CÀI ĐẶT TÀI NGUYÊN THÀNH CÔNG 100%!
echo   Bây giờ bạn có thể nhấp đôi vào file auto_solver.py để dùng.
echo ==========================================================

:END
pause
