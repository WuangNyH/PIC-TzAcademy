from datetime import datetime


class Task:
    def __init__(self, description: str, due_date: datetime, status: str = "todo"):
        self.description = description
        self.due_date = due_date
        self.status = status

    def is_overdue(self, now: datetime) -> bool:
        return now > self.due_date and self.status != "done"

    def __str__(self) -> str:
        return f"[{self.status.upper()}] {self.description} (Hạn: {self.due_date.strftime('%Y-%m-%d')})"
