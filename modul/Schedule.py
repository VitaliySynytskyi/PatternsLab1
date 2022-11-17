from collections import defaultdict

class Schedule:
    """Class represents schedule of tickets
    Arguments:
        title (str): Just name of Schedule.
    Methods:
        print_schedule () -> None:
            Print string of schedule based on tickets.
    """
    def __init__(self, title):
        self.title = title
        self.timetable = defaultdict(list)

    def print_schedule(self):
        print(self.timetable)