from abc import abstractmethod

class InfoStation:
    """Represents of information about 'Depo'.
    Arguments:
        id (int): ID of 'Station'.
        title (str): title where 'Station' located.
        x, y: coordinates of Station
    """
    def __init__(self, id: int, title: str, x, y):
        self.id = id
        self.title = title
        self.x = x
        self.y = y


    @abstractmethod
    def personal_manage(self):
        pass

class Station(InfoStation):
    def __init__(self, id: int, title: str, x, y):
        self.id = id
        self.title = title
        self.x = x
        self.y = y
        self.transports = []

    def print_station(self):
        print(self.id, self.title, self.x, self.y)

    def route_manage(self, town_a, town_b, distance, truck):
        pass

    def personal_manage(self, passengers, staff):
        pass

