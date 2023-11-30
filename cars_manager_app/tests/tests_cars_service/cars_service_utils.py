import os
from typing import Final

from cars_manager_app.data_loader.factory.car.factory.processor.data_processor import DataProcessor
from cars_manager_app.data_loader.factory.car.factory.json_car_factory import JsonCarFactory
from cars_manager_app.cars.model import Car


def init_cars(file_name: str) -> list[Car]:
    FILE_BASE_PATH: Final = '\\'.join([os.path.dirname(os.path.dirname(__file__)), 'data_test\\'])
    filename = f'{FILE_BASE_PATH}{file_name}'
    return DataProcessor(JsonCarFactory()).process(filename)
