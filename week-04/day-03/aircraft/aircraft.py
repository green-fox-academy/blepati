class Aircraft(object):
    def __init__(self, max_ammo = 0, base_damage = 0):
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

aircraft = Aircraft(12, 50)
print(aircraft.refill(100))
print(aircraft.fight())
