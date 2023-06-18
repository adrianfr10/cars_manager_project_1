from cars_manager_app.data_loader.factory.car.factory.processor.data_processor import DataProcessor
from cars_manager_app.data_loader.factory.car.factory.json_car_factory import JsonCarFactory
from cars_manager_app.cars.service import CarsService
import os


def main():
    current_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_path, '..', 'data', 'cars_test.json')
    cars = DataProcessor(JsonCarFactory()).process(file_path)
    cars_service = CarsService(cars)

    # Place here in future code to manage cars service methods

    return cars_service


if __name__ == '__main__':
    main()
