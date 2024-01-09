from utils.Rules import Rules
from utils.Input import Input
from pytest import MonkeyPatch
from models.Product import Product


def test_exists_rule_with_given_list_of_dicts(monkeypatch: MonkeyPatch):
    usersList = [
        {'name': 'user 1', 'family': 'user 2'},
        {'name': 'user 2', 'family': 'user 3'},
        {'name': 'user 3', 'family': 'user 4'},
    ]

    inputs = ['doesnt exists', 'user 2']
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

    user = Input.get(
        name='name',
        inputMsg='get name:',
        rules=[Rules.exists(usersList, 'name')]
    )

    assert len(user) == 1
    assert user[0] == usersList[1]


def test_exists_rule_with_given_list_of_classes(monkeypatch: MonkeyPatch):
    productsList = [
        Product('product 1', 4),
        Product('product 2', 2),
        Product('product 3', 9),
    ]

    inputs = ['doesnt exists', 'product 2']
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

    product = Input.get(
        name='name',
        inputMsg='get name:',
        rules=[Rules.exists(productsList, 'name')]
    )

    assert len(product) == 1
    assert product[0] == productsList[1]
