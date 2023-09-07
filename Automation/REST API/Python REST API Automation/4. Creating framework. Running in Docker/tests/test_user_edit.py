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


    # def test_edit_created_user_by_unauthorized_user(self):
    #     """Создание нового пользователя
    #        Редактирование созданного пользователя без авторизации
    #        Проверяем, что сервер отвечает ошибкой
    #        Авторизовываемся созданным пользователем и проверяем, что данные не изменились"""

    #     # REGISTER
    #     register_data = self.prepare_registration_data()
    #     response1 = MyRequests.post("/user/", data=register_data)

    #     Assertions.assert_code_status(response1, 200)
    #     Assertions.assert_json_has_key(response1, "id")

    #     email = register_data["email"]
    #     password = register_data["password"]
    #     last_name = register_data["lastName"]
    #     user_id = self.get_json_value(response1, "id")

    #     # EDIT
    #     new_last_name = "Changed last name"
    #     response2 = MyRequests.put(f"/user/78631",                                  
    #                              data={"lastName": new_last_name}
    #                              )

    #     Assertions.assert_code_status(response2, 400)
    #     Assertions.assert_response_text_value(response2, "Auth token not supplied")

    #     # LOGIN
    #     login_data = {
    #         "email": email,
    #         "password": password
    #     }
    #     response3 = MyRequests.post("/user/login", data=login_data)

    #     auth_sid = self.get_cookie(response3, "auth_sid")
    #     token = self.get_header(response3, "x-csrf-token")

    #     # GET
    #     response4 = MyRequests.get(f"/user/{user_id}", 
    #                              headers={"x-csrf-token": token},
    #                              cookies={"auth_sid": auth_sid}
    #                              )
        
    #     Assertions.assert_json_value_by_name(response4, "lastName", last_name, "Wrong last name of the user after edit")


    # def test_edit_new_created_user_by_another_authorized_user(self):
    #     """Создание первого нового пользователя
    #        Создание второго нового пользователя
    #        Авторизация второго созданного пользователя
    #        Редактирование первого созданного пользователя, будучи авторизованным вторым пользователем
    #        Проверяем, что сервер отвечает ошибкой
    #        Авторизовываемся первым созданным пользователем и проверяем, что данные не изменились"""
        
    #     # REGISTER FIRST USER
    #     register_data_first_user = self.prepare_registration_data()
    #     response1 = MyRequests.post("/user/", data=register_data_first_user)

    #     Assertions.assert_code_status(response1, 200)
    #     Assertions.assert_json_has_key(response1, "id")

    #     email = register_data_first_user["email"]
    #     first_name_first_user = register_data_first_user["firstName"]
    #     password_first_user = register_data_first_user["password"]
    #     user_id_first_user = self.get_json_value(response1, "id")

    #     # # REGISTER SECOND USER
    #     # email_second_user = "4_user@test.com"
    #     # register_data_second_user = self.prepare_registration_data(email=email_second_user)
    #     # response2 = MyRequests.post("/user/", data=register_data_second_user)

    #     # Assertions.assert_code_status(response1, 200)
    #     # Assertions.assert_json_has_key(response1, "id")

    #     # password_second_user = register_data_second_user["password"]           
    #     # user_id_second_user = self.get_json_value(response1, "id")

    #     # print(user_id_second_user, email_second_user)

    #     # LOGIN SECOND USER
    #     login_data_second_user = {
    #         "email": email,
    #         "password": password_first_user
    #     }
    #     response3 = MyRequests.post("/user/login", data=login_data_second_user)
        
    #     auth_sid_second_user = self.get_cookie(response3, "auth_sid")
    #     token_second_user = self.get_header(response3, "x-csrf-token")

    #     # EDIT FIRST USER
    #     new_name = "Changed name"
    #     response4 = MyRequests.put(f"/user/2432", 
    #                              headers={"x-csrf-token": token_second_user},
    #                              cookies={"auth_sid": auth_sid_second_user},
    #                              data={"firstName": new_name}
    #                              )
    #     print(response4.status_code)
    #     print(response4.content)


    def test_edit_email_to_invalid_just_created_user(self):
        """Создание нового пользователя
           Авторизация созданного пользователя
           Редактирование емэйла созданного пользователя без @ в названии емэйла
           Проверяем, что емэйл пользователя не изменился"""
        
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data["email"]
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
        new_email = "Changed email"
        response3 = MyRequests.put(f"/user/{user_id}", 
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid},
                                 data={"email": new_email}
                                 )

        Assertions.assert_code_status(response3, 400)
        Assertions.assert_response_text_value(response3, "Invalid email format")

        # GET
        response4 = MyRequests.get(f"/user/{user_id}", 
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
                                 )

        Assertions.assert_json_value_by_name(response4, "email", email, "Email was changed, but shouldn't have been")


    def test_edit_first_name_to_invalid_just_created_user(self):
        """Создание нового пользователя
           Авторизация созданного пользователя
           Редактирование имени созданного пользователя на невалидное - длиной в один символ
           Проверяем, что имя пользователя не изменилось"""
        
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        first_name = register_data["firstName"]
        email = register_data["email"]
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
        new_first_name = "x"
        response3 = MyRequests.put(f"/user/{user_id}", 
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid},
                                 data={"firstName": new_first_name}
                                 )

        Assertions.assert_code_status(response3, 400)
        Assertions.assert_json_value_by_name(response3, "error", "Too short value for field firstName", "Unexpected response!")

        # GET
        response4 = MyRequests.get(f"/user/{user_id}", 
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
                                 )

        Assertions.assert_json_value_by_name(response4, "firstName", first_name, "First name was changed, but shouldn't have been")