class Aircraft(object):
    def __init__(self, aircraft_type = " ", max_ammo = 0, base_damage = 0):
        self.aircraft_type = aircraft_type
        self.max_ammo = max_ammo
        self.base_damage = base_damage
        self.ammo = 0

    def fight(self):
        damage = self.ammo * self.base_damage
        self.ammo = 0
        return damage

    def refill(self, bullet_amount):
        if bullet_amount <= self.max_ammo:
            self.ammo = bullet_amount
            return 0
        else:
            self.ammo = self.max_ammo
            remaining_bullet = bullet_amount - self.max_ammo
            return remaining_bullet

    def get_type(self):
        print(str(self.aircraft_type))

    def get_status(self):
        print("Type: " + str(self.aircraft_type) + ", Ammo: " + str(self.ammo) + ", Base Damage: " + str(self.base_damage) + ", All Damage: " + str(self.fight()))

class F16(Aircraft):
    def __init__(self):
        super().__init__("F16", 8, 30)

class F30(Aircraft):
    def __init__(self):
        super().__init__("F30", 12, 50)

aircraft = F16()
print(aircraft.refill(100))
print(aircraft.fight())
print(aircraft.refill(10))
aircraft.get_type()
aircraft.get_status()
