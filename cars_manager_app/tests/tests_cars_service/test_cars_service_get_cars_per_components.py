import pytest

from ..utils import *


@pytest.fixture
def expected_cars_per_components() -> dict[str, list[Car]]:
    return {'ABS': [bmw],
            'ALLOY WHEELS': [bmw],
            'AIR CONDITIONING': [mazda, fiat],
            'BLUETOOTH': [mazda, fiat]
            }


def test_when_dict_of_cars_per_components_is_correct(cars_service, expected_cars_per_components) -> None:
    cars_per_components = cars_service.get_cars_per_components()
    assert cars_per_components == expected_cars_per_components
