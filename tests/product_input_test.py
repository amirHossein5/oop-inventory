from pytest import MonkeyPatch
from models.Product import Product
from models.Store import Store
from utils.ProductInput import ProductInput
import pytest


@pytest.fixture(autouse=True)
def run_around_tests():
    Store.products().clear()


def test_creates_product_from_input(monkeypatch: MonkeyPatch):
    expectedProduct = Product('testname', 2, 'kg')

    inputs = ['testname', 'kg', '2']
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

    product = ProductInput.createProductFromInput()
    assert product == expectedProduct


def test_createProductFromInput_recalls_input_when_invalid_value_given(monkeypatch: MonkeyPatch):
    expectedProduct = Product('testname', 2, 'kg')
    Store.products().append(Product('a product name', 1))

    inputs = [
        '', 'a product name', 'testname'
        '', 'kg',
        'string quantity', '-1', '2'
    ]
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

    product = ProductInput.createProductFromInput()
    assert product == expectedProduct


def test_getProductFromInput_returns_none_when_no_product_exists():
    assert ProductInput.getProductFromInput() is None


def test_getProductFromInput_recalls_input_when_invalid_value_given(monkeypatch: MonkeyPatch):
    expectedProduct = Product('product1', 1)
    Store.products().append(expectedProduct)

    inputs = [
        'a product that does not exists', 'product1'
    ]
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

    product = ProductInput.getProductFromInput()
    assert product == expectedProduct


def test_updating_product_with_updateProductFromInput(monkeypatch: MonkeyPatch):
    oldProduct = Product('old product', 2)

    inputs = [
        'new product',
        'kg',
        '5',
    ]
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

    newProduct = ProductInput.updateProductFromInput(oldProduct)

    assert oldProduct != newProduct
    assert newProduct.name == 'new product'
    assert newProduct.quantity == 5
    assert newProduct.suffix == 'kg'

def test_updateProductFromInput_inputs_have_default_value(monkeypatch: MonkeyPatch):
    oldProduct = Product('old product', 2, suffix='kg')

    inputs = ['', '', '']
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

    newProduct = ProductInput.updateProductFromInput(oldProduct)

    assert newProduct == oldProduct

