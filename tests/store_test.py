import pytest
from models.Store import Store
from models.Product import Product


@pytest.fixture(autouse=True)
def run_around_tests():
    Store.products().clear()


def test_products_property_is_private():
    assert '_Store__products' in Store.__dict__

    with pytest.raises(AttributeError):
        Store.__products


def test_store_has_zero_products_by_default():
    assert len(Store.products()) == 0


def test_adding_products_to_store():
    products = [
        Product('test1', quantity=10, suffix='item'),
        Product('test2', quantity=1, suffix='kg'),
    ]

    for product in products:
        Store.products().append(product)

    assert Store.products() == products
