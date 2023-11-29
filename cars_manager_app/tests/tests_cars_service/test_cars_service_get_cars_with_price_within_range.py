import pytest

from decimal import Decimal

class TestGetCarsWithinRangeIsCorrect:

    def test_when_some_cars_have_price_within_range(self, cars_service) -> None:
        cars_with_price_within_range = cars_service.get_cars_with_price_within_range(Decimal('155000'), Decimal('170000'))
        assert 'BMW' == cars_with_price_within_range[0].model


    def test_when_no_cars_have_price_within_range(self, cars_service) -> None:
        cars_with_price_within_range = cars_service.get_cars_with_price_within_range(Decimal('1'), Decimal('100'))
        assert cars_with_price_within_range == []


class TestGetCarsWithinRangeIsNotCorrect:

    def test_when_price_ranges_are_not_correct(self, cars_service) -> None:
        with pytest.raises(ValueError) as ve:
            cars_service.get_cars_with_price_within_range(Decimal('5000'), Decimal('2000'))
        assert str(ve.value) == 'Price range is not correct'

    def test_when_values_have_wrong_types(self, cars_service) -> None:
        with pytest.raises(ValueError) as ve:
            cars_service.get_cars_with_price_within_range(1, 10000)
        assert str(ve.value) == 'Wrong price value types'
