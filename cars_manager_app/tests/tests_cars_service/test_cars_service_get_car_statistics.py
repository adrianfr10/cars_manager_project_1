import os
import unittest
from typing import Final
from unittest import TestCase

from cars_manager_app.cars.enums import Statistics
from cars_manager_app.cars.service import CarsService
from cars_manager_app.data_loader.json_data import get_cars


class TestCarsServiceGetCarStatistics(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        FILE_BASE_PATH: Final = '\\'.join([os.path.dirname(os.path.dirname(__file__)), 'data\\'])
        file = 'cars_test.json'
        filename = f'{FILE_BASE_PATH}{file}'
        cars = get_cars(filename)
        cls.cars_service = CarsService(cars)

    def test_when_cars_statistics_are_correct(self) -> None:
        cars_statistics = self.cars_service.get_car_statistics(Statistics.PRICE)
        expected_dict_of_car_statistics = {Statistics.PRICE: {'avg': 140000.0, 'max': 160000.0, 'min': 120000.0}}
        self.assertDictEqual(cars_statistics, expected_dict_of_car_statistics)


if __name__ == '__main__':
    unittest.main()
