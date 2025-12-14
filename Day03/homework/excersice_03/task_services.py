from datetime import datetime

from homework.excersice_03.task import Task


def load_tasks(filename: str) -> list[Task] | None:
    tasks = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            file.readline()

            for line_number, line in enumerate(file, start=2):

                attributes = line.strip().split(";")
                if len(attributes) != 3:
                    print(
                        f"Cảnh báo: Dòng thứ {line_number} không đúng định dạng, bỏ qua."
                    )
                    continue

                if attributes[2] not in ("todo", "done"):
                    print(
                        f"Cảnh báo: Dòng thứ {line_number} có dữ liệu không hợp lệ, bỏ qua."
                    )
                    continue

                try:
                    task = Task(
                        description=attributes[0],
                        due_date=datetime.strptime(attributes[1], "%Y-%m-%d"),
                        status=attributes[2],
                    )
                except ValueError:
                    print(
                        f"Cảnh báo: Dòng thứ {line_number} có dữ liệu không hợp lệ, bỏ qua."
                    )
                    continue

                tasks.append(task)

            return tasks

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{filename}'.")
    except Exception:
        print(f"Lỗi: Có lỗi xảy ra khi đọc file '{filename}'.")


def save_tasks(filename: str, tasks: list[Task]) -> None:
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("Mô tả;YYYY-MM-DD;trạng_thái\n")

            for task in tasks:
                file.write(
                    f"{task.description};{task.due_date.strftime('%Y-%m-%d')};{task.status}\n"
                )

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{filename}'.")
    except Exception:
        print(f"Lỗi: Có lỗi xảy ra khi đọc file '{filename}'.")


def filter_overdue_tasks(tasks: list[Task], now: datetime) -> list[Task]:
    return [task for task in tasks if task.is_overdue(now)]


def mark_task_as_done(task: Task) -> None:
    task.status = "done"
