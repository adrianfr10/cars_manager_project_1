import os
import unittest
from typing import Final
from unittest import TestCase

from cars_manager_app.cars.service import CarsService
from .cars_service_utils import init_cars


class TestCarsServiceCountCarsWithColor(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.cars_service = CarsService(init_cars('cars_test.json'))

    def test_when_dict_of_counted_by_colors_cars_is_correct(self) -> None:
        cars_counted_by_colors = self.cars_service.count_cars_with_color()
        expected_cars_counted_by_colors = {'BLACK': 1, 'WHITE': 2}
        self.assertDictEqual(expected_cars_counted_by_colors, cars_counted_by_colors)


if __name__ == '__main__':
    unittest.main()
