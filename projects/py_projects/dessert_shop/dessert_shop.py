# LM  Dessert Shop Project (Main File)
from tabulate import tabulate
from dessert import *


# Sorry if this class should be in the classes file (dessert.py), but the instructions made it sound like it should go in this file.
class DessertShop:

    def userPromptCandy(self):
        while True:
            name = input("\nEnter the name of candy: ").strip().title()
            if name == "":
                print("\nInvalid Input (Please enter a name of a candy and don't just click enter)")
                continue
            break

        while True:
            weight = input("\nEnter the weight (lbs): ").strip()
            try:
                weight = float(weight)
            except ValueError:
                print("\nInvalid Input (Please enter a number [a float specifically])")
                continue
            if weight <= 0:
                print("\nInvalid Input (Enter a number greater than 0)")
                continue
            break

        while True:
            price = input("\nEnter the price per pound: ").strip()
            try:
                price = float(price)
            except ValueError:
                print("\nInvalid Input (Please enter a number [a float specifically])")
                continue
            if price <= 0:
                print("\nInvalid Input (Enter a number greater than 0)")
                continue
            break

        return Candy(name, price, weight)

    def userPromptCookie(self):
        while True:
            name = input("\nEnter the type of cookie: ").strip().title()
            if name == "":
                print("\nInvalid Input (Please enter a type of cookie and don't just click enter)")
                continue
            break

        while True:
            amount = input("\nEnter the amount of cookies: ").strip()
            try:
                amount = int(amount)
            except ValueError:
                print("\nInvalid Input (Please enter an integer)")
                continue
            if amount <= 0:
                print("\nInvalid Input (Enter a number greater than 0)")
                continue
            break

        while True:
            price = input("\nEnter the price per dozen: ").strip()
            try:
                price = float(price)
            except ValueError:
                print("\nInvalid Input (Please enter a number [a float specifically])")
                continue
            if price <= 0:
                print("\nInvalid Input (Enter a number greater than 0)")
                continue
            break

        return Cookie(name, price, amount)

    def userPromptIcecream(self):
        while True:
            name = input("\nEnter the flavor of ice cream: ").strip().title()
            if name == "":
                print("\nInvalid Input (Please enter an ice cream flavor and don't just click enter)")
                continue
            break

        while True:
            number = input("\nEnter the number of scoops: ").strip()
            try:
                number = int(number)
            except ValueError:
                print("\nInvalid Input (Please enter an integer)")
                continue
            if number <= 0:
                print("\nInvalid Input (Enter a number greater than 0)")
                continue
            break

        while True:
            price = input("\nEnter the price per scoop: ").strip()
            try:
                price = float(price)
            except ValueError:
                print("\nInvalid Input (Please enter a number [a float specifically])")
                continue
            if price <= 0:
                print("\nInvalid Input (Enter a number greater than 0)")
                continue
            break

        return IceCream(name, price, number)

    def userPromptSundae(self):
        while True:
            name = input("\nEnter the flavor of ice cream: ").strip().title()
            if name == "":
                print("\nInvalid Input (Please enter an ice cream flavor and don't just click enter)")
                continue
            break

        while True:
            number = input("\nEnter the number of scoops: ").strip()
            try:
                number = int(number)
            except ValueError:
                print("\nInvalid Input (Please enter an integer)")
                continue
            if number <= 0:
                print("\nInvalid Input (Enter a number greater than 0)")
                continue
            break

        while True:
            price = input("\nEnter the price per scoop: ").strip()
            try:
                price = float(price)
            except ValueError:
                print("\nInvalid Input (Please enter a number [a float specifically])")
                continue
            if price <= 0:
                print("\nInvalid Input (Enter a number greater than 0)")
                continue
            break

    
        while True:
            topping = input("\nEnter the topping: ").strip().title()
            if topping == "":
                print("\nInvalid Input (Please enter a topping name and don't just click enter)")
                continue
            break

        while True:
            topping_price = input("\nEnter the price for the topping: ").strip()
            try:
                topping_price = float(topping_price)
            except ValueError:
                print("\nInvalid Input (Please enter a number [a float specifically])")
                continue
            if topping_price <= 0:
                print("\nInvalid Input (Enter a number greater than 0)")
                continue
            break

        return Sundae(name, price, number, topping, topping_price)


