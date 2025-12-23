from sqlalchemy import String, Text, Integer
from sqlalchemy.orm import Mapped, mapped_column

from enums import Priority
from models import Base, TimeMixin


class Todo(Base, TimeMixin):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    priority: Mapped[Priority] = mapped_column(
        Integer, nullable=False, default=Priority.MEDIUM
    )
    done: Mapped[bool] = mapped_column(nullable=False, default=False)
