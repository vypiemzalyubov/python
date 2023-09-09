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


    @allure.description("Удаление неавторизованного пользователя другим авторизованным пользователем")
    @pytest.mark.negative
    def test_delete_unauthorized_user_by_authorized_user(self):

        # REGISTER FIRST USER
        email1 = f"{''.join(__import__('random').choice(__import__('string').ascii_letters) for _ in range(9))}@example.com"
        register_data1 = self.prepare_registration_data(email=email1)
        response_register1 = MyRequests.post("/user/", data=register_data1)

        Assertions.assert_code_status(response_register1, 200)
        Assertions.assert_json_has_key(response_register1, "id")

        first_name1 = register_data1["firstName"]
        password1 = register_data1["password"]
        user_id1 = self.get_json_value(response_register1, "id")
        
        # REGISTER SECOND USER
        email2 = f"{''.join(__import__('random').choice(__import__('string').ascii_letters) for _ in range(10))}@example.com"
        register_data2 = self.prepare_registration_data(email=email2)
        response_register2 = MyRequests.post("/user/", data=register_data2)

        Assertions.assert_code_status(response_register2, 200)
        Assertions.assert_json_has_key(response_register2, "id")

        password2 = register_data2["password"]

        # LOGIN SECOND USER
        login_data_second_user = {
            "email": email2,
            "password": password2
        }
        response_login_second_user = MyRequests.post("/user/login", data=login_data_second_user)
        
        auth_sid_second_user = self.get_cookie(response_login_second_user, "auth_sid")
        token_second_user = self.get_header(response_login_second_user, "x-csrf-token")

        # DELETE FIRST USER BY AUTHORIZED SECOND USER
        response_delete = MyRequests.delete(
            f"/user/{user_id1}",
            headers={"x-csrf-token": token_second_user},
            cookies={"auth_sid": auth_sid_second_user}
        )

        Assertions.assert_code_status(response_delete, 200)

        # LOGIN FIRST USER
        login_data_first_user = {
            "email": email1,
            "password": password1
        }
        response_login_first_user = MyRequests.post("/user/login", data=login_data_first_user)
        
        auth_sid2 = self.get_cookie(response_login_first_user, "auth_sid")
        token2 = self.get_header(response_login_first_user, "x-csrf-token")

        # GET & CHECK FIRST USER
        response_check = MyRequests.get(f"/user/{user_id1}",
                                 headers={"x-csrf-token": token2},
                                 cookies={"auth_sid": auth_sid2}
                                 )

        Assertions.assert_json_value_by_name(response_check, "id", user_id1, "User was deleted, but shouldn't have been")