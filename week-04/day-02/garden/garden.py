from plants import Flower
from plants import Tree

class Garden(object):
    def __init__(self, flowers = 0, trees = 0):
        self.flowers_inside = []
        self.trees_inside = []
        self.dry_plants = []

    def add_flower(self, flower):
        self.flowers_inside.append(flower)

    def add_tree(self, tree):
        self.trees_inside.append(tree)

    def print_statuses(self):
        for flower in self.flowers_inside:
            if flower.need_water():
                self.dry_plants.append(flower)
                print("The " + flower.color + " Flower needs water")
            else:
                print("The " + flower.color + " Flower does not need water")
        for tree in self.trees_inside:
            if tree.need_water():
                self.dry_plants.append(tree)
                print("The " + tree.color + " Tree needs water")
            else:
                print("The " + tree.color + " Tree does not need water")

    def watering_all(self, can_of_water):
        water_for_one = int(can_of_water) // len(self.dry_plants)
        for dry_plant in self.dry_plants:
            dry_plant.watering(water_for_one)



garden = Garden()
flower1 = Flower("yellow", 4)
flower2 = Flower("red", 2)
garden.add_flower(flower1)
garden.add_flower(flower2)
tree1 = Tree("green", 6)
tree2 = Tree("brown", 5)
garden.add_tree(tree1)
garden.add_tree(tree2)
garden.print_statuses()
garden.watering_all(40)
garden.print_statuses()
garden.watering_all(70)
garden.print_statuses()
