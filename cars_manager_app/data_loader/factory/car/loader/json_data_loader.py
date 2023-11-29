import json
from typing import Any

from .data_loader import DataLoader


class JsonDataLoader(DataLoader):

    def get_data(self, filepath: str) -> list[dict[str, Any]]:
        if not filepath.endswith('.json'):
            raise AttributeError('File has incorrect extension')
        try:
            with open(filepath, 'r') as jf:
                return json.load(jf)
        except json.decoder.JSONDecodeError as e:
            raise  json.decoder.JSONDecodeError("File has invalid JSON format or file is empty", "", 0) from e
        except FileNotFoundError as e:
            raise FileNotFoundError(f'File not found: {e}')
        except Exception as e:
            print(f"Unexpected error: {e}")



