# LM  Classes and Objects Notes (3rd Period)

class Person:
    """Person class with first and last names as well as age.
    Method to get full name, increase age by 1"""
    first_name: str
    last_name: str
    age: int

    def __init__(self, _first_name="John", last_name="Doe", age=0): # You have to add default values from right to left
        """Sets all values"""
        self._first_name = _first_name
        self.last_name = last_name
        self.age = age

    # setter functions/methods change the values of the attributes
    def setAge(self):
        """Increase age by 1"""
        self.age += 1
    
    # getter methods return/display attributes
    def full(self):
        """Create full name"""
        return self._first_name + " " + self.last_name
    
    def __str__(self): # Kind of like overloading
        return f"First name: {self._first_name}\nLast name: {self.last_name}\nage: {self.age}\n"
        

tia = Person("Tia", "LaRose", 28)
alex = Person("Alex", "LaRose", 37)

tia.setAge()

print(f"{tia.full()}'s Age: {tia.age}")
print(f"{alex.full()}'s Age: {alex.age}")

print()
print(tia)


# What is a class?
    # A class is an abstraction of an object. It is a zoomed out version of the thing it represents. Every class has __init__ to intialize attributes for the object.
    # It has attributes (variables) and methods (functions).

# What is an object?
    # An instance of a class

# How is a class a form of encapsulation?
    # It puts all of the information in one place.

# How is a class an abstraction of an object?
    # A class is an abstraction because it gets one level further from the specifics. Tia and Alex are both a person so Person is an abstraction. Person is broader so more abstract. (Covers more)
    # It is zoomed out. It covers all/any of that type.

# How do you access information in an object?
    # Using a getter or using object_name.info_name

# How do you initialize a class?
    # Seen Above (either class Person or __init__)

# How do you set a default value 
    # In the parameters of the __init__ function, set values to them from right to left.

# How do you use type hinting?
    # It double checks to make sure that the data_type stays correct.
    # Example:
        # first_name: str
        # last_name: str
        # age: int

# How do you set an attribute to be private?
    # They start public.
    # if you add a _ before an item then it tells people that it is private and shouldn't be used outside of the function.


# How do you make a class method?
    # It's just a function inside of a class. It has self in it's parameters.

# Why do we include docstrings/
    # To document what a class is and what it is doing with multiline comments.

# What does "self" do as a parameter for class methods?
    # It just interacts with this one object.
    # It only does it for that current instance. (If its for Tia then it won't do it for Alex)

# What are getter and setter methods?
    # getter methods return/display attributes
    # setter functions/methods change the values of the attributes

# What are magic methods?
    # Special methods starting or ending with __     (def __name__)

# Where are class objects saved? (heap or stack?)
    # Objects are saved in the Heap.
