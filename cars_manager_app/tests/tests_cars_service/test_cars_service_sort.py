import pytest

from cars_manager_app.cars.enums import Sort
from ..utils import *


@pytest.mark.parametrize(
    "parameter, expected_sorted",
    [
        (Sort.COLOR, [bmw, mazda, fiat]),
        (Sort.MILEAGE, [bmw, mazda, fiat]),
        (Sort.MODEL, [bmw, fiat, mazda]),
        (Sort.PRICE, [mazda, fiat, bmw])
    ])
def test_when_sorted_data_is_correct(cars_service, parameter: Sort, expected_sorted: list[Car]) -> None:
    sorted_cars = cars_service.sort(parameter, False)
    assert sorted_cars == expected_sorted
