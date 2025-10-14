# Test case/file for Parent and Child Classes Notes
from parent_child import *


def test_Animal_set():
    test_animal = Animal(0, "None")

    # double checks
    assert test_animal.age == 0 
    assert test_animal.color == "None"