from models.Product import Product
from utils.Input import Input
from utils.Rules import Rules
from models.Store import Store


class ProductInput(Input):
    @staticmethod
    def createProductFromInput() -> Product:
        name = Input.get(
            name='name',
            inputMsg='product name: ',
            rules=[Rules.required, Rules.unique(ignore=None)]
        )
        suffix = Input.get(
            name='suffix',
            inputMsg='product suffix(kg,item,..): ',
        )
        quantity = Input.get(
            name='quantity',
            inputMsg='quantity: ',
            rules=[Rules.required, Rules.uint]
        )
        return Product(name, quantity, suffix)

    @staticmethod
    def updateProductFromInput(product: Product) -> None:
        name = Input.get(
            name='name',
            inputMsg=f'new name({product.name}): ',
            rules=[Rules.required, Rules.unique(ignore=product)],
            default=product.name
        )
        suffix = Input.get(
            name='suffix',
            inputMsg=f'new suffix({product.suffix}): ',
            default=product.suffix
        )
        quantity = Input.get(
            name='quantity',
            inputMsg=f'quantity({product.quantity}): ',
            rules=[Rules.required, Rules.uint],
            default=product.quantity
        )

        return Product(name, quantity, suffix)

    @staticmethod
    def getProductFromInput() -> Product | None:
        if len(Store.products()) == 0:
            return None

        product = Input.get(
            name='name',
            inputMsg='write product name: ',
            rules=[Rules.required, Rules.exists(Store.products(), 'name')]
        )

        return product[0]
