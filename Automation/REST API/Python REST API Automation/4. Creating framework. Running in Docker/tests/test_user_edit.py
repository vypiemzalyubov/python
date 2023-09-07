import allure
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


@allure.epic("User editing cases")
class TestUserEdit(BaseCase):


    def test_edit_just_created_user(self):
        """Создание нового пользователя
           Авторизация созданного пользователя
           Редактирование созданного пользователя
           Проверяем, что данные пользователя успешно отредактировались"""
        
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data["email"]
        first_name = register_data["firstName"]
        password = register_data["password"]
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            "email": email,
            "password": password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # EDIT
        new_name = "Changed name"
        response3 = MyRequests.put(f"/user/{user_id}", 
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid},
                                 data={"firstName": new_name}
                                 )
        
        Assertions.assert_code_status(response3, 200)

        # GET
        response4 = MyRequests.get(f"/user/{user_id}", 
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
                                 )
        
        Assertions.assert_json_value_by_name(response4, "firstName", new_name, "Wrong name of the user after edit")


    def test_edit_just_created_user_by_unauthorized_user(self):
        """Создание нового пользователя
           Редактирование созданного пользователя без авторизации
           Проверяем, что сервер отвечает ошибкой
           Авторизовываемся созданным пользователем и проверяем, что данные не изменились"""

        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data["email"]
        password = register_data["password"]
        last_name = register_data["lastName"]
        user_id = self.get_json_value(response1, "id")

        # EDIT
        new_last_name = "Changed last name"
        response2 = MyRequests.put(f"/user/{user_id}",                                  
                                 data={"lastName": new_last_name}
                                 )
        
        Assertions.assert_code_status(response2, 400)
        Assertions.assert_response_text_value(response2, "Auth token not supplied")

        # LOGIN
        login_data = {
            "email": email,
            "password": password
        }
        response3 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response3, "auth_sid")
        token = self.get_header(response3, "x-csrf-token")

        # GET
        response4 = MyRequests.get(f"/user/{user_id}", 
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
                                 )
        
        Assertions.assert_json_value_by_name(response4, "lastName", last_name, "Wrong last name of the user after edit")


    def test_edit_just_created_user_by_another_authorized_user(self):
        """Создание первого нового пользователя
           Авторизация созданного пользователя
           Создание второго нового пользователя
           Редактирование второго созданного пользователя, будучи авторизованным первым пользователем
           Проверяем, что сервер отвечает ошибкой"""
        
        # REGISTER 1
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data["email"]
        password = register_data["password"]

        # LOGIN
        login_data = {
            "email": email,
            "password": password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")     