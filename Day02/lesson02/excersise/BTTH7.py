from typing import Any


def print_name_age(student: dict[str, Any]) -> None:
    print(f"Name: {student.get('name')}\nAge: {student.get('age')}")


def calculate_average_score(student: dict[str, Any]) -> None:
    scores = student.get("scores", [])
    avg_score = sum(scores) / len(scores) if scores else 0.0
    student.update(avg_score=avg_score)


if __name__ == "__main__":
    student: dict[str, Any] = {
        "name": "Nguyen Van A",
        "age": 20,
        "scores": [7.5, 8.0, 6.5, 9.0],
    }

    print_name_age(student)
    calculate_average_score(student)
    print(f"Average Score: {student.get('avg_score')}")
