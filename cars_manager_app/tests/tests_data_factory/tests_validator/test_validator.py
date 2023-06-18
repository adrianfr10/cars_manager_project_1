import pytest

from cars_manager_app.data_loader.factory.car.validator.validator import *


def test_when_validate_number_is_correct() -> None:
    assert Validator.validate_number('23')


def test_when_validate_number_raises_exception() -> None:
    with pytest.raises(Exception) as e:
        test_value = Validator.validate_number('23.6')
        assert e.value == test_value


def test_when_validate_string_is_correct() -> None:
    assert Validator.validate_string("TESTVALUE")
    assert Validator.validate_string("TEST VALUE")


def test_when_validate_string_raises_exception() -> None:
    with pytest.raises(Exception) as e:
        test_value = Validator.validate_string('TEST $%^')
        assert e.value == test_value


def test_when_validate_decimal_is_correct() -> None:
    assert Validator.validate_decimal('34.6')


def test_when_validate_decimal_raises_exception() -> None:
    with pytest.raises(Exception) as e:
        test_value = Validator.validate_decimal('12')
        assert e.value == test_value


def test_when_matches_regex_is_correct() -> None:
    assert Validator.matches_regex('[A-Za-z ]', 'test string')


def test_when_matches_regex_raises_exception() -> None:
    with pytest.raises(Exception) as e:
        test_value = Validator.matches_regex('[A-Z]', 'test regex')
        assert e.value == test_value
