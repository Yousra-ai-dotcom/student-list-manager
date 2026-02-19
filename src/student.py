"""Student model used by the CLI application."""

from dataclasses import dataclass


@dataclass
class Student:
    """Represents one student.

    Attributes:
        student_id: Unique identifier of the student (for example "1" or "42").
        name: Display name of the student.
    """

    student_id: str
    name: str
