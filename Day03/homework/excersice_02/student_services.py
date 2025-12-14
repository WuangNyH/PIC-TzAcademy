from typing import Any

from homework.excersice_02.student import Student


def load_students_from_file(filename: str) -> list[Any] | None:
    students = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            file.readline()

            for line_number, line in enumerate(file, start=2):

                attributes = line.strip().split(",")
                if len(attributes) != 3:
                    print(
                        f"Cảnh báo: Dòng thứ {line_number} không đúng định dạng, bỏ qua."
                    )
                    continue

                try:
                    student = Student(
                        name=attributes[0],
                        age=int(attributes[1]),
                        score=float(attributes[2]),
                    )
                except ValueError:
                    print(
                        f"Cảnh báo: Dòng thứ {line_number} có dữ liệu không hợp lệ, bỏ qua."
                    )
                    continue

                students.append(student)

        return students

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{filename}'.")
    except Exception:
        print(f"Lỗi: Có lỗi xảy ra khi đọc file '{filename}'.")


def calc_avg_score(students: list[Student]) -> float:
    if not students:
        return 0.0

    total_score = sum(student.score for student in students)
    return total_score / len(students)


def find_top_student(students: list[Student]) -> Student | None:
    if not students:
        return None

    top_student = max(students, key=lambda student: student.score)
    return top_student


def filter_failed(students: list[Student]) -> list[Student]:
    return [student for student in students if not student.is_passed()]
