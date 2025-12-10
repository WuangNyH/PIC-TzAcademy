# BTTH7: Viết lại các bài tập đã làm bằng hàm
# 7a. Hàm tính tổng từ 1 đến n
def sum_to_n(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


# 7b. Hàm kiểm tra năm nhuận
def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# 7c. Hàm đếm ký tự
def count_char(string: str, char: str) -> int:
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count


x = int(input("Nhập một số nguyên dương n: "))
print(f"Tổng từ 1 đến {x} là: {sum_to_n(x)}")

nam = int(input("Nhập một năm: "))
if is_leap_year(nam):
    print(f"{nam} là năm nhuận.")
else:
    print(f"{nam} không phải là năm nhuận.")

s = input("Nhập một chuỗi ký tự: ")
c = input("Nhập một ký tự để đếm: ")
print(f"Số lần xuất hiện của ký tự '{c}' trong chuỗi là: {count_char(s, c)}")
