from plants import Flower
from plants import Tree

class Garden(object):
    def __init__(self, flowers = 0, trees = 0):
        self.flowers_inside = []
        self.trees_inside = []

    def print_statuses(self):
        for flower in self.flowers_inside:
            flower.need_water()
        for tree in self.trees_inside:
            tree.need_water()
            
    def add_flower(self, flower):
        self.flowers_inside.append(flower)

    def add_tree(self, tree):
        self.trees_inside.append(tree)

    #def dry_plants(self, ):

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
