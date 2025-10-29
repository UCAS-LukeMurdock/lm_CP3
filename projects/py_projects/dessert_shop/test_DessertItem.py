# Test cases for DessertItem Class
from dessert import DessertItem, Candy


def test_DessertItem_default_set():
    test_item = Candy()
    assert test_item.name == ""
    assert test_item.tax_percent == 7.25

def test_DessertItem_provided_set():
    test_item = Candy("Jolly Rancher", 3.76, 8.9, 6.13)
    assert test_item.name == "Jolly Rancher"
    assert test_item.tax_percent == 6.13

def test_DessertItem_updated_set():
    test_item = Candy("Jolly Rancher", 3.76, 8.9, 6.3)
    test_item.name = "KitKat"
    test_item.tax_percent == 3.57

    assert test_item.name == "KitKat"
    assert test_item.tax_percent == 3.57