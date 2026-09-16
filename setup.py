import os
import sys
import subprocess

def run_cmd(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr

def install_all():
    print("==========================================================")
    print("   BỘ CÀI ĐẶT TÀI NGUYÊN TỰ ĐỘNG - GEMINI AUTO SOLVER")
    print("==========================================================")
    print()

    packages = ["google-genai", "pillow", "pyinstaller"]
    
    # 1. Thử nâng cấp pip
    print("[*] Đang cập nhật pip...")
    run_cmd(f'"{sys.executable}" -m pip install --upgrade pip')

    # 2. Lần lượt thử các kiểu lệnh cài đặt
    print("[*] Đang tiến hành cài đặt các thư viện cần thiết...\n")
    
    methods = [
        f'"{sys.executable}" -m pip install',
        f'"{sys.executable}" -m pip install --user',
        'pip install',
        'pip install --user'
    ]

    success = False
    for pkg in packages:
        pkg_installed = False
        print(f"--> Đang cài đặt {pkg}...")
        
        for method in methods:
            cmd = f"{method} {pkg}"
            ok, out = run_cmd(cmd)
            if ok:
                print(f"    [✔] Cài đặt thành công: {pkg}")
                pkg_installed = True
                break
        
        if not pkg_installed:
            print(f"    [✘] Lỗi cài đặt {pkg}")

    print("\n==========================================================")
    print("   [✔] HOÀN TẤT QUÁ TRÌNH CÀI ĐẶT!")
    print("==========================================================")
    input("\nNhấn phím Enter để thoát...")

if __name__ == "__main__":
    install_all()
