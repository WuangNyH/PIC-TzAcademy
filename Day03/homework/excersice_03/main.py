from datetime import datetime

from homework.excersice_03.task import Task
from homework.excersice_03.task_services import (
    load_tasks,
    filter_overdue_tasks,
    save_tasks,
    mark_task_as_done,
)

FILENAME = "tasks.txt"


def get_tasks() -> list[Task]:
    tasks = load_tasks(FILENAME)

    if tasks is None:
        tasks = []

    return tasks


def display_tasks(tasks: list[Task]) -> None:
    if not tasks:
        print("Không có task nào.")
        return

    print("Danh sách các task:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def save() -> None:
    tasks = get_tasks()
    save_tasks(FILENAME, tasks)


if __name__ == "__main__":
    while True:
        print("\n1. Xem tất cả các task")
        print("2. Xem các task hết hạn")
        print("3. Thêm task mới")
        print("4. Đánh dấu task đã hoàn thành")
        print("5. Thoát")

        try:
            choice = int(input("Chọn chức năng (1-5): "))

            if choice < 1 or choice > 5:
                raise ValueError

        except ValueError:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
            continue

        if choice == 1:
            tasks = get_tasks()
            display_tasks(tasks)

        elif choice == 2:
            tasks = get_tasks()

            if not tasks:
                print("Không có task nào.")
                continue

            now = datetime.now()
            overdue_tasks = filter_overdue_tasks(tasks, now)
            display_tasks(overdue_tasks)

        elif choice == 3:
            description = input("Nhập mô tả task: ")
            due_date = None

            while True:
                due_date_str = input("Nhập hạn hoàn thành (YYYY-MM-DD): ")

                try:
                    due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Định dạng ngày không hợp lệ. Vui lòng thử lại.")
                    continue

            new_task = Task(description=description, due_date=due_date)
            tasks = get_tasks()
            tasks.append(new_task)
            save_tasks(FILENAME, tasks)
            print("Đã thêm task mới.")

        elif choice == 4:
            tasks = get_tasks()
            display_tasks(tasks)

            try:
                task_idx = int(input("Chọn số thứ tự của task đã hoàn thành: ")) - 1

                if task_idx < 0 or task_idx >= len(tasks):
                    raise ValueError

            except ValueError:
                print("Lựa chọn không hợp lệ.")
                continue

            mark_task_as_done(tasks[task_idx])
            save_tasks(FILENAME, tasks)
            print("Đã đánh dấu task là hoàn thành.")

        elif choice == 5:
            exit()
