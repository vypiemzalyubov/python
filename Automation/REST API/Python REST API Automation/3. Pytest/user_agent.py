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
# Пример того, как должен выглядеть запрос с указанным User Agent:
# requests.get(
#     "https://playground.learnqa.ru/ajax/api/user_agent_check",
#     headers={"User-Agent": "Some value here"}
# )
# На самом деле метод не всегда работает правильно. Ответом к задаче должен быть список из тех User Agent, 
# которые вернули неправильным хотя бы один параметр, с указанием того, какой именно параметр неправильный.

import pytest
import requests

class TestUserAgent:

    user_agents = [
        ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"),
        # Expected values: 'platform': 'Mobile', 'browser': 'No', 'device': 'Android'
        ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"),
        # 'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'
        ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"),
        # 'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"),
        # 'platform': 'Web', 'browser': 'Chrome', 'device': 'No'
        ("Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1")
        # 'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'
    ]

    @pytest.mark.parametrize("user_agent", user_agents)
    def test_check_user_agent(self, user_agent):

        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        headers={"User-Agent": user_agent}

        if user_agent == "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30":
            response1 = requests.get(url, headers=headers)
            assert response1.status_code == 200, "Wrong response status code"
            assert response1.json()["platform"] == 'Mobile' and response1.json()["browser"] == 'No' and response1.json()["device"] == 'Android', f"Wrong answer to request with user-agent {response1.request.headers}"

        if user_agent == "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1":
            response2 = requests.get(url, headers=headers)
            assert response2.status_code == 200, "Wrong response status code"
            assert response2.json()["platform"] == 'Mobile' and response2.json()["browser"] == 'Chrome' and response2.json()["device"] == 'iOS', f"Wrong answer to request with user-agent {response2.request.headers}"

        if user_agent == "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)":
            response3 = requests.get(url, headers=headers)
            assert response3.status_code == 200, "Wrong response status code"
            assert response3.json()["platform"] == 'Googlebot' and response3.json()["browser"] == 'Unknown' and response3.json()["device"] == 'Unknown', f"Wrong answer to request with user-agent {response3.request.headers}"            

        if user_agent == "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0":
            response4 = requests.get(url, headers=headers)
            assert response4.status_code == 200, "Wrong response status code"
            assert response4.json()["platform"] == 'Web' and response4.json()["browser"] == 'Chrome' and response4.json()["device"] == 'No', f"Wrong answer to request with user-agent {response4.request.headers}"

        if user_agent == "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1":
            response5 = requests.get(url, headers=headers)
            assert response5.status_code == 200, "Wrong response status code"
            assert response5.json()["platform"] == 'Mobile' and response5.json()["browser"] == 'No' and response5.json()["device"] == 'iPhone', f"Wrong answer to request with user-agent {response5.request.headers}"            