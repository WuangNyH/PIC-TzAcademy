def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_in_month(month: int, year: int) -> int:
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if month in (4, 6, 9, 11):
        return 30
    if month == 2:
        return 29 if is_leap_year(year) else 28
    return -1


def next_date(day: int, month: int, year: int) -> tuple[int, int, int]:
    d = day + 1
    m = month
    y = year
    if d > days_in_month(m, y):
        d = 1
        m += 1
        if m > 12:
            m = 1
            y += 1
    return d, m, y


def previous_date(day: int, month: int, year: int) -> tuple[int, int, int]:
    d = day - 1
    m = month
    y = year
    if d < 1:
        m -= 1
        if m < 1:
            m = 12
            y -= 1
        d = days_in_month(m, y)
    return d, m, y


def format_date(dmy: tuple[int, int, int]) -> str:
    d, m, y = dmy
    return f"{d:02d}-{m:02d}-{y:04d}"


while True:
    year = int(input("Nhập năm: "))
    if year > 0:
        break
    print("Năm phải là số dương (> 0).")

while True:
    month = int(input("Nhập tháng: "))
    if 1 <= month <= 12:
        break
    print("Tháng phải nằm trong khoảng 1 và 12.")

while True:
    day = int(input("Nhập ngày: "))
    max_day = days_in_month(month, year)
    if 1 <= day <= max_day:
        break
    print(f"Ngày phải nằm trong khoảng 1 và {max_day} cho tháng {month} năm {year}.")

next_dmy = next_date(day, month, year)
prev_dmy = previous_date(day, month, year)

print("Ngày đã nhập   :", format_date((day, month, year)))
print("Ngày trước đó   :", format_date(prev_dmy))
print("Ngày kế tiếp    :", format_date(next_dmy))
