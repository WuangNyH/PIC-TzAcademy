from typing import Any

if __name__ == "__main__":
    students: dict[str, dict[str, Any]] = {
        "SV01": {"name": "Nguyen Van A", "age": 20},
        "SV02": {"name": "Tran Thi B", "age": 21},
    }

    student_03 = {"name": "Le Van C", "age": 22}
    students["SV03"] = student_03
    print(students)

    students["SV01"]["age"] += 1
    print(students["SV01"])

    for key, value in students.items():
        print(f"{key}: {value.get("name")} ({value.get("age")})")
