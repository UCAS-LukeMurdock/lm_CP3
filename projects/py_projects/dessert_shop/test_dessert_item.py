# Test cases for DessertItem Class
from dessert import DessertItem, Candy


def test_dessert_item_default_set():
    test_dessert = Candy()
    assert test_dessert.name == ""
    assert test_dessert.tax_percent == 7.25

def test_dessert_item_provided_set():
    test_dessert = Candy("Jolly Rancher", 3.76, 8.9, 6.13)
    assert test_dessert.name == "Jolly Rancher"
    assert test_dessert.tax_percent == 6.13

def test_dessertitem_updated_set():
    test_dessert = Candy("Jolly Rancher", 3.76, 8.9, 6.3)
    test_dessert.name = "KitKat"
    test_dessert.tax_percent == 3.57

    assert test_dessert.name == "KitKat"
    assert test_dessert.tax_percent == 3.57