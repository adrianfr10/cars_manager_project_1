import pytest
import os
import logging
from typing import Final

from cars_manager_app.data_loader.factory.car.factory.processor.data_processor import DataProcessor
from cars_manager_app.data_loader.factory.car.factory.json_car_factory import JsonCarFactory
from ..cars.service import CarsService

logger = logging.getLogger(__name__)


@pytest.fixture
def cars_service() -> CarsService:
    FILE_BASE_PATH: Final = '\\'.join([os.path.dirname(os.path.abspath(__file__)), 'data\\'])
    file = 'cars_test.json'
    filename = f'{FILE_BASE_PATH}{file}'
    cars = DataProcessor(JsonCarFactory()).process(filename)
    return CarsService(cars)
