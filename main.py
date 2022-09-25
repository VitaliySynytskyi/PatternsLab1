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
        if course in self.courses:
            print("".concat(self.full_name, " currently enroll this course"))   
        else:
            self.courses = self.courses.append(course)
            print("".concat(self.full_name, " enrolled this course"))
        

    def unenroll(self, course) -> None:
        if not(course in self.courses):
            print("".concat(self.full_name, " currently unenrolled this course")) 
        else:
            self.courses = self.courses.pop(course)
            print("".concat(self.full_name, " unenrolled this course"))
        


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

    def fill_notes(self, date: date, note: str) -> None:
        date = datetime.now()
        self.notes.append({date: note})

    def remove_note(self, date: date):
        if self.notes.index(date):
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
        if (assignment.is_done):
            print("Assignment is done. You can get your mark: 5.")
        else:
            print("Assignment isn't done. You can't get your mark.")


if __name__ == "__main__":
    Professor1 = Professor("Andriy", "Tarnavskogo", "291-302-0543", "someProfessor@gmail.com", 5000)
    print(vars(Professor1))
# create 2 students
    VStudent = Student("Vitaliy Syn", "Doroshenka 50", "0971275232", "olehmuz87@gmail.com", 999, 11.5)
    VStudent2 = Student("Vitaliy Syn", "Doroshenka 50", "0971275232", "olehmuz87@gmail.com", 999, 11.5)
# create course
    DesignPatterns = Course("DesignPatterns",
                 date(2022, 10, 10),
                 date(2023, 10, 10),
                 "DesignPatterns",
                 [],
                 [],
                 5)
# create DesignPatterns Progress and check methods of it;
    DesignPatternsProgress = CourseProgress([], 0, [], [])
# create new note
    DesignPatternsProgress.fill_notes(date(2022, 12, 10), "1231")
    print(vars(DesignPatternsProgress))
# remove this note
    DesignPatternsProgress.remove_note(date(2022, 12, 10))
    print(vars(DesignPatternsProgress))
# check methods of Course class
# /add new student to course
    DesignPatterns.add_student(VStudent)
    print(vars(DesignPatterns))
# add another one, but limit 1 stop adding;
    DesignPatterns.add_student(VStudent2)
# limit test
    DesignPatterns.add_student(VStudent2)
# removing of student
    DesignPatterns.remove_student(VStudent)
    print(vars(DesignPatterns))
# Student methods
    VStudent2.can_enroll(DesignPatterns)
    VStudent2.enroll(DesignPatterns)
    print(vars(VStudent2))
    VStudent2.unenroll(DesignPatterns)
    print(vars(VStudent2))