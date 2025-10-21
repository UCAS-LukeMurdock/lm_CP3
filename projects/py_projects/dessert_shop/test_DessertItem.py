# Test case for DessertItem Class
from dessert import DessertItem


def test_DessertItem_default_set():
    test_item = DessertItem()
    assert test_item.name == ""

def test_DessertItem_provided_set():
    test_item = DessertItem("Cake")
    assert test_item.name == "Cake"

def test_DessertItem_updated_set():
    test_item = DessertItem("Cake")
    test_item.name = "Cupcake"
    assert test_item.name == "Cupcake"