import pytest
import allure
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


@allure.epic("Registrations cases")
class TestUserRegister(BaseCase):

    def test_create_user_successfully(self):
        """Создание нового пользователя"""
        data = self.prepare_registration_data()
        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        """Создание пользователя с существующим емэйлом"""
        email = "vinkotov@example.com"
        data = self.prepare_registration_data(email)
        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    def test_create_user_with_invalid_email(self):
        """Создание пользователя с некорректным email - без символа @"""
        email = "testexample.com"
        data = self.prepare_registration_data(email)
        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Invalid email format", f"Unexpected email {email}. Missing @"

    # user_data = [
    #     ("no_cookie"),
    #     ("no_token")
    # ]   

    # @pytest.mark.parametrize("input, expected_results", user_data)
    def test_create_user_without_specifying_one_of_fields(self):
        """Создание пользователя без указания одного из полей"""
        data =  {
            "password": "1234",
            "username": "learnqa",
            "firstName": "learnqa",
            "lastName": "learnqa",
        }
        
        response = MyRequests.post("/user/", data=data)
        print(response.content)