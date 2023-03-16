from .data_loader import DataLoader
from typing import Any
import json


class JsonDataLoader(DataLoader):

    def get_data(self, filepath: str) -> list[dict[str, Any]]:
        with open(filepath, 'r') as jf:
            return json.load(jf)
