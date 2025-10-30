# Test cases for Sundae Class
from dessert import DessertItem, IceCream, Sundae


def test_sundae_default_set():
    test_sundae = Sundae()
    assert test_sundae.name == ""
    assert test_sundae.price_per_scoop == 0.0
    assert test_sundae.scoops == 0
    assert test_sundae.topping_name == ""
    assert test_sundae.topping_price == 0.0
    assert test_sundae.tax_percent == 7.25

def test_sundae_provided_set():
    test_sundae = Sundae("Chocolate", 6.32, 7, "Sprinkles", 0.07, 9.99)
    assert test_sundae.name == "Chocolate"
    assert test_sundae.price_per_scoop == 6.32
    assert test_sundae.scoops == 7
    assert test_sundae.topping_name == "Sprinkles"
    assert test_sundae.topping_price == 0.07
    assert test_sundae.tax_percent == 9.99

def test_sundae_updated_set():
    test_sundae = Sundae("Chocolate", 6.32, 7, "Sprinkles", 0.07, 9.99)

    test_sundae.name = "Mint"
    test_sundae.price_per_scoop = 1.24
    test_sundae.scoops = 5
    test_sundae.topping_name = "Oreo"
    test_sundae.topping_price = 4.5
    test_sundae.tax_percent = 1.11

    assert test_sundae.name == "Mint"
    assert test_sundae.price_per_scoop == 1.24
    assert test_sundae.scoops == 5
    assert test_sundae.topping_name == "Oreo"
    assert test_sundae.topping_price == 4.5
    assert test_sundae.tax_percent == 1.11

def test_sundae_calculateCost_set():
    test_sundae = Sundae("Chocolate", 6.32, 7, "Sprinkles", 0.07)
    assert test_sundae.calculateCost() == 44.31

def test_sundae_calculateTax_set():
    test_sundae = Sundae("Chocolate", 6.32, 7, "Sprinkles", 0.07)
    assert test_sundae.calculateTax() == 3.21