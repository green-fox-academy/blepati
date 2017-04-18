from aircraft import Aircraft
from aircraft import F16
from aircraft import F35

class Carrier(object):
    def __init__(self):
        self.aircrafts_inside = []
        self.health = 2300
        self.bullet_amount = 28

    def add_aircraft(self, aircraft_type):
        self.aircrafts_inside.append(aircraft_type)

    def fill(self):
        for aircraft in self.aircrafts_inside:
            if aircraft.aircraft_type == "F35":
                aircraft.refill(self.bullet_amount)
        for aircraft in self.aircrafts_inside:
            if self.bullet_amount > 0 and aircraft.aircraft_type == "F16":
                aircraft.refill(self.bullet_amount)



carrier1 = Carrier()
aircraft1 = F16()
aircraft2 = F35()
aircraft3 = F16()
aircraft4 = F35()
aircraft5 = F16()

carrier1.add_aircraft(aircraft1)
carrier1.add_aircraft(aircraft2)
carrier1.add_aircraft(aircraft3)
carrier1.add_aircraft(aircraft4)
carrier1.add_aircraft(aircraft5)

carrier1.fill()
aircraft1.get_status()
aircraft2.get_status()
aircraft3.get_status()
aircraft4.get_status()
aircraft5.get_status()
