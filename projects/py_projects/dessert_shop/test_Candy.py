# Test cases for Candy Class
from dessert import DessertItem, Candy


def test_Candy_default_set():
    test_candy = Candy()
    assert test_candy.name == ""
    assert test_candy.price_per_pound == 0.0
    assert test_candy.candy_weight == 0.0

def test_Candy_provided_set():
    test_candy = Candy("Jolly Rancher", 3.76, 8.9)
    assert test_candy.name == "Jolly Rancher"
    assert test_candy.price_per_pound == 3.76
    assert test_candy.candy_weight == 8.9

def test_Candy_updated_set():
    test_candy = Candy("Jolly Rancher", 3.76, 8.9)

    test_candy.name = "KitKat"
    test_candy.price_per_pound = 4.89
    test_candy.candy_weight = 2.3

    assert test_candy.name == "KitKat"
    assert test_candy.price_per_pound == 4.89
    assert test_candy.candy_weight == 2.3