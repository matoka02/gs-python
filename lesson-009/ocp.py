from abc import ABC, abstractclassmethod
from enum import Enum


class Product(Enum):
    SHIRT = 1
    TSHIRT = 2
    PANT = 3


class DiscountCalculator():
    def __init__(self, product_type, cost) -> None:
        self.product_type = product_type
        self.cost = cost

    def get_discount(self):
        if self.product_type == Product.SHIRT:
            return self.cost - (self.cost * 0.10)
        elif self.product_type == Product.TSHIRT:
            return self.cost - (self.cost * 0.15)
        elif self.product_type == Product.PANT:
            return self.cost - (self.cost * 0.20)


ds_shirt = DiscountCalculator(Product.SHIRT, 100)
print(ds_shirt.get_discount())
ds_tshirt = DiscountCalculator(Product.TSHIRT, 1000)
print(ds_tshirt.get_discount())
ds_pant = DiscountCalculator(Product.PANT, 500)
print(ds_pant.get_discount())

print('------------------------------')

# рефакторинг

class DiscountCalculator2(ABC):
    @abstractclassmethod
    def get_discounted_product(cls):
        pass


class DiscountCalculatorShirt(DiscountCalculator2):
    def __init__(self, cost) -> None:
        self.cost = cost

    def get_discounted_product(self):
        return self.cost - (self.cost * 0.10)


class DiscountCalculatorTShirt(DiscountCalculator2):
    def __init__(self, cost) -> None:
        self.cost = cost

    def get_discounted_product(self):
        return self.cost - (self.cost * 0.15)


class DiscountCalculatorPant(DiscountCalculator2):
    def __init__(self, cost) -> None:
        self.cost = cost

    def get_discounted_product(self):
        return self.cost - (self.cost * 0.20)


ds_shirt = DiscountCalculatorShirt(100)
print(ds_shirt.get_discounted_product())
ds_tshirt = DiscountCalculatorTShirt(1000)
print(ds_tshirt.get_discounted_product())
ds_pant = DiscountCalculatorPant(500)
print(ds_pant.get_discounted_product())

print('------------------------------')

