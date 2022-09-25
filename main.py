from __future__ import annotations

from typing import List
from datetime import date, datetime


class Student:
    """This class represents student object

    Attributes:
        full_name (str): Full name of the student.
        address (str): Student adress.
        phone_number (str): student's number.
        
    """
    def __init__(self,
                 full_name: str,
                 address: str,
                 phone_number: str,
                 email: str) -> None:
        """Student initializer"""
        self.full_name = full_name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.average_mark = 0.0
        self.courses: List[Course] = []

    def taken_courses(self) -> List[Course] | None:
        if self.courses:
            return self.courses
        else:
            print("Немає курсів")

    def enroll(self, course: Course) -> None:
        """Stands for enrolling current student into course

        Args:
            course (Course): Course to be enrolled.

        Returns:
            None.
            
        """

        if course in self.courses:
            print(self.full_name, " currently enroll this course")  
        else:
            self.courses.append(course)
            print(self.full_name, " enrolled this course")
        

    def unenroll(self, course) -> None:
        if course not in self.courses:
            print(self.full_name, " currently unenrolled this course")
        else:
            self.courses.remove(course)
            print(self.full_name, " unenrolled this course")
        


class CourseProgress:

    def __init__(self,
                 received_marks: dict
                 ) -> None:
        self.received_marks = received_marks
        self.visited_lectures = 0
        self.completed_assigments = {}
        self.notes = {}

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
        self.notes.update({date: note})

    def remove_note(self, date: date):
        if self.notes.index(date):
            self.notes.pop({date: self.note})



class Course:
    LIMIT = 30

    def __init__(self,
                 title: str,
                 start_date: datetime,
                 end_date: datetime,
                 description: str
                 ) -> None:
        self.title = title
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.lectures = []
        self.assigments = []
        self.students: List[Student] = []

    def add_student(self, student: Student) -> None:
        if len(self.students) < Course.LIMIT:
            self.students.append(student)
            student.enroll(course=self)
        else:
            print(f"Limit has been exeeded")

    def remove_student(self, student: Student) -> None:
        self.students.remove(student)
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
    professor1 = Professor("Andriy", "Tarnavskogo", "291-302-0543", "someProfessor@gmail.com", 5000)
    print(vars(professor1))
# create 2 students
    vstudent = Student(full_name="Vitaliy Syn", 
                       address="Doroshenka 50", 
                       phone_number="0971275232", 
                       email="Vitaliy1@gmail.com")
    vstudent2 = Student(full_name="Vitaliy Syn2", 
                       address="Doroshenka 50", 
                       phone_number="0971275232", 
                       email="Vitaliy2@gmail.com")
# create course
    design_patterns = Course("DesignPatterns",
                 date(2022, 10, 10),
                 date(2023, 10, 10),
                 "DesignPatterns")
# create DesignPatterns Progress and check methods of it;
    design_patterns_progress = CourseProgress(received_marks={})
# create new note
    design_patterns_progress.fill_notes(date(2022, 12, 15), "1231")
# remove this note
    # DesignPatternsProgress.remove_note(date(2022, 12, 15))
    # print(vars(DesignPatternsProgress))
# check methods of Course class
# /add new student to course
    design_patterns.add_student(vstudent)
# add another one, but limit 1 stop adding;
    design_patterns.add_student(vstudent2)
# limit test
    #design_patterns.add_student(vstudent2)
# removing of student
# Student methods
    vstudent2.unenroll(design_patterns)
    vstudent2.enroll(design_patterns)
    
    help(Student)
