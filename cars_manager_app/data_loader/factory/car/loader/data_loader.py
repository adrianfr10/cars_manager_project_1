from abc import ABC, abstractmethod
from typing import Any


class DataLoader(ABC):
    @abstractmethod
    def get_data(self, filepath: str) -> list[dict[str, Any]]:
        pass
