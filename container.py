"""
Class container
"""

class Container:
    def __init__(self, type, durability, capacity, capacity_max):

        """
        constructeur
        """
        self.type = type
        self.durability = durability
        self.capacity = capacity
        self.capacity_max = capacity_max

    def drink(self, quantity):
        """
        Action boire
        :param quantity:
        :return:
        """
        if self.capacity >= quantity:
            self.capacity -= quantity
            self.durability += 1
        else:
            print("impossible de boire")

    def fill(self, quantity):
        if quantity < (self.capacity_max - self.capacity):
            self.capacity += quantity
            self.durability -= 0.5
        else:
            self.capacity = self.capacity_max
            self.durability -= 0.5
