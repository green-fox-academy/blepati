class Flower(object):
    def __init__(self, color, amount):
        self.color = color
        self.amount = amount

    def need_water(self):
        if self.amount <= 5:
            print("The " + self.color + " Flower needs water")
        else:
            print("The " + self.color + " Flower does not need water")

    def watering(self, amount):
        self.amount += amount * 0.75
        return self.amount

class Tree(Flower):
    def __init__(self, color, amount):
        super().__init__(color, amount)

    def need_water(self):
        if self.amount <= 10:
            print("The " + self.color + " Tree needs water")
        else:
            print("The " + self.color + " Tree does not need water")

    def watering(self, amount):
        self.amount += amount * 0.40
        return self.amount
