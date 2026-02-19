"""Service layer for student management operations."""

from student import Student


class StudentService:
    """Handles in-memory student operations."""

    def __init__(self) -> None:
        self._students: list[Student] = []

    def print_list(self) -> None:
        if not self._students:
            print("No students found.")
            return

        print("Students:")
        for student in self._students:
            print(f"- {student.student_id}: {student.name}")

    def add_student(self, student_id: str, name: str) -> bool:
        for student in self._students:
            if student.student_id == student_id:
                return False

        self._students.append(Student(student_id=student_id, name=name))
        return True

    def remove_student(self, student_id: str) -> bool:
        for student in self._students:
            if student.student_id == student_id:
                self._students.remove(student)
                return True
        return False
