from enum import Enum


class Sort(Enum):
    """
    Enum defining sorting criteria for the collection of cars
    """
    COLOR = 1   # Sort by color
    MILEAGE = 2 # Sort by mileage
    MODEL = 3   # Sort by model
    PRICE = 4   # Sort by price


class Statistics(Enum):
    """
    Enum defining attributes of cars, which will be used in calculating statistics
    """
    PRICE = "price"     # Calculate statistics for price
    MILEAGE = "mileage" # Calculate statistics for mileage
