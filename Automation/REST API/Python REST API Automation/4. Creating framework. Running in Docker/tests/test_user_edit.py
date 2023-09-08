import allure
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
import time


@allure.epic("User editing cases")
class TestUserEdit(BaseCase):


    @allure.description("Редактирование данных созданного пользователя, после авторизации тем же пользователем")
    def test_edit_just_created_user(self):

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

        # GET & CHECK
        response4 = MyRequests.get(f"/user/{user_id}", 
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
                                 )
        
        Assertions.assert_json_value_by_name(response4, "firstName", new_name, "Wrong name of the user after edit")


    @allure.description("Редактирование данных созданного пользователя без авторизации")
    def test_edit_created_user_by_unauthorized_user(self):

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
        response2 = MyRequests.put(f"/user/78631",                                  
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

        # GET & CHECK
        response4 = MyRequests.get(f"/user/{user_id}", 
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
                                 )
        
        Assertions.assert_json_value_by_name(response4, "lastName", last_name, "Last name was changed, but shouldn't have been")


    @allure.description("Редактирование данных созданного пользователя, будучи авторизованным другим пользователем")
    def test_edit_new_created_user_by_another_authorized_user(self):
        
        # REGISTER FIRST USER
        email1 = f"{''.join(__import__('random').choice(__import__('string').ascii_letters) for _ in range(9))}@example.com"
        register_data1 = self.prepare_registration_data(email=email1)
        response1 = MyRequests.post("/user/", data=register_data1)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        first_name1 = register_data1["firstName"]
        password1 = register_data1["password"]
        user_id1 = self.get_json_value(response1, "id")
        
        # REGISTER SECOND USER
        email2 = f"{''.join(__import__('random').choice(__import__('string').ascii_letters) for _ in range(10))}@example.com"
        register_data2 = self.prepare_registration_data(email=email2)
        response2 = MyRequests.post("/user/", data=register_data2)

        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")

        password2 = register_data2["password"]

        # LOGIN SECOND USER
        login_data1 = {
            "email": email2,
            "password": password2
        }
        response_login1 = MyRequests.post("/user/login", data=login_data1)
        
        auth_sid1 = self.get_cookie(response_login1, "auth_sid")
        token1 = self.get_header(response_login1, "x-csrf-token")

        # EDIT FIRST USER BY AUTHORIZED SECOND USER
        new_name = "Test name"
        response_edit = MyRequests.put(f"/user/{user_id1}", 
                                 headers={"x-csrf-token": token1},
                                 cookies={"auth_sid": auth_sid1},
                                 data={"firstName": new_name}
                                 )
        
        Assertions.assert_code_status(response_edit, 200)

        # LOGIN FIRST USER
        login_data2 = {
            "email": email1,
            "password": password1
        }
        response_login2 = MyRequests.post("/user/login", data=login_data2)
        
        auth_sid2 = self.get_cookie(response_login2, "auth_sid")
        token2 = self.get_header(response_login2, "x-csrf-token")

        # GET & CHECK FIRST USER
        response_check = MyRequests.get(f"/user/{user_id1}", 
                                 headers={"x-csrf-token": token2},
                                 cookies={"auth_sid": auth_sid2}
                                 )

        Assertions.assert_json_value_by_name(response_check, "firstName", first_name1, "First name was changed, but shouldn't have been")


    @allure.description("Редактирование емэйла созданного пользователя на невалидный - без символа @, после авторизации тем же пользователем")
    def test_edit_email_to_invalid_just_created_user(self):
        
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
        new_email = "testexample.com"
        response3 = MyRequests.put(f"/user/{user_id}", 
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid},
                                 data={"email": new_email}
                                 )

        Assertions.assert_code_status(response3, 400)
        Assertions.assert_response_text_value(response3, "Invalid email format")

        # GET & CHECK
        response4 = MyRequests.get(f"/user/{user_id}", 
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
                                 )

        Assertions.assert_json_value_by_name(response4, "email", email, "Email was changed, but shouldn't have been")


    @allure.description("Редактирование имени созданного пользователя на невалидное - длиной в один символ, после авторизации тем же пользователем")
    def test_edit_first_name_to_invalid_just_created_user(self):
        
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

        # GET & CHECK
        response4 = MyRequests.get(f"/user/{user_id}", 
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
                                 )

        Assertions.assert_json_value_by_name(response4, "firstName", first_name, "First name was changed, but shouldn't have been")