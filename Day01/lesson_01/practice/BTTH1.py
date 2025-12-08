# BTTH1: Kiểm tra tuổi
age = int(input("Nhập tuổi: "))

if age < 0:
    print("Tuổi không hợp lệ")
elif age <= 11:
    print("Trẻ em")
elif age <= 17:
    print("Thiếu niên")
elif age <= 30:
    print("Thanh niên")
else:
    print("Người già")
