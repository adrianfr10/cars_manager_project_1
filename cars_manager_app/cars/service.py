from .model import Car
from itertools import chain
from decimal import Decimal
from collections import defaultdict, Counter
from statistics import mean


class CarsService:

    def __init__(self, cars: list[Car]) -> None:
        self.cars = cars
