# LM  Parent and Child Classes Notes


class Animal():
    def __init__(self, age, color):
        self.age = age
        self.color = color
    
    def move(self):
        pass
    
    def __str__(self):
        return f"Age: {self.age}\nColor: {self.color}"
    
    def __eq__(self, other): # Overwrites ==
        return (self.age == other.age and self.color == other.color)
    
class Dog(Animal):
    def __init__(self, age, color, owner, breed, name):
        super().__init__(age, color) # You are going to the parent class and grabbing a specific method from it and doing it
        self.owner = owner
        self.breed = breed
        self.name = name

    def move(self):
        print(f"\n{self.name} runs")

    def __str__(self): # The string method is overwritten for just this child class
        return f"Name: {self.name}\nAge: {self.age}\nColor: {self.color}\nOwner: {self.owner}\nBreed: {self.breed}\n"
    
    def __eq__(self, other): # Overwrites ==
        return (self.age == other.age and
                self.color == other.color and
                self.owner == other.owner and
                self.breed == other.breed and
                self.name == other.name)


bobby = Dog(5, "brown", "Jill", "Bulldog", "Bobby")
birdy = Dog(1, "Black", "Nikkie", "Lab", "Birdy")

alex = Animal(16, "White")
nick = Animal(16, "White")

print(bobby)
print(alex)

print(alex==nick)
print(bobby == birdy)

bobby.move()


# What is a parent/abstract class?
    # A parent class is a class that is more abstract then child classes which have pieces of the parent class in it.

# How do you create a child class?
    # By putting the parent class in the parenthesis and using super() when you want to use parent methods.
    # Example Seen Above (Dog)

# How does a child class inherit from the parent class?
    # By using super.

# What are class diagrams?
    # Diagrams used to explain multiple classes and how they interact.
    # Has attributes with data type and if it is public (+) or private (-) AND methods.

# How are class diagrams used to show a parent/child relationship?
    # They use white arrows that point from child to parent class. (Shows Inheritance)
    # Child classes have access to all that the parent has.

# How do you overload operators in a class?
    # Using magic methods like __eq__

# What are test cases?
    # 

# Why do we use test cases?
    # To make sure we don't break the code we already written.
    # It lets us make test cases that checks to make sure the code works.

# How do we create test cases?
    # On a separate file, in the same folder.
    # test_filename.py
        # filename_test.py
