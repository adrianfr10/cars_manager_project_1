import os

from cars_manager_app.cars.service import CarsService
from cars_manager_app.data_loader.factory.car.factory.json_car_factory import JsonCarFactory
from cars_manager_app.data_loader.factory.car.factory.processor.data_processor import DataProcessor


def load_cars_service() -> CarsService:
    current_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_path, '..', 'data_test', 'cars_test.json')
    cars = DataProcessor(JsonCarFactory()).process(file_path)
    cars_service = CarsService(cars)
    return cars_service