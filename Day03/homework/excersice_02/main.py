from homework.excersice_02.student_services import (
    load_students_from_file,
    calc_avg_score,
    find_top_student,
    filter_failed,
)

if __name__ == "__main__":
    filename = input("Nhập tên file điểm sinh viên: ")

    students = load_students_from_file(filename)

    if students is None:
        exit()

    while True:
        print("\n1. Điểm trung bình lớp")
        print("2. Sinh viên điểm cao nhất")
        print("3. Danh sách sinh viên bị rớt")
        print("4. Thoát")

        try:
            choice = int(input("Chọn chức năng (1-4): "))

            if choice < 1 or choice > 4:
                raise ValueError

        except ValueError:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
            continue

        if choice == 1:
            avg_score = calc_avg_score(students)
            print(f"Điểm trung bình lớp: {avg_score:.2f}")

        elif choice == 2:
            if not students:
                print("Không có sinh viên trong danh sách.")
                continue

            top_student = find_top_student(students)
            print(f"Sinh viên có điểm cao nhất: {top_student}")

        elif choice == 3:
            if not students:
                print("Không có sinh viên trong danh sách.")
                continue

            failed_students = filter_failed(students)

            if not failed_students:
                print("Không có sinh viên bị rớt.")
            else:
                print("Danh sách sinh viên bị rớt:")
                for student in failed_students:
                    print(student)

        elif choice == 4:
            exit()
