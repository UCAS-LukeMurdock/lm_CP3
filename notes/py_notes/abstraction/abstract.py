# LM  Abstraction (Abstract Classes) Notes
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    @abstractmethod
    def move(self):
        pass

class Quadrupeds(Animal):
    def __init__(self, name):
        super().__init__(name)

    def move(self):
        print(f"{self.name} can walk or run.")

class Aquatic(Animal):
    def __init__(self, name):
        super().__init__(name)

    def move(self):
        print(f"{self.name} can swim.")

class SeaLion(Aquatic, Quadrupeds):
    def __init__(self, name):
        super().__init__(name)

    def eats(self):
        print(f"{self.name} eats penguins and krill.")


sealion = SeaLion("Greg")

print(sealion)
sealion.move()
sealion.eats()
print(Aquatic.mro())
print(SeaLion.mro())

    # Can't create an object from the abstract Animal class
# animal = Animal("Goose")
# print(animal)
    


# NOTES


# Why can't you create an object from an abstract class?
    # They are too abstract

        # Because its only purpose is to be a parent class to another class so it doesn't need to be able to create objects.

# How do abstract classes and abstract methods work together?
    # Abstract classes have at least one abstract method and they are overwritten in that classes child classes.
    # Abstract methods always need to be changed in the later child classes or else errors.

# What does abc stand for?
    # Abstract Base Class

# What are decorators? 
    # They begin with the @ symbol and they are used to give further information about what follows.

# What is an abstract method?
    # A method pecifically written in a parent class to be overwritten by a child class

# What is a concrete method?
    # normal methods

# What is an abstract class?
    # A placeholder class, a ghost class, objects can't be made from it, it is made specificaly to be a parent class.
    # Inherits from ABC
    # It needs at least one abstractmethod

# How do you make an abstract method?
    # @abstractmethod
    # Then the method

# How can you create a class that inherits from multiple parent classes?
    # class Child(ParentOne, ParentTwo)

# Why does the inheritance order matter?
    # It matters because then you will use the correct method instead of another one that you didn't want it to inherit.
    # The first class in the order gets higher precedence

# What does the mro() method do when you call it on a class?
    # It tells you the Method Resolution Order
    # Also known as the inheritence order (which classes are inherited from first)

# What is Method resolution order?
    # The order of priority in inheritence for a class
