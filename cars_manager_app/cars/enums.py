from enum import Enum


class Sort(Enum):
    COLOR = 1
    MILEAGE = 2
    MODEL = 3
    PRICE = 4


class Statistics(Enum):
    PRICE = "price"
    MILEAGE = "mileage"
