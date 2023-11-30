import pytest

from cars_manager_app.data_loader.factory.car.validator.validator import *


class TestWhenValidatorIsCorrect:

    def test_when_validate_number_is_correct(self) -> None:
        assert Validator.validate_number('23')

    def test_when_validate_decimal_is_correct(self) -> None:
        assert Validator.validate_decimal('34.6')

    def test_when_validate_string_is_correct(self) -> None:
        assert Validator.validate_string("TESTVALUE")
        assert Validator.validate_string("TEST VALUE")

    def test_when_matches_regex_is_correct(self) -> None:
        assert Validator.matches_regex('[A-Za-z ]', 'test string')


class TestWhenValidatorRaisesException:

    def test_when_validate_number_raises_exception(self) -> None:
        with pytest.raises(Exception):
            Validator.validate_number('23.6')


    def test_when_validate_string_raises_exception(self) -> None:
        with pytest.raises(Exception):
            Validator.validate_string('TEST $%^')


    def test_when_validate_decimal_raises_exception(self) -> None:
        with pytest.raises(Exception):
            Validator.validate_decimal('test')


    def test_when_matches_regex_raises_exception(self) -> None:
        test_value = Validator.matches_regex('[A-Z]', 'test regex')
        assert test_value == False
