from decimal import Decimal
from unittest.mock import MagicMock

import pytest

from cars_manager_app.cars.model import Car
from cars_manager_app.data_loader.factory.car.converter.converter import Converter
from cars_manager_app.data_loader.factory.car.converter.to_car_converter import ToCarConverter
from cars_manager_app.data_loader.factory.car.factory.data_factory import DataFactory
from cars_manager_app.data_loader.factory.car.factory.processor.data_processor import DataProcessor
from cars_manager_app.data_loader.factory.car.loader.data_loader import DataLoader
from cars_manager_app.data_loader.factory.car.loader.json_data_loader import JsonDataLoader
from cars_manager_app.data_loader.factory.car.validator.car_validator import CarValidator
from cars_manager_app.data_loader.factory.car.validator.validator import Validator


class MockDataFactory(DataFactory):

    def create_data_loader(self) -> DataLoader:
        json_data_loader = JsonDataLoader()

        return_value = [
            {
                "model": "BMW",
                "price": 160000.0,
                "color": "BLACK",
                "mileage": 1500,
                "components": [
                    "ABS",
                    "ALLOY WHEELS"
                ]
            },
            {
                "model": "AUDI",
                "price": 100000,
                "color": "white",
                "mileage": 1500.0,
                "components": []
            }
        ]

        json_data_loader.get_data = MagicMock(return_value=return_value)
        return json_data_loader

    def create_validator(self) -> Validator:
        car_validator = CarValidator()
        validated_return_value = [{
            "model": "BMW",
            "price": 160000.0,
            "color": "BLACK",
            "mileage": 1500,
            "components": [
                "ABS",
                "ALLOY WHEELS"
            ]
        }]

        car_validator.validate = MagicMock(return_value=validated_return_value)
        return car_validator

    def create_converter(self) -> Converter:
        to_car_converter = ToCarConverter()
        converted_return_value = [Car(model="BMW",
                                      price=Decimal('160000.0'),
                                      color="BLACK",
                                      mileage=1500,
                                     components=["ABS", "ALLOY WHEELS"]
                                      )
                                  ]
        to_car_converter.convert = MagicMock(return_value=converted_return_value)
        return to_car_converter


@pytest.fixture()
def processed_return_value() -> list[Car]:
    return [Car(model="BMW",
                price=Decimal('160000.0'),
                color="BLACK",
                mileage=1500,
                components=["ABS", "ALLOY WHEELS"]
                )
            ]


def test_when_data_processor_works_correct(processed_return_value) -> None:
    data_processor = DataProcessor(MockDataFactory())
    assert processed_return_value == data_processor.process(None)
