import pytest
import allure
from lib.schema import schema_user_register, schema_user_info, schema_unauthorized_user
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


@allure.epic("User info getting cases")
class TestUserGet(BaseCase):


    @allure.description("Получение данных пользователя без авторизации. Получаем только username")
    @pytest.mark.positive
    def test_get_user_details_not_auth(self):
        response = MyRequests.get("/user/2")
        
        Assertions.assert_validate_json_schema(response, schema_unauthorized_user)
        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_not_key(response, "email")
        Assertions.assert_json_has_not_key(response, "firstName")
        Assertions.assert_json_has_not_key(response, "lastName")


    @allure.description("Получение данных авторизованного пользователя после авторизации этого пользователя. Получаем все поля")
    @pytest.mark.positive
    def test_get_user_details_auth_as_same_user(self):
        data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }        
        response1 = MyRequests.post("/user/login", data=data)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = MyRequests.get(f"/user/{user_id_from_auth_method}", 
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
                                 )
        expected_fields = ["username", "email", "firstName", "lastName"]
        
        Assertions.assert_validate_json_schema(response2, schema_user_info)
        Assertions.assert_json_has_keys(response2, expected_fields)


    @allure.description("Получение данных неавторизованного пользователя авторизованным пользователем. Получаем только username")
    @pytest.mark.positive    
    def test_get_user_details_auth_as_another_user(self):
        data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }        
        response1 = MyRequests.post("/user/login", data=data)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")

        response2 = MyRequests.get("/user/1", 
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
                                 )

        Assertions.assert_validate_json_schema(response2, schema_unauthorized_user)
        Assertions.assert_json_has_key(response2, "username")
        Assertions.assert_json_has_not_key(response2, "email")
        Assertions.assert_json_has_not_key(response2, "firstName")
        Assertions.assert_json_has_not_key(response2, "lastName")