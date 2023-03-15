from .model import Car
from .enums import Sort, Statistics
from .exception.cars import CarsServiceException

from collections import Counter, defaultdict
from decimal import Decimal
from statistics import mean


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

    # -----------------------------------------------------------------------------------------------

    def get_cars_with_mileage_greater_than(self, mileage: int) -> list[Car]:
        """
        Method returns a list of Car objects with mileage greater than value given as an argument.
        :param mileage:
        :return:
        """
        if mileage <= 0:
            raise CarsServiceException('Mileage value must be positive')

        return [car for car in self.cars if car.has_mileage_greater_than(mileage)]

    # -----------------------------------------------------------------------------------------------

    def count_cars_with_color(self) -> dict[str, int]:
        """
        Method counts how many Car objects have certain color and returns a dict with key - color
         and value - count of Car object of that color.
        :return:
        """
        return dict(Counter([car.color for car in self.cars]))

    # -----------------------------------------------------------------------------------------------

    def get_most_expensive_cars_per_model(self) -> dict[str, list[Car]]:
        """
        Method returns a dict of Car objects, with key - Car model and value - most expensive
        Car objects from certain model.
        :return:
        """
        grouped_by_model = defaultdict(list)
        for car in self.cars:
            grouped_by_model[car.model].append(car)

        color_with_most_expensive_cars = []
        for color, cars in grouped_by_model.items():
            grouped_by_price = defaultdict(list)
            for car in cars:
                grouped_by_price[car.price].append(car)
                max_price_cars = max(grouped_by_price.items(), key=lambda pair: pair[0])[1]
                color_with_most_expensive_cars.append((color, max_price_cars))
        return dict(color_with_most_expensive_cars)

    # -----------------------------------------------------------------------------------------------

    def get_car_statistics(self, statistics_type: Statistics) -> dict[Statistics, dict]:
        """
        Method returns a dict of statistics of a Car objects collection that include average, max
        and min value for price and mileage.
        :return:
        """

        return {
            statistics_type: {
                "avg": mean([getattr(car, statistics_type.value) for car in self.cars]),
                "max": max([getattr(car, statistics_type.value) for car in self.cars]),
                "min": min([getattr(car, statistics_type.value) for car in self.cars])
            }
        }

    # -----------------------------------------------------------------------------------------------
    def get_cars_with_sorted_components(self) -> list[Car]:
        """
        Method returns a list of Car objects with alphabetically sorted components.
        :return:
        """
        return [car.with_sorted_components() for car in self.cars]

    # -----------------------------------------------------------------------------------------------
    def get_cars_with_price_within_range(self, price_min: Decimal, price_max: Decimal) -> list[Car]:
        """
        Method returns a list of Car objects that have a price parameter in range of a given min and max value.
        :param price_min:
        :param price_max:
        :return:
        """
        if price_min <= Decimal('0') or price_min > price_max:
            raise ValueError('Price range is not correct')

        return [car for car in self.cars if car.has_price_within_range(price_min, price_max)]

    # -----------------------------------------------------------------------------------------------
    def get_most_expensive(self) -> list[Car]:
        """
        Method returns a list of Car object(s) of the highest price out of all objects in a collection.
        :return:
        """
        grouped_by_price = defaultdict(list)

        for car in self.cars:
            grouped_by_price[car.price].append(car)
        max_price = max(grouped_by_price.keys())
        return [v for k, v in grouped_by_price.items() if k == max_price][0]
