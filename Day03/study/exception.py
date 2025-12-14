# try:
#     # đoạn code có nguy cơ lỗi
#     x = 10 / 0
# except ZeroDivisionError:
#     print("Không thể chia cho 0!")
#
# try:
#     raw = input("Nhập một số nguyên: ")
#     x = int(raw)
#     y = 10 / x
#     print(f"Kết quả 10 / {x} =", y)
# except ValueError:
#     print("Lỗi: Bạn phải nhập một số nguyên hợp lệ!")
# except ZeroDivisionError:
#     print("Lỗi: Không thể chia cho 0!")
# except Exception as e:
#     print("Lỗi không xác định:", e)

filename = input("Nhập tên file: ")

try:
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("File không tồn tại!")
except PermissionError:
    print("Bạn không có quyền đọc file này!")
except Exception as e:
    print("Lỗi khác:", e)
