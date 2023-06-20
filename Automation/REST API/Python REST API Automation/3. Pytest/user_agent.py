# User Agent
# 
# User Agent - это один из заголовков, позволяющий серверу узнавать, с какого девайса и браузера пришел запрос. Он формируется автоматически клиентом, например браузером. 
# Определив, с какого девайса или браузера пришел к нам пользователь мы сможем отдать ему только тот контент, который ему нужен.
# Наш разработчик написал метод: https://playground.learnqa.ru/ajax/api/user_agent_check.
# Метод определяет по строке заголовка User Agent следующие параметры:
# - device - iOS или Android
# - browser - Chrome, Firefox или другой браузер
# - platform - мобильное приложение или веб
# Если метод не может определить какой-то из параметров, он выставляет значение Unknown.
# Наша задача написать параметризированный тест. Этот тест должен брать из дата-провайдера User Agent и ожидаемые значения, GET-делать запрос с этим User Agent и убеждаться, 
# что результат работы нашего метода правильный - т.е. в ответе ожидаемое значение всех трех полей.
# Список User Agent и ожидаемых значений можно найти по этой ссылке: https://gist.github.com/KotovVitaliy/138894aa5b6fa442163561b5db6e2e26.
# На самом деле метод не всегда работает правильно. 
# Ответом к задаче должен быть User Agent, который вернул неправильным хотя бы один параметр, с указанием того, какой именно параметр неправильный.

import pytest
import requests

class TestUserAgent:

    data_provider = [
        ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
         {"platform": "Mobile", 
         "browser": "No", 
         "device": "Android"}),
        ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1", 
         {"platform": "Mobile", 
         "browser": "Chrome", 
         "device": "iOS"}),
        ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
         {"platform": "Googlebot", 
         "browser": "Unknown", 
         "device": "Unknown"}),            
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0",
         {"platform": "Web", 
         "browser": "Chrome", 
         "device": "No"}),            
        ("Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
         {"platform": "Mobile", 
         "browser": "No", 
         "device": "iPhone"})
    ]    

    @pytest.mark.parametrize("user_agent, expected_results", data_provider)
    def test_check_user_agent(self, user_agent, expected_results):

        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        headers={"User-Agent": user_agent}

        response = requests.get(url, headers=headers)
        
        assert expected_results["platform"] == response.json()["platform"],\
            f'Incorrect parameter "{response.json()["platform"]}" in the response to the request with the User-Agent: {response.request.headers}'
        
        assert expected_results["browser"] == response.json()["browser"],\
            f'Incorrect parameter "{response.json()["browser"]}" in the response to the request with the User-Agent: {response.request.headers}'
        
        assert expected_results["device"] == response.json()["device"],\
                f'Incorrect parameter "{response.json()["device"]}" in the response to the request with the User-Agent: {response.request.headers}'
 