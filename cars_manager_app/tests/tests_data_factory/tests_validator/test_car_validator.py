import pytest
from typing import Any
from cars_manager_app.data_loader.factory.car.validator.car_validator import CarValidator


@pytest.fixture
def car_data() -> dict[str, Any]:
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


def test_if_validate_car_is_correct(car_data) -> None:
    validator = CarValidator()
    assert validator.validate(car_data)

