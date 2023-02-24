from ..cars.model import Car
import json
from ..validators.model_types_validator import validate_car


def get_cars(filepath: str) -> list[Car]:
    with open(filepath) as json_file:
        return [Car.of(validate_car(data)) for data in json.load(json_file)]
