def print_menu() -> None:
    print("Menu:\n")
    print("1. Xin chào")
    print("2. Tính chỉ số BMI")
    print("3. Thoát")

def greet() -> None:
    print("Xin chào! Chúc bạn một ngày tốt lành!")

def calculate_bmi() -> None:
    print("Mẹo mày bé!")

if __name__ == "__main__":
    while True:
        try:
            print_menu()
            choice = int(input("Vui lòng chọn một tùy chọn (1-3): "))

            if choice < 1 or choice > 3:
                print("Lựa chọn hợp lệ là từ 1 đến 3, vui lòng thử lại.")
                continue

            if choice == 1:
                greet()
            elif choice == 2:
                calculate_bmi()
            elif choice == 3:
                print("Thoát chương trình. Tạm biệt!")
                exit()
        except ValueError:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")
