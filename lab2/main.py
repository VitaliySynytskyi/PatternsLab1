"""Assignment2"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, List
from datetime import date, datetime
from collections import defaultdict


class Student:
    """This class represents student object

    Attributes:
        full_name (str): Full name of the student.
        address (str): Student's address.
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

    def get_taken_courses(self, enrollment) -> List[str]:
        return enrollment.student_courses[self.id]


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
        self.completed_assignments = {}
        self.notes = {}

    def get_progress_to_date(self, date: date) -> float:
        """Progress to date

        Args:
            date (datetime): Current date by which to look for marks.

        Returns:
            The sum of points is divided by the number of grades before that date.
        """

        assignments = [value for key,
                                 value in self.completed_assignments.items() if key <= date]
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
                                 value in self.completed_assignments.items()]
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
    """This class represents course object

    Attributes:
        title (str): Tittle of the course
        start_date (datetime): Start date of the course
        end_date (datetime): End date of the course
        description (str): Description of the course
    """
    LIMIT = 30

    def __init__(self,
                 title: str,
                 start_date: datetime,
                 end_date: datetime,
                 description: str,
                 ) -> None:
        """Course initializer"""
        self.title = title
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.lectures = []
        self.assignments = []
        self.students: List[Student] = []
        self.seminars: List[int]

    def get_student_ids(self, enrollment) -> List[int]:
        return enrollment.course_students[self.title]


class Professor:
    """This class represents course object

    Attributes:
        name (str): Name of the professor.
        address (str): Professor's address
        phone_number (str): Professor's phone number
        email (str): Professor's email
        salary (float): Professor's salary
    """

    def __init__(self,
                 name: str,
                 address: str,
                 phone_number: str,
                 email: str,
                 salary: float) -> None:
        """Professor initializer"""
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.salary = salary

    def check_assigment(self, assignment: dict):
        """Checking the task and assessment

        Args:
            assignment (dict): The task to be checked

        Returns:
            None.
        """

        if assignment.is_done:
            print("Assignment is done. You can get your mark: 5.")
        else:
            print("Assignment isn't done. You can't get your mark.")


@dataclass
class PersonalInfo:
    id: int
    full_name: str
    address: str
    phone_number: str
    email: str
    position: int
    rank: str
    salary: float

    @property
    def first_name(self) -> str:
        return self.full_name.split()[0]

    @property
    def last_name(self) -> str:
        return self.full_name.split()[1]


class Department:
    """This class represents student object

    Attributes:
    title (str):
    students (List[Student]):
    professors (List[Professor]):
    courses (List[str]):   course names
    requests (dict(str, bool)):  contains requests from the staff
    """

    title: str
    students: List[Student]
    professors: List[Professor]
    courses: List[str]  # course names
    requests: dict(str, bool)  # contains requests from the staff

    def proceed_requests(self, request: str) -> Any:
        if request in self.requests:
            self.requests[request] = True
            print(f"Request - {self.requests[request]} is done")
            return True

        print(f"Request {request} not found")
        return False


class Staff:
    personal_info: PersonalInfo

    def ask_sick_leave(self, department: Department) -> bool:
        department.requests.update("Ask for leave", False)
        return False

    def send_request(self, department: Department, request: str) -> bool:
        department.requests.update(request, False)
        return True

class Student(Staff):
    def send_request(self, department: Department, request: str) -> bool:
        department.requests.update(request, False)
        return True

    def ask_sick_leave(self, department: Department) -> bool:
        department.requests.update("Ask for leave", False)
        return False


class Seminar:
    id: int
    title: str
    deadline: datetime
    assignments: List[dict]
    status: Any
    related_course: str  # course name

    def implement_item(self, item_name: str) -> str:
        pass

    def add_comment(self, comment: str) -> None:
        pass


class Enrollment:

    def __init__(self) -> None:
        self.student_courses = defaultdict(list)
        self.course_students = defaultdict(list)
        self.postgraduate_student = defaultdict(list)

    def enroll(self, student_id: int, course_title: str) -> None:

        if student_id in self.student_courses:
            print(self.full_name, " currently enroll this course")
        else:
            self.student_courses[student_id].append(course_title)
            self.course_students[course_title].append(student_id)
            print(self.full_name, " enrolled this course")

    def unenroll(self, student_id: int, course_title: str) -> None:

        if student_id not in self.student_courses:
            print(self.full_name, " currently unenrolled this course")
        else:
            del self.student_courses[course_title]
            del self.course_students[student_id]
            print(self.full_name, " unenrolled this course")


class Professor(Staff):
    def send_request(self, department: Department, request: str) -> bool:
        department.requests.update(request, False)
        return True

    def ask_sick_leave(self, department: Department) -> bool:
        department.requests.update("Ask for leave", False)
        return False

    def add_postgraduate_student(self, student_id: int) -> None:
        self.postgraduate_student.append(student_id)
        del self.course_students[student_id]

    def request_support(self, request: str) -> None:
        pass



def main():
    """main function"""

    personal_info1 = PersonalInfo(1, "first last", "address", "43 43 43", "email", "position", "rank", 4343.0)
    course2 = Course("Fundamentals of C#", '01-01-2020', '01-05-2020', "5456")
    professor2 = Professor("Dima")
    course2.Professor = professor2
    print(personal_info1.first_name, personal_info1.last_name, sep=" ")

    # help(Student)


if __name__ == "__main__":
    main()
