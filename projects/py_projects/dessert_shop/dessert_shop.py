# LM  Dessert Shop Project
from dessert import *


def menu(): # Creates Objects in the order and then prints them and their amount

    order = Order()
    order.add(Candy("Gummy Bears", 0.34, 1.25))
    order.add(Candy("Candy Corn", 2.45, 0.36))
    order.add(Cookie("Chocolate Chip", 6, 2.17))
    order.add(IceCream("Mint Chocolate Chip", 2, 1.66))
    order.add(IceCream("Cookies and Cream", 1, 1.52))
    order.add(Sundae("Vanilla", 2, 1.00, "Fudge", 0.33))

    for item in order.order:
        print(item.name)

    print(f"\nNumber of item in order: {len(order)}")


menu()