def main(): # The user inputs parts of certain dessert items and then objects are created out of those which are then printed out in a receipt format

    # Luke Murdock's previous code for Parts before Part 5
    """
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
    data.append(["---------", "---------", "---------"])
    data.append(["Order Subtotals", f"${round(order.orderCost(), 2)}", f"${round(order.orderTax(), 2)}"])
    data.append(["Order Total", "", f"${round(order.orderCost() + order.orderTax(), 2)}"])
    data.append(["Total Items in the order:", "", len(order)])
    print(tabulate(data, headers=["Name", "Cost", "Tax"], tablefmt="fsql"))
    """



    '''
    Code to implement the main loop of terminal-based user interface for
    Dessert Shop Part 4. Students should be able to paste this code into their own 
    main() method as-is and use it without change.

    Author: George Rudolph
    Date: 2 Jun 2023
    '''
    shop = DessertShop() 
    order = Order()
    '''
    order.add(Candy('Candy Corn', 1.5, 0.25))
    order.add(Candy('Gummy Bears', 0.25, 0.35))
    order.add(Cookie('Chocolate Chip', 6, 3.99))
    order.add(IceCream('Pistachio', 2, 0.79))
    order.add(Sundae('Vanilla', 3, 0.69, 'Hot Fudge', 1.29))
    order.add(Cookie('Oatmeal Raisin', 2, 3.45))
    '''
    
    done: bool = False
    # build the prompt string once
    prompt = '\n'.join([ '\n',
            '1: Candy',
            '2: Cookie',            
            '3: Ice Cream',
            '4: Sundae',
            '\nWhat would you like to add to the order? (1-4, Enter for done): '
    ])

    while not done:
        choice = input(prompt)
        match choice:
            case '':
                done = True
            case '1':            
                item = shop.userPromptCandy()
                order.add(item)
                print(f'\n{item.name} has been added to your order.')
            case '2':            
                item = shop.userPromptCookie()
                order.add(item)
                print(f'\n{item.name} has been added to your order.')
            case '3':            
                item = shop.userPromptIcecream()
                order.add(item)
                print(f'\n{item.name} has been added to your order.')
            case '4':            
                item = shop.userPromptSundae()
                order.add(item)
                print(f'\n{item.name} has been added to your order.')
            case _:            
                print('\nInvalid response:  Please enter a choice from the menu (1-4) or Enter')
    print()

    # Luke Murdock's code for the receipt
    data = []
    for item in order.order:
        data.append([item.name, f"${item.calculateCost()}", f"${item.calculateTax()}"])

    data.append(["---------", "---------", "---------"])
    data.append(["Order Subtotals", f"${round(order.orderCost(), 2)}", f"${round(order.orderTax(), 2)}"])
    data.append(["Order Total", "", f"${round(order.orderCost() + order.orderTax(), 2)}"])
    data.append(["Total Items in the order:", "", len(order)])
    
    print(tabulate(data, headers=["Name", "Cost", "Tax"], tablefmt="fsql"))
    print('\n')

main()

# Make the changes to the classes to allow for calculating Totals and Tax
# Make DessertItem an abstract class
# Use tabulate to print out a receipt like the one above
# Create a DessertShop class that asks the user for the needed information to create each of the dessert items
# Validate user inputs (Make sure they can change to the correct data types AND that they are positive numbers!)

# TEST

