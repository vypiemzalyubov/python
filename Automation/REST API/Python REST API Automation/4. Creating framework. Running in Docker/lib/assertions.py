import allure
import json
from requests import Response


class Assertions:


    @staticmethod
    @allure.step("Проверка статус кода")
    def assert_code_status(response: Response, expected_status_code: int) -> None:
        assert response.status_code == expected_status_code, \
            f"Unexpected status code! Expected: {expected_status_code}. Actual: {response.status_code}"


    @staticmethod
    @allure.step("Проверка значения в JSON ответе по ключу")
    def assert_json_value_by_name(response: Response, name: str, expected_value: str, error_message: str) -> None:
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not JSON format. Response text is '{response.text}'"
        assert name in response_as_dict, f"Response JSON doesn't key '{name}'"
        assert response_as_dict[name] == expected_value, error_message


    @staticmethod
    @allure.step("Проверка наличия ключа в JSON ответе")
    def assert_json_has_key(response: Response, name: str) -> None:
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not JSON format. Response text is '{response.text}'"
        assert name in response_as_dict, f"Response JSON doesn't key '{name}'"


    @staticmethod
    @allure.step("Проверка наличия нескольких ключей в JSON ответе")
    def assert_json_has_keys(response: Response, names: list) -> None:
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not JSON format. Response text is '{response.text}'"
        for name in names:
            assert name in response_as_dict, f"Response JSON doesn't keys '{name}'"        


    @staticmethod
    @allure.step("Проверка отсутсвия ключа в JSON ответе")
    def assert_json_has_not_key(response: Response, name: str) -> None:
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not JSON format. Response text is '{response.text}'"
        assert name not in response_as_dict, f"Response JSON shouldn't have key '{name}'. But it's present"        


    @staticmethod
    @allure.step("Проверка значения в текстовом ответе")
    def assert_response_text_value(response: Response, expexted_value: str) -> None:
        response_text = response.content.decode("utf-8")
        assert response_text == expexted_value, f"Unexpected response content: {response.content}"