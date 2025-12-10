def factorial(num: int) -> int:
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


while True:
    n = int(input("Nhập một số nguyên dương: "))
    if n > 0:
        break
    print("Số phải là số nguyên dương (> 0).")

total = 0.0

for i in range(1, n + 1):
    total += 1 / factorial(2 * i - 1)

print(f"Tổng là: {total}")
