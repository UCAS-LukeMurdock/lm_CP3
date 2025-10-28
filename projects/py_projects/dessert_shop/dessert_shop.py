# LM  Dessert Shop Project (Main File)
from tabulate import tabulate
from dessert import *

# data = [["Bruce Wayne", "Batman", "123-4567"], ["Clark Kent", "Superman", "987-6543"]]
# print(tabulate(data, headers=["Name", "Job", "Number"]))

def menu(): # Creates Objects in the order and then prints them and their amount

    order = Order()
    order.add(Candy("Gummy Bears", 1.25, 0.34))
    order.add(Candy("Candy Corn", 2.45, 0.36))
    order.add(Cookie("Chocolate Chip", 2.17, 6))
    order.add(IceCream("Mint Chocolate Chip", 1.66, 2))
    order.add(IceCream("Cookies and Cream", 1.52, 1))
    order.add(Sundae("Vanilla", 1.00, 2, "Fudge", 0.33))

    for item in order.order:
        print(item.name)

    print(f"\nNumber of item in order: {len(order)}\n")

    data = []
    for item in order.order:
        data.append([item.name, f"${item.calculateCost()}", f"${item.calculateTax()}"])
    data.append(["-----------------", "---------", "---------"])
    data.append(["Total", f"${round(order.orderCost(), 2)}", f"${round(order.orderTax(), 2)}"])
    data.append(["-----------------", "---------", "---------"])
    data.append(["Grand Total", f"${round(order.orderCost() + order.orderTax(), 2)}", ""])
    print(tabulate(data, headers=["Item", "Cost", "Tax"]))


menu()
