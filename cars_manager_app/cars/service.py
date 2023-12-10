from collections import Counter, defaultdict
from decimal import Decimal
from statistics import mean
from typing import Callable, Any

from .enums import Sort, Statistics
from .model import Car


class CarsService:

    def __init__(self, cars: list[Car]) -> None:
        if not cars:
            raise ValueError("Initial car list cannot be empty")
        self.cars = cars

    # -----------------------------------------------------------------------------------------------

    def sort(self, comparison_func: Callable, descending: bool) -> list[Car]:
        if not isinstance(descending, bool):
            raise ValueError("Descending parameter must be a boolean value.")
        return sorted(self.cars, key=comparison_func, reverse=descending)

    @staticmethod
    def get_comparison_func(sort_by: Sort) -> Callable[[Car], Any]:
        """
        Returns a comparison function based on the sort criteria and order.
        :param sort_by: Attribute to sort by (e.g., "color", "mileage", "model", "price").
        :return: Comparison function.
        """
        match sort_by:
            case Sort.COLOR:
                return lambda car: car.color
            case Sort.MILEAGE:
                return lambda car: car.mileage
            case Sort.MODEL:
                return lambda car: car.model
            case Sort.PRICE:
                return lambda car: car.price
            case _:
                raise ValueError("Invalid sort criteria")

    # # -----------------------------------------------------------------------------------------------

    def get_cars_with_mileage_greater_than(self, mileage: int) -> list[Car]:
        """
        Method returns a list of Car objects with mileage greater than value given as an argument.
        :param mileage:
        :return:
        """
        if not isinstance(mileage, int):
            raise TypeError("Wrong mileage value type")

        return [car for car in self.cars if car.has_mileage_greater_than(mileage)]

    # -----------------------------------------------------------------------------------------------

    def count_cars_with_color(self) -> dict[str, int]:
        """
        Method counts how many Car objects have certain color and returns a dict with key - color
         and value - count of Car object of that color. Collection is sorted by descending values
        :return:
        """
        cars_with_counted_colors = Counter([car.color for car in self.cars])
        return dict(sorted(cars_with_counted_colors.items(), key=lambda item: item[1], reverse=True))

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

        most_expensive_cars_per_model = {}
        for model, cars in grouped_by_model.items():
            max_price_car = max(cars, key=lambda c: c.price, default=None)
            most_expensive_cars = [car for car in cars if car.has_price(max_price_car.price)]
            most_expensive_cars_per_model[model] = most_expensive_cars

        return most_expensive_cars_per_model

    # -----------------------------------------------------------------------------------------------

    def get_car_statistics(self, statistics_type: Statistics) -> dict[Statistics, dict[str, float]]:
        """
        Method returns a dict of statistics of a Car objects collection that include average, max
        and min value for price and mileage.
        :return:
        """
        if statistics_type not in Statistics:
            raise ValueError("Wrong parameter name")

        values = [getattr(car, statistics_type.value) for car in self.cars]
        return {
            statistics_type.value.upper(): {
                "avg": mean(values),
                "max": max(values),
                "min": min(values)
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

        if not all(isinstance(price, Decimal) for price in [price_min, price_max]):
            raise ValueError('Wrong price value types')

        if price_min > price_max:
            raise ValueError('Price range is not correct')

        return [car for car in self.cars if car.has_price_within_range(price_min, price_max)]

    # -----------------------------------------------------------------------------------------------
    def get_most_expensive(self) -> list[Car]:
        """
        Method returns a list of Car object(s) of the highest price out of all objects in a collection.
        :return:
        """
        max_price = max([car.price for car in self.cars])
        return [car for car in self.cars if car.price == max_price]

    # -----------------------------------------------------------------------------------------------

    def get_cars_per_components(self) -> dict[str, list[Car]]:
        """
        Method returns a dict of Car object, with key - component, and value - list of Car object with that component.
        Collection is sorted by length of values list
        :return:
        """
        grouped_by_components = defaultdict(list)

        for car in self.cars:
            for component in car.components:
                grouped_by_components[component].append(car)

        return dict(sorted(grouped_by_components.items(), key=lambda pair: len(pair[1]), reverse=True))