""""
INSTRUCTIONS:
PART 1:
Problem
In Part 4, you will add the functionality to calculate the cost of any Dessert Item along with the associated tax. Also you will add the ability in the Order class to calculate the cost of all items in the order as well as the associated total tax.

Finally, you will implement the ability to print out the receipt to the console.

To do this, you will make updates to your Dessert Shop system as described below.

Changes to DessertItem Class
Make it an abstract class

Add attribute tax_percent: float with the default value 7.25.

Add a new abstract method, calculate_cost(): float

Include a new method calculate_tax(): float that calculates and returns the actual tax for the item, rounded to 2 decimal places.

Changes to All Dessert Classes Candy, Cookie, IceCream, Sundae
Add a method calculate_cost() that overrides the superclass method and returns the correct cost for the item, rounded to 2 decimal places.

Note:

Convert cookie_quantity to dozens before calculating the cost of the cookies.

The cost of a Sundae is the cost of the ice cream plus the cost of the topping.

Changes to Order Class
Add a new method, order_cost(), that calculates and returns the total cost for all items in the order

Add a new method, order_tax(), calculates and returns the total tax for all items in the order

Changes to main()
Add a loop in the main() to generate the list-of-lists required by tabulate. Each row in the list should include:

The name of the dessert,

The cost of each item

The tax of the item

Values should match what is shown in the example run below.

Add a row for subtotal of all the items in the order and the total tax for the order as shown in the example.

Add a row for the total cost for the order (subtotal + total tax)

Add a row for the total number of items in the order as shown in the example

Print the receipt using tabulate. You output should match the provided sample run.

Example of using tabulate:

from tabulate import tabulate
​
data = [
    ["Will", 15],
    ["Hope", 19],
    ["Jill", 20],
]
​
​
print(tabulate(data, headers=["Character", "Age"], tablefmt="fsql"))
 

Test Cases
Modify your DessertItem test cases to use an instance of the Candy class. You have to test an abstract class by testing one of its concrete subclasses.

Add new test cases to DessertItem test code that test the tax_percent attribute

Add new test cases to test method calculate_cost for each respective dessert subclass.

Add new test cases to test superclass method calculate_tax for each respective dessert subclass. Hint: Use the code that created example objects in main() from Part 2 as a source of test cases for each kind of object here.

Sample Run
Your output format and values should match what is here.

DessertShop4SR.png

Key Requirements
Dessert Shop 4 extends the functionality of Dessert Shop 3.

Attribute tax_percent is in DessertItem class

Method calculate_cost is abstract in DessertItem and concrete in all inheriting subclasses

Method calculate_tax is concrete in DessertItem and is NOT overrriden in any inheriting subclasses

Pytest test cases have been created or modified as described above

The output should look similar to the sample run shown above

Your workspace should have the following 7 files:

dessert.py

dessertshop.py

test_dessert.py

test_candy.py

test_cookie.py

test_icecream.py

test_sundae.py

This way you don’t end up with one huge test file.

PART 2:
Problem
In this part of the project, you add a command line user interface to your program. To do this, you will make changes to dessertshop.py module.

There should be no changes to the DessertItem class and the subclasses.

Changes to dessertshop module
Add a new class DessertShop to the module. The DessertShop class will have 4 new methods:

user_prompt_candy()

user_prompt_cookie()

user_prompt_icecream()

user_prompt_sundae()

Each method should do the following:

Prompt user for enough input to create the required line item on the receipt

Get user input

Validate the input

If an input is invalid (e.g., a negative price or quantity), continue prompting the user until a valid value is entered.

Convert input values to the proper types as-needed

Create an object of the proper type

Return the newly created object to the caller

main() Code to Copy and Use
We give you code that runs the main loop in the provided file ui.py. Click here Download hereto download

You should be able to cut and paste it into your own main function in your dessertshop.py as-is.

At the end of the main function, print the receipt to the console exactly as you implemented it in Part 4.

Test Cases
You do not need to create any new pytest test cases for Part 5. However, make sure to upload your existing test cases and re-run them to ensure they still pass.

Key Program Requirements
A terminal-based user interface has been added to your Dessert Shop program.

Output should look similar to the sample run.

Submit the following 7 files in your workspace:

dessert.py

dessertshop.py

test_dessert.py

test_candy.py

test_cookie.py

test_icecream.py

test_sundae.py

Only dessertshop.py should have changed in Part 5 unless you needed to correct other issues.

Sample Run
1: Candy
2: Cookie
3: Ice Cream
4: Sundae
What would you like to add to the order? (1-4, Enter for done): 1
​Enter name of candy: Candy Corn
Enter weight (lbs): 5
Enter price per pound: 4.99

1: Candy
2: Cookie
3: Ice Cream
4: Sundae

What would you like to add to the order? (1-4, Enter for done): 3
​Enter the type of ice cream: Pistachio
Enter the number of scoops: 2
Enter the price per scoop: 0.79

1: Candy
2: Cookie
3: Ice Cream
4: Sundae

​What would you like to add to the order? (1-4, Enter for done): 4
Enter the type of ice cream: Vanilla
Enter the number of scoops: 3
Enter the price per scoop: 0.69
Enter the topping: Hot Fudge
Enter the price for the topping: 1.29

1: Candy
2: Cookie
3: Ice Cream
4: Sundae

What would you like to add to the order? (1-4, Enter for done):
KEY REMINDERS:
Make the changes to the classes to allow for calculating Totals and Tax
Make DessertItem an abstract class
Use tabulate to print out a receipt like the one above
Create a DessertShop class that asks the user for the needed information to create each of the dessert items
Validate user inputs (Make sure they can change to the correct data types AND that they are positive numbers!)
"""











