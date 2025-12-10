# BTTH8: Viết hàm định dạng tên với optional middle name
def format_name(first: str, last: str, middle: str | None = None) -> str:
    if middle:
        return f"{first} {middle} {last}"

    return f"{first} {last}"


first_name = input("Nhập tên: ")
last_name = input("Nhập họ: ")
middle_name = input("Nhập tên đệm (nhấn Enter nếu không có): ")

print("Tên đầy đủ là:", format_name(first_name, last_name, middle_name))
