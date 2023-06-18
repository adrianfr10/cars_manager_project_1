import unittest

from cars_manager_app.data_loader.factory.car.converter.to_car_converter import ToCarConverter
from cars_manager_app.data_loader.factory.car.factory.json_car_factory import JsonCarFactory
from cars_manager_app.data_loader.factory.car.loader.json_data_loader import JsonDataLoader
from cars_manager_app.data_loader.factory.car.validator.car_validator import CarValidator


class TestJsonCarFactory(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.json_car_factory = JsonCarFactory()

    def test_if_type_of_create_data_loader_is_correct(self) -> None:
        self.assertIsInstance(self.json_car_factory.create_data_loader(), JsonDataLoader)

    def test_if_type_of_create_validator_is_correct(self) -> None:
        self.assertIsInstance(self.json_car_factory.create_validator(), CarValidator)

    def test_if_type_of_create_converter_is_correct(self) -> None:
        self.assertIsInstance(self.json_car_factory.create_converter(), ToCarConverter)


if __name__ == '__main__':
    unittest.main()
