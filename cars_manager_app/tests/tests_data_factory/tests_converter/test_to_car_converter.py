from decimal import Decimal
from typing import Any

import pytest

from cars_manager_app.cars.model import Car
from cars_manager_app.data_loader.factory.car.converter.to_car_converter import ToCarConverter


class TestToCarConverter:

    @pytest.fixture
    def data_before_convert(self) -> list[dict[str, Any]]:
        return [{
            'model': 'BMW',
            'price': 160000.0,
            'color': "BLACK",
            'mileage': 1500,
            'components': ["ABS", "ALLOY WHEELS"]
        }]

    @pytest.fixture
    def data_after_convert(self) -> list[Car]:
        return [Car(model="BMW",
            price=Decimal('160000.0'),
            color="BLACK",
            mileage=1500,
            components=["ABS", "ALLOY WHEELS"]
            )
        ]
    def test_when_converter_works_correctly(self, data_before_convert, data_after_convert) -> None:
        to_car_converter = ToCarConverter()
        assert data_after_convert == to_car_converter.convert(data_before_convert)

    def test_when_conversion_does_not_work(self) -> None:
        with pytest.raises(Exception) as e:
            invalid_data_before_convert = [{
                'model': 'BMW',
                'price': 1600,
            }]
            converter = ToCarConverter()
            converter.convert(invalid_data_before_convert)

