from requests import Response
import json.decoder
from datetime import datetime


class BaseCase:

    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Cannot find cookie with name {cookie_name} in the last response"
        return response.cookies[cookie_name]
    
    def get_header(self, response: Response, header_name):
        assert header_name in response.headers, f"Cannot find header with name {header_name} in the last response"
        return response.headers[header_name]
    
    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecoderError:
            assert False, f"Response is not JSON format. Response text is '{response.text}'"
        assert name in response_as_dict, f"Response JSON doesn't key '{name}'"
        return response_as_dict[name]
    
    def prepare_registration_data(self, email=None):
        if email is None:
                base_part = "learnqa"
                domain = "example.com"
                random_part = datetime.now().strftime("%m%d%Y%H%M%S")
                email = f"{base_part}{random_part}@{domain}"
        data = {
            "password": "1234",
            "username": "learnqa",
            "firstName": "learnqa",
            "lastName": "learnqa",
            "email": email
        }
        return data