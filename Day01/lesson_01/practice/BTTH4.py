# BTTH4: Tính tổng từ 1 đến n
n = 0
tong = 0

while n <= 0:
    n = int(input("Nhập một số nguyên dương n: "))
    if n <= 0:
        print("Vui lòng nhập số nguyên dương lớn hơn 0.")

for i in range(1, n + 1):
    tong += i

print(f"Tổng từ 1 đến {n} là: {tong}")
