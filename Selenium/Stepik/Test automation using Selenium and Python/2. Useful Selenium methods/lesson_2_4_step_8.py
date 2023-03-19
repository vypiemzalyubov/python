# Задание: ждем нужный текст на странице
# 
# Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене. 
# Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.
# 
# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
# 
# 1. Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# 2. Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# 3. Нажать на кнопку "Book"
# 4. Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 13).until(
            EC.text_to_be_present_in_element((By.XPATH, "//*[@id='price']"), "100")
        )
    button = browser.find_element(By.XPATH, "//*[@id='book']").click()

    x_element = browser.find_element(By.XPATH, "//*[@id='input_value']").text
    res_calc = calc(x_element)
    input = browser.find_element(By.XPATH, "//*[@id='answer']").send_keys(res_calc)
    button_submit = browser.find_element(By.XPATH, "//*[@type='submit']").click()    

finally:
    time.sleep(5)
    browser.quit()