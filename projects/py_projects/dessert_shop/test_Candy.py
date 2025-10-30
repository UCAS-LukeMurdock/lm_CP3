# Test cases for Candy Class
from dessert import DessertItem, Candy


def test_candy_default_set():
    test_candy = Candy()
    assert test_candy.name == ""
    assert test_candy.price_per_pound == 0.0
    assert test_candy.candy_weight == 0.0
    assert test_candy.tax_percent == 7.25

def test_candy_provided_set():
    test_candy = Candy("Jolly Rancher", 3.76, 8.9, 6.13)
    assert test_candy.name == "Jolly Rancher"
    assert test_candy.price_per_pound == 3.76
    assert test_candy.candy_weight == 8.9
    assert test_candy.tax_percent == 6.13

def test_candy_updated_set():
    test_candy = Candy("Jolly Rancher", 3.76, 8.9, 6.13)

    test_candy.name = "KitKat"
    test_candy.price_per_pound = 4.89
    test_candy.candy_weight = 2.3
    test_candy.tax_percent = 8.97

    assert test_candy.name == "KitKat"
    assert test_candy.price_per_pound == 4.89
    assert test_candy.candy_weight == 2.3
    assert test_candy.tax_percent == 8.97

def test_candy_calculateCost_set():
    test_candy = Candy("Jolly Rancher", 3.76, 8.9)
    assert test_candy.calculateCost() == 33.46

def test_candy_calculateTax_set():
    test_candy = Candy("Jolly Rancher", 3.76, 8.9)
    assert test_candy.calculateTax() == 2.43