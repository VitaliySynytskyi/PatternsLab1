from __future__ import annotations

from typing import List, Any
from datetime import date, datetime


class Student:

    def __init__(self,
                 full_name: str,
                 adress: str,
                 phone_number: str,
                 email: str,
                 student_number: int,
                 average_mark: float) -> None:
        self.full_name = full_name
        self.adress = adress
        self.phone_number = phone_number
        self.email = email
        self.student_number = student_number
        self.average_mark = average_mark
        self.courses = []

    def taken_courses(self) -> List[Any] | None:
        if self.courses:
            return self.courses
        else:
            print("None")

    def enroll(self, course) -> None:
        pass

    def unenroll(self, course) -> None:
        pass


class CourseProgress:

    def __init__(self,
                 received_marks: dict,
                 visited_lectures: int,
                 completed_assigments: dict,
                 notes: dict) -> None:
        self.received_marks = received_marks
        self.visited_lectures = visited_lectures
        self.completed_assigments = completed_assigments
        self.notes = notes

    def get_progress_to_date(self,
                             date: datetime) -> float:
        assignments = [value for key, value in self.completed_assigments.items() if key <= date]
        marks = []
        for assignment in assignments:
            marks.append(assignments.get('mark'))
        return sum(marks) / len(marks)

    def get_final_mark(self) -> None:
        assignments = [value for key, value in self.completed_assigments.items()]
        marks = []
        for assignment in assignments:
            marks.append(assignments.get('mark'))
        return sum(marks) / len(marks)

    def fill_notes(self, note: str) -> None:
        date = datetime.now()
        self.notes.update({date: note})

    def remove_note(self, date: datetime):
        if self.notes.get(date):
            self.notes.pop({date: self.note})


class Course:
    LIMIT = 30

    def __init__(self,
                 title: str,
                 start_date: datetime,
                 end_date: datetime,
                 description: str,
                 lectures: list[str],
                 assigments: List[dict],
                 limit: int) -> None:
        self.title = title
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.lectures = lectures
        self.assigments = assigments
        self.limit = limit
        self.students = List[Student]

    def add_student(self, student: Student) -> None:
        number_students = any
        if number_students > self.LIMIT:
            self.students.append(student)
            student.enroll(course=self)

    def remove_student(self, student: Student) -> None:
        number_students = any
        if number_students > self.LIMIT:
            self.students.pop(student)
            student.unenroll(course=self)


class Professor:

    def __init__(self,
                 name: str,
                 address: str,
                 phone_number: str,
                 email: str,
                 salary: float) -> None:
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.salary = salary

    def check_assigment(self, assignment: dict):
        pass
