# Test cases for IceCream Class
from dessert import DessertItem, IceCream


def test_IceCream_default_set():
    test_ice_cream = IceCream()
    assert test_ice_cream.name == ""
    assert test_ice_cream.price_per_scoop == 0.0
    assert test_ice_cream.scoops == 0

def test_IceCream_provided_set():
    test_ice_cream = IceCream("Chocolate", 6.32, 7)
    assert test_ice_cream.name == "Chocolate"
    assert test_ice_cream.price_per_scoop == 6.32
    assert test_ice_cream.scoops == 7

def test_IceCream_updated_set():
    test_ice_cream = IceCream("Chocolate", 6.32, 7)

    test_ice_cream.name = "Mint"
    test_ice_cream.price_per_scoop = 1.24
    test_ice_cream.scoops = 5

    assert test_ice_cream.name == "Mint"
    assert test_ice_cream.price_per_scoop == 1.24
    assert test_ice_cream.scoops == 5