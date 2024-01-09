from models.Store import Store
from utils.Action import Action
from controllers.Controller import Controller


class MainController(Controller):
    @staticmethod
    def invoke() -> None:
        print('Inventory Overview:')
        print('(* as low quantity)')
        print()

        for product in Store.products():
            prefix = '*' if product.hasLowQuantity else '-'

            print(f'{prefix} [{product.name}] {product.itemsLeft} left')

        return Controller.nextActions([
            Action(input='[c]reate product', key='c', action='create_product'),
            Action(input='[s]how product actions', key='s', action='show_product'),
            Action(input='[q]uit', key='q', action=lambda _: exit)
        ])
