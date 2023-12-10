import pytest

from cars_manager_app.cars.enums import Sort
from cars_manager_app.cars.model import Car
from ..utils import bmw, mazda, fiat


class TestSortIsCorrect:

    @pytest.mark.parametrize(
        "parameter, expected_sorted",
        [
            (Sort.COLOR, [bmw, mazda, fiat]),
            (Sort.MILEAGE, [bmw, mazda, fiat]),
            (Sort.MODEL, [bmw, fiat, mazda]),
            (Sort.PRICE, [mazda, fiat, bmw])
        ])
    def test_when_sorted_data_is_correct(self, cars_service, parameter: Sort, expected_sorted: list[Car]) -> None:
        sorted_cars = cars_service.sort(cars_service.get_comparison_func(parameter), False)
        assert sorted_cars == expected_sorted

class TestSortNotCorrect:

    def test_sort_attribute_incorrect(self, cars_service) -> None:
        with pytest.raises(ValueError) as ve:
            cars_service.sort(cars_service.get_comparison_func(5), False)
        assert str(ve.value) == "Invalid sort criteria"

    def test_sort_descending_value_incorrect(self, cars_service) -> None:
        with pytest.raises(ValueError) as ve:
            cars_service.sort(cars_service.get_comparison_func(Sort.COLOR), "True")
        assert str(ve.value) == "Descending parameter must be a boolean value."
