from .data_factory import DataFactory
from ..loader.json_data_loader import JsonDataLoader
from ..validator.car_validator import CarValidator
from ..converter.to_car_converter import ToCarConverter


class JsonCarFactory(DataFactory):
    def create_data_loader(self):
        return JsonDataLoader()

    def create_validator(self):
        return CarValidator()

    def create_converter(self):
        return ToCarConverter()
