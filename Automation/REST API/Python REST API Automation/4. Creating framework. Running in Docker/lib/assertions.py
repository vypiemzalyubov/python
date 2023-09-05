import json
from requests import Response


class Assertions:

    @staticmethod
    def assert_code_status(response: Response, expected_status_code):
        """Метод проверки статус кода"""
        assert response.status_code == expected_status_code, \
            f"Unexpected status code! Expected: {expected_status_code}. Actual: {response.status_code}"
    
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        """Метод проверки значения в ответе JSON по ключу"""
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not JSON format. Response text is '{response.text}'"
        assert name in response_as_dict, f"Response JSON doesn't key '{name}'"
        assert response_as_dict[name] == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, name):
        """Метод проверки наличия ключа в ответе JSON"""
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not JSON format. Response text is '{response.text}'"
        assert name in response_as_dict, f"Response JSON doesn't key '{name}'"

    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
        """Метод проверки наличия нескольких ключей в ответе JSON"""
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not JSON format. Response text is '{response.text}'"
        for name in names:
            assert name in response_as_dict, f"Response JSON doesn't keys '{name}'"        

    @staticmethod
    def assert_json_has_not_key(response: Response, name):
        """Метод проверки отсутсвия ключа в ответе JSON"""
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not JSON format. Response text is '{response.text}'"
        assert name not in response_as_dict, f"Response JSON shouldn't have key '{name}'. But it's present"        
