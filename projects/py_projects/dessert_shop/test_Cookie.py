# Test cases for Cookie Class
from dessert import DessertItem, Cookie


def test_Cookie_default_set():
    test_cookie = Cookie()
    assert test_cookie.name == ""
    assert test_cookie.price_per_dozen == 0.0
    assert test_cookie.cookie_amount == 0

def test_Cookie_provided_set():
    test_cookie = Cookie("Chocolate Chip", 2.78, 3)
    assert test_cookie.name == "Chocolate Chip"
    assert test_cookie.price_per_dozen == 2.78
    assert test_cookie.cookie_amount == 3

def test_Cookie_updated_set():
    test_cookie = Cookie("Chocolate Chip", 2.78, 3)

    test_cookie.name = "Pumpkin"
    test_cookie.price_per_dozen = 1.38
    test_cookie.cookie_amount = 2

    assert test_cookie.name == "Pumpkin"
    assert test_cookie.price_per_dozen == 1.38
    assert test_cookie.cookie_amount == 2