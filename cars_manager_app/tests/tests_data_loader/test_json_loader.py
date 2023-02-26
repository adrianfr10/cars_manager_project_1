import pytest
import os
from typing import Final
from cars_manager_app.data_loader.json_data import get_cars
from ..utils import *


@pytest.fixture
def unpacked_cars() -> list[Car]:
    FILEPATH: Final[str] = '\\'.join([os.path.dirname(os.path.dirname(__file__)), 'data\\cars_test.json'])
    return get_cars(FILEPATH)


def test_get_cars(unpacked_cars) -> None:
    assert unpacked_cars == [bmw, mazda, fiat]
