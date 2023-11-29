import pytest

from cars_manager_app.cars.model import Car
from ..utils import bmw, mazda, fiat


class TestGetCarsPerComponentsIsCorrect:
    @pytest.fixture
    def expected_cars_per_components(self) -> dict[str, list[Car]]:
        return {'AIR CONDITIONING': [mazda, fiat],
                'BLUETOOTH': [mazda, fiat],
                'ABS': [bmw],
                'ALLOY WHEELS': [bmw],
                }


    def test_when_dict_of_cars_per_components_is_correct(self, cars_service, expected_cars_per_components) -> None:
        cars_per_components = cars_service.get_cars_per_components()
        assert cars_per_components == expected_cars_per_components
