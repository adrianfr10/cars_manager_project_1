from .converter import Converter
from cars_manager_app.cars.model import Car
from typing import Any


class ToCarConverter(Converter):

    def convert(self, data: list[dict[str, Any]]) -> list[Any]:
        if not data:
            raise ValueError("Invalid data_test")
        return [Car.of(car_data) for car_data in data]
