import pytest
import os
import logging
from typing import Final
from ..cars.model import Car
from ..cars.service import CarsService
from ..data_loader.json_data import get_cars
logger = logging.getLogger(__name__)


@pytest.fixture
def cars_service() -> CarsService:
    FILE_BASE_PATH: Final = '\\'.join([os.path.dirname(os.path.abspath(__file__)), 'data\\'])
    file = 'cars_test.json'
    filename = f'{FILE_BASE_PATH}{file}'
    cars = get_cars(filename)
    return CarsService(cars)
