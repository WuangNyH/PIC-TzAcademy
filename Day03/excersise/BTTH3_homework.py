def print_menu():
    print("Chọn chức năng:\n")
    print("1. Đọc toàn bộ file (read)")
    print("2. Đọc từng dòng (readline)")
    print("3. Ghi đè file (write)")
    print("4. Ghi thêm vào file (append)")
    print("5. Thoát")

def read_file(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    return content
