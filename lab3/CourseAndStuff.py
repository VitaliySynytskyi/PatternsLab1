from datetime import date, datetime
from typing import List, Any
from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Group:
    id: int
    title: str
    student_list: list
    department_id: int

@dataclass
class PersonalInfo:
    """Data class with personal information"""

    id: int
    name: str
    adress: str
    phone_number: str
    email: str
    position: int
    rank: str
    salary: float

    @property
    def first_name(self) -> str:
        return self.name.split()[0]

    @property
    def last_name(self) -> str:
        return self.name.split()[1]


class Department:
    def __init__(self, title: str):
        self.title = title
        self.students: List[Student] = []
        self.professors: List[Professor] = []
        self.courses: List[Course] = []
        self.requests: List[str] = []
        self.ill_person: List[str] = []

    def get_ill_person(self):
        """Return a list of ill person"""
        return self.ill_person

    def get_requests(self):
        """Return a list of requests"""
        return self.requests


class Staff(ABC):
    def __init__(self, _pesonal_info: PersonalInfo):
        self._persoanl_info = _pesonal_info

    @abstractmethod
    def ask_sick_leave(self, department: Department) -> bool:
        pass

    @abstractmethod
    def send_request(self, department: Department) -> bool:
        pass


class CourseProgress:
    """This class represents course progress

    Attributes:
        received_marks (dict): Marks received by a student
    """

    def __init__(self,
                 received_marks: dict
                 ) -> None:
        """CourseProgress initializer"""
        self.received_marks = received_marks
        self.visited_lectures = 0
        self.completed_assigments = {}
        self.notes = {}

    def get_progress_to_date(self, date: date) -> float:
        """Progress to date

        Args:
            date (datetime): Current date by which to look for marks.

        Returns:
            The sum of points is divided by the number of grades before that date.
        """

        assignments = [value for key,
                       value in self.completed_assigments.items() if key <= date]
        marks = []
        for assignment in assignments:
            marks.append(assignment.get('mark'))
        return sum(marks) / len(marks)

    def get_final_mark(self) -> None:
        """Progress to final

        Args:
            None.

        Returns:
            The sum of points is divided by the final number of marks.
        """

        assignments = [value for key,
                       value in self.completed_assigments.items()]
        marks = []
        for assignment in assignments:
            marks.append(assignment.get('mark'))
        return sum(marks) / len(marks)

    def fill_notes(self, date: date, note: str) -> None:
        """A note for the date is attached

        Args:
            date (date): Date of adding the note
            note (str): Note that is attached

        Returns:
            None.
        """

        self.notes.update({date: note})

    def remove_note(self, date: date):
        """A note for the date is deleted

        Args:
            date (date): Date to delete the note

        Returns:
            None.
        """

        del self.notes[date]



class Course:
    def __init__(
        self,
        title: str,
        star_date: datetime,
        end_date: datetime,
        description: str,
        lectures: list[str],
        assigments: list[str],
        limit: int,
    ):
        self.title = title
        self.start_date = star_date
        self.end_date = end_date
        self.description = description
        self.lectures = lectures
        self.assigments = assigments
        self.limit = limit
        self.students = []
        self.seminars: List[int] = []

    def check_students(self):
        """Returns the list of students enrolled in the course"""
        return self.students

    @abstractmethod
    def add_student(Student):
        pass

    @abstractmethod
    def remove_student(Student):
      pass
    


class Seminar:
    def __init__(
        self,
        id: int,
        title: str,
        deadline: datetime,
        assignments: List[dict],
        status: Any,
        related_course: str,
    ):
        pass

    def implement_item(item_name: str) -> str:
        pass


class Student(Staff):
    def __init__(
        self,
        name: str,
        address: str,
        phone_number: str,
        email: str,
        course_progress: CourseProgress,
    ):
        self._personal_info = PersonalInfo(
            None, name, None, None, None, None, None, None
        )
        self.average_mark = 0.0
        self.course_progress = course_progress
        self.courses = []

    def ask_sick_leave(self, department: Department):
        """Add student name to list of ill person and allow not to go to class"""
        department.ill_person.append(f"student {self._personal_info.first_name} is ill")
        print(f"{self._personal_info.first_name} you can not go to class today")

    def send_request(self, department: Department):
        """Add student request to list of requests"""
        reques = input("Write your request:")
        department.requests.append(
            f"Student {self._personal_info.first_name} want to {reques}"
        )

    def taken_course(self):
        """Returns the courses for which the student is enrolled"""
        return self.courses


class PostGraduateStudent(Student):
    def __init__(self, phd_status: str):
        self.phd_status = phd_status


