import re


def validate_number(number: str) -> str:
    if not re.match(r'^[0-9]+$', str(number)):
        raise ValueError("Wrong integer format.")
    return number


def validate_string(given_string: str) -> str:
    if not re.match(r'^[A-Z\s]*$', given_string):
        raise ValueError("Wrong string format.")
    return given_string


def validate_decimal(given_number: str) -> str:
    if not re.match(r'^(\d+(\.\d+)?)$', str(given_number)):
        raise ValueError("Wrong decimal value format.")
    return given_number
