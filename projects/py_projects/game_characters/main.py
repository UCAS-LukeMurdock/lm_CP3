# LM  Game Character Classes Project
import csv

class Character:
    def __init__(self):
        pass
    def __str__(self):
        return f": {} | "

def menu(): # Introduces the program and then lets the user choose one of the options
    print("\n\nWelcome, where you can see, add, remove, or search through it.")
    while True:
        choice = input("\nDisplay(1) Search(2) Add(3) Remove(4) Edit(5) Exit(6)\n", 1,6)
        if choice == "1":
            ()
        elif choice == "2":
            ()
        elif choice == "3":
            ()
        elif choice == "4":
            ()
        elif choice == "5":
            ()
        elif choice == "6":
            print("\n\n\nCome Back Soon!\n\n\n")
            break
        else:
            print("Invalid Input! (Enter a number 1-6)")
menu()

"""
INSTRUCTIONS:
    Create a class diagram properly showing the relationship between the "Character" parent class and child classes such as Warrior, Mage, Archer, etc.
    The parent class should hold all information that is common (at least 2 attributes and 1 shared method),
    the child classes should all hold any unique attributes and methods for that particular character type (a minimum of 1 attribute and 1 class). 

OUTPUT EXAMPLE: 
    None. This isn't code that will run

KEY REMINDERS:
    Create a parent "Character" class with at least 2 common attributes and 1 shared method.
    Design child classes (Warrior, Mage, Archer, etc.) that inherit from the "Character" class.
    Each child class should have at least 1 unique attribute and 1 unique method.
    Use proper class diagram notation to show inheritance relationships.
    Include getter and setter methods for relevant attributes in the parent class.
    Use meaningful and descriptive names for classes, attributes, and methods.
    Show the class hierarchy clearly in the class diagram.
    Include any class-specific methods in the appropriate child classes."""