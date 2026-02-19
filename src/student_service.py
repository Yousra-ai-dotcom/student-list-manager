"""Service layer for student management operations."""

from student import Student


class StudentService:
    """Handles in-memory student operations."""

    def __init__(self) -> None:
        self._students: list[Student] = []

    def print_list(self) -> None:
        pass

    def add_student(self, student_id: str, name: str) -> bool:
        pass

    def remove_student(self, student_id: str) -> bool:
        pass