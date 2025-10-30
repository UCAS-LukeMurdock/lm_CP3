# Test cases for Cookie Class
from dessert import DessertItem, Cookie


def test_cookie_default_set():
    test_cookie = Cookie()
    assert test_cookie.name == ""
    assert test_cookie.price_per_dozen == 0.0
    assert test_cookie.cookie_amount == 0
    assert test_cookie.tax_percent == 7.25

def test_cookie_provided_set():
    test_cookie = Cookie("Chocolate Chip", 2.78, 3, 4.53)
    assert test_cookie.name == "Chocolate Chip"
    assert test_cookie.price_per_dozen == 2.78
    assert test_cookie.cookie_amount == 3
    assert test_cookie.tax_percent == 4.53

def test_cookie_updated_set():
    test_cookie = Cookie("Chocolate Chip", 2.78, 3, 4.53)
    test_cookie.name = "Pumpkin"
    test_cookie.price_per_dozen = 1.38
    test_cookie.cookie_amount = 2
    test_cookie.tax_percent = 7.35

    assert test_cookie.name == "Pumpkin"
    assert test_cookie.price_per_dozen == 1.38
    assert test_cookie.cookie_amount == 2
    assert test_cookie.tax_percent == 7.35

def test_cookie_calculateCost_set():
    test_cookie = Cookie("Chocolate Chip", 2.78, 3)
    assert test_cookie.calculateCost() == 0.695

def test_cookie_calculateTax_set():
    test_cookie = Cookie("Chocolate Chip", 2.78, 3)
    assert test_cookie.calculateTax() == 0.05