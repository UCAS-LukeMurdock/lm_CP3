# LM  Dessert Shop Classes File

class DessertItem: # Parent Class for Desserts. Has a name attribute that is shared to its children classes
    def __init__(self, name = ""):
        self.name = name


# Child Classes of DessertItem with extra attributes
class Candy(DessertItem):
    def __init__(self, name = "", price_per_pound = 0.0, candy_weight = 0.0):
        super().__init__(name)
        self.price_per_pound = price_per_pound
        self.candy_weight = candy_weight


class Cookie(DessertItem):
    def __init__(self, name = "", price_per_dozen = 0.0, cookie_amount = 0):
        self.price_per_dozen = price_per_dozen
        super().__init__(name)
        self.cookie_amount = cookie_amount


class IceCream(DessertItem):
    def __init__(self, name = "", price_per_scoop = 0.0, scoops = 0):
        super().__init__(name)
        self.price_per_scoop = price_per_scoop
        self.scoops = scoops

class Sundae(IceCream): # Child Class of IceCream that has everything it has plus topping name and price.
    def __init__(self, name = "", price_per_scoop = 0.0, scoops = 0, topping_name = "", topping_price = 0.0):
        super().__init__(name, price_per_scoop, scoops)
        self.price_per_scoop = price_per_scoop
        self.scoops = scoops

        self.topping_name = topping_name
        self.topping_price = topping_price



class Order: # Order Class that has a list attribute that things can be added to and the length of it can be returned.
    def __init__(self):
        self.order = []
    
    def add(self, item): # Adds a Dessert Item to the order
        self.order.append(item)

    def __len__(self):
        return len(self.order)
        