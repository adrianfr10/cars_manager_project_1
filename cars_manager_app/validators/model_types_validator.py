from typing import Any
from .basic_validator import *


def validate_car(car_data: dict[str, Any]) -> dict[str, Any]:
    validate_string(car_data['model'])
    validate_decimal(car_data['price'])
    validate_string(car_data['color'])
    validate_number(car_data['mileage'])
    [validate_string(comp) for comp in car_data['components']]
    return car_data
