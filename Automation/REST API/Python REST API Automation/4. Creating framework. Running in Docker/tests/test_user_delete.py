import pytest
import allure
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


@allure.epic("User deleting cases")
class TestUserDelete(BaseCase):
    

    @allure.description("Авторизация пользователя и проверка, что пользователя с правами администратора нельзя удалить")
    @pytest.mark.negative
    def test_delete_admin_user(self):

        # LOGIN
        data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }
        response1 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        # DELETE
        response2 = MyRequests.delete(
            f"/user/{user_id_from_auth_method}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )        
        
        Assertions.assert_code_status(response2, 400)
        Assertions.assert_response_text_value(response2, "Please, do not delete test users with ID 1, 2, 3, 4 or 5.")


    @allure.description("Создание пользователя, авторизация, удаление и проверка, что пользователь удален")
    @pytest.mark.positive
    def test_delete_user_after_create(self):
        
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            "email": register_data["email"],
            "password": register_data["password"]
        }        
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # DELETE
        response3 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response3, 200)

        # GET & CHECK
        response4 = MyRequests.get(f"/user/{user_id}", 
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
                                 )
        
        Assertions.assert_code_status(response4, 404)
        Assertions.assert_response_text_value(response4, "User not found")