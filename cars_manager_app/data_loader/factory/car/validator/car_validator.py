from .validator import Validator
from typing import Any
from dataclasses import dataclass


@dataclass
class CarValidator(Validator):

    def validate(self, data: list[dict[str, Any]]) -> list[dict[str, Any]]:

        if len(data) == 0:
            raise ValueError("File has an empty list")

        for car_data in data:
            Validator.validate_string(car_data['model'])
            Validator.validate_decimal(car_data['price'])
            Validator.validate_string(car_data['color'])
            Validator.validate_number(car_data['mileage'])
            [Validator.validate_string(comp) for comp in car_data['components']]

        return data
