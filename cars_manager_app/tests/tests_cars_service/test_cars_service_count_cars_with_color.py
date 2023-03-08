import os
import unittest
from typing import Final
from unittest import TestCase

from cars_manager_app.cars.service import CarsService
from cars_manager_app.data_loader.json_data import get_cars


class TestCarsServiceCountCarsWithColor(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        FILE_BASE_PATH: Final = '\\'.join([os.path.dirname(os.path.dirname(__file__)), 'data\\'])
        file = 'cars_test.json'
        filename = f'{FILE_BASE_PATH}{file}'
        cars = get_cars(filename)
        cls.cars_service = CarsService(cars)

    def test_when_dict_of_counted_by_colors_cars_is_correct(self) -> None:
        cars_counted_by_colors = self.cars_service.count_cars_with_color()
        expected_cars_counted_by_colors = {'BLACK': 1, 'WHITE': 2}
        self.assertDictEqual(expected_cars_counted_by_colors, cars_counted_by_colors)


if __name__ == '__main__':
    unittest.main()
