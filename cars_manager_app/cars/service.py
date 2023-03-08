from .model import Car
from .enums import Sort
from .exception.cars import CarsServiceException

from collections import Counter


class CarsService:

    def __init__(self, cars: list[Car]) -> None:
        self.cars = cars

    # -----------------------------------------------------------------------------------------------
    def sort(self, sort: Sort, descending: bool) -> list[Car]:
        """
        Method sorts a collection of Car objects, color, mileage, price or model wise, according to
        an argument given, and has also a possibility of sorting in ascending or descending order.
        :param sort:
        :param descending:
        :return:
        """
        match sort:
            case Sort.COLOR:
                return sorted(self.cars, key=lambda car: car.color, reverse=descending)
            case Sort.MILEAGE:
                return sorted(self.cars, key=lambda car: car.mileage, reverse=descending)
            case Sort.MODEL:
                return sorted(self.cars, key=lambda car: car.model, reverse=descending)
            case Sort.PRICE:
                return sorted(self.cars, key=lambda car: car.price, reverse=descending)

    def get_cars_with_mileage_greater_than(self, mileage: int) -> list[Car]:
        """
        Method returns a list of Car objects with mileage greater than value given as an argument.
        :param mileage:
        :return:
        """
        if mileage <= 0:
            raise CarsServiceException('Mileage value must be positive')

        return [car for car in self.cars if car.has_mileage_greater_than(mileage)]

    def count_cars_with_color(self) -> dict[str, int]:
        """
        Method counts how many Car objects have certain color and returns a dict with key - color
         and value - count of Car object of that color.
        :return:
        """
        return dict(Counter([car.color for car in self.cars]))
