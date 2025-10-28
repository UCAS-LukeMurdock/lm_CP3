# LM  Dessert Shop Classes File
from abc import ABC, abstractmethod

class DessertItem(ABC): # Parent Class for Desserts. Has a name attribute that is shared to its children classes
    def __init__(self, name = "", tax_percent = 7.25):
        self.name = name
        self.tax_percent = tax_percent

    @abstractmethod
    def calculateCost(self):
        pass
        
    def calculateTax(self):
        return round(self.calculateCost() * (self.tax_percent / 100), 2)


# Child Classes of DessertItem with extra attributes
class Candy(DessertItem):
    def __init__(self, name = "", price_per_pound = 0.0, candy_weight = 0.0, tax_percent = 7.25):
        super().__init__(name, tax_percent)
        self.price_per_pound = price_per_pound
        self.candy_weight = candy_weight

    def calculateCost(self):
        return round(self.price_per_pound * self.candy_weight, 2)


class Cookie(DessertItem):
    def __init__(self, name = "", price_per_dozen = 0.0, cookie_amount = 0, tax_percent = 7.25):
        super().__init__(name, tax_percent)
        self.price_per_dozen = price_per_dozen
        self.cookie_amount = cookie_amount

    def calculateCost(self):
        return round((self.price_per_dozen / 12) * self.cookie_amount, 2)


class IceCream(DessertItem):
    def __init__(self, name = "", price_per_scoop = 0.0, scoops = 0, tax_percent = 7.25):
        super().__init__(name, tax_percent)
        self.price_per_scoop = price_per_scoop
        self.scoops = scoops

    def calculateCost(self):
        return round(self.price_per_scoop * self.scoops, 2)

class Sundae(IceCream): # Child Class of IceCream that has everything it has plus topping name and price.
    def __init__(self, name = "", price_per_scoop = 0.0, scoops = 0, topping_name = "", topping_price = 0.0, tax_percent = 7.25):
        super().__init__(name, tax_percent, price_per_scoop, scoops)
        self.price_per_scoop = price_per_scoop
        self.scoops = scoops

        self.topping_name = topping_name
        self.topping_price = topping_price

    def calculateCost(self):
        return round(super().calculateCost() + self.topping_price, 2)



class Order: # Order Class that has a list attribute that things can be added to and the length of it can be returned.
    def __init__(self):
        self.order = []
    
    def add(self, item): # Adds a Dessert Item to the order
        self.order.append(item)

    def __len__(self):
        return len(self.order)
    
    def orderCost(self): # Calculates the total cost of the order
        total = 0
        for item in self.order:
            total += item.calculateCost()
        return round(total, 2)
    
    def orderTax(self): # Calculates the total tax of the order
        total = 0
        for item in self.order:
            total += item.calculateTax()
        return round(total, 2)
        