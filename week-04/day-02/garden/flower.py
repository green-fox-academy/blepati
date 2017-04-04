class Flower():
    def __init__(self, color = "white", amount = 5):
        self.color = color
        self.amount = amount

    def need_water(self, amount):
        if self.amount <= 5:
            print("The " + self.color + " Flower need water")
        else:
            print("The " + self.color + " Flower does not need water")

flower = Flower()
print(flower.color)
