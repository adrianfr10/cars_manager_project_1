from .model import Car
from .enums import Sort


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
