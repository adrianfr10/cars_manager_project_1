import pytest

from ..utils import mazda, fiat

class TestGetCarsWithMileageGreaterThanIsCorrect:

    def test_when_some_cars_has_mileage_greater_than(self, cars_service) -> None:
        cars_with_greater_mileage = cars_service.get_cars_with_mileage_greater_than(1600)
        expected_cars_with_greater_mileage = [mazda, fiat]
        assert cars_with_greater_mileage == expected_cars_with_greater_mileage

    def test_when_no_car_has_mileage_greater_then(self, cars_service) -> None:
        cars_with_greater_mileage = cars_service.get_cars_with_mileage_greater_than(5000)
        assert cars_with_greater_mileage == []


class TestGetCarsWithMileageGreaterThanIsNotCorrect:

    def test_when_mileage_type_is_not_correct(self, cars_service) -> None:
        with pytest.raises(TypeError) as te:
            cars_service.get_cars_with_mileage_greater_than('1200')
        assert str(te.value) == 'Wrong mileage value type'

