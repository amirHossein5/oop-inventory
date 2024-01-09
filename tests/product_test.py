from models.Product import Product
import pytest


def test_setting_negative_quantity_raises_error():
    Product('test1', 0, suffix='sfx')

    with pytest.raises(ValueError):
        Product('test1', -1, suffix='sfx')


def test_getting_items_left_property():
    assert Product('test1', 10, suffix='sfx').itemsLeft == '10 sfx'


def test_products_under_certain_quantity_are_considered_as_low_quantity():
    for q in range(11):
        assert Product('test1', q, suffix='sfx').hasLowQuantity == bool(q < 10)
