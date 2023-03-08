from cars_manager_app.cars.exception.cars import CarsServiceException
from ..utils import mazda, fiat
import pytest


def test_when_mileage_is_not_correct(cars_service) -> None:
    with pytest.raises(CarsServiceException) as ce:
        cars_service.get_cars_with_mileage_greater_than(-1)
        assert str(ce.value) == 'Mileage value must be positive'


def test_when_no_car_has_mileage_greater_then(cars_service) -> None:
    cars_with_greater_mileage = cars_service.get_cars_with_mileage_greater_than(5000)
    assert cars_with_greater_mileage == []


def test_when_some_cars_has_mileage_greater_than(cars_service) -> None:
    cars_with_greater_mileage = cars_service.get_cars_with_mileage_greater_than(1600)
    expected_cars_with_greater_mileage = [mazda, fiat]
    assert cars_with_greater_mileage == expected_cars_with_greater_mileage
