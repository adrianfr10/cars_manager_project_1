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
