from abc import ABC, abstractmethod


class DataFactory(ABC):

    @abstractmethod
    def create_data_loader(self):
        pass

    @abstractmethod
    def create_validator(self):
        pass

    @abstractmethod
    def create_converter(self):
        pass
