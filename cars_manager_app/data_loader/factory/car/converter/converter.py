from abc import ABC, abstractmethod
from typing import Any


class Converter(ABC):
    @abstractmethod
    def convert(self, data: dict[str, Any]) -> Any:
        pass
    