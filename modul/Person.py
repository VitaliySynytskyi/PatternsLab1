class Person:
    def __init__(self,name):

        self.surname = name
        self.lisst = []

    def buy_ticket(self, station_a, station_b, transport):
        transport.passengers.append(self.surname)
        self.lisst.append(transport.title)