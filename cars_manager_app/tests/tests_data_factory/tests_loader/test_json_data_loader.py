import json.encoder

import pytest
from cars_manager_app.data_loader.factory.car.loader.json_data_loader import JsonDataLoader
import os


class TestDataLoaderJsonDataLoaderPathNotCorrect:

    @pytest.fixture()
    def incorrect_extension_path(self) -> str:
        return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data_test', 'test_file.txt'))

    @pytest.fixture()
    def not_existing_path(self) -> str:
        return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data_test', 'file.json'))

    def test_when_path_has_incorrect_extension(self, incorrect_extension_path) -> None:
        with pytest.raises(AttributeError) as ae:
            loader = JsonDataLoader()
            loader.get_data(incorrect_extension_path)
        assert str(ae.value) == 'File has incorrect extension'

    def test_when_file_not_found(self, not_existing_path) -> None:
        with pytest.raises(FileNotFoundError) as e:
            loader = JsonDataLoader()
            loader.get_data(os.path.abspath(not_existing_path))
        assert str(e.value).startswith(f'File not found')


class TestDataLoaderJsonDataLoaderContentNotCorrect:
    @pytest.fixture()
    def cars_empty_test_path(self) -> str:
        return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data_test', 'file_empty_entirely.json'))


    def test_when_file_has_no_content(self, cars_empty_test_path) -> None:
        with pytest.raises(json.decoder.JSONDecodeError) as e:
            loader = JsonDataLoader()
            loader.get_data(cars_empty_test_path)
        assert str(e.value).startswith("File has invalid JSON format or file is empty")


class TestDataLoaderJsonDataLoaderContentCorrect:
    @pytest.fixture()
    def cars_valid_content(self) -> str:
        return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data_test', 'cars_test.json'))

    def test_when_file_content_is_present(self, cars_valid_content) -> None:
        loader = JsonDataLoader()
        result = loader.get_data(cars_valid_content)
        assert 3 == len(result)
