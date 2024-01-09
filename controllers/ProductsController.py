from utils.ProductInput import ProductInput
from main import action
from models.Store import Store
from controllers.Controller import Controller
from utils.Action import Action
from utils.Input import Input
from utils.Rules import Rules


class ProductsController(Controller):
    @staticmethod
    def create() -> None:
        print('-- creating product')

        product = ProductInput.createProductFromInput()

        if Input.confirm('Are you sure want to create?(y/n): '):
            Store.products().append(product)
            print('created')
        else:
            print('cancelled')

        action('main_page')

    @staticmethod
    def show() -> None:
        product = ProductInput.getProductFromInput()

        if product is None:
            print('no product exists, create one first')
            return action('main_page')

        print()
        print(f'-- show product [{product.name}]')
        print(
            f"left: {product.itemsLeft} {'(low)' if product.hasLowQuantity else ''}"
        )
        print(f'suffix: {product.suffix}')

        return Controller.nextActions([
            Action(
                input='change product [q]uantity', key='q',
                action='update_product_quantity',
                params={'product': product}
            ),
            Action(
                input='[u]pdate product properties', key='u',
                action='update_product',
                params={'product': product}
            ),
            Action(
                input='[d]elete product', key='d',
                action='delete_product',
                params={'product': product}
            ),
        ])

    @staticmethod
    def updateQuantity(params: dict) -> None:
        product = params['product']

        print(f'-- update {product.name} quantity')

        newQuantity = Input.get(
            name='quantity',
            inputMsg=f'from {product.itemsLeft} to: ',
            rules=[Rules.required, Rules.uint],
        )

        product.quantity = newQuantity

        print('quantity updated')
        action('main_page')

    @staticmethod
    def update(params: dict) -> None:
        product = params['product']

        print(f'-- update product {product.name}')
        newProduct = ProductInput.updateProductFromInput(product)
        print()

        if Input.confirm('Are you sure want to update?(y/n): '):
            product.name = newProduct.name
            product.quantity = newProduct.quantity
            product.suffix = newProduct.suffix
            print('updated')
        else:
            print('cancelled')

        action('main_page')

    @staticmethod
    def delete(params: dict) -> None:
        product = params['product']

        print(f'-- Delete [{product.name}] with {product.itemsLeft} left')

        if Input.confirm('Are you sure?(y/n): '):
            for k, p in enumerate(Store.products()):
                if p is product:
                    del (Store.products()[k])
            print('deleted')
        else:
            print('cancelled')

        action('main_page')