"""
INSTRUCTIONS:
Part One of a multistep project to create a Dessert shop (Yes this is pulled from UVU. . . I am not sorry)

STEP 1:
Create a file named "dessert" on this file create the 5 classes listed below:

DessertItem (Parent class)
Attributes: 
name: str
Default Value: ""
Methods:
Constructor (__init__)

Candy
Attributes:
name: str
Default Value: ""
candy_weight: float
Default Value: 0.0
price_per_pound: float
Default Value: 0.0
Methods:
Constructor (__init__)

Cookie
Attributes:
name: str
Default Value: ""
cookie_quantity: int
Default Value: 0
price_per_dozen: float
Default Value: 0.0
Methods:
Constructor (__init__)

IceCream
Attributes:
name: str
Default Value: ""
scoop_count: int
Default Value: 0
price_per_scoop: float
Default Value: 0.0
Methods:
Constructor (__init__)

Sundae (subclass of IceCream)
Attributes: 
name: str
Default Value: ""
scoop_count: int
Default Value: 0
price_per_scoop: float
Default Value: 0.0
topping_name: str
Default Value: ""
topping_price: float
Default Value: 0.0
Methods:
Constructor (__init__)
STEP 2:
Add an order class that will keep track of all the items a customer buys

Add a new file that test the classes by making examples of each and adding them to an order

Order
Attributes: 
order: list
Value = []
Methods:
Constructor (__init__)
add(item)
Takes a single DessertItem argument and adds it to the order list
__len__()
Magic method returns the number of items in the order
dessert_shop.py

Import your classes

Create a main() function that

Creates a new instance of the order class
Adds the following items to the order
Candy("Candy Corn", 1.5, .25)
Candy("Gummy Bears", .25, .35)
Cookie("Chocolate Chip", 6, 3.99)
IceCream("Pistachio", 2, .79)
Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29)
Cookie("Oatmeal Raisin", 2, 3.45)
Prints out the name of each DessertItem in the order
Print out the total number of items in the order
STEP 3:
Create pytests cases for constructors, attributes, and methods

Create a different "test" page for each of the classes you need to test (DessertItem, Candy, Cookie, IceCream, Sundae)

NOTE: You don't need to write tests for the Order class

Write three test cases for each of the five classes listed above:

Default values: Verify attributes are initialized with default values.

Provided values: Verify attributes are initialized correctly with given values.

Updated values: Confirm that attributes can be updated and that the changes are reflected correctly.

Note:

All test cases must be implemented using pytest.

EXAMPLE TERMINAL OUTPUT:

Candy Corn
Gummy Bears
Chocolate Chip
Pistachio
Vanilla
Oatmeal Raisin
Total number of items in order: 6
PROJECT CLASS DIAGRAM: 

image.png

KEY REMINDERS:
Create a separate folder (or repository) called Dessert Shop
Create a file named "dessert.py" containing the following classes: DessertItem, Candy, Cookie, IceCream, and Sundae.
Implement the DessertItem class as the parent class with a 'name' attribute and constructor.
Create Candy, Cookie, and IceCream classes as subclasses of DessertItem, each with their specific attributes and constructors.
Implement the Sundae class as a subclass of IceCream with additional attributes for toppings.
Ensure all classes have appropriate default values for their attributes.
Create an Order class in the same file with methods to add items and get the order length.
Create a separate file named "dessert_shop.py" to test the classes.
In dessert_shop.py, import the classes from dessert.py and create a main() function.
In the main() function, create an Order instance and add various dessert items to it.
Print the name of each DessertItem in the order and the total number of items.
Create separate test files for each class (DessertItem, Candy, Cookie, IceCream, Sundae) using pytest.
Write three test cases for each class: default values, provided values, and updated values.
Ensure proper Python syntax, including correct indentation and method definitions.
Use meaningful variable and method names for code clarity.
Add comments to explain code logic where necessary.
Test all classes thoroughly to ensure required functionality works as expected.
"""