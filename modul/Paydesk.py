from collections import defaultdict

class Casa:
    def __init__(self):
        self.lisst = defaultdict(list)

    def buy_ticket(self, client, station_a, station_b):
        self.lisst[client].append(station_a)
        transport = station_a.transports[0]
        transport.passengers.append(client)

