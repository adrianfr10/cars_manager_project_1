from dataclasses import dataclass
from decimal import Decimal
from typing import Self


@dataclass
class Car:
    model: str
    price: Decimal
    color: str
    mileage: int
    components: list[str]

    @classmethod
    def of(cls, data: dict) -> Self:
        return Car(data['model'],
                   Decimal(data['price']),
                   data['color'],
                   int(data['mileage']),
                   data['components'])

    def has_mileage_greater_than(self, limit_mileage: int) -> bool:
        return self.mileage > limit_mileage

    def with_sorted_components(self) -> Self:
        return Car(
            self.model,
            self.price,
            self.color,
            self.mileage,
            sorted(self.components)
        )

    def has_price_within_range(self, price_from: Decimal, price_to: Decimal) -> bool:
        return price_from <= self.price <= price_to

    def has_price(self, price: Decimal) -> bool:
        return self.price == price

