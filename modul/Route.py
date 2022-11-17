from collections import defaultdict
import json
import requests

from Schedule import Schedule


class Route:
    def __init__(self, schedule: Schedule):
        self.route_dict = defaultdict(list)
        self.schedule = schedule


    def route_create(self, transport, station_a, station_b):
        self.url_info = requests.get(
            f"https://api.tomtom.com/routing/1/calculateRoute/{station_a.x},{station_a.y}:{station_b.x},{station_b.y}/json?key=lxQBgFn2k02GNm9w5XBmGcrQhZaQmzBQ").text
        self.route_info = json.loads(self.url_info)
