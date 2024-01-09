from dataclasses import dataclass
from models.Store import Store
from models.Product import Product


@dataclass
class Validation:
    hasErrors: bool
    value: any = None
    castedValue: any = None
    errorMsg: str = ''


class Rules:
    @staticmethod
    def required(fieldName: str, value: str) -> Validation:
        if len(value.strip()) == 0:
            return Validation(
                hasErrors=True,
                errorMsg=f'{fieldName} should not be empty'
            )
        return Validation(hasErrors=False, value=value, castedValue=value)

    @staticmethod
    def uint(fieldName: str, value: str) -> Validation:
        if not value.isdigit() or int(value) < 0:
            return Validation(
                hasErrors=True,
                errorMsg=f'{fieldName} must be a non negative number'
            )

        return Validation(hasErrors=False, value=value, castedValue=int(value))

    @staticmethod
    def unique(ignore: Product = None) -> Validation:
        def __unique(fieldName: str, value: str):
            products = [p for p in Store.products() if p.name == value]

            if ignore:
                for k, p in enumerate(products):
                    if p is ignore:
                        del (products[k])

            if len(products) != 0:
                return Validation(
                    hasErrors=True,
                    errorMsg=f'{fieldName} should be unique'
                )

            return Validation(hasErrors=False, value=value, castedValue=value)

        return __unique

    @staticmethod
    def exists(items: list[dict], key: str) -> Validation:
        def __exists(fieldName: str, value: str):
            found = []

            for k, i in enumerate(items):
                if hasattr(i, '__dict__'):
                    i = i.__dict__

                if i[key] == value:
                    found.append(items[k])

            if len(found) != 0:
                return Validation(hasErrors=False, value=value, castedValue=found)

            return Validation(
                hasErrors=True,
                errorMsg=f'"{value}" not found'
            )

        return __exists
