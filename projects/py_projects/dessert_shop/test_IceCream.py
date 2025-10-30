# Test cases for IceCream Class
from dessert import DessertItem, IceCream


def test_icecream_default_set():
    test_icecream = IceCream()
    assert test_icecream.name == ""
    assert test_icecream.price_per_scoop == 0.0
    assert test_icecream.scoops == 0
    assert test_icecream.tax_percent == 7.25

def test_icecream_provided_set():
    test_icecream = IceCream("Chocolate", 6.32, 7, 1.07)
    assert test_icecream.name == "Chocolate"
    assert test_icecream.price_per_scoop == 6.32
    assert test_icecream.scoops == 7
    assert test_icecream.tax_percent == 1.07

def test_icecream_updated_set():
    test_icecream = IceCream("Chocolate", 6.32, 7, 1.07)

    test_icecream.name = "Mint"
    test_icecream.price_per_scoop = 1.24
    test_icecream.scoops = 5
    test_icecream.tax_percent = 2.76

    assert test_icecream.name == "Mint"
    assert test_icecream.price_per_scoop == 1.24
    assert test_icecream.scoops == 5
    assert test_icecream.tax_percent == 2.76

def test_icecream_calculateCost_set():
    test_icecream = IceCream("Chocolate", 6.32, 7)
    assert test_icecream.calculateCost() == 44.24

def test_icecream_calculateTax_set():
    test_icecream = IceCream("Chocolate", 6.32, 7)
    assert test_icecream.calculateTax() == 3.21