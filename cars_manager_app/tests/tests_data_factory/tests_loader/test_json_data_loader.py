import unittest
from unittest.mock import mock_open, patch

from cars_manager_app.data_loader.factory.car.loader.json_data_loader import JsonDataLoader


class TestDataLoader(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='[{'
                                                              '"model": "BMW",'
                                                              ' "price": 160000.0,'
                                                              ' "color": "BLACK",'
                                                              ' "mileage": 1500,'
                                                              ' "components": ["ABS", "ALLOY WHEELS"]'
                                                              '}]')
    def test_get_data(self, mock_file_open):
        data_loader = JsonDataLoader()

        filepath = 'fake_file.json'
        data = data_loader.get_data(filepath)

        expected_data = [{"model": "BMW",
                          "price": 160000.0,
                          "color": "BLACK",
                          "mileage": 1500,
                          "components": ["ABS", "ALLOY WHEELS"]}]
        self.assertEqual(data, expected_data)


if __name__ == '__main__':
    unittest.main()
