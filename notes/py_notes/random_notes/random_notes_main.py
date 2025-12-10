# LM  Random Notes
from collections import namedtuple

"""
Named Tuple:
    Template
    More agile version of a class
    Preunpacking a tuple
"""


    # Ex:
# Define a namedtuple called 'Point' with fields 'x' and 'y'
Point = namedtuple('Point', ['x', 'y'])

# Create an instance
p = Point(10, 20)

# Access elements by name and by index
print(p.x)     # Output: 10
print(p[1])    # Output: 20


    # Ex 2:
Color = namedtuple('Color', ['red', 'green', 'blue'])
red = Color(255,0,0)
print(red.red)

# --------------------------------------------------------------------------------------------
"""
Dataclasses
"""
from dataclasses import dataclass, field

@dataclass(order=True, frozen=True) # Order allows sort_index or somethign | Frozen makes it so values can't be changed after initialization
class Person:
    sort_index: int = field(init=False, repr=False) # Doesn't need to be initialized | isn't printed
    name: str
    job: str
    age: int

    def __post_init__(self):
        object.__setattr__(self, 'sort_index', self.age) # Makes frozen not get mad at it

person1 = Person("Tia", "Sales", 29)
person2 = Person("Katie", "Dispatch", 35)
person3 = Person("Katie", "Dispatch", 35)

print(person1) # More readable print
print(person2 == person3) # Compares content
print(person1>person2) # Uses sort_index

# --------------------------------------------------------------------------------------------
"""
sorted()
    Returns a new list that is ordered
    Sets, tuples, lists can be turned into an ordered list through this
"""

people = [person1, person2, person3]
nums = [1,53,8456,3234,5654,2332,45,6,645]

sort_nums = sorted(nums)
reverse_nums = sorted(nums, reverse=True)

print(sort_nums)
print(reverse_nums)


# def age_sort(person):
#     return person.age

# sort_people = sorted(people, key=age_sort)


"Lambdas are used for small, simple one line functions that do little things"

sort_people = sorted(people, key=lambda person: person.name) # lambda (function) | person (parameter) | person.name (return) [can sort by ABCs]
print(sort_people)

from operator import attrgetter
sort_people = sorted(people, key=attrgetter('job'))
print(sort_people)

# --------------------------------------------------------------------------------------------
"""
*args, *kwargs

args = arguments
kwargs = key word arguments

Look at W3Schools
"""
# *args ---------------------------
def hello(age=12, *name): # Changing the parameter/arguments into a list (or maybe tuple) basically  (It needs to be the last one)
    print(age)
    for x in name:
        print(f"Hello {x}!")

hello(12, "Alex", "Katie", "Andrew")

# **kwargs -------------------------

# def another(fname, lname):
#     print(f"Hello {fname} {lname}!")

def another(**names):
    if "mname" in names:
        print(f"Hello {names['fname']} {names['mname']} {names['lname']}!")
    else:
        print(f"Hello {names['fname']} {names['lname']}!")
   


another(fname="Jake", mname="Francois", lname="LaRose")
another(fname="Jake", lname="LaRose")