class Professor:
    def __init__(
        self, name: str, address: str, phone_numer: str, email: str, salary: float
    ):
        self._personal_info = PersonalInfo(
            None, name, None, None, None, None, None, None
        )

    def check_assignment(self, assigment: dict):
        """Checks the assignment and assigns a grade for it"""
        if assigment["is_done"]:
            assigment["mark"] = 5.0
        else:
            assigment["mark"] = 1.0
        print(f"{self._personal_info.first_name} check your assigment")
        print(f"Your mark:{assigment['mark']}")

    def request_support(self, department: Department):
        """Add professor request to list of requests"""
        request = input("Write your request:")
        department.requests.append(
            f"Professor {self._personal_info.first_name} want to {request}"
        )

    def add_postgraduate_student(self, student: PostGraduateStudent):
        self.postgraduate_student.append(id)
        del self.course_students[id]

    def ask_sick_leave(self, department: Department) -> bool:
        """Add professor name to list of ill person and allows not to conduct the lesson if he finds a replacement"""
        department.ill_person.append(
            f"Professor {self._personal_info.first_name} is ill"
        )
        print(f"{self._personal_info.first_name} you must find a replacement")

    def send_request(self, department: Department) -> bool:
        """Add professor request to list of requests"""
        request = input("Write your request:")
        department.requests.append(
            f"Professor {self._personal_info.first_name} want to {request}"
        )


class Enrollment:
    @staticmethod
    def enroll(course: Course, student: Student):
        """If there are places for the course add student name to list of students on the course and course title to list of courses"""
        if (
            course.limit > len(course.students)
            and student._personal_info.name not in course.students
        ):
            course.students.append(student._personal_info.name)
            student.courses.append(course.title)
            print(
                f"Student {student._personal_info.name} has been added to the course {course.title}"
            )
        else:
            print("Too many students or this student is already in the course")

    @staticmethod
    def unenroll(course: Course, student: Student):
        """Remove students from the course and course title from students courses"""
        course.students.remove(student._personal_info.name)
        student.courses.remove(course.title)
        print(f"{student._personal_info.name} remove from course {course.title}")

class Math(Course):
    def __init__(self, title:str,
                 assignments: list[str],   students_limit: int):
        self.title = title
        self.limit = students_limit
        self.assignments = assignments
        self.students: Student = []
        self.seminars: List = []
        
        #function for adding students into the list

    def add_student(self, student: List):

        if self.limit > len(self.students):
            student.courses.append(self.title)
            self.students.append(student)
            Enrollment.enroll(student, self)
            print(f"Student {student.name} has been added to the course {self.title}")
        else:
            print(f"Too many students in {self.title} course")

        # function for removing students from list

    def delete_student(self, student):
        student.unenroll(self.title)
        self.students.remove(student)
        print(f"student {student.name} are removed from the {self.title} !")

class Programming(Course):
    def __init__(self, title: str,
                 assignments: list[str],  students_limit: int):
        self.title = title
        self.limit = students_limit
        self.assignments = assignments
        self.students: Student = []
        self.seminars: List = []
        
        #function for adding students into the list

    def add_student(self, student: List):

        if self.limit > len(self.students):
            student.courses.append(self.title)
            self.students.append(student)
            Enrollment.enroll(student, self)
            print(f"Student {student.name} has been added to the course {self.title}")
        else:
            print(f"Too many students in {self.title} course")

        # function for removing students from list

    def delete_student(self, student):
        student.unenroll(self.title)
        self.students.remove(student)
        print(f"student {student.name} are removed from the {self.title} !")

class Algorithms(Course):
    def __init__(self, title:str,
                 assignments: list[str],   students_limit: int):
        self.title = title
        self.limit = students_limit
        self.assignments = assignments
        self.students: Student = []
        self.seminars: List = []
        
        #function for adding students into the list
    def add_student(self, student: List):

        if self.limit > len(self.students):
            student.courses.append(self.title)
            self.students.append(student)
            Enrollment.enroll(student, self)
            print(f"Student {student.name} has been added to the course {self.title}")
        else:
            print(f"Too many students in {self.title} course")

        # function for removing students from tbe list

    def delete_student(self, student):
        student.unenroll(self.title)
        self.students.remove(student)
        print(f"student {student.name} are removed from the {self.title} !")

class MathProfessor(Professor):
    """Math professor method of professor class"""
    def create_course(self,  math:Math) -> Course:
        if math.title=='Math':
            Professor.create_course(self)
            print(f"{math.title} course created by {self.first_name} {self.second_name}")
            return f"{math.title} course created by {self.first_name} {self.second_name}"
        else:
            print(f"{math.title} is wrong course title")
            return f"{math.title} is wrong course title"


class ProgrammingProfessor(Professor):
    """Programming professor method of professor class"""
    def create_course(self,  prog:Programming) -> Course:
        if prog.title=='Programming':
            Professor.create_course(self)
            print(f"{prog.title} course created by {self.first_name} {self.second_name}")
            return f"{prog.title} course created by {self.first_name} {self.second_name}"
        else:
            print('{prog.title} is wrong course title')

class AlgorithmsProfessor(Professor):
    """Algorithms professor method of professor class"""
    def create_course(self,  algo:Algorithms) -> Course:
        if algo.title=='Algorithms':
            Professor.create_course(self)
            print(f"{algo.title} course created by {self.first_name} {self.second_name}")
            return f"{algo.title} course created by {self.first_name} {self.second_name}"
        else:
            print(f"{algo.title} is wrong course title")
