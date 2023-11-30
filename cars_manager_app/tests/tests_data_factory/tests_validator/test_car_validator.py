import pytest

from cars_manager_app.data_loader.factory.car.validator.car_validator import CarValidator


class TestCarValidator:

    def test_when_validate_car_is_correct(self) -> None:
        validator = CarValidator()
        car_data = [{
            "model": "BMW",
            "price": 160000.0,
            "color": "BLACK",
            "mileage": 1500,
            "components": [
                "ABS",
                "ALLOY WHEELS"
            ]
        }]
        assert validator.validate(car_data)

    def test_when_validate_car_raises_exception(self) -> None:
        invalid_car_data = [{
            "model": "BMW",
            "price": 160000,
            "color": "BLACK",
            "mileage": 1500,
            "components": [
                "abs",
                "ALLOY WHEELS"
            ]
        }
        ]
        with pytest.raises(ValueError):
            validator = CarValidator()
            validator.validate(invalid_car_data)
