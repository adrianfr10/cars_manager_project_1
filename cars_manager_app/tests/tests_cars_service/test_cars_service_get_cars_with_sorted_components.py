from ..utils import *

#todo do poprawy, moze się da parametrize napewno sie da
def test_when_list_of_cars_with_sorted_components_is_correct(cars_service) -> None:
    cars_with_sorted_components = cars_service.get_cars_with_sorted_components()
    sorted_bmw, sorted_mazda, sorted_fiat = sorted(bmw.components), sorted(mazda.components), sorted(fiat.components)
    assert cars_with_sorted_components[0].components == sorted_bmw
    assert cars_with_sorted_components[1].components == sorted_mazda
    assert cars_with_sorted_components[2].components == sorted_fiat


