# LM  Dessert Shop Classes File

class DessertItem:
    def __init__(self, name = ""):
        self.name = name

    def __str__(self):
        return f": {1} | "

class Candy(DessertItem):
    def __init__(self, name = "", price_per_pound = 0.0, amount = 0.0):
        super().__init__(name)
        self.price_per_pound = price_per_pound
        self.amount = amount

class Cookies(DessertItem):
    def __init__(self, name = "", price_per_dozen = 0.0, cookie_amount = 0):
        self.price_per_dozen = price_per_dozen
        super().__init__(name)
        self.cookie_amount = cookie_amount



class IceCream(DessertItem):
    def __init__(self, name = "", price_per_scoop = 0.0, scoops = 0):
        super().__init__(name)
        self.price_per_scoop = price_per_scoop
        self.scoops = scoops



class Sundae(IceCream):
    def __init__(self, name = "", price_per_scoop = 0.0, scoops = 0, topping_name = "", topping_price = 0.0):
        super().__init__(name, price_per_scoop, scoops)
        self.price_per_scoop = price_per_scoop
        self.scoops = scoops

        self.topping_name = topping_name
        self.topping_price = topping_price


class Order:
    def __init__(self):
        self.order = []
    
    def add(self, item): # Adds a Dessert Item to the order
        self.order.append(item)

    def __len__(self):
        return len(self.order)
        