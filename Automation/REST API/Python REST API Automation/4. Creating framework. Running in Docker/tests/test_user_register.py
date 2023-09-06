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
        Assertions.assert_response_text_value(response, f"Users with email '{email}' already exists", f"Unexpected response content {response.content}")


    def test_create_user_with_invalid_email(self):
        """Создание пользователя с некорректным email - без символа @"""
        email = "testexample.com"
        data = self.prepare_registration_data(email)
        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        Assertions.assert_response_text_value(response, f"Invalid email format", f"Unexpected email {email}. Missing @")


    @pytest.mark.parametrize("password, username, firstname, lastname, email", [
        (None, "bot", "bot_fname", "bot_lname", "bot@example.com"),
        ("1234", None, "bot_fname", "bot_lname", "bot@example.com"),
        ("1234", "bot", None, "bot_lname", "bot@example.com"),
        ("1234", "bot", "bot_fname", None, "bot@example.com"),
        ("1234", "bot", "bot_fname", "bot_lname", None)
    ])
    def test_create_user_without_specifying_one_of_fields(self, password, username, firstname, lastname, email):
        """Создание пользователя без указания одного из полей"""
        data = {
            "password": password,
            "username": username,
            "firstName": firstname,
            "lastName": lastname,
            "email": email            
        }
        response = MyRequests.post("/user/", data=data)
        missing_param = next(key for key, value in data.items() if value == None)
        
        Assertions.assert_code_status(response, 400)
        Assertions.assert_response_text_value(response, f"The following required params are missed: {missing_param}", f"Missing required param: {missing_param}")


    def test_create_user_with_short_name(self):
        """Создание пользователя с очень коротким именем в один символ"""
        data = {
            "password": "1234",
            "username": "x",
            "firstName": "learnqa",
            "lastName": "learnqa",
            "email": "test1@email.com"
        }        
        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        Assertions.assert_response_text_value(response, f"The value of 'username' field is too short", f"Too short username: {data['username']}")