from ..utils import bmw


def test_when_list_of_most_expensive_cars_is_correct(cars_service) -> None:
    most_expensive_cars = cars_service.get_most_expensive()
    expected_most_expensive_cars = [bmw]
    assert most_expensive_cars == expected_most_expensive_cars



