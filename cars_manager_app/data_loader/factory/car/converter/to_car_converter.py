from .converter import Converter
from cars_manager_app.cars.model import Car
from typing import Any


class ToCarConverter(Converter):

    def convert(self, data: dict[str, Any]) -> Any:
        return Car.of(data)
