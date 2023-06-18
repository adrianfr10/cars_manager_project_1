from .validator import Validator
from typing import Any
from dataclasses import dataclass


@dataclass
class CarValidator(Validator):

    def validate(self, data: dict[str, Any]) -> dict[str, Any]:
        Validator.validate_string(data['model'])
        Validator.validate_decimal(data['price'])
        Validator.validate_string(data['color'])
        Validator.validate_number(data['mileage'])
        [Validator.validate_string(comp) for comp in data['components']]

        return data
