# Test cases for IceCream Class
from dessert import DessertItem, IceCream


def test_IceCream_default_set():
    test_ice_cream = IceCream()
    assert test_ice_cream.name == ""
    assert test_ice_cream.price_per_scoop == 0.0
    assert test_ice_cream.scoops == 0
    assert test_candy.tax_percent == 7.25

def test_IceCream_provided_set():
    test_ice_cream = IceCream("Chocolate", 6.32, 7)
    assert test_ice_cream.name == "Chocolate"
    assert test_ice_cream.price_per_scoop == 6.32
    assert test_ice_cream.scoops == 7
    assert test_candy.tax_percent == 7.25

def test_IceCream_updated_set():
    test_ice_cream = IceCream("Chocolate", 6.32, 7)

    test_ice_cream.name = "Mint"
    test_ice_cream.price_per_scoop = 1.24
    test_ice_cream.scoops = 5
    test_candy.tax_percent = 7.25

    assert test_ice_cream.name == "Mint"
    assert test_ice_cream.price_per_scoop == 1.24
    assert test_ice_cream.scoops == 5
    assert test_candy.tax_percent == 7.25

def test_Candy_calculateCost_set():
    test_candy = Candy("Jolly Rancher", 3.76, 8.9)
    assert test_candy.calculateCost() == 33.46

def test_Candy_calculateTax_set():
    test_candy = Candy("Jolly Rancher", 3.76, 8.9)
    assert test_candy.calculateTax() == 2.43