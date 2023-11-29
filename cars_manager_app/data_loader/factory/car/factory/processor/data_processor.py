from ..data_factory import DataFactory
from typing import Any


class DataProcessor:
    def __init__(self, data_factory: DataFactory):
        self.data_loader = data_factory.create_data_loader()
        self.validator = data_factory.create_validator()
        self.converter = data_factory.create_converter()

    def process(self, path: str) -> list[Any]:
        loader_data = self.data_loader.get_data(path)
        validated_data = self.validator.validate(loader_data)
        return self.converter.convert(validated_data)
