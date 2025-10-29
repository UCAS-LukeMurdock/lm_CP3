# Test cases for Cookie Class
from dessert import DessertItem, Cookie


def test_Cookie_default_set():
    test_cookie = Cookie()
    assert test_cookie.name == ""
    assert test_cookie.price_per_dozen == 0.0
    assert test_cookie.cookie_amount == 0
    assert test_candy.tax_percent == 7.25

def test_Cookie_provided_set():
    test_cookie = Cookie("Chocolate Chip", 2.78, 3)
    assert test_cookie.name == "Chocolate Chip"
    assert test_cookie.price_per_dozen == 2.78
    assert test_cookie.cookie_amount == 3
    assert test_candy.tax_percent == 7.25

def test_Cookie_updated_set():
    test_cookie = Cookie("Chocolate Chip", 2.78, 3)

    test_cookie.name = "Pumpkin"
    test_cookie.price_per_dozen = 1.38
    test_cookie.cookie_amount = 2
    test_candy.tax_percent = 7.25

    assert test_cookie.name == "Pumpkin"
    assert test_cookie.price_per_dozen == 1.38
    assert test_cookie.cookie_amount == 2
    assert test_candy.tax_percent == 7.25

def test_Candy_calculateCost_set():
    test_candy = Candy("Jolly Rancher", 3.76, 8.9)
    assert test_candy.calculateCost() == 33.46

def test_Candy_calculateTax_set():
    test_candy = Candy("Jolly Rancher", 3.76, 8.9)
    assert test_candy.calculateTax() == 2.43