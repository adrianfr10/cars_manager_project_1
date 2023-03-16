from abc import ABC, abstractmethod
from typing import Any
import re


class Validator(ABC):
    @abstractmethod
    def validate(self, data: dict[str, Any]) -> dict[str, Any]:
        pass

    @staticmethod
    def matches_regex(regex: str, text: str) -> bool:
        return re.match(regex, text) is not None

    @staticmethod
    def validate_number(number: str) -> str:
        if not re.match(r'^[0-9]+$', str(number)):
            raise ValueError("Wrong integer format.")
        return number

    @staticmethod
    def validate_string(text: str) -> str:
        if not re.match(r'^[A-Z\s]*$', text):
            raise ValueError("Wrong string format.")
        return text

    @staticmethod
    def validate_decimal(given_number: str) -> str:
        if not re.match(r'^(\d+(\.\d+)?)$', str(given_number)):
            raise ValueError("Wrong decimal value format.")
        return given_number
