# a. Dùng vòng lặp + unpacking tuple để in ra danh sách học viên theo format
def print_student_info(list_students: list[tuple]) -> None:
    for student_id, name, age in list_students:
        print(f"{student_id} - {name} ({age})")


# b. Tạo một list mới python_scores chỉ chứa tuple (student_id, name, python_score)
def get_python_scores(list_students: list[tuple], list_scores: dict) -> list[tuple]:
    python_scores = []

    for student_id, name, age in list_students:
        if student_id in list_scores and "python" in list_scores[student_id]:
            score = list_scores[student_id]["python"]
            python_scores.append((student_id, name, score))

    return python_scores


# c. Tìm học viên có điểm Python cao nhất từ python_scores và in ra: Top Python: <name> - <score>
def get_top_python_student(python_scores: list[tuple]) -> tuple:
    top_student = python_scores[0]

    for student in python_scores[1:]:
        if student[2] > top_student[2]:
            top_student = student

    return top_student


# d. Thêm môn mới "database" vào courses (dùng set) và gán tạm điểm database = 0 cho tất cả sinh viên trong scores
def add_course(set_courses: set, dict_scores: dict, new_course: str) -> None:
    set_courses.add(new_course)

    for student_id in dict_scores:
        dict_scores[student_id][new_course] = 0.0


if __name__ == "__main__":
    students = [
        ("SV01", "Nguyen Van A", 20),
        ("SV02", "Tran Thi B", 21),
        ("SV03", "Le Van C", 19),
    ]

    scores = {
        "SV01": {"math": 8.0, "python": 7.5},
        "SV02": {"math": 6.5, "python": 8.5},
        "SV03": {"math": 9.0, "python": 9.5},
    }

    courses = {"math", "python"}

    print("Student Information:")
    print_student_info(students)

    python_scores = get_python_scores(students, scores)
    print("\nPython Scores:")
    for student_id, name, score in python_scores:
        print(f"{student_id} - {name}: {score}")

    print("\nTop Python Student:")
    top_student = get_top_python_student(python_scores)
    print(f"Top Python: {top_student[1]} - {top_student[2]}")

    print("\nAdd 'database' course:")
    add_course(courses, scores, "database")
    print("Updated Courses:", courses)
    print("Updated Scores:")
    for student_id, score_dict in scores.items():
        print(f"{student_id}: {score_dict}")
