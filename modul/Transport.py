class Transport:
    """Represents of information about 'Transport'.
    Arguments:
        title (str): Name of 'Transport'.
        max_size_of_passengers (int): Limit of passengers in 'Transport'.
    """
    def __init__(self, title, max_size_of_passengers):
        self.title = title
        self.passengers = []

class Bus(Transport):
    def print_busname(title):
        print(title)

