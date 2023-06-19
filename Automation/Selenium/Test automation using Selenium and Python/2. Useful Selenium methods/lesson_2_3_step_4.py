# Задание: принимаем alert
# 
# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
# 
# 1. Открыть страницу http://suninjuly.github.io/alert_accept.html
# 2. Нажать на кнопку
# 3. Принять confirm
# 4. На новой странице решить капчу для роботов, чтобы получить число с ответом

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser.get("http://suninjuly.github.io/alert_accept.html")

    button = browser.find_element(By.XPATH, "//*[text()='I want to go on a magical journey!']").click()

    confirm = browser.switch_to.alert.accept()

    x_element = browser.find_element(By.XPATH, "//*[@id='input_value']").text
    res_calc = calc(x_element)
    input = browser.find_element(By.XPATH, "//*[@id='answer']").send_keys(res_calc)
    button_submit = browser.find_element(By.XPATH, "//*[@type='submit']").click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)

finally:
    time.sleep(5)
    browser.quit()