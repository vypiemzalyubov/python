# В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver на новую вкладку и решить в ней задачу.
# 
# Сценарий для реализации выглядит так:
# 
# Открыть страницу http://suninjuly.github.io/redirect_accept.html
# Нажать на кнопку
# Переключиться на новую вкладку
# Пройти капчу для робота и получить число-ответ

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    button = browser.find_element(By.XPATH, "//*[contains(@class,'trollface')]").click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.XPATH, "//*[@id='input_value']").text
    res_calc = calc(x_element)
    input = browser.find_element(By.XPATH, "//*[@id='answer']").send_keys(res_calc)
    button_submit = browser.find_element(By.XPATH, "//*[@type='submit']").click()

finally:
    time.sleep(5)
    browser.quit()