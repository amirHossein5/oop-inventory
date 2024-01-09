from bootstrap import bootstrap


def actions() -> dict:
    from controllers.ProductsController import ProductsController
    from controllers.MainController import MainController

    return {
        'main_page': MainController.invoke,
        'create_product': ProductsController.create,
        'show_product': ProductsController.show,
        'update_product_quantity': ProductsController.updateQuantity,
        'update_product': ProductsController.update,
        'delete_product': ProductsController.delete,
    }


def main():
    bootstrap()
    return action('main_page', False)


def action(name: str, printBefore: bool = True, params: dict = {}) -> None:
    method = actions().get(name)

    if not method:
        raise ValueError('Method not found in actions')
    if not callable(method):
        raise ValueError(f'{method} is not callable from actions')

    if printBefore:
        print()

    if len(params) == 0:
        return method()
    return method(params)


if __name__ == "__main__":
    main()
