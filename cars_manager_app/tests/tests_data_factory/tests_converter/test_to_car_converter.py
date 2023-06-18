from typing import Any

import pytest

from cars_manager_app.cars.model import Car
from cars_manager_app.data_loader.factory.car.converter.to_car_converter import ToCarConverter


@pytest.fixture
def car_data() -> dict[str, Any]:
    return {
            'model': 'BMW',
            'price': 160000,
            'color': "BLACK",
            'mileage': 1500,
            'components': ["ABS", "ALLOY WHEELS"]
        }


def test_if_returned_type_is_correct(car_data) -> None:
    converter = ToCarConverter()
    assert type(converter.convert(car_data)) == Car

