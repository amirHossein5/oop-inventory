from models.Product import Product


class Store:
    __products: list[Product] = []

    @staticmethod
    def products():
        return Store._Store__products
