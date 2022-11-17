from CourseAndStuff import *

# assigment_1 = {
#     "title": "assigment_1",
#     "deskription": "deskription_1",
#     "is_done": True,
#     "mark": 0.0,
# }
# student1 = Student("Vitaliy Syn", "ds", "dsds", "dsds", None)
# course1 = Course("Programing", None, None, None, None, None, 10)
# professor1 = Professor("Oleh", None, None, None, None)
# department1 = Department("LNU department")
# student1.send_request(department1)
# print(department1.get_requests())
# Enrollment.enroll(course1, student1)
# Enrollment.unenroll(course1, student1)
# course1_progress = CourseProgress(received_marks={})
# course1_progress.fill_notes(date(2022, 10, 11), "1231")
# print(vars(course1_progress))
# course1_progress.remove_note(date(2022, 10, 11))
# print(vars(course1_progress))

assignment2 = {"title": "testing", "description" : "testing", "is_done": False, "mark": 0.0}
student12=Student( 'Vitalii Syn','Lviv','09873947542','vitalii@gmail.com', 4)
course12 = Algorithms('Algorithms', assignment2,  100)
Enrollment.enroll(course12, student12)