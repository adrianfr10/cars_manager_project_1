import pytest

from ..utils import bmw, mazda, fiat

class TestGetCarsWithSortedComponentsIsCorrect:
    @pytest.mark.parametrize(
        "car_index, expected_sorted",
        [
            (0, sorted(bmw.components)),
            (1, sorted(mazda.components)),
            (2, sorted(fiat.components)),
        ])
    def test_when_cars_with_sorted_components_are_correct(self, cars_service, car_index, expected_sorted) -> None:
        cars_with_sorted_components = cars_service.get_cars_with_sorted_components()
        assert cars_with_sorted_components[car_index].components == expected_sorted
