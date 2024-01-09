from models.Store import Store
from models.Product import Product


def bootstrap() -> None:
    Store.products().append(Product('rice', quantity=4, suffix='kg'))
    Store.products().append(Product('mouse', quantity=23))
    Store.products().append(Product('pizza', quantity=10))
