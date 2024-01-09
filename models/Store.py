from models.Product import Product


class Store:
    __products: list[Product] = []

    @staticmethod
    def products() -> list[Product]:
        return Store._Store__products
