from dataclasses import dataclass
from decimal import Decimal
from typing import Self


@dataclass
class Car:
    """
    Represents a Car object, with attributes like: model, price, color, mileage and components.
    These objects are being used in the CarsService class, which performs different operations on them.
    """
    model: str
    price: Decimal
    color: str
    mileage: int
    components: list[str]

    @classmethod
    def of(cls, data: dict) -> Self:
        """
        This method takes a car data in a dict form and transforms it into a Car object.
        :param data:
        :return:
        """
        return Car(data['model'],
                   Decimal(data['price']),
                   data['color'],
                   int(data['mileage']),
                   data['components'])

    def has_mileage_greater_than(self, limit_mileage: int) -> bool:
        """
        This method checks if the mileage attribute of one car is greater than specified limit.
        :param limit_mileage:
        :return:
        """
        return self.mileage > limit_mileage

    def with_sorted_components(self) -> Self:
        """
        This method returns a car with components attribute sorted phonetically.
        :return:
        """
        return Car(
            self.model,
            self.price,
            self.color,
            self.mileage,
            sorted(self.components)
        )

    def has_price_within_range(self, price_from: Decimal, price_to: Decimal) -> bool:
        """
        This method checks if car's price is between a specified range
        :param price_from:
        :param price_to:
        :return:
        """
        return price_from <= self.price <= price_to

    def has_price(self, price: Decimal) -> bool:
        """
        This method checks if the price of one car is the same as the price of another car.
        :param price:
        :return:
        """
        return self.price == price

