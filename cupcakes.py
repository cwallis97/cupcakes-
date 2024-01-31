from abc import ABC, abstractmethod

class Cupcake(ABC):
    def __init__(self, name, price, flavor, frosting, filling=None):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling

    def add_sprinkles(self, *args):
        pass

    @abstractmethod
    def calculate_price(self, quantity):
        pass

class Regular(Cupcake):
    def calculate_price(self, quantity):
        return self.price * quantity

class Mini(Cupcake):
    def calculate_price(self, quantity):
        return self.price * quantity * 0.8

class Large(Cupcake):
    def calculate_price(self, quantity):
        return self.price * quantity * 1.2
