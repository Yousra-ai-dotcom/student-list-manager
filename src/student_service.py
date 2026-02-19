"""Service layer for student management operations."""

import csv
import json

from student import Student


class StudentService:
    """Handles in-memory student operations.

    This class exposes methods used by the CLI to list, add, remove, and
    export students.
    """

    def __init__(self) -> None:
        """Initializes an empty in-memory student list."""
        self._students: list[Student] = []

    def print_list(self) -> None:
        """Prints all students to stdout.

        Returns:
            None.
        """
        if not self._students:
            print("No students found.")
            return

        print("Students:")
        for student in self._students:
            print(f"- {student.student_id}: {student.name}")

    def add_student(self, student_id: str, name: str) -> bool:
        """Adds a student if the id is unique.

        Args:
            student_id: Unique identifier for the student.
            name: Student display name.

        Returns:
            True if the student was added, False if the id already exists.
        """
        if self._find_by_id(student_id) is not None:
            return False

        self._students.append(Student(student_id=student_id, name=name))
        return True

    def remove_student(self, student_id: str) -> bool:
        """Removes a student by id.

        Args:
            student_id: Id of the student to remove.

        Returns:
            True if the student was found and removed, False otherwise.
        """
        student: Student | None = self._find_by_id(student_id)
        if student is None:
            return False

        self._students.remove(student)
        return True

    def export_students_csv(self, file_path: str) -> None:
        """Exports students to a CSV file.

        Args:
            file_path: Output path for the CSV file.

        Returns:
            None.
        """
        with open(file_path, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["id", "name"])

            for student in self._students:
                writer.writerow([student.student_id, student.name])

    def export_students_json(self, file_path: str) -> None:
        """Exports students to a JSON file.

        Args:
            file_path: Output path for the JSON file.

        Returns:
            None.
        """
        data: list[dict[str, str]] = []
        for student in self._students:
            data.append({"id": student.student_id, "name": student.name})

        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=2, ensure_ascii=False)

    def _find_by_id(self, student_id: str) -> Student | None:
        """Finds a student by id.

        Args:
            student_id: Id to search for.

        Returns:
            The matching Student if found, otherwise None.
        """
        for student in self._students:
            if student.student_id == student_id:
                return student
        return None
