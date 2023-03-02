import pytest
import os
import logging
from typing import Final
from ..cars.model import Car
from ..data_loader.json_data import get_cars
logger = logging.getLogger(__name__)


@pytest.fixture
def cars_service() -> list[Car]:
    FILE_BASE_PATH: Final = '\\'.join([os.path.dirname(os.path.abspath(__file__)), 'data\\'])
    file = 'cars_test.json'
    filename = f'{FILE_BASE_PATH}{file}'
    return get_cars(filename)
