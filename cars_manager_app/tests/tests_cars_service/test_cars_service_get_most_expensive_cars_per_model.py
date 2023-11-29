from ..utils import bmw, mazda, fiat

class TestGetMostExpensiveCarsPerModel:

    def test_when_dict_of_most_expensive_cars_per_model_is_correct(self, cars_service) -> None:
        most_expensive_cars_per_model = cars_service.get_most_expensive_cars_per_model()
        expected_most_expensive_cars_per_model = {"BMW": [bmw], "MAZDA": [mazda], "FIAT": [fiat]}
        assert most_expensive_cars_per_model == expected_most_expensive_cars_per_model
