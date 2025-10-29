# Test cases for Sundae Class
from dessert import DessertItem, IceCream, Sundae


def test_Sundae_default_set():
    test_sundae = Sundae()
    assert test_sundae.name == ""
    assert test_sundae.price_per_scoop == 0.0
    assert test_sundae.scoops == 0
    assert test_sundae.topping_name == ""
    assert test_sundae.topping_price == 0.0
    assert test_candy.tax_percent == 7.25

def test_Sundae_provided_set():
    test_sundae = Sundae("Chocolate", 6.32, 7, "Sprinkles", 0.07)
    assert test_sundae.name == "Chocolate"
    assert test_sundae.price_per_scoop == 6.32
    assert test_sundae.scoops == 7
    assert test_sundae.topping_name == "Sprinkles"
    assert test_sundae.topping_price == 0.07
    assert test_candy.tax_percent == 7.25

def test_Sundae_updated_set():
    test_sundae = Sundae("Chocolate", 6.32, 7, "Sprinkles", 0.07)

    test_sundae.name = "Mint"
    test_sundae.price_per_scoop = 1.24
    test_sundae.scoops = 5
    test_sundae.topping_name = "Oreo"
    test_sundae.topping_price = 4.5
    test_candy.tax_percent = 7.25

    assert test_sundae.name == "Mint"
    assert test_sundae.price_per_scoop == 1.24
    assert test_sundae.scoops == 5
    assert test_sundae.topping_name == "Oreo"
    assert test_sundae.topping_price == 4.5
    assert test_candy.tax_percent == 7.25

def test_Candy_calculateCost_set():
    test_candy = Candy("Jolly Rancher", 3.76, 8.9)
    assert test_candy.calculateCost() == 33.46

def test_Candy_calculateTax_set():
    test_candy = Candy("Jolly Rancher", 3.76, 8.9)
    assert test_candy.calculateTax() == 2.43