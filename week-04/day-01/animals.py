
class Animals:
    def __init__(self, name, hunger, thirst):
        self.name = name
        self.hunger = hunger
        self.thirst = thirst

    def eat(self):
        self.hunger -= 1

    def drink(self):
        self.thirst -= 1

    def play(self):
        self.hunger += 1
        self.thirst += 1


animal = Animals("zebra", 50, 50)
print(animal.name, animal.hunger, animal.thirst)
animal.eat()
print(animal.hunger)
