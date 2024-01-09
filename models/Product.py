from dataclasses import dataclass


@dataclass
class Product:
    name: str
    quantity: int
    suffix: str = 'item'

    def __post_init__(self):
        if self.quantity < 0:
            raise ValueError("Quantity couldn't be lower than 0")

    @property
    def itemsLeft(self) -> str:
        return f'{self.quantity} {self.suffix}'

    @property
    def hasLowQuantity(self) -> str:
        return self.quantity < 10
