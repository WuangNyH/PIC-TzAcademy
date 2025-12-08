# BTTH5: Đếm số ký tự 'a' trong chuỗi
string = input("Nhập một chuỗi: ")
count_a = 0

for c in string:
    if c.lower() == 'a':
        count_a += 1

print(f"Số ký tự 'a' trong chuỗi là: {count_a}")
