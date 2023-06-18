from cars_manager_app.data_loader.factory.car.factory.json_car_factory import JsonCarFactory
from unittest.mock import MagicMock
import pytest


@pytest.fixture
def return_value():
    return {
        "model": "BMW",
        "price": 160000.0,
        "color": "BLACK",
        "mileage": 1500,
        "components": [
          "ABS",
          "ALLOY WHEELS"
        ]
    }


def test_data_processor(return_value):
    data_factory = JsonCarFactory()
    data_factory.create_data_loader = MagicMock()

    fake_path = "/path/to/fake_data.json"

    data_loader_mock = MagicMock()
    data_loader_mock.get_data.return_value = return_value
    data_factory.create_data_loader.return_value = data_loader_mock

    test_result = data_factory.create_data_loader(fake_path)

    data_factory.create_data_loader.assert_called_once_with(fake_path)
