from controllers.MainController import MainController
from controllers.ProductsController import ProductsController

actions = {
    'main_page': MainController.invoke,
    'create_product': ProductsController.create,
    'show_product': ProductsController.show,
    'update_product_quantity': ProductsController.updateQuantity,
    'update_product': ProductsController.update,
    'delete_product': ProductsController.delete,
}
