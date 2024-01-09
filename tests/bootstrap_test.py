from models.Store import Store
from bootstrap import bootstrap
import pytest


@pytest.fixture(autouse=True)
def run_around_tests():
    Store.products().clear()


def test_adds_products_to_store():
    assert len(Store.products()) == 0

    bootstrap()

    assert len(Store.products()) != 0
