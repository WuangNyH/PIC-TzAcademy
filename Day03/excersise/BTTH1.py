if __name__ == "__main__":
    while True:
        try:
            num = int(input("Nhập số: "))
            print(f"Bạn đã nhập: {num}")
            break
        except ValueError:
            print("Nhập sai, vui lòng nhập lại")
