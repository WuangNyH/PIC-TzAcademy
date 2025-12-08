# BTTH3: Kiểm tra năm nhuận
year = int(input("Nhập vào một năm: "))

if (year < 0):
    print("Năm không hợp lệ. Vui lòng nhập một năm dương.")

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} là năm nhuận.")
else:
    print(f"{year} không phải là năm nhuận.")
