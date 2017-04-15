class Flower(object):
    def __init__(self, color, amount):
        self.color = color
        self.amount = amount

    def need_water(self):
        return self.amount <= 5

    def watering(self, amount):
        self.amount += amount * 0.75
        return self.amount

class Tree(Flower):
    def __init__(self, color, amount):
        super().__init__(color, amount)

    def need_water(self):
        return self.amount <= 10

    def watering(self, amount):
        self.amount += amount * 0.40
        return self.amount
