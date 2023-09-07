import pytest
import allure
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


@allure.epic("User info getting cases")
class TestUserGet(BaseCase):


    def test_get_user_details_not_auth(self):
        """Получение данных пользователя без предварительной авторизации
           Получаем только username"""
        response = MyRequests.get("/user/2")
        
        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_not_key(response, "email")
        Assertions.assert_json_has_not_key(response, "firstName")
        Assertions.assert_json_has_not_key(response, "lastName")


    def test_get_user_details_auth_as_same_user(self):
        """Авторизация и получение данных авторизованного пользователя
           Авторизовываемся пользователем с ID 2 и делаем запрос для получения данных того же пользователя 
           Получаем все поля"""
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
        
        Assertions.assert_json_has_keys(response2, expected_fields)

    
    def test_get_user_details_auth_as_another_user(self):
        """Получение данных неавторизованного пользователя авторизованным пользователем
           Авторизовываемся пользователем с ID 2 и делаем запрос для получения данных неавторизованного пользователя
           Получаем только username"""
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

        Assertions.assert_json_has_key(response2, "username")
        Assertions.assert_json_has_not_key(response2, "email")
        Assertions.assert_json_has_not_key(response2, "firstName")
        Assertions.assert_json_has_not_key(response2, "lastName")